import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

PRODUCT_ID = os.getenv("PRODUCT_ID")
API_TOKEN = os.getenv("API_TOKEN")

BASE_URL = f"https://api.infomaniak.com/1/ai/{PRODUCT_ID}/openai/chat/completions"
HEADERS = {
"Authorization": f"Bearer {API_TOKEN}",
"Content-Type": "application/json"
}

def llm_call(query: str) -> None:
    data = {
        "model": "llama3",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant. Be concise."},
            {"role": "user", "content": "Quelle est la couleur du lac Léman?"}
        ],
        "temperature": 0.2, # what value to use here? 
        "stream": True,
    }
    response = requests.request("POST", url=BASE_URL, json=data, headers=HEADERS)

    # TODO: catch possible exceptions here
    print(response.status_code)

    for line in response.iter_lines(decode_unicode=True):
        if line:
            data = line[len("data: "):]
            if data == "[DONE]":
                print()
                break
            else:
                data = json.loads(data)
                out = data["choices"][0]["delta"].get("content", "")
                print(out, end="", flush=True)


user_query = "Quelle est la couleur du lac Léman?"
llm_call(user_query)
