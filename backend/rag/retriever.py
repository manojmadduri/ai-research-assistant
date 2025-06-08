from .vector_store import load_index
from .embedder import get_embedding
import numpy as np

def search_documents(query: str, top_k: int = 3):
    index, metadata = load_index()
    if not index or not metadata:
        return ["No documents in the vector store"]

    query_vector = np.array([get_embedding(query)]).astype("float32")
    D, I = index.search(query_vector, top_k)
    return [metadata[i] for i in I[0] if i < len(metadata)]