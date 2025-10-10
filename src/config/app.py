import streamlit as st
from src.pages.chatbot import chatbot
from src.pages.pratice import pratice

def run():
    # Configuration de la page
    st.set_page_config(
        page_title="Mon Application Streamlit",
        page_icon="🚀",
        layout="wide"
    )
    
    # Sidebar pour la navigation
    st.sidebar.title("🧭 Navigation")
    st.sidebar.write("---")
    
    # Menu de navigation
    page = st.sidebar.radio(
        "Choisissez une page :",
        ["Chatbot", "Pratique"],
        index=0
    )
    
    st.sidebar.write("---")
    st.sidebar.info("Utilisez le menu ci-dessus pour naviguer entre les pages")
    
    # Affichage de la page sélectionnée
    if page == "Chatbot":
        chatbot()
    elif page == "Pratique":
        pratice()

