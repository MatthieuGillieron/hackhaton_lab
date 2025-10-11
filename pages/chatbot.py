import streamlit as st
import os
import time
import requests
from dotenv import load_dotenv
from config.app import setup_sidebar
from typing import Generator, Iterator
import json

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
   # page_icon="🤖",
    layout="wide"
)

setup_sidebar()

def stream_llm_response(response: requests.models.Response) -> Iterator[str]:
    response_gen = response.iter_lines(decode_unicode=True)
    for line in response_gen:
        if line:
            data = line[len("data: "):]
            if data == "[DONE]":
                yield ""
            else:
                data = json.loads(data)
                assistant_response = data["choices"][0]["delta"].get("content", "")
                yield assistant_response
                # TODO: find a way to remove this sleep?
                time.sleep(0.01)


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
        "temperature": 0.7, # TODO: what value to use here?
        "stream": True,
    }
    # Appeler l'API et afficher la réponse
    with st.chat_message("assistant", avatar="🤖"):
        # TODO: spinner not working, showing a ghost of the full message
        # with st.spinner("Thinking..."):
        try:
            # Faire la requête à l'API
            req_response = requests.post(url=BASE_URL, json=payload, headers=HEADERS)
            req_response.raise_for_status()
            assistant_response = stream_llm_response(req_response)
        except Exception as e:
            assistant_response = f"❌ Erreur : {str(e)}"

        # with st.container():
        # get partial response and start showing
        out_stream_response = st.write_stream(assistant_response)
        st.session_state.messages.append({"role": "assistant", "content": out_stream_response})
