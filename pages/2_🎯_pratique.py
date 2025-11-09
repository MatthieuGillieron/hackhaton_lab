import streamlit as st
from src.ui.components.sidebar import setup_sidebar

st.set_page_config(
    page_title="Pratique - IA LAB",
    #page_icon="📝",
    layout="wide"
)

# Configuration de la sidebar
setup_sidebar()

# CSS pour styliser les boutons
st.markdown("""
<style>
    /* Styliser les boutons Streamlit - même style que les boutons Exécuter/Réinitialiser */
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
</style>
""", unsafe_allow_html=True)

# Afficher les cards de sélection
st.title("Essaye les différents domaines de l'informatique")
st.write("Amuse-toi ici, tu seras aidé-e par Sparky !")

st.write("---")

# Création des cards

# Espacement
st.write("")
st.write("")

# Première ligne de cards avec marges
empty1, col1, col2, empty2 = st.columns([0.5, 2, 2, 0.5], gap="large")

with col1:
    with st.container(border=True):
        st.markdown('<p style="font-size: 1.8em; font-weight: bold; color: #c81e70; margin-bottom: 15px; text-align: center;">🫆 Cybersécurité</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 1.05em; color: #4b5563; line-height: 1.7; text-align: justify; margin-bottom: 20px;">Protèges les banques, les jeux vidéo… Tu chasses les hackers, tu fermes les failles, tu sauves des millions de données… et tu le fais en mode ninja du code. 🎮💥</p>', unsafe_allow_html=True)
        
        if st.button("Commencer la pratique", key="cyber", use_container_width=True, type="primary"):
            st.switch_page("pages/5_🔒_cyber.py")

with col2:
    with st.container(border=True):
        st.markdown('<p style="font-size: 1.8em; font-weight: bold; color: #c81e70; margin-bottom: 15px; text-align: center;">💻 Développement Backend</p>', unsafe_allow_html=True)
        st.markdown("<p style=\"font-size: 1.05em; color: #4b5563; line-height: 1.7; text-align: justify; margin-bottom: 20px;\"> Le super-héros de l'ombre, il crée et fait tourner tous les mécanismes secrets d'un site ou d'une app. Sans lui, rien ne fonctionne, même si on ne le voit pas à l'écran !</p>", unsafe_allow_html=True)
        
        if st.button("Commencer la pratique", key="backend", use_container_width=True, type="primary"):
            st.switch_page("pages/3_💻_backend.py")

# Deuxième ligne de cards avec marges
empty3, col3, col4, empty4 = st.columns([0.5, 2, 2, 0.5], gap="large")

with col3:
    with st.container(border=True):
        st.markdown('<p style="font-size: 1.8em; font-weight: bold; color: #c81e70; margin-bottom: 15px; text-align: center;">🎮 Développement de Jeux Vidéo</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 1.05em; color: #4b5563; line-height: 1.7; text-align: justify; margin-bottom: 20px;">Le magicien du numérique qui utilise le code pour donner vie à des mondes entiers et à des personnages incroyables. Il transforme une idée en une aventure interactive dans laquelle on peut plonger !</p>', unsafe_allow_html=True)
        
        if st.button("Commencer la pratique", key="gamedev", use_container_width=True, type="primary"):
            st.switch_page("pages/6_🎮_gamedev.py")

with col4:
    with st.container(border=True):
        st.markdown('<p style="font-size: 1.8em; font-weight: bold; color: #c81e70; margin-bottom: 15px; text-align: center;">🌐 Développement Frontend</p>', unsafe_allow_html=True)
        st.markdown("<p style=\"font-size: 1.05em; color: #4b5563; line-height: 1.7; text-align: justify; margin-bottom: 20px;\"> L'artiste du web, il produit les interfaces cool et intuitives sur le web et les smartphones. C'est lui qui fait en sorte qu'un site soit beau, rapide et agréable à utiliser !</p>", unsafe_allow_html=True)
        
        if st.button("Commencer la pratique", key="frontend", use_container_width=True, type="primary"):
            st.switch_page("pages/4_🌐_frontend.py")
