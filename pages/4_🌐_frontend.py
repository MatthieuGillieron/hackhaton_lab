import streamlit as st
import re
from src.ui.components.sidebar import setup_sidebar
from src.ui.styles.practice import get_practice_page_style
from src.core.llm import explain_error_with_llm

st.set_page_config(
    page_title="Frontend - Pratique",
    page_icon="🌐",
    layout="wide"
)

setup_sidebar()
st.markdown(get_practice_page_style(), unsafe_allow_html=True)

if st.button("← Retour à la sélection"):
    st.switch_page("pages/2_🎯_pratique.py")

st.title("🌐 Développement Frontend")
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
            <h4 style="color: #c81e70; margin-top: 0; font-size: 1.1em; font-weight: 600;">📚 Documentation Streamlit</h4>
            <p style="color: #1a1a1a; font-weight: 500;">Voici les commandes Streamlit à connaître :</p>
            <ul style="color: #1a1a1a;">
                <li><code style="background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;">st.title("Mon titre")</code> : Affiche un titre principal</li>
                <li><code style="background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;">st.header("Mon en-tête")</code> : Affiche un sous-titre</li>
                <li><code style="background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;">st.write("Mon texte")</code> : Affiche du texte simple</li>
                <li><code style="background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;">st.balloons()</code> : Déclenche l'effet des ballons 🎈</li>
            </ul>
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
            <h4 style="color: #c81e70; margin-top: 0; font-size: 1.1em; font-weight: 600;">💡 Exercice pratique</h4>
            <p style="color: #1a1a1a; font-weight: 500;"><strong>Objectif</strong> : Créer une page Streamlit simple</p>
            <ul style="color: #1a1a1a;">
                <li>Utilise <code style="background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;">st.title()</code> pour créer un titre</li>
                <li>Ajoute du texte avec <code style="background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;">st.write()</code></li>
                <li>Déclenche l'effet des ballons avec <code style="background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;">st.balloons()</code></li>
                <li>Clique sur Exécuter pour voir le résultat !</li>
            </ul>
        </div>
    </div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

if 'frontend_code' not in st.session_state:
    st.session_state['frontend_code'] = """# Créez votre page Streamlit ici !
st.title("Ma première page Streamlit")
st.write("Bienvenue dans le monde du développement frontend !")
st.balloons()
"""

if 'frontend_last_executed' not in st.session_state:
    st.session_state['frontend_last_executed'] = None

with st.container(border=True):
    col_ide, col_output = st.columns([45, 55])
    
    with col_ide:
        st.subheader("🖥️ Éditeur de Code Streamlit")
        
        current_code = st.text_area(
            "Code Streamlit",
            value=st.session_state['frontend_code'],
            height=300,
            key="code_editor_frontend",
            help="Écrivez votre code Streamlit ici",
            label_visibility="collapsed"
        )
        
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("Exécuter", use_container_width=True, type="primary", key="exec_btn"):
                st.session_state['frontend_code'] = current_code
                st.session_state['frontend_last_executed'] = current_code
                st.rerun()
        with btn_col2:
            if st.button("Réinitialiser", use_container_width=True):
                st.session_state['frontend_code'] = """# Créez votre page Streamlit ici !
st.title("Ma première page Streamlit")
st.write("Bienvenue dans le monde du développement frontend !")
st.balloons()
"""
                st.session_state['frontend_last_executed'] = None
                st.rerun()
    
    with col_output:
        st.subheader("📤 Aperçu de votre page")
        
        with st.container(border=True, height=500):
            if st.session_state['frontend_last_executed'] is not None:
                try:
                    exec(st.session_state['frontend_last_executed'])
                    
                except Exception as e:
                    st.error(f"❌ Erreur lors de l'exécution :")
                    st.code(str(e), language="text")
                    st.write("---")
                    
                    with st.spinner("Sparky analyse votre erreur..."):
                        explanation = explain_error_with_llm(
                            st.session_state['frontend_last_executed'], 
                            str(e),
                            "Streamlit"
                        )
                    
                    explanation_html = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', explanation)
                    explanation_html = re.sub(r'`([^`]+)`', r'"<strong>\1</strong>"', explanation_html)
                    explanation_html = explanation_html.replace("\n", "<br>")
                    
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
                st.markdown(
                    """
                    <div style="height: 400px; display: flex; align-items: center; justify-content: center; color: #888;">
                        <p style="text-align: center;">Aucun aperçu pour le moment.<br>Exécutez votre code pour voir le résultat ici.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
