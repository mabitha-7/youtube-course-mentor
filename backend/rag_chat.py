import os
from dotenv import load_dotenv
import google.generativeai as genai

from retriever import search_chunks

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_question(question):

    chunks = search_chunks(question)

    context = "\n\n".join(chunks)

    prompt = f"""
You are UMATE, an AI YouTube Learning Assistant.

Rules:
1. Answer ONLY from the provided context.
2. If the answer is not available in the context, say:
   "This topic is not covered in the uploaded video."
3. Keep answers clear and concise.

Context:
{context}

Question:
{question}
"""

    try:

        print("Calling Gemini...")

        response = model.generate_content(prompt)

        print("Gemini Success")

        return response.text

    except Exception as e:

        print("Gemini Error:", e)

        if len(context) > 0:
            return (
                "Gemini quota exceeded. Relevant content from the video:\n\n"
                + context[:1000]
            )

        return "This topic is not covered in the uploaded video."