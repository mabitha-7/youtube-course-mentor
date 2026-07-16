from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from youtube_utils import get_transcript
from rag_utils import split_text
from vector_store import store_chunks, clear_collection
from rag_chat import ask_question
from retriever import search_chunks

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "UMATE Backend Running"
    }


@app.get("/transcript/{video_id}")
def transcript(video_id: str):
    try:
        transcript_text = get_transcript(video_id)

        # Split transcript into chunks
        chunks = split_text(transcript_text)

        # Remove old video data
        clear_collection()

        # Store new video chunks
        store_chunks(chunks)

        return {
            "success": True,
            "transcript": transcript_text,
            "chunks_stored": len(chunks)
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


@app.post("/ask")
def ask(data: QuestionRequest):

    chunks = search_chunks(data.question)

    answer = ask_question(data.question)

    return {
        "success": True,
        "answer": answer,
        "sources": chunks
    }