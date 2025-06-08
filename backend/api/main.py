from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import query, upload
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI Research Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(query.router, prefix="/query", tags=["Query"])
app.include_router(upload.router, prefix="/upload", tags=["Upload"])

@app.get("/")
def root():
    return {"message": "AI Research Assistant is running"}