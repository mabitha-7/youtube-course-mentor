
🎓 AI-Powered YouTube Course Mentor using RAG

An AI-powered learning assistant that transforms YouTube educational videos into an interactive learning experience using Retrieval-Augmented Generation (RAG).

The application extracts video transcripts, converts them into vector embeddings, stores them in a ChromaDB vector database, and retrieves the most relevant content to generate accurate answers using Google Gemini.
<img width="277" height="410" alt="image" src="https://github.com/user-attachments/assets/cbf89eaf-b872-45bf-ab0c-7624889e67a9" />


## 🚀 Features

- 🎥 Extracts YouTube video transcripts
- 🤖 AI-powered Question Answering using RAG
- 🔍 Semantic Search with Vector Embeddings
- 🧠 Context-aware responses using Google Gemini
- 📚 ChromaDB Vector Database
- 💬 Interactive React-based Chat Interface
- ⚡ FastAPI Backend

---

## 🛠️ Tech Stack

### Frontend
- React.js
- CSS

### Backend
- Python
- FastAPI

### AI & RAG
- Google Gemini
- LangChain
- ChromaDB
- Sentence Transformers

### Other Tools
- YouTube Transcript API

---

## 📂 Project Structure

```
youtube-course-mentor
│
├── backend
│   ├── main.py
│   ├── rag_chat.py
│   ├── retriever.py
│   ├── vector_store.py
│   └── youtube_utils.py
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/mabitha-7/youtube-course-mentor.git
```

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

uvicorn main:app --reload
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## 🎯 Workflow

```
YouTube Video
      │
      ▼
Transcript Extraction
      │
      ▼
Chunking
      │
      ▼
Vector Embeddings
      │
      ▼
ChromaDB
      │
      ▼
User Question
      │
      ▼
Retriever
      │
      ▼
Google Gemini
      │
      ▼
AI Response
```

---

## 📌 Future Enhancements

- 🎤 Voice-based Question Answering
- 📝 AI Notes Generator
- 📚 Playlist Support
- 🧩 Quiz Generation
- 📈 Learning Progress Tracker
- ⏱️ Timestamp-based Answers

---

## 👩‍💻 Developed By

**Mabitha M**

B.Tech – Artificial Intelligence & Machine Learning
