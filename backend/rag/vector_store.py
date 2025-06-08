import os
import faiss
import pickle
import numpy as np

INDEX_FILE = "data/vector_store/faiss.index"
META_FILE = "data/vector_store/metadata.pkl"

def save_index(index, metadata):
    faiss.write_index(index, INDEX_FILE)
    with open(META_FILE, "wb") as f:
        pickle.dump(metadata, f)

def load_index():
    if not os.path.exists(INDEX_FILE):
        return None, []
    index = faiss.read_index(INDEX_FILE)
    with open(META_FILE, "rb") as f:
        metadata = pickle.load(f)
    return index, metadata

def create_or_update_index(new_vectors: list, new_texts: list):
    dim = len(new_vectors[0])
    index, metadata = load_index()

    if index is None:
        index = faiss.IndexFlatL2(dim)
        metadata = []

    index.add(np.array(new_vectors).astype("float32"))
    metadata.extend(new_texts)

    save_index(index, metadata)
    return len(metadata)