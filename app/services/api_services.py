# app/services/api_services.py

import httpx

async def query_ollama_api(model: str, question: str) -> dict:
    url = "http://localhost:11434/api/chat"
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": question}
        ]
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)
        return response.json()
