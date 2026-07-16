import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="youtube_course"
)


def clear_collection():
    try:
        data = collection.get()

        if len(data["ids"]) > 0:
            collection.delete(
                ids=data["ids"]
            )

    except Exception as e:
        print("Collection Clear Error:", e)


def store_chunks(chunks):

    embeddings = model.encode(chunks).tolist()

    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )

    return len(chunks)