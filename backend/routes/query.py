from fastapi import APIRouter, Form
from rag.generator import generate_answer

query_router = APIRouter()

@query_router.post("/")
async def ask_question(query: str = Form(...)):
    response = generate_answer(query)
    return {"answer": response}