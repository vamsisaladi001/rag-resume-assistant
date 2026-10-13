# 📄 RAG Resume Assistant using Gemini, LangChain & ChromaDB

## 📌 Overview
This project implements a basic Retrieval-Augmented Generation (RAG) pipeline that allows users to ask questions about a PDF resume. It uses Google Gemini embeddings, ChromaDB for vector storage and similarity search, and a Gemini LLM to generate answers based on retrieved document context.

## 🚀 Features
- **PDF Loading:** Extracts text from PDF documents using PyPDFLoader.
- **Text Chunking:** Splits documents into manageable chunks using RecursiveCharacterTextSplitter.
- **Embeddings:** Converts text into vector representations using Google Gemini Embeddings.
- **Vector Database:** Stores and retrieves relevant document chunks using ChromaDB.
- **Semantic Search:** Retrieves relevant context based on user questions.
- **LLM Integration:** Uses Google Gemini to generate context-aware answers.
- **Prompt Templates:** Structures questions and retrieved context using LangChain PromptTemplate.

## 🛠️ Tech Stack
- Python
- LangChain
- Google Gemini API
- ChromaDB
- Vector Embeddings
- PyPDFLoader

## ⚙️ How It Works
1. Load a PDF resume.
2. Split the extracted text into chunks.
3. Generate embeddings for each chunk.
4. Store the embeddings in ChromaDB.
5. Retrieve relevant chunks based on a user's question.
6. Pass the retrieved context and question to the Gemini LLM.
7. Generate an answer grounded in the retrieved context.

## 📂 Project Structure
```text
rag-resume-assistant/
├── main.py
├── requirements.txt
├── .gitignore
├── .env
└── resume_geetha.pdf
```

## 🔧 Installation

### 1. Clone the repository
```bash
git clone https://github.com/vamsisaladi001/rag-resume-assistant.git
cd rag-resume-assistant
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
```

Windows PowerShell:
```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure your Gemini API key
Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Keep your API key private. Never commit your `.env` file.

### 5. Run the application
Ensure the PDF file configured in `main.py` is available, then run:

```bash
python main.py
```

## 🎯 Learning Outcomes
- Understanding the fundamentals of Retrieval-Augmented Generation (RAG).
- Working with document loaders, text splitters and embeddings.
- Implementing semantic search using a vector database.
- Connecting retrieved context to an LLM for question answering.
- Building a foundation for more advanced AI applications.

## 🔮 Future Improvements
- Support multiple PDF and TXT documents.
- Add conversational memory.
- Build REST APIs using FastAPI.
- Add a web interface for interactive question answering.
- Improve retrieval quality and evaluate answer accuracy.

## 👨‍💻 Author
**Vamsi Saladi**

GitHub: [@vamsisaladi001](https://github.com/vamsisaladi001)

---

⭐ If you find this project useful, feel free to explore the repository and follow my learning journey in Generative AI.
