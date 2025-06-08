from fastapi import APIRouter, File, UploadFile
from rag.document_loader import process_file

router = APIRouter()

@router.post("/")
async def upload_document(file: UploadFile = File(...)):
    result = process_file(file)
    return {"status": "uploaded", "details": result}