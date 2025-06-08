# Utility functionsimport re

def clean_text(text):
    return re.sub(r'\s+', ' ', text.strip())

def count_tokens(text):
    return len(text.split())

def chunk_text(text, chunk_size=300):
    words = text.split()
    return [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
