"""Classes d'embeddings pour ChromaDB"""

import numpy as np
import requests
from chromadb import Documents, EmbeddingFunction, Embeddings
from src.utils.config import PRODUCT_ID, API_TOKEN


class MultilingualGemma2(EmbeddingFunction):
    """Embedding function utilisant l'API Infomaniak"""

    def __init__(self, model_name: str) -> None:
        self.model_name = model_name
        self.url = f"https://api.infomaniak.com/1/ai/{PRODUCT_ID}/openai/v1/embeddings"
        self.headers = {
            "Authorization": f"Bearer {API_TOKEN}",
            "Content-Type": "application/json",
        }

    def __call__(self, input_data: Documents) -> Embeddings:
        payload = {
            "input": input_data,
            "model": self.model_name,
        }

        req = requests.post(url=self.url, json=payload, headers=self.headers)
        res = req.json()
        data = res["data"]
        embeddings = [np.array(x["embedding"]) for x in data]

        return embeddings
