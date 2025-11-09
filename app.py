"""
Sparky - Application d'orientation professionnelle en informatique
Point d'entrée principal
"""
import streamlit as st

st.set_page_config(
    page_title="Sparky - IA LAB",
    page_icon="🚀",
    layout="wide"
)

# Redirection vers la page chatbot
st.switch_page("pages/1_🤖_chatbot.py")
