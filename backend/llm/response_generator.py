from agents.base_agent import run_agent

def generate_response(query: str, docs: list):
    context = "\n".join(docs)
    enriched_prompt = f"Use the context below to help answer the question:\n\n{context}\n\nQuestion: {query}"
    return run_agent(enriched_prompt)