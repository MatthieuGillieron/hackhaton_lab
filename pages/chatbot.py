import streamlit as st
import os
import time
import requests
from dotenv import load_dotenv
from config.app import setup_sidebar
from typing import Generator, Iterator
from sentence_transformers import SentenceTransformer
import chromadb
import numpy as np
from chromadb import Collection, Documents, EmbeddingFunction, Embeddings
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

MODEL_NAME = "bge_multilingual_gemma2"
DB_PATH = "data/"

NETIQUETTE = """
Tu es Sparky, un assistant sympa qui aide les jeunes adolescents à découvrir les métiers de l’informatique en Suisse 💻🎓.
Tu recois de jeunes adolescents parlant français, agés de 12 à 16 ans. Adapte ton language à ceux-ci et sois amusant.
L'idée de te nommer ainsi est d'insufler l'étincelle de la passion de l'informatique.

Refuse aimablement toute injure, haine et language inappoprié. Si ton utilisateur insiste sur des sujets inapropriés, injurieux ou/et haineux,
réponds alors que tu a demandé à un membre du Staff de venir aider l'adolescent.

Toutes tes réponses doivent s'adresser à toutes et tous, sois inclusif dans tes réponses, et même encourage le public féminin. Elles sont
autant capables que les hommes.

Ceux qui viennent te parler sont à la recherche d'un métier de l'informatique et les filières disponibles pour ce métier. Ne sort pas du domaine de
l'informatique. Si l'utilisateur dévie, réoriente le vers ce qu'il veut faire plus tard, ou au moins sur ce qu'il pourrait faire plus tard.

Demande-lui s'il a les skill qui te sembleraientt utile.
Insite sur le fait que les mathématiques ne sont pas nécessaires à ces mèters. Cela aide, mais on y arrive sans également.

Sois encourageant, valorise ses points forts, encourage-le.

Oriente-le vers un mètier qui pourrait lui plaire, tout en tenant compte de ses préférences.
Tu peux lui parler éventuellement de la passion pour l'informatique, du fait de participer aux avancées technologique
Pour le développement informatique, tu peux même insister sur le "pouvoir" créateur du développeur.
Le jeune peut être intéressé par les jeux vidéos, plus que probablement. Parle-lui alors des métiers informatiques autour de la conception des jeux
vidéos, sans le laisser se décourager par les débouchés restreints dans nos contrées.

Sois concis et plutot high-level dans tes réponses Le but est de conserver l'attention du jeune qui t'interroge.
Ton texte doit idéallement consister en 1 à 2 paragraphes de 2-3 phrases max. 

Si la demande du jeune est très précise, tu peux outrepasser les règles du nombre de paragraphe et de phrases.

Attention, le jeune n'a que 5 minutes environ à disposition avec toi. Guide-le vers un de ses futurs possibles.

Tu n'es pas là pour le guider pour son cv et s'enregistrer sur les sites en ligne, mais lui suggère où aller et que faire.

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

class MultinligualGemma2(EmbeddingFunction):
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name
        self.url = f"https://api.infomaniak.com/1/ai/{PRODUCT_ID}/openai/v1/embeddings"
        self.headers = {
          'Authorization': f"Bearer {API_TOKEN}",
          'Content-Type': 'application/json',
        }

    def __call__(self, input_data: Documents) -> Embeddings:
        payload = {
            "input": input_data,
            "model": self.model_name,
        }

        req = requests.post(url=self.url, json=payload, headers=self.headers)
        res = req.json()
        data = res["data"]
        embeddings = [np.array(x["embedding"]) for x in data]

        return embeddings


class SentenceTransformerFunction(EmbeddingFunction):
    def __init__(self, model_name: str) -> None:
        self.model_name = model_name
        self.model = SentenceTransformer(self.model_name)

    def __call__(self, input_data: Documents) -> Embeddings:
        embeddings = self.model.encode(input_data)
        return embeddings


@st.cache_resource
def get_db_collection(path: str, model_name: str) -> Collection:
    client = chromadb.PersistentClient(path=path)

    collection = client.get_collection(
        name="main-gemma",
        embedding_function=MultinligualGemma2(model_name),
    )
    print(collection)
    return collection


collection = get_db_collection(DB_PATH, MODEL_NAME)

st.set_page_config(
    page_title="Chatbot",
   # page_icon="🤖",
    layout="wide"
)

setup_sidebar()

# init historique des messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hey 👋 moi c'est Sparky ⚡️ !\n\nJe suis là pour t'aider à découvrir les métiers de l'informatique en Suisse 🇨🇭 — que tu sois curieux·se de coder, de bidouiller des ordis 🖥️, de créer des jeux 🎮 ou même de bosser dans la cybersécurité 🔒"
        }
    ]

st.title("Découvre les métiers dans l'informatique")
st.write("l'assistant **IA** Sparky t'aidera à découvrir les nombreux métiers !")

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
