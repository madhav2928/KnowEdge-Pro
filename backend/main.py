from fastapi import FastAPI, UploadFile, File, Form
from routes.upload import upload_router
from routes.query import query_router
from routes.config import config_router
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

from vectorstore.faiss_handler import _corpus, _index

app = FastAPI(title="KnowEdge Pro - AI Knowledge Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"] for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(upload_router, prefix="/upload")
app.include_router(query_router, prefix="/query")
app.include_router(config_router, prefix="/byok")
# Debug endpoint to return all stored chunks and their embeddings
@app.get("/debug/chunks")
def list_chunks_with_embeddings():
    vectors = _index.reconstruct_n(0, _index.ntotal)  # Reconstruct stored vectors
    chunk_embeddings = []
    for i, (text, vector) in enumerate(zip(_corpus, vectors)):
        chunk_embeddings.append({
            "id": i,
            "text": text,
            "embedding": vector.tolist()
        })
    return JSONResponse(content={"chunks": chunk_embeddings})