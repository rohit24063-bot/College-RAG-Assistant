# College Assistant using LangGraph + RAG

A Retrieval-Augmented Generation (RAG) chatbot built using **LangGraph**, **LangChain**, **FAISS**, **Groq Llama 3.3**, and **Streamlit**. The application automatically classifies student queries and retrieves information from the appropriate college documents to generate accurate responses.

## Live Demo

**Application:**  
https://college-rag-assistant-jy4htpwsoh3d9qebizaxd7.streamlit.app/

## Features

- Answers academic handbook related queries using RAG
- Answers fee structure related queries using a dedicated knowledge base
- Automatic query classification using LangGraph conditional routing
- Handles general conversations without document retrieval
- Personalized responses based on the selected student programme
- Semantic search using FAISS and HuggingFace embeddings
- Interactive Streamlit chat interface with conversation history

---

## System Architecture

```text
                User Question
                      │
                      ▼
             Query Classification
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
 Academic Query    Fee Query    General Query
        │             │             │
        ▼             ▼             ▼
 Academic RAG     Fee RAG       LLM Only
        │             │
        └──────┬──────┘
               ▼
       Response Generation
               ▼
        Streamlit Interface
```

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | LangGraph |
| LLM Framework | LangChain |
| Vector Store | FAISS |
| Embeddings | HuggingFace (all-MiniLM-L6-v2) |
| LLM | Groq Llama 3.3 70B |
| UI | Streamlit |
| Document Loader | PyPDF |
| Environment | Python Dotenv |

---

## Project Structure

```text
College-RAG-Assistant/
│
├── app.py
├── conditional_RAG.py
├── academics_handbook.pdf
├── fee_structure.pdf
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/College-RAG-Assistant.git
```

Move into the project directory:

```bash
cd College-RAG-Assistant
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## Running the Application

```bash
streamlit run app.py
```

The application will be available at:

```
http://localhost:8501
```

---

## Workflow

1. User selects their programme.
2. User submits a query.
3. LangGraph classifies the query.
4. Academic queries search the Academic Handbook.
5. Fee-related queries search the Fee Structure document.
6. General queries are answered directly by the LLM.
7. The response is displayed in the Streamlit interface.

---

## Future Improvements

- Persistent FAISS index
- Multi-document support
- Conversation memory
- Source citations
- Chat export
- Voice input
- Authentication
- Admin document management

---

## Author

**Rohit Kaushik**

Mechanical Engineering Undergraduate  
IIT Goa

GitHub: https://github.com/YOUR_GITHUB_USERNAME

LinkedIn: https://linkedin.com/in/YOUR_LINKEDIN_USERNAME
