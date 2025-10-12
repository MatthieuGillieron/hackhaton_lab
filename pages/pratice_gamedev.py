import streamlit as st
import streamlit.components.v1 as components
from config.app import setup_sidebar

st.set_page_config(
    page_title="Game Dev - Pratique",
    page_icon="🎮",
    layout="wide"
)

# Configuration de la sidebar
setup_sidebar()

# Bouton retour
if st.button("← Retour à la sélection"):
    st.switch_page("pages/pratice.py")

# Titre et sous-titre
st.title("🎮 Développement de Jeux Vidéo")
st.write("### Module de pratique en Développement de Jeux Vidéo")
st.write("---")

# Section Introduction (gauche) et Bienvenue (droite)
col_intro, col_welcome = st.columns(2)

with col_intro:
    st.info("""📚 **Commandes pour déplacer le rond**

Utilise ces commandes simples :

- `haut()` : Monte le rond ⬆️
- `bas()` : Descend le rond ⬇️
- `gauche()` : Va à gauche ⬅️
- `droite()` : Va à droite ➡️

**Exemples :**
```
haut()
droite()
bas()
```
""")

with col_welcome:
    st.info("""💡 **Exercice : Déplace le rond**

**Mission :** Écris des commandes pour déplacer le rond !

**Objectif :** Fais aller le rond du coin en haut à gauche vers le coin en bas à droite.

📝 **Astuce :** 
- Pour aller en haut à gauche : `haut()` puis `gauche()`
- Pour aller en bas à droite : `bas()` puis `droite()`
- Tu peux répéter les commandes !
""")

st.write("---")

# Initialiser le code par défaut
if 'gamedev_code' not in st.session_state:
    st.session_state['gamedev_code'] = """// 🎮 ÉCRIS TES COMMANDES ICI !

// Exemple : déplace le rond en haut puis à droite
haut()
haut()
haut()
droite()
droite()

// ✏️ À TOI ! Écris tes commandes ci-dessous :



"""

# Initialiser le dernier code exécuté
if 'gamedev_last_executed' not in st.session_state:
    st.session_state['gamedev_last_executed'] = None

# Section IDE (gauche) et Output (droite)
# IDE 45%, Aperçu 55%
col_ide, col_output = st.columns([45, 55])

with col_ide:
    st.subheader("🖥️ Éditeur de Code JavaScript")
    
    # Utiliser text_area pour une édition stable
    current_code = st.text_area(
        "Code JavaScript",
        value=st.session_state['gamedev_code'],
        height=300,
        key="code_editor_gamedev",
        help="Écrivez votre code JavaScript ici",
        label_visibility="collapsed"
    )
    
    # Boutons en dessous de l'éditeur
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        if st.button("▶️ Exécuter", use_container_width=True, type="primary", key="exec_btn"):
            # Sauvegarder le code et marquer comme devant être exécuté
            st.session_state['gamedev_code'] = current_code
            st.session_state['gamedev_last_executed'] = current_code
            st.rerun()
    with btn_col2:
        if st.button("🔄 Réinitialiser", use_container_width=True):
            st.session_state['gamedev_code'] = """// 🎮 ÉCRIS TES COMMANDES ICI !

// Exemple : déplace le rond en haut puis à droite
haut()
haut()
haut()
droite()
droite()

// ✏️ À TOI ! Écris tes commandes ci-dessous :



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
                            background-color: #0f0f23;
                            font-family: Arial, sans-serif;
                        }}
                        #gameCanvas {{
                            border: 3px solid #00ff88;
                            border-radius: 8px;
                            background-color: #1a1a2e;
                        }}
                        .info {{
                            color: #00ff88;
                            text-align: center;
                            margin-bottom: 10px;
                            font-size: 14px;
                        }}
                    </style>
                </head>
                <body>
                    <div>
                        <div class="info">🎮 Le rond vert se déplace selon tes commandes !</div>
                        <canvas id="gameCanvas" width="400" height="400"></canvas>
                    </div>
                    <script>
                    // === CODE DU JEU (automatique) ===
                    const canvas = document.getElementById('gameCanvas');
                    const ctx = canvas.getContext('2d');
                    let x = 200;
                    let y = 200;
                    const pas = 30;
                    
                    // Fonctions de déplacement
                    function haut() {{ y -= pas; dessiner(); }}
                    function bas() {{ y += pas; dessiner(); }}
                    function gauche() {{ x -= pas; dessiner(); }}
                    function droite() {{ x += pas; dessiner(); }}
                    
                    function dessiner() {{
                        ctx.fillStyle = '#1a1a2e';
                        ctx.fillRect(0, 0, canvas.width, canvas.height);
                        ctx.fillStyle = '#00ff88';
                        ctx.beginPath();
                        ctx.arc(x, y, 25, 0, Math.PI * 2);
                        ctx.fill();
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
        else:
            # Message par défaut
            st.markdown(
                """
                <div style="height: 400px; display: flex; align-items: center; justify-content: center; color: #888;">
                    <p style="text-align: center;">Aucun aperçu pour le moment.<br>Exécutez votre code pour voir le jeu ici.</p>
                </div>
                """,
                unsafe_allow_html=True
            )
