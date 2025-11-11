import streamlit as st
from src.ui.components.sidebar import setup_sidebar
from src.core.rag import get_db_collection, query_rag
from src.core.llm import call_llm, stream_llm_response
from src.utils.constants import NETIQUETTE, WELCOME_MESSAGE

# Initialiser la collection RAG
collection = get_db_collection()

st.set_page_config(
    page_title="Chatbot",
    layout="wide"
)

setup_sidebar()

# Ajouter le bouton Clear dans la sidebar
with st.sidebar:
    if st.button("🗑️ Effacer", key="clear_chat", width="stretch"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": WELCOME_MESSAGE
            }
        ]
        st.rerun()

# CSS pour réduire l'espace en haut et styliser le bouton Clear
st.markdown("""
<style>
    /* Réduire l'espace en haut du titre */
    .main .block-container {
        padding-top: 1.5rem !important;
    }
    
    h1 {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
    
    /* Style du bouton Clear dans la sidebar - compact */
    section[data-testid="stSidebar"] div[data-testid="stButton"] button,
    section[data-testid="stSidebar"] div[data-testid="stButton"] button:active,
    section[data-testid="stSidebar"] div[data-testid="stButton"] button:focus,
    section[data-testid="stSidebar"] div[data-testid="stButton"] button:focus-visible {
        background: transparent !important;
        background-color: transparent !important;
        background-image: none !important;
        border: 1.5px solid rgba(255, 255, 255, 0.3) !important;
        color: white !important;
        font-weight: 500 !important;
        font-size: 0.8rem !important;
        padding: 0.35rem 0.6rem !important;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15) !important;
        transition: all 0.3s ease !important;
    }
    
    /* Effet hover léger */
    section[data-testid="stSidebar"] div[data-testid="stButton"] button:hover {
        background: rgba(255, 255, 255, 0.1) !important;
        background-color: rgba(255, 255, 255, 0.1) !important;
        background-image: none !important;
        border: 2px solid rgba(255, 255, 255, 0.5) !important;
        color: white !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.25) !important;
    }
</style>
""", unsafe_allow_html=True)

# init historique des messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": WELCOME_MESSAGE
        }
    ]

st.title("Découvre les métiers dans l'informatique")
st.write("l'assistant **IA** Sparky t'aidera à découvrir les nombreux métiers !")

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

    ids, docs = query_rag(collection, prompt)
    print("[DEBUG] ids taken:", ids)

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

    # Appeler l'API et afficher la réponse
    with st.chat_message("assistant", avatar="🤖"):
        try:
            req_response = call_llm(messages)
            assistant_response = stream_llm_response(req_response)
            out_stream_response = st.write_stream(assistant_response)
        except Exception as e:
            out_stream_response = f"❌ Erreur : {str(e)}"
            st.write(out_stream_response)

    st.session_state.messages.append({"role": "assistant", "content": out_stream_response})
