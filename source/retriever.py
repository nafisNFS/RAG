

import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

class Retriever:
    def __init__(self, model_name="BAAI/bge-m3"):
        self.model = SentenceTransformer(model_name)
        self.index = faiss.read_index("data/faiss_index.index")
        with open("data/chunks.pkl", "rb") as f:
            self.chunks = pickle.load(f)

    def get_top_chunks(self, query, top_k=3):
        query_vec = self.model.encode([query])
        D, I = self.index.search(np.array(query_vec), top_k)
        return [self.chunks[i] for i in I[0]]

if __name__ == "__main__":
    retriever = Retriever()
    query = "বিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?"
    results = retriever.get_top_chunks(query)
    for i, r in enumerate(results):
        print(f"Chunk {i+1}:\n{r}\n")
