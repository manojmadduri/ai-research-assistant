import os
from .embedder import get_embedding
from .vector_store import create_or_update_index
from PyPDF2 import PdfReader

def process_file(file):
    ext = file.filename.split(".")[-1].lower()
    if ext == "pdf":
        text = extract_text_from_pdf(file)
    else:
        text = file.file.read().decode("utf-8")

    chunks = split_text(text)
    vectors = [get_embedding(chunk) for chunk in chunks]
    create_or_update_index(vectors, chunks)

    save_path = os.path.join("data", "documents", file.filename)
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(text)

    return f"{file.filename} uploaded and indexed with {len(chunks)} chunks."

def extract_text_from_pdf(file):
    reader = PdfReader(file.file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def split_text(text: str, chunk_size: int = 300):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]