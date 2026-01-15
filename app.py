import logging
import os
from fastapi import FastAPI
import chromadb
import ollama
import uuid

from pydantic import BaseModel

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

app = FastAPI()
chroma = chromadb.PersistentClient(path="./db")
collection = chroma.get_or_create_collection("docs")
MODEL_NAME = os.environ.get("MODEL_NAME", "tinyllama")
USE_MOCK = os.environ.get("USE_MOCK_LLM", "0") == "1"

logger.info(f"Using model {MODEL_NAME}")


class Update(BaseModel):
    content: str


@app.get("/")
def default():
    return {"message": "Hello world!"}


@app.get("/query")
def query(q: str):
    results = collection.query(query_texts=[q], n_results=1)
    context = results["documents"][0][0] if len(results["documents"][0]) > 0 else ""

    if USE_MOCK:
        return {"answer": context}
    else:
        answer = ollama.generate(
            model=MODEL_NAME,
            prompt=f"Context:\n{context}\n\nQuestion: {q}\n\nAnswer clearly and concisely:",
        )

        logger.info(
            f"Query executed against model:\n\tQuery: {q}\n\tResponse: {answer['response']}"
        )

        return {"answer": answer["response"]}


@app.post("/add")
def add(update: Update):
    id = str(uuid.uuid4())
    collection.add(ids=[id], documents=[update.content])
    logger.info(
        f"Content added to knowledge base:\n\tID: {id}\n\tContent: {update.content}"
    )
    return {"status": "all good"}


@app.get("/health")
def health():
    return {"status": "ok"}
