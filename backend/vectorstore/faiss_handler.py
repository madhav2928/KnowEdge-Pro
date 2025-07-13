import faiss
import numpy as np
from embedding.factory import get_embedding

_index = faiss.IndexFlatL2(384)  # dim for MiniLM
_corpus = []

# In-memory temporary; can persist using faiss.write_index

def store_chunks(chunks):
    global _corpus
    vectors = get_embedding(chunks)
    _index.add(np.array(vectors).astype('float32'))
    _corpus.extend(chunks)
    return list(range(len(_corpus)))

def retrieve_similar(query: str, top_k=3):
    query_vector = get_embedding([query])
    D, I = _index.search(np.array(query_vector).astype('float32'), top_k)
    return [(_corpus[i], float(D[0][idx])) for idx, i in enumerate(I[0])]