import streamlit as st
import os
import requests
from dotenv import load_dotenv
from config.app import setup_sidebar
load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
PRODUCT_ID = os.getenv("PRODUCT_ID")

# API Infomaniak
BASE_URL = f"https://api.infomaniak.com/1/ai/{PRODUCT_ID}/openai/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="wide"
)

setup_sidebar()

# init historique des messages
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("Découvrez les métier dans l'informatique")
st.write("l'assistant IA vous aidera à découvrir les métier dans l'informatique")

# réinitialiser la conv
col1, col2 = st.columns([6, 1])
with col2:
    if st.button("🗑️ Clear", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

st.write("---")

# Afficher l'historique
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user", avatar="👤"):
            st.markdown(message["content"])
    else:
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(message["content"])


# prompt user
if prompt := st.chat_input("Écrivez votre message ici..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
        
    
    # setting payload
    payload = {
        "model": "qwen3",
        "messages": st.session_state.messages,
        "temperature": 0.7,
        "max_tokens": 1000
    }
    
    # Appeler l'API et afficher la réponse
    with st.chat_message("assistant", avatar="🤖"):
        message_placeholder = st.empty()
        
        try:
            # Faire la requête à l'API
            response = requests.post(BASE_URL, headers=HEADERS, json=payload)
            response.raise_for_status()
            
            # Extraire la réponse
            assistant_response = response.json()["choices"][0]["message"]["content"]
            
            # Afficher la réponse
            message_placeholder.markdown(assistant_response)
            
            # Ajouter la réponse à l'historique
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
            
        except Exception as e:
            error_message = f"❌ Erreur : {str(e)}"
            message_placeholder.markdown(error_message)
            st.session_state.messages.append({"role": "assistant", "content": error_message})

