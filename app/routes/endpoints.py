# app/routes/endpoints.py

from fastapi import APIRouter, HTTPException

from ..services.api_services import query_ollama_api

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "The server is running!"}

@router.post("/ask")
async def ask_question(model: str, question: str):
    try:
        response = await query_ollama_api(model, question)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

