import faiss
import numpy as np
import pickle


def create_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

if __name__ == "__main__":
    with open("data/embeddings.pkl", "rb") as f:
        chunks, embeddings = pickle.load(f)

    embeddings_np = np.array(embeddings)
    index = create_faiss_index(embeddings_np)

    faiss.write_index(index, "data/faiss_index.index")
    with open("data/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print("FAISS index built and saved.")
