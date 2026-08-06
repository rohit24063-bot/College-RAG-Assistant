import os
from typing import TypedDict, Annotated

import streamlit as st
from dotenv import load_dotenv

from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END

from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()

# ----------------------------------------------------
# Streamlit Config
# ----------------------------------------------------

st.set_page_config(
    page_title="College Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 College Assistant")
st.write("Ask any academic, fee or general college-related question.")

# ----------------------------------------------------
# Load Embeddings
# ----------------------------------------------------

@st.cache_resource
def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


embeddings = load_embeddings()

# ----------------------------------------------------
# Build Retriever
# ----------------------------------------------------

@st.cache_resource
def build_retriever(pdf_path: str):

    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    return vectorstore.as_retriever(
        search_kwargs={"k": 4}
    )


academic_retriever = build_retriever("academics_handbook.pdf")
fee_retriever = build_retriever("fee_structure.pdf")

# ----------------------------------------------------
# LLM
# ----------------------------------------------------

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.4
)

# ----------------------------------------------------
# State
# ----------------------------------------------------

class State(TypedDict):
    programme: str
    messages: Annotated[list, add_messages]
    query_type: str
    retrieved_context: str

# ----------------------------------------------------
# Nodes
# ----------------------------------------------------

def classifier_node(state: State):

    last_message = state["messages"][-1].content

    prompt = f"""
Classify the following student query into exactly ONE category.

Categories:

academic
fee
general

Academic:
attendance, exams, grading, credits, syllabus, promotion,
course structure, degree requirements, training etc.

Fee:
tuition, payment, refund, scholarships,
late fee or money related questions.

General:
greetings or anything else.

Query:
{last_message}

Return only one word.
"""

    response = llm.invoke(prompt)

    category = response.content.strip().lower()

    if "academic" in category:
        category = "academic"

    elif "fee" in category:
        category = "fee"

    else:
        category = "general"

    return {"query_type": category}


def academic_rag_node(state: State):

    query = state["messages"][-1].content

    docs = academic_retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return {
        "retrieved_context": context
    }


def fee_rag_node(state: State):

    query = state["messages"][-1].content

    docs = fee_retriever.invoke(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return {
        "retrieved_context": context
    }


def general_node(state: State):

    return {
        "retrieved_context": "NO_RETRIEVAL_NEEDED"
    }


def response_node(state: State):

    query = state["messages"][-1].content

    programme = state["programme"]

    context = state["retrieved_context"]

    if context == "NO_RETRIEVAL_NEEDED":

        prompt = f"""
You are a friendly college assistant.

Student Programme:
{programme}

Answer naturally.

Question:
{query}
"""

    else:

        prompt = f"""
You are a college assistant.

Student Programme:
{programme}

Use ONLY the context below while answering.

Context:
{context}

Question:
{query}

Give a clear and friendly answer.
"""

    response = llm.invoke(prompt)

    return {
        "messages": [
            ("ai", response.content)
        ]
    }

# ----------------------------------------------------
# Router
# ----------------------------------------------------

def route_query(state: State):

    if state["query_type"] == "academic":
        return "academic_rag"

    elif state["query_type"] == "fee":
        return "fee_rag"

    else:
        return "general"

# ----------------------------------------------------
# Build Graph
# ----------------------------------------------------

graph = StateGraph(State)

graph.add_node("classifier", classifier_node)
graph.add_node("academic_rag", academic_rag_node)
graph.add_node("fee_rag", fee_rag_node)
graph.add_node("general", general_node)
graph.add_node("response", response_node)

graph.add_edge(START, "classifier")

graph.add_conditional_edges(
    "classifier",
    route_query
)

graph.add_edge("academic_rag", "response")
graph.add_edge("fee_rag", "response")
graph.add_edge("general", "response")

graph.add_edge("response", END)

app = graph.compile()

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

st.sidebar.title("Student Details")

programme = st.sidebar.selectbox(
    "Select your Programme",
    [
        "BCA",
        "BBA",
        "B.Com (H)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.success(f"Current Programme: {programme}")

# ----------------------------------------------------
# Chat History
# ----------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------------------------------
# Chat Input
# ----------------------------------------------------

prompt = st.chat_input(
    "Ask your question..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            result = app.invoke(
                {
                    "programme": programme,
                    "messages": [
                        ("human", prompt)
                    ]
                }
            )

            answer = result["messages"][-1].content

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )