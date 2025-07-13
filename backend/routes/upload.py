from fastapi import APIRouter, UploadFile, File
from utils.chunker import chunk_pdf
from vectorstore.faiss_handler import store_chunks

upload_router = APIRouter()

@upload_router.post("/")
async def upload_doc(file: UploadFile = File(...)):
    text_chunks = chunk_pdf(file)
    ids = store_chunks(text_chunks)
    return {"message": "Document processed.", "chunks_stored": len(ids)}