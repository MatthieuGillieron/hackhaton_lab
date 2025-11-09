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
    """
    Appelle l'API LLM Infomaniak
    
    Args:
        messages: Liste des messages (system, user, assistant)
        model: Nom du modèle
        temperature: Température de génération
        max_tokens: Nombre max de tokens
        stream: Activer le streaming
        
    Returns:
        Response object
    """
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


def explain_error_with_llm(code: str, error: str, context: str = "Python") -> str:
    """
    Demande au LLM d'expliquer une erreur de manière pédagogique
    
    Args:
        code: Code qui a généré l'erreur
        error: Message d'erreur
        context: Contexte (Python, JavaScript, etc.)
        
    Returns:
        Explication pédagogique de l'erreur
    """
    prompt = f"""Tu es un professeur de programmation {context} pour débutants. Un élève a écrit ce code :

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
  Exemple : "**print()**" ou "**st.title()**" ou "**if**"
- Le format est toujours : guillemets + astérisques + contenu + astérisques + guillemets : "**contenu**"
- FERME TOUJOURS les astérisques avant de continuer le texte normal
Reste concis et utilise un langage simple. Maximum 3-4 phrases."""

    try:
        response = call_llm(
            messages=[
                {"role": "system", "content": "Tu es un professeur de programmation patient et pédagogue."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300,
            stream=False
        )
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Impossible d'obtenir une explication : {str(e)}"
