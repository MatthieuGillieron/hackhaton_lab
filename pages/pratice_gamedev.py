import streamlit as st
import streamlit.components.v1 as components
import os
import re
import requests
from dotenv import load_dotenv
from config.app import setup_sidebar

st.set_page_config(
    page_title="Game Dev - Pratique",
    page_icon="🎮",
    layout="wide"
)

load_dotenv()

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
    prompt = f"""Tu es un professeur de programmation pour jeunes débutants. Un élève a écrit ces commandes JavaScript simples :

{code}

Il a obtenu cette erreur :
{error}

Explique-lui de manière très simple et pédagogique :
1. Quelle est l'erreur
2. Pourquoi elle se produit
3. Comment la corriger

IMPORTANT - Format à respecter EXACTEMENT :
- N'utilise JAMAIS de backticks (``` ou ` simple).
- Pour les commandes/fonctions : mets-les entre guillemets doubles avec le contenu en gras
  Exemple : "**haut()**" ou "**droite()**" ou "**bas()**"
- Le format est toujours : guillemets + astérisques + contenu + astérisques + guillemets : "**contenu**"
- FERME TOUJOURS les astérisques avant de continuer le texte normal
Reste concis et utilise un langage très simple pour un jeune. Maximum 3-4 phrases."""

    payload = {
        "model": "qwen3",
        "messages": [
            {"role": "system", "content": "Tu es un professeur de programmation patient et pédagogue pour jeunes débutants."},
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

# CSS pour styliser les boutons et réduire les marges
st.markdown("""
<style>
    /* Cacher/réduire le header blanc de Streamlit */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
        height: 0 !important;
    }
    
    /* Réduire les marges en haut de la page */
    section.main > div {
        padding-top: 2rem !important;
    }
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 1rem !important;
        max-width: 100% !important;
    }
    
    /* Ajuster l'espacement du premier élément */
    section[data-testid="stVerticalBlock"] > div:first-child {
        padding-top: 0 !important;
    }
    
    /* Styliser les boutons Streamlit */
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
    
    /* Wrapper IDE - cibler tous les containers avec bordure sur cette page */
    section[data-testid="stVerticalBlock"] div[style*="border: 1px solid rgba(49, 51, 63, 0.2)"] {
        background: linear-gradient(135deg, rgba(222, 56, 142, 0.04), rgba(18, 170, 178, 0.04)) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        border-radius: 15px !important;
        border: 1px solid rgba(222, 56, 142, 0.2) !important;
        padding: 20px !important;
        box-shadow: 0 2px 8px 0 rgba(0, 0, 0, 0.08) !important;
    }
</style>
""", unsafe_allow_html=True)

# Bouton retour
if st.button("← Retour à la sélection"):
    st.switch_page("pages/pratice.py")

# Titre et sous-titre
st.title("🎮 Développement de Jeux Vidéo")
#st.write("### Module de pratique en Développement de Jeux Vidéo")
st.write("---")

# Sections avec effet glassmorphism subtil
st.markdown("""
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
        <div style="
            background: linear-gradient(135deg, rgba(222, 56, 142, 0.08), rgba(18, 170, 178, 0.08));
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border-radius: 15px;
            border: 1px solid rgba(222, 56, 142, 0.2);
            padding: 20px;
            box-shadow: 0 2px 8px 0 rgba(0, 0, 0, 0.08);
        ">
            <h4 style="color: #c81e70; margin-top: 0; font-size: 1.1em; font-weight: 600;">📚 Commandes pour déplacer le rond</h4>
            <p style="color: #1a1a1a; font-weight: 500;">Utilise ces commandes avec un nombre :</p>
            <ul style="color: #1a1a1a;">
                <li><code style="background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;">haut(2)</code> : Monte le rond 2 fois ⬆️</li>
                <li><code style="background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;">bas(3)</code> : Descend le rond 3 fois ⬇️</li>
                <li><code style="background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;">gauche(1)</code> : Va à gauche 1 fois ⬅️</li>
                <li><code style="background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;">droite(4)</code> : Va à droite 4 fois ➡️</li>
            </ul>
            <p style="color: #1a1a1a; margin-top: 10px;">💡 Le nombre indique combien de fois le rond se déplace !</p>
        </div>
        <div style="
            background: linear-gradient(135deg, rgba(222, 56, 142, 0.08), rgba(18, 170, 178, 0.08));
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border-radius: 15px;
            border: 1px solid rgba(222, 56, 142, 0.2);
            padding: 20px;
            box-shadow: 0 2px 8px 0 rgba(0, 0, 0, 0.08);
        ">
            <h4 style="color: #c81e70; margin-top: 0; font-size: 1.1em; font-weight: 600;">💡 Exercice : Mets le rond dans la cage</h4>
            <p style="color: #1a1a1a; font-weight: 500;"><strong>Mission</strong> : Le rond bleu commence au centre. Déplace-le dans la cage en haut à droite ! 🎯</p>
            <p style="color: #1a1a1a; font-weight: 500;"><strong>La cage</strong> : C'est la zone rose avec 3 murs dans le coin en haut à droite.</p>
            <p style="color: #1a1a1a;">📝 <strong>Astuce</strong> : Utilise les nombres pour déplacer plus vite ! Par exemple <code style="background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;">haut(5)</code></p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Espace entre les sections
st.write("")
st.write("")

# Initialiser le code par défaut
if 'gamedev_code' not in st.session_state:
    st.session_state['gamedev_code'] = """// 🎮 DÉPLACE LE ROND DANS LA CAGE !

// Exemple : déplace le rond en haut 3 fois puis à droite 2 fois
haut(3)
droite(2)

// ✏️ À TOI ! Écris tes commandes pour atteindre la cage rose en haut à droite :



"""

# Initialiser le dernier code exécuté
if 'gamedev_last_executed' not in st.session_state:
    st.session_state['gamedev_last_executed'] = None

# Wrapper pour IDE et résultat
with st.container(border=True):
    # Section IDE (gauche) et Output (droite)
    # IDE 45%, Aperçu 55%
    col_ide, col_output = st.columns([45, 55])
    
    with col_ide:
        st.subheader("🖥️ Éditeur de Commandes")
        
        # Utiliser text_area pour une édition stable
        current_code = st.text_area(
            "Code JavaScript",
            value=st.session_state['gamedev_code'],
            height=300,
            key="code_editor_gamedev",
            help="Écrivez vos commandes JavaScript ici",
            label_visibility="collapsed"
        )
        
        # Boutons en dessous de l'éditeur
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("Exécuter", use_container_width=True, type="primary", key="exec_btn"):
                # Sauvegarder le code et marquer comme devant être exécuté
                st.session_state['gamedev_code'] = current_code
                st.session_state['gamedev_last_executed'] = current_code
                st.rerun()
        with btn_col2:
            if st.button("Réinitialiser", use_container_width=True):
                st.session_state['gamedev_code'] = """// 🎮 DÉPLACE LE ROND DANS LA CAGE !

// Exemple : déplace le rond en haut 3 fois puis à droite 2 fois
haut(3)
droite(2)

// ✏️ À TOI ! Écris tes commandes pour atteindre la cage rose en haut à droite :



"""
                st.session_state['gamedev_last_executed'] = None
                st.rerun()
    
    with col_output:
        st.subheader("🎮 Aperçu du jeu")
        
        # Container Streamlit natif avec bordure
        with st.container(border=True, height=500):
            # Zone de résultat
            if st.session_state['gamedev_last_executed'] is not None:
                try:
                    # Créer le HTML avec canvas
                    html_code = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <style>
                        body {{
                            margin: 0;
                            padding: 20px;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            background-color: #f8f9fa;
                            font-family: Arial, sans-serif;
                        }}
                        #gameCanvas {{
                            border: 3px solid #de388e;
                            border-radius: 8px;
                            background-color: #ffffff;
                            box-shadow: 0 4px 12px rgba(222, 56, 142, 0.15);
                        }}
                        .info {{
                            color: #c81e70;
                            text-align: center;
                            margin-bottom: 10px;
                            font-size: 14px;
                            font-weight: 600;
                        }}
                    </style>
                </head>
                <body>
                    <div>
                        <div class="info">🎮 Déplace le rond bleu dans la cage rose !</div>
                        <canvas id="gameCanvas" width="400" height="400"></canvas>
                    </div>
                    <script>
                    // === CODE DU JEU (automatique) ===
                    const canvas = document.getElementById('gameCanvas');
                    const ctx = canvas.getContext('2d');
                    let x = 200;
                    let y = 200;
                    const pas = 20;  // Déplacements plus courts
                    
                    // Fonctions de déplacement avec paramètre
                    function haut(n = 1) {{ 
                        for(let i = 0; i < n; i++) {{
                            y -= pas; 
                        }}
                        dessiner(); 
                    }}
                    function bas(n = 1) {{ 
                        for(let i = 0; i < n; i++) {{
                            y += pas; 
                        }}
                        dessiner(); 
                    }}
                    function gauche(n = 1) {{ 
                        for(let i = 0; i < n; i++) {{
                            x -= pas; 
                        }}
                        dessiner(); 
                    }}
                    function droite(n = 1) {{ 
                        for(let i = 0; i < n; i++) {{
                            x += pas; 
                        }}
                        dessiner(); 
                    }}
                    
                    // Dessiner la cage (3 murs en haut à droite, ouverture vers le centre)
                    function dessinerCage() {{
                        ctx.strokeStyle = '#de388e';
                        ctx.lineWidth = 4;
                        
                        // Mur du haut (horizontal)
                        ctx.beginPath();
                        ctx.moveTo(290, 70);
                        ctx.lineTo(370, 70);
                        ctx.stroke();
                        
                        // Mur de droite (vertical)
                        ctx.beginPath();
                        ctx.moveTo(370, 70);
                        ctx.lineTo(370, 150);
                        ctx.stroke();
                        
                        // Mur du bas (horizontal)
                        ctx.beginPath();
                        ctx.moveTo(290, 150);
                        ctx.lineTo(370, 150);
                        ctx.stroke();
                        
                        // Zone de la cage (fond semi-transparent)
                        ctx.fillStyle = 'rgba(222, 56, 142, 0.08)';
                        ctx.fillRect(290, 70, 80, 80);
                    }}
                    
                    function dessiner() {{
                        // Fond blanc
                        ctx.fillStyle = '#ffffff';
                        ctx.fillRect(0, 0, canvas.width, canvas.height);
                        
                        // Dessiner la cage
                        dessinerCage();
                        
                        // Dessiner le rond (plus petit)
                        ctx.fillStyle = '#12aab2';
                        ctx.beginPath();
                        ctx.arc(x, y, 12, 0, Math.PI * 2);
                        ctx.fill();
                        
                        // Bordure du rond
                        ctx.strokeStyle = '#0d8a91';
                        ctx.lineWidth = 2;
                        ctx.stroke();
                    }}
                    
                    // Dessiner la position initiale
                    dessiner();
                    
                    // === TES COMMANDES ===
                    {st.session_state['gamedev_last_executed']}
                    </script>
                </body>
                </html>
                    """
                    
                    # Afficher le jeu dans un iframe
                    components.html(html_code, height=480, scrolling=False)
                    
                except Exception as e:
                    st.error(f"❌ Erreur lors de l'exécution :")
                    st.code(str(e), language="text")
                    
                    # Demander au LLM d'expliquer l'erreur
                    st.write("---")
                    
                    with st.spinner("Sparky analyse votre erreur..."):
                        explanation = explain_error_with_llm(
                            st.session_state['gamedev_last_executed'], 
                            str(e)
                        )
                    
                    # Convertir le markdown en HTML <strong> de manière plus robuste
                    # Remplacer les paires de ** par <strong>...</strong>
                    explanation_html = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', explanation)
                    # Remplacer les single backticks ` par des guillemets + gras
                    explanation_html = re.sub(r'`([^`]+)`', r'"<strong>\1</strong>"', explanation_html)
                    
                    # Remplacer les retours à la ligne par des <br>
                    explanation_html = explanation_html.replace("\n", "<br>")
                    
                    # Afficher l'explication avec le style glassmorphism
                    st.markdown(f"""
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
                        <p style="color: #1a1a1a; line-height: 1.6; margin-bottom: 0;">{explanation_html}</p>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                # Message par défaut
                st.markdown(
                    """
                    <div style="height: 342px; display: flex; align-items: center; justify-content: center; color: #888;">
                        <p style="text-align: center;">Aucun aperçu pour le moment.<br>Exécutez votre code pour voir le jeu ici.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
