import logging
import os
from fastapi import FastAPI, HTTPException
from starlette.concurrency import run_in_threadpool
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
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")
USE_MOCK = os.environ.get("USE_MOCK_LLM", "0") == "1"

logger.info(f"Using model {MODEL_NAME}")

client = ollama.AsyncClient(host=OLLAMA_HOST)


class Update(BaseModel):
    content: str


@app.get("/")
def default():
    return {"message": "Hello world!"}


@app.get("/query")
async def query(q: str):
    results = await run_in_threadpool(
        collection.query, query_texts=[q], n_results=1
    )

    context = (
        results["documents"][0][0]
        if results["documents"] is not None
        and len(results["documents"]) > 0
        and len(results["documents"][0]) > 0
        else ""
    )

    if USE_MOCK:
        return {"answer": context}
    else:
        try:
            answer = await client.generate(
                model=MODEL_NAME,
                prompt=f"Context:\n{context}\n\nQuestion: {q}\n\nAnswer clearly and concisely:",
            )

            logger.info(
                f"Query executed against model:\n\tQuery: {q}\n\tResponse: {answer['response']}"
            )

            return {"answer": answer["response"]}
        except ollama.ResponseError as e:
            logger.error(f"ResponseError from ollama. Status code: {e.status_code}")
            if e.status_code == 404:
                logger.info(f"Pulling {MODEL_NAME}")
                await client.pull(MODEL_NAME)
                answer = await client.generate(
                    model=MODEL_NAME,
                    prompt=f"Context:\n{context}\n\nQuestion: {q}\n\nAnswer clearly and concisely:",
                )

                logger.info(
                    f"Query executed against model:\n\tQuery: {q}\n\tResponse: {answer['response']}"
                )

                return {"answer": answer["response"]}
            else:
                raise HTTPException(status_code=500, detail="Server error")
        except Exception:
            logger.exception(
                f"Error querying model {MODEL_NAME} at {OLLAMA_HOST}"
            )
            raise HTTPException(
                status_code=500,
                detail="Server error",
            )


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
