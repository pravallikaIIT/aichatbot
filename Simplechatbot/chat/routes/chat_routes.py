from fastapi import APIRouter
from pydantic import BaseModel
from services.ollama_service import generate_response

router = APIRouter()

class ChatRequest(BaseModel):
    user_id: str
    message: str

@router.post("/chat")
def chat(request: ChatRequest):
    reply = generate_response(request.user_id, request.message)
    return {"reply": reply}