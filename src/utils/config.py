"""Configuration centralisée de l'application"""
import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
API_TOKEN = os.getenv("API_TOKEN")
PRODUCT_ID = os.getenv("PRODUCT_ID")
BASE_URL = f"https://api.infomaniak.com/1/ai/{PRODUCT_ID}/openai/chat/completions"
EMBEDDINGS_URL = f"https://api.infomaniak.com/1/ai/{PRODUCT_ID}/openai/v1/embeddings"

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

# Model Configuration
MODEL_NAME = "bge_multilingual_gemma2"
LLM_MODEL = "qwen3"

# Paths
DB_PATH = "data/"

# LLM Parameters
DEFAULT_TEMPERATURE = 0.5
DEFAULT_MAX_TOKENS = 500
