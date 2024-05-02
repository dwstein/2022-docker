# app/services/api_services.py


from fastapi import HTTPException
import httpx
import logging
import json
from models.models import Conversation  # Ensure you import your Conversation model

logger = logging.getLogger(__name__)

def parse_json_response(raw_json):
    """ Attempt to parse multiple JSON objects if found. """
    try:
        objs = []
        idx = 0
        while idx != len(raw_json):
            obj, idx = json.JSONDecoder().raw_decode(raw_json, idx=idx)
            objs.append(obj)
            raw_json = raw_json[idx:].strip()
            idx = 0 if raw_json else len(raw_json)
        return objs
    except json.JSONDecodeError as e:
        logger.error("Failed to decode JSON: " + str(e))
        raise

async def query_ollama_api(model: str, question: str, conversation: Conversation) -> dict:
    url = "http://ollama-container:11434/api/chat"
    payload = {
        "model": model,
        "messages": conversation.get_history() + [{"role": "user", "content": question}],
        "stream": False
    }
    try:
        async with httpx.AsyncClient(timeout=20.0) as client:
            response = await client.post(url, json=payload)
            response.raise_for_status()
            try:
                # First try parsing normally
                answer = response.json()
            except json.JSONDecodeError:
                # If normal parsing fails, attempt to parse multiple JSON objects
                answer = parse_json_response(response.text)
                if not answer:
                    raise HTTPException(status_code=500, detail="Invalid JSON response")
            # Assuming the relevant information is in the first JSON object if multiple were parsed
            first_answer = answer[0] if isinstance(answer, list) else answer
            conversation.add_message("user", question)
            conversation.add_message("llm", first_answer.get("message", {}).get("content", ""))
            return first_answer
    except httpx.HTTPStatusError as http_err:
        logger.error("HTTP status error occurred: {0}".format(http_err))
        raise HTTPException(status_code=http_err.response.status_code, detail=str(http_err.response.text))
    except httpx.RequestError as req_err:
        logger.error("Request failed: {0}".format(req_err))
        raise HTTPException(status_code=500, detail="Network error")

