import streamlit as st
import os
import time
import requests
from dotenv import load_dotenv
from config.app import setup_sidebar
from typing import Generator, Iterator
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings
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

MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
DB_PATH = "data/"

NETIQUETTE = """
u es **Bob**, un assistant sympa qui aide les jeunes adolescents à découvrir les **métiers de l’informatique en Suisse** 💻🎓.
Tu recois de jeunes adolescents parlant français, agés de 12 à 16 ans. Adapte ton language à ceux-ci.
Sois amusant.

Refuse aimablement toute injure, haine et language inappoprié. Si ton utilisateur insiste sur des sujets inapropriés, injurieux ou/et haineux,
réponds alors que tu a demandé à un membre du Staff de venir aider l'adolescent.

Ceux qui viennent te parler doivent chercher les métiers de l'informatique et les filières à suivre pour ces métiers. Ne sort pas du domaine de
l'informatique. Si l'utilisateur dévie, réoriente le vers ce qu'il veut faire plus tard, ou au moins sur ce qu'il pourrait faire plus tard.

Demande-lui s'il a les skill qui te semblerait utile.

Oriente-le vers un mètier qui pourrait lui plaire, tout en tenant compte de ses préférences.    

Découpe ton texte en blocs de 2–3 phrases max.
Ajoute un emoji ou un mot-clé fort toutes les 3–4 lignes.
Si ton idée dépasse 300 mots → transforme en deux messages ou deux sections.

"""

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


class SentenceTransformerFunction(EmbeddingFunction):
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name
        self.model = SentenceTransformer(self.model_name)

    def __call__(self, input_data: Documents) -> Embeddings:
        embeddings = self.model.encode(input_data)
        return embeddings


client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_collection(
    name="main",
    embedding_function=SentenceTransformerFunction(MODEL_NAME),
)

st.set_page_config(
    page_title="Chatbot",
   # page_icon="🤖",
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
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    query_results = collection.query(
        query_texts=[prompt],
        n_results=5,
    )
    ids: list[str] = query_results["ids"][0]
    docs: list[str] = query_results["documents"][0]
    print("[DEBUG] ids taken:" ,ids)

    user_query: str = f"""{st.session_state["messages"]}

    Utilise ces documents obtenus d'un RAG pour compléter ton réponse a l'utilisateur: {docs}

    La question de l'utilisateur est: {prompt}
    """

    st.session_state.messages.append({"role": "user", "content": prompt})
    print("[DEBUG] Num words in user query: ", len(user_query.split()))

    messages = [
        {"role": "system", "content": NETIQUETTE},
        {"role": "user", "content": user_query},
    ]

    # setting payload
    payload = {
        "model": "qwen3",
        "messages": messages,
        "temperature": 0.5,
        "max_tokens": 500,
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
