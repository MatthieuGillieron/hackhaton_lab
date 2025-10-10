import streamlit as st
from config.app import setup_sidebar

st.set_page_config(
    page_title="IA LAB",
    page_icon="🚀",
    layout="wide"
)

# Configuration de la sidebar
setup_sidebar()

# Redirection vers la page chatbot
st.switch_page("pages/chatbot.py")