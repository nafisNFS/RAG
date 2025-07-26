

from sentence_transformers import SentenceTransformer
import pickle

def embed_chunks(chunks, model_name="BAAI/bge-m3"):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(chunks, show_progress_bar=True)
    return embeddings

if __name__ == "__main__":
    with open("data/chunks.txt", "r", encoding="utf-8") as f:
        chunks = [c.strip() for c in f.read().split("\n\n") if c.strip()]

    embeddings = embed_chunks(chunks)

    with open("data/embeddings.pkl", "wb") as f:
        pickle.dump((chunks, embeddings), f)

    print("Embeddings saved.")
