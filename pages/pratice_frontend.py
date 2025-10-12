import streamlit as st
import os
import requests
from io import StringIO
from contextlib import redirect_stdout
from dotenv import load_dotenv

st.set_page_config(
    page_title="Frontend - Pratique",
    page_icon="🌐",
    layout="wide"
)

from config.app import setup_sidebar

load_dotenv()

try:
    from streamlit_monaco import st_monaco
    HAS_MONACO = True
except ImportError:
    HAS_MONACO = False

# Configuration API
API_TOKEN = os.getenv("API_TOKEN")
PRODUCT_ID = os.getenv("PRODUCT_ID")
BASE_URL = f"https://api.infomaniak.com/1/ai/{PRODUCT_ID}/openai/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def explain_error_with_llm(code: str, error: str) -> str:
    """Demande au LLM d'expliquer l'erreur de manière pédagogique"""
    prompt = f"""Tu es un professeur de programmation Python pour débutants. Un élève a écrit ce code :

```python
{code}
```

Il a obtenu cette erreur :
```
{error}
```

Explique-lui de manière simple et pédagogique :
1. Quelle est l'erreur
2. Pourquoi elle se produit
3. Comment la corriger

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

# Configuration de la sidebar
setup_sidebar()

# Bouton retour
if st.button("← Retour à la sélection"):
    st.switch_page("pages/pratice.py")

# Titre et sous-titre
st.title("🌐 Développement Frontend")
st.write("### Module de pratique en Développement Frontend")
st.write("---")

# Section Introduction (gauche) et Bienvenue (droite)
col_intro, col_welcome = st.columns(2)

with col_intro:
    st.info("""📚 **Documentation Streamlit**

Voici les commandes Streamlit à connaître :
- `st.title("Mon titre")` : Affiche un titre principal
- `st.header("Mon en-tête")` : Affiche un sous-titre
- `st.write("Mon texte")` : Affiche du texte simple
- `st.balloons()` : Déclenche l'effet des ballons 🎈
- `st.snow()` : Déclenche l'effet de neige ❄️
""")

with col_welcome:
    st.info("""💡 **Exercice pratique**

**Objectif** : Créer une page Streamlit simple

1. Utilise `st.title()` pour créer un titre
2. Ajoute du texte avec `st.write()`
3. Déclenche l'effet des ballons avec `st.balloons()`
4. Clique sur Exécuter pour voir le résultat !
""")

st.write("---")

# Initialiser le code par défaut
if 'frontend_code' not in st.session_state:
    st.session_state['frontend_code'] = """# Créez votre page Streamlit ici !
st.title("Ma première page Streamlit")
st.write("Bienvenue dans le monde du développement frontend !")
st.balloons()
"""

# Initialiser le dernier code exécuté
if 'frontend_last_executed' not in st.session_state:
    st.session_state['frontend_last_executed'] = None

# Section IDE (gauche) et Output (droite)
# IDE 45%, Aperçu 55%
col_ide, col_output = st.columns([45, 55])

with col_ide:
    st.subheader("🖥️ Éditeur de Code Streamlit")
    
    # Utiliser text_area pour une édition stable
    current_code = st.text_area(
        "Code Streamlit",
        value=st.session_state['frontend_code'],
        height=300,
        key="code_editor_frontend",
        help="Écrivez votre code Streamlit ici",
        label_visibility="collapsed"
    )
    
    # Boutons en dessous de l'éditeur
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        if st.button("▶️ Exécuter", use_container_width=True, type="primary", key="exec_btn"):
            # Sauvegarder le code et marquer comme devant être exécuté
            st.session_state['frontend_code'] = current_code
            st.session_state['frontend_last_executed'] = current_code
            st.rerun()
    with btn_col2:
        if st.button("🔄 Réinitialiser", use_container_width=True):
            st.session_state['frontend_code'] = """# Créez votre page Streamlit ici !
st.title("Ma première page Streamlit")
st.write("Bienvenue dans le monde du développement frontend !")
st.balloons()
"""
            st.session_state['frontend_last_executed'] = None
            st.rerun()

with col_output:
    st.subheader("📤 Aperçu de votre page")
    
    # CSS pour limiter la hauteur de l'aperçu
    st.markdown("""
        <style>
        /* Limiter la hauteur du container d'aperçu */
        div[data-testid="stVerticalBlock"] > div:has(> div > h3:contains("Aperçu")) {
            max-height: 500px;
            overflow-y: auto;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Container Streamlit natif avec bordure
    with st.container(border=True, height=500):
        # Zone de résultat
        if st.session_state['frontend_last_executed'] is not None:
            try:
                # Exécuter le dernier code validé dans ce container
                exec(st.session_state['frontend_last_executed'])
                
            except Exception as e:
                st.error(f"❌ Erreur lors de l'exécution :")
                st.code(str(e), language="text")
                
                # Demander au LLM d'expliquer l'erreur
                st.write("---")
                st.write("🤖 **Explication de l'erreur par l'assistant IA :**")
                
                with st.spinner("L'assistant analyse votre erreur..."):
                    explanation = explain_error_with_llm(
                        st.session_state['frontend_last_executed'], 
                        str(e)
                    )
                
                st.info(explanation)
        else:
            # Message par défaut
            st.markdown(
                """
                <div style="height: 400px; display: flex; align-items: center; justify-content: center; color: #888;">
                    <p style="text-align: center;">Aucun aperçu pour le moment.<br>Exécutez votre code pour voir le résultat ici.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
