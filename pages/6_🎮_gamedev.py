import streamlit as st
import streamlit.components.v1 as components
from src.ui.components.sidebar import setup_sidebar
from src.ui.styles.practice import get_practice_page_style

st.set_page_config(
    page_title="Game Dev - Pratique",
    page_icon="🎮",
    layout="wide"
)

setup_sidebar()
st.markdown(get_practice_page_style(), unsafe_allow_html=True)

if st.button("← Retour à la sélection"):
    st.switch_page("pages/2_🎯_pratique.py")

st.title("🎮 Développement de Jeux Vidéo")
st.write("---")

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

if 'gamedev_code' not in st.session_state:
    st.session_state['gamedev_code'] = """// 🎮 DÉPLACE LE ROND DANS LA CAGE !

// Exemple : déplace le rond en haut 3 fois puis à droite 2 fois
haut(3)
droite(2)

// ✏️ À TOI ! Écris tes commandes pour atteindre la cage rose en haut à droite :



"""

if 'gamedev_last_executed' not in st.session_state:
    st.session_state['gamedev_last_executed'] = None

with st.container(border=True):
    col_ide, col_output = st.columns([45, 55])
    
    with col_ide:
        st.subheader("🖥️ Éditeur de Commandes")
        
        current_code = st.text_area(
            "Code JavaScript",
            value=st.session_state['gamedev_code'],
            height=300,
            key="code_editor_gamedev",
            help="Écrivez vos commandes JavaScript ici",
            label_visibility="collapsed"
        )
        
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("Exécuter", use_container_width=True, type="primary", key="exec_btn"):
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
        
        with st.container(border=True, height=500):
            if st.session_state['gamedev_last_executed'] is not None:
                try:
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
                    const canvas = document.getElementById('gameCanvas');
                    const ctx = canvas.getContext('2d');
                    let x = 200;
                    let y = 200;
                    const pas = 20;
                    
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
                    
                    function dessinerCage() {{
                        ctx.strokeStyle = '#de388e';
                        ctx.lineWidth = 4;
                        
                        ctx.beginPath();
                        ctx.moveTo(290, 70);
                        ctx.lineTo(370, 70);
                        ctx.stroke();
                        
                        ctx.beginPath();
                        ctx.moveTo(370, 70);
                        ctx.lineTo(370, 150);
                        ctx.stroke();
                        
                        ctx.beginPath();
                        ctx.moveTo(290, 150);
                        ctx.lineTo(370, 150);
                        ctx.stroke();
                        
                        ctx.fillStyle = 'rgba(222, 56, 142, 0.08)';
                        ctx.fillRect(290, 70, 80, 80);
                    }}
                    
                    function dessiner() {{
                        ctx.fillStyle = '#ffffff';
                        ctx.fillRect(0, 0, canvas.width, canvas.height);
                        
                        dessinerCage();
                        
                        ctx.fillStyle = '#12aab2';
                        ctx.beginPath();
                        ctx.arc(x, y, 12, 0, Math.PI * 2);
                        ctx.fill();
                        
                        ctx.strokeStyle = '#0d8a91';
                        ctx.lineWidth = 2;
                        ctx.stroke();
                    }}
                    
                    dessiner();
                    
                    {st.session_state['gamedev_last_executed']}
                    </script>
                </body>
                </html>
                    """
                    
                    components.html(html_code, height=480, scrolling=False)
                except Exception as e:
                    st.error(f"❌ Erreur : {str(e)}")
            else:
                st.info("Exécutez votre code pour voir le jeu ici.")
