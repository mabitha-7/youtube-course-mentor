from retriever import search_chunks

question = "What is a neural network?"

results = search_chunks(question)

print("\nTop Retrieved Chunks:\n")

for i, chunk in enumerate(results, start=1):
    print(f"\nChunk {i}:\n")
    print(chunk)
    print("-" * 50)