"""Gestion de la base vectorielle ChromaDB"""

import streamlit as st
import chromadb
from chromadb import Collection
from src.core.embeddings import MultilingualGemma2
from src.utils.config import DB_PATH, MODEL_NAME


@st.cache_resource
def get_db_collection(path: str = DB_PATH, model_name: str = MODEL_NAME) -> Collection:
    """Récupère la collection ChromaDB avec cache Streamlit"""
    client = chromadb.PersistentClient(path=path)

    collection = client.get_collection(
        name="main-gemma",
        embedding_function=MultilingualGemma2(model_name),
    )

    return collection


def query_rag(
    collection: Collection, query: str, n_results: int = 5
) -> tuple[list[str], list[str]]:
    """
    Interroge la base RAG

    Returns:
        tuple: (ids, documents)
    """
    query_results = collection.query(
        query_texts=[query],
        n_results=n_results,
    )

    ids = query_results["ids"][0]
    docs = query_results["documents"][0]

    return ids, docs
