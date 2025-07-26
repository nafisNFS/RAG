

from fastapi import FastAPI
from pydantic import BaseModel
from retriever import Retriever
from generator import generate_answer

app = FastAPI()
retriever = Retriever()

class Query(BaseModel):
    query: str

@app.post("/ask")
def ask(q: Query):
    chunks = retriever.get_top_chunks(q.query)
    context = "\n".join(chunks)
    answer = generate_answer(q.query, context)
    return {"answer": answer}
