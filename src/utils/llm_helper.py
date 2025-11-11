"""Helper pour LLM et formatage des erreurs"""
import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
PRODUCT_ID = os.getenv("PRODUCT_ID")
BASE_URL = f"https://api.infomaniak.com/1/ai/{PRODUCT_ID}/openai/chat/completions"
HEADERS = {"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"}

def explain_error_with_llm(code: str, error: str, context: str = "Python") -> str:
    """Demande au LLM d'expliquer l'erreur de manière pédagogique"""
    prompt = f"""Tu es un professeur de programmation pour débutants. Un élève a écrit ce code {context} :

{code}

Il a obtenu cette erreur :
{error}

Explique-lui de manière simple et pédagogique :
1. Quelle est l'erreur
2. Pourquoi elle se produit
3. Comment la corriger

IMPORTANT - Format à respecter EXACTEMENT :
- N'utilise JAMAIS de backticks (``` ou ` simple).
- Pour les variables/fonctions/mots-clés : mets-les entre guillemets doubles avec le contenu en gras
  Exemple : "**print()**" ou "**haut()**" ou "**if**"
- Le format est toujours : guillemets + astérisques + contenu + astérisques + guillemets : "**contenu**"
- FERME TOUJOURS les astérisques avant de continuer le texte normal
Reste concis et utilise un langage simple. Maximum 3-4 phrases."""

    payload = {
        "model": "qwen3",
        "messages": [
            {"role": "system", "content": "Tu es un professeur de programmation patient et pédagogue."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 300
    }
    
    try:
        response = requests.post(BASE_URL, headers=HEADERS, json=payload, timeout=10)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Impossible d'obtenir une explication : {str(e)}"

def format_error_explanation(explanation: str) -> str:
    """Formate l'explication en HTML"""
    html = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', explanation)
    html = re.sub(r'`([^`]+)`', r'"<strong>\1</strong>"', html)
    html = html.replace("\n", "<br>")
    
    return f"""
    <div style="
        background: linear-gradient(135deg, rgba(222, 56, 142, 0.08), rgba(18, 170, 178, 0.08));
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border-radius: 15px;
        border: 1px solid rgba(222, 56, 142, 0.2);
        padding: 20px;
        box-shadow: 0 2px 8px 0 rgba(0, 0, 0, 0.08);
        margin-top: 10px;
    ">
        <h4 style="color: #c81e70; margin-top: 0; font-size: 1.1em; font-weight: 600; margin-bottom: 15px;">🧠 Explication de l'erreur par Sparky</h4>
        <p style="color: #1a1a1a; line-height: 1.6; margin-bottom: 0;">{html}</p>
    </div>
    """

# CSS partagé pour toutes les pages
SHARED_CSS = """
<style>
    header[data-testid="stHeader"] {
        background-color: transparent !important;
        height: 0 !important;
    }
    
    section.main > div {
        padding-top: 2rem !important;
    }
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 1rem !important;
        max-width: 100% !important;
    }
    
    section[data-testid="stVerticalBlock"] > div:first-child {
        padding-top: 0 !important;
    }
    
    button[kind="primary"] {
        background: linear-gradient(135deg, rgba(222, 56, 142, 0.15), rgba(18, 170, 178, 0.15)) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        border: 1px solid rgba(222, 56, 142, 0.3) !important;
        color: #de388e !important;
        font-weight: 600 !important;
        box-shadow: 0 2px 8px 0 rgba(0, 0, 0, 0.08) !important;
    }
    
    button[kind="primary"]:hover {
        background: linear-gradient(135deg, rgba(222, 56, 142, 0.25), rgba(18, 170, 178, 0.25)) !important;
        border: 1px solid rgba(222, 56, 142, 0.5) !important;
        box-shadow: 0 4px 12px rgba(222, 56, 142, 0.2) !important;
        transform: translateY(-1px) !important;
    }
    
    button[kind="secondary"] {
        background: white !important;
        border: 1px solid rgba(222, 56, 142, 0.5) !important;
        color: #de388e !important;
        box-shadow: 0 2px 8px 0 rgba(0, 0, 0, 0.05) !important;
    }
    
    button[kind="secondary"]:hover {
        background: rgba(222, 56, 142, 0.1) !important;
        border: 1px solid rgba(222, 56, 142, 0.8) !important;
    }
    
    section[data-testid="stVerticalBlock"] div[style*="border: 1px solid rgba(49, 51, 63, 0.2)"] {
        background: linear-gradient(135deg, rgba(222, 56, 142, 0.04), rgba(18, 170, 178, 0.04)) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        border-radius: 15px !important;
        border: 1px solid rgba(222, 56, 142, 0.2) !important;
        padding: 20px !important;
        box-shadow: 0 2px 8px 0 rgba(0, 0, 0, 0.08) !important;
    }
    
    section[data-testid="stSidebar"] div[data-testid="stButton"] button,
    section[data-testid="stSidebar"] div[data-testid="stButton"] button:active,
    section[data-testid="stSidebar"] div[data-testid="stButton"] button:focus,
    section[data-testid="stSidebar"] div[data-testid="stButton"] button:focus-visible {
        background: transparent !important;
        background-color: transparent !important;
        background-image: none !important;
        border: 1.5px solid rgba(255, 255, 255, 0.3) !important;
        color: white !important;
        font-weight: 500 !important;
        font-size: 0.8rem !important;
        padding: 0.35rem 0.6rem !important;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15) !important;
        transition: all 0.3s ease !important;
    }
    
    section[data-testid="stSidebar"] div[data-testid="stButton"] button:hover {
        background: rgba(255, 255, 255, 0.1) !important;
        background-color: rgba(255, 255, 255, 0.1) !important;
        background-image: none !important;
        border: 2px solid rgba(255, 255, 255, 0.5) !important;
        color: white !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.25) !important;
    }
</style>
"""

def create_info_section(title: str, items: list[str]) -> str:
    """Crée une section d'information avec style glassmorphism"""
    items_html = "".join([f"<li>{item}</li>" for item in items])
    return f"""
    <div style="
        background: linear-gradient(135deg, rgba(222, 56, 142, 0.08), rgba(18, 170, 178, 0.08));
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border-radius: 15px;
        border: 1px solid rgba(222, 56, 142, 0.2);
        padding: 20px;
        box-shadow: 0 2px 8px 0 rgba(0, 0, 0, 0.08);
    ">
        <h4 style="color: #c81e70; margin-top: 0; font-size: 1.1em; font-weight: 600;">{title}</h4>
        <ul style="color: #1a1a1a;">{items_html}</ul>
    </div>
    """

def create_two_column_info(sections: list[dict]) -> str:
    """Crée une grille 2 colonnes avec sections d'info"""
    sections_html = "".join([create_info_section(s["title"], s["items"]) for s in sections])
    return f"""
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
        {sections_html}
    </div>
    """
