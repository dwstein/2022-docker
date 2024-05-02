# app/services/api_services.py

from fastapi import HTTPException
import httpx
import logging
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

logger = logging.getLogger(__name__)

class OllamaService:
    def __init__(self, model_name="gemma:2b"):
        self.base_url = "http://ollama-container:11434/api/chat"
        self.model_name = model_name
        self.headers = {"Content-Type": "application/json"}
        # Define the prompt template
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a world class technical documentation writer."),
            ("user", "{input}")
        ])

    async def format_question(self, question: str) -> str:
        """
        Uses the prompt template to format the question.
        """
        return self.prompt.render({"input": question})

    async def query(self, question: str, session_id: str = None) -> dict:
        """
        Formats the question using the prompt template and sends it to the Ollama API.
        """
        formatted_question = await self.format_question(question)
        payload = {
            "model": self.model_name,
            "question": formatted_question,
            "session_id": session_id  # Include the session ID for context if provided
        }
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(self.base_url, json=payload, headers=self.headers)
                response.raise_for_status()  # Handles HTTP errors
                return response.json()  # Returns the JSON response
        except httpx.HTTPStatusError as exc:
            logger.error(f"HTTP status error occurred: {exc.response.status_code}, {exc.response.text}")
            raise HTTPException(status_code=exc.response.status_code, detail=str(exc.response.text))
        except httpx.RequestError as exc:
            logger.error(f"Network error occurred: {exc}")
            raise HTTPException(status_code=500, detail="Network error during API call to Ollama")
