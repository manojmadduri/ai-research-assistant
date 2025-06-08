from fastapi import APIRouter
from pydantic import BaseModel

from rag.retriever import search_documents
from llm.response_generator import generate_response

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/")
async def query_ai(req: QueryRequest):
    documents = search_documents(req.query)
    response = generate_response(req.query, documents)
    return {"response": response}