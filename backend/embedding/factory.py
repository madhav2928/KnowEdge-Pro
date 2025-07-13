from config import Config
from sentence_transformers import SentenceTransformer

_model = None

def get_embedding_model():
    global _model
    if not _model:
        _model = SentenceTransformer(Config.EMBEDDING_MODEL)
    return _model

def get_embedding(texts: list[str]) -> list[list[float]]:
    model = get_embedding_model()
    return model.encode(texts, convert_to_numpy=True).tolist()
