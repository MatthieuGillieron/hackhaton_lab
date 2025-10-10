import streamlit as st
from src.config.app import apply_sidebar_style

st.set_page_config(
    page_title="Chatbot - IA LAB",
    page_icon="🤖",
    layout="wide"
)

# Appliquer le style personnalisé
apply_sidebar_style()

# Sidebar
st.sidebar.image("src/images/42.png", use_container_width=True)
st.sidebar.markdown('<p style="margin-bottom: -40px; margin-top: 75px; padding: 0;">Navigation</p>', unsafe_allow_html=True)
st.sidebar.write("---")

# Menu de navigation
st.sidebar.page_link("pages/chatbot.py", label="🤖 Chatbot", use_container_width=True)
st.sidebar.page_link("pages/pratice.py", label="📝 Pratique", use_container_width=True)

st.sidebar.write("---")

# Contenu de la page Chatbot
st.title("🤖 Chatbot")
st.write("Bienvenue sur la page du chatbot")

# Contenu de votre chatbot ici
st.write("---")
st.info("Cette page contiendra votre chatbot")

