"""Client API LLM (Infomaniak)"""
import time
import json
import requests
from typing import Iterator
from src.utils.config import BASE_URL, HEADERS, LLM_MODEL, DEFAULT_TEMPERATURE, DEFAULT_MAX_TOKENS


def stream_llm_response(response: requests.models.Response) -> Iterator[str]:
    """Stream la réponse du LLM ligne par ligne"""
    response_gen = response.iter_lines(decode_unicode=True)
    for line in response_gen:
        if line:
            data = line[len("data: "):]
            if data == "[DONE]":
                yield ""
            else:
                data = json.loads(data)
                assistant_response = data["choices"][0]["delta"].get("content", "")
                yield assistant_response
                time.sleep(0.01)


def call_llm(
    messages: list[dict],
    model: str = LLM_MODEL,
    temperature: float = DEFAULT_TEMPERATURE,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    stream: bool = True
) -> requests.Response:
  
     
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": stream,
    }
    
    response = requests.post(url=BASE_URL, json=payload, headers=HEADERS)
    response.raise_for_status()
    
    return response



