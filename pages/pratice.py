import streamlit as st
from config.app import setup_sidebar

st.set_page_config(
    page_title="Pratique - IA LAB",
    page_icon="📝",
    layout="wide"
)

# Configuration de la sidebar
setup_sidebar()

# Contenu de la page Pratique
st.title("📝 Pratique")
st.write("Bienvenue sur la page de pratique")

# Contenu de votre page de pratique ici
st.write("---")
st.info("Cette page contiendra vos exercices de pratique")

