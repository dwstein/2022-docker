# app/routes/endpoints.py

from typing import Optional
import uuid
import logging
from fastapi import APIRouter, HTTPException, Depends, Response

from ..services.api_services import query_ollama_api
from models.models import Conversation  # Ensure correct relative import path

# Setup logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

router = APIRouter()

# Simulated database or in-memory store for conversations
conversations = {}

def get_or_create_conversation(conversation_id: Optional[str] = None) -> (Conversation, str):
    if conversation_id:
        if conversation_id in conversations:
            logger.info(f"Retrieved existing conversation with ID {conversation_id}")
            return conversations[conversation_id], conversation_id
        else:
            logger.warning(f"Conversation ID {conversation_id} not found in existing records.")
            raise HTTPException(status_code=404, detail="Conversation ID not found")
    else:
        new_conv_id = str(uuid.uuid4())
        new_conv = Conversation()
        conversations[new_conv_id] = new_conv
        logger.info(f"Created new conversation with ID {new_conv_id}")
        return new_conv, new_conv_id


@router.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "The server is running!"}

@router.post("/ask")
async def ask_question(response: Response, model: str, question: str, conversation_id: Optional[str] = None):
    conversation, conv_id = get_or_create_conversation(conversation_id)
    if not conversation_id:
        response.headers['X-Conversation-ID'] = conv_id  # Include the new conversation ID in the response headers
    logger.info(f"Asking question: {question} using model: {model} in conversation: {conv_id}")
    try:
        api_response = await query_ollama_api(model, question, conversation)
        logger.info("Query successful, returning response")
        return api_response
    except Exception as e:
        logger.error(f"Error in ask_question: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal Server Error")

