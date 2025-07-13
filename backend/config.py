import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Existing config
    LLM_PROVIDER = os.getenv("LLM_PROVIDER")
    LLM_MODEL = os.getenv("LLM_MODEL")
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
    EMBEDDING_PROVIDER = os.getenv("EMBEDDING_PROVIDER")
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")
    HF_API_TOKEN = os.getenv("HF_API_TOKEN")

    # 🆕 New universal LLM config
    LLM_API_URL = os.getenv("LLM_API_URL")
    LLM_API_METHOD = os.getenv("LLM_API_METHOD", "POST")
    LLM_API_KEY_HEADER = os.getenv("LLM_API_KEY_HEADER", "Authorization")
    LLM_API_KEY_PREFIX = os.getenv("LLM_API_KEY_PREFIX", "")  # e.g., Bearer
    LLM_API_KEY = os.getenv("LLM_API_KEY")
    LLM_REQUEST_BODY_TEMPLATE = os.getenv("LLM_REQUEST_BODY_TEMPLATE")
    LLM_RESPONSE_JSON_PATH = os.getenv("LLM_RESPONSE_JSON_PATH")  # e.g., choices.0.message.content