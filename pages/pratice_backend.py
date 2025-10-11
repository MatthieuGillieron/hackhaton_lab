import streamlit as st
import os
import requests
from io import StringIO
from contextlib import redirect_stdout
from dotenv import load_dotenv

st.set_page_config(
    page_title="Backend - Pratique",
    page_icon="💻",
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
st.title("💻 Développement Backend")
st.write("### Module de pratique en Développement Backend")
st.write("---")

# Section Introduction (gauche) et Bienvenue (droite)
col_intro, col_welcome = st.columns(2)

with col_intro:
    st.info("""📚 **Documentation**

Voici quelque points clés à connaitre :
- personage_1 est une varibale : on peut lui donner une valeur
- print est une fonction qui permet d'afficher un message à l'écran
- Pourafficher du texte avec print(), on doit le mettre entre guillemets
- Pour recuperer la valeur d'une variable, on doit l'appeler sans les guillemets
""")

with col_welcome:
    st.info("""💡 **Guide de pratique**

Lis bien la documentation et essaie de comprendre les points clés.
- Ensuite rend toi dans l'éditeur de code en dessous
- Essaie de comprendre le code
- Modifie, regarde ce qu'il ce passe
- Et essaie de finir l'exercice
""")

st.write("---")

# Initialiser le code par défaut
if 'backend_code' not in st.session_state:
    st.session_state['backend_code'] = """# Écrivez votre code Python ici
personnage_1 = "Christophe"
personnage_2 = "Frederic"

#print est une fonction qui permet d'afficher un message à l'écran
print("Salut, je m'appelle", personnage_1, "et toi ?")
print("Salut", personnage_1, "je m'appelle", personnage_2)
"""

# Initialiser l'état d'exécution
if 'run_backend_code' not in st.session_state:
    st.session_state['run_backend_code'] = False

# Section IDE (gauche) et Output (droite)
col_ide, col_output = st.columns(2)

with col_ide:
    st.subheader("🖥️ Éditeur de Code Python")
    
    # Éditeur de code avec coloration syntaxique Monaco
    if HAS_MONACO:
        content = st_monaco(
            value=st.session_state['backend_code'],
            height="180px",
            language="python",
            lineNumbers=True,
            minimap=False,
            theme="vs-dark"
        )
        # Sauvegarder le contenu de l'éditeur
        if content is not None:
            st.session_state['backend_code'] = content
    else:
        # Fallback vers text_area classique si le package n'est pas installé
        code = st.text_area(
            "Code Python",
            value=st.session_state['backend_code'],
            height=180,
            key="code_editor",
            help="Écrivez votre code Python ici",
            label_visibility="collapsed"
        )
        st.session_state['backend_code'] = code
        st.info("💡 Pour activer la coloration syntaxique, installez : `pip install streamlit-monaco`")
    
    # Boutons en dessous de l'éditeur
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        if st.button("▶️ Exécuter", use_container_width=True, type="primary", key="exec_btn"):
            st.session_state['run_backend_code'] = True
            st.rerun()
    with btn_col2:
        if st.button("🔄 Réinitialiser", use_container_width=True):
            st.session_state['backend_code'] = """# Écrivez votre code Python ici
personnage_1 = "Christophe"
personnage_2 = "Frederic"

#print est une fonction qui permet d'afficher un message à l'écran
print("Salut, je m'appelle", personnage_1, "et toi ?")
print("Salut", personnage_1, "je m'appelle", personnage_2)
"""
            st.session_state['run_backend_code'] = False
            st.rerun()

with col_output:
    st.subheader("📤 Résultat de l'exécution")
    
    # Conteneur avec bordure et hauteur fixe
    with st.container(border=True):
        # Zone de résultat avec hauteur fixe
        if st.session_state['run_backend_code']:
            # Capturer la sortie avec contextlib
            output_buffer = StringIO()
            
            try:
                # Exécuter le code avec redirection de stdout
                with redirect_stdout(output_buffer):
                    exec(st.session_state['backend_code'])
                
                output = output_buffer.getvalue()
                
                if output:
                    st.code(output, language="text")
                    st.success("✅ Code exécuté avec succès !")
                else:
                    st.info("ℹ️ Le code s'est exécuté mais n'a rien affiché (pas de print())")
                    
            except Exception as e:
                st.error(f"❌ Erreur lors de l'exécution :")
                st.code(str(e), language="text")
                
                # Demander au LLM d'expliquer l'erreur
                st.write("---")
                st.write("🤖 **Explication de l'erreur par l'assistant IA :**")
                
                with st.spinner("L'assistant analyse votre erreur..."):
                    explanation = explain_error_with_llm(
                        st.session_state['backend_code'], 
                        str(e)
                    )
                
                st.info(explanation)
            
            finally:
                st.session_state['run_backend_code'] = False
        else:
            # Message par défaut centré avec hauteur fixe
            st.markdown(
                """
                <div style="height: 385px; display: flex; align-items: center; justify-content: center; color: #888;">
                    <p style="text-align: center;">Aucun résultat pour le moment.<br>Exécutez votre code pour voir le résultat ici.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
