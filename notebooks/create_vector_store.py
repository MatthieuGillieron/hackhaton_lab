import chromadb
from sentence_transformers import SentenceTransformer
from chromadb import Documents, EmbeddingFunction, Embeddings
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import requests


DB_PATH = "./data/"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"


class SentenceTransformerFunction(EmbeddingFunction):
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name
        self.model = SentenceTransformer(self.model_name)

    def __call__(self, input_data: Documents) -> Embeddings:
        embeddings = self.model.encode(input_data)
        return embeddings


def url_to_string(url: str) -> str:
    if not url.startswith("https://"):
        url = "https://" + url

    res = requests.get(url, headers=HEADERS)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    site_text = " ".join([text for text in soup.stripped_strings])
    return site_text


client = chromadb.PersistentClient(path=DB_PATH)

# data processing
df = pd.read_csv("./data/processed-links.csv")

ids: list[str] = df["title"].to_list()
documents: list[str] = df["text_summary"].to_list()
metadatas: list[dict[str, str]] = df.loc[:, ["title", "type", "url"]].to_dict("records")

# create and add to vector store
collection = client.create_collection(
    name="main",
    embedding_function=SentenceTransformerFunction(MODEL_NAME),
)

collection.add(
    ids=ids,
    metadatas=metadatas,
    documents=documents,
)
