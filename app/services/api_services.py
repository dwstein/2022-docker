# app/services/api_services.py

from fastapi import HTTPException
import httpx
import logging

logger = logging.getLogger(__name__)

async def query_ollama_api(model: str, question: str) -> dict:
    url = "http://ollama-container:11434/api/chat"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": question}],
        "stream": False
    }
    try:
        async with httpx.AsyncClient(timeout=20.0) as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as http_err:
        logger.error(f"HTTP status error occurred: {http_err}; Response: {http_err.response.text if http_err.response else 'No response'}")
        raise HTTPException(status_code=500, detail=f"HTTP status error: {http_err.response.text if http_err.response else 'No response'}")
    except httpx.TimeoutException as timeout_err:
        logger.error("Timeout occurred while trying to connect to the Ollama API")
        raise HTTPException(status_code=504, detail="Timeout connecting to the Ollama API. Please try again later.")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="An unexpected error has occurred. Please contact support.")

