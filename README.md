# 🎓 College Assistant using LangGraph + RAG

An intelligent college assistant chatbot built using **LangGraph**, **LangChain**, **Retrieval-Augmented Generation (RAG)**, **FAISS**, **Groq Llama 3.3**, and **Streamlit**. The assistant answers student queries by intelligently routing them to the appropriate knowledge base, providing accurate responses based on official college documents.

---

## 🚀 Live Demo

**Deployed Application:**  
> 🔗 **[https://college-rag-assistant-jy4htpwsoh3d9qebizaxd7.streamlit.app/]**

Example:

https://college-rag-assistant.streamlit.app

---

## 📂 GitHub Repository

> https://github.com/YOUR_USERNAME/College-RAG-Assistant

---

## ✨ Features

- 📚 Answers academic handbook related questions using RAG
- 💰 Answers fee structure related queries using a separate knowledge base
- 🧠 Automatically classifies user queries using LangGraph conditional routing
- 💬 Supports general conversational questions without retrieval
- 🎓 Personalizes responses based on the selected student programme
- ⚡ Fast semantic search using FAISS Vector Store
- 🤖 Powered by Groq's Llama 3.3 70B model
- 🖥️ Interactive Streamlit chat interface with chat history

---

## 🏗️ System Architecture

```
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
        Streamlit Chat UI
```

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Framework | LangGraph |
| LLM Framework | LangChain |
| Vector Database | FAISS |
| Embeddings | HuggingFace (all-MiniLM-L6-v2) |
| LLM | Groq - Llama 3.3 70B |
| UI | Streamlit |
| Document Loader | PyPDF |
| Environment | Python Dotenv |

---

## 📁 Project Structure

```
College-RAG-Assistant/
│
├── app.py
├── conditional_RAG.py
├── academics_handbook.pdf
├── fee_structure.pdf
├── requirements.txt
├── README.md
├── .gitignore
└── .env (not uploaded)
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/College-RAG-Assistant.git
```

Move into the project directory

```bash
cd College-RAG-Assistant
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project directory.

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will be available at

```
http://localhost:8501
```

---

## 📄 Knowledge Base

This chatbot retrieves information from:

- 📘 Academic Handbook PDF
- 💵 Fee Structure PDF

The assistant automatically selects the appropriate document based on the user's query using LangGraph conditional routing.

---

## 🧠 Workflow

1. User selects their programme.
2. User asks a question.
3. LangGraph classifies the query.
4. Academic queries search the Academic Handbook.
5. Fee-related queries search the Fee Structure document.
6. General questions are answered directly by the LLM.
7. The final response is displayed in the Streamlit interface.

---

## 📸 Screenshots

Add screenshots of your application here after deployment.

Example:

- Home Page
- Chat Interface
- Academic Query Example
- Fee Query Example

---

## 🔮 Future Improvements

- Persistent FAISS index for faster startup
- Conversation memory
- Multiple PDF support
- Source citations in responses
- Chat export feature
- Authentication for students
- Voice input support
- Admin dashboard for document management

---

## 👨‍💻 Author

**Rohit Kaushik**

Mechanical Engineering Undergraduate  
IIT Goa

LinkedIn: *(Add your LinkedIn URL)*

GitHub: *(Add your GitHub Profile URL)*

---

## ⭐ If you found this project useful

If you like this project, consider giving it a ⭐ on GitHub.

It helps others discover the project and supports my work.

---
