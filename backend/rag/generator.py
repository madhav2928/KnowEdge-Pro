from llm.factory import get_llm_response
from vectorstore.faiss_handler import retrieve_similar

def generate_answer(question: str):
    context_chunks = retrieve_similar(question)
    context = "\n\n".join([chunk for chunk, _ in context_chunks])
    prompt = f"Answer the following based on the context:\n{context}\n\nQuestion: {question}"
    return get_llm_response(prompt)