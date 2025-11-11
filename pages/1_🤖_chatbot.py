import streamlit as st
from src.ui.components.sidebar import setup_sidebar
from src.core.rag import get_db_collection, query_rag
from src.core.llm import call_llm, stream_llm_response
from src.utils.constants import NETIQUETTE, WELCOME_MESSAGE
from src.utils.llm_helper import SHARED_CSS

#init db rag
collection = get_db_collection()


st.set_page_config(
    page_title="Chatbot",
    layout="wide"
)

setup_sidebar()


with st.sidebar:
    if st.button("🗑️ Effacer", key="clear_chat", width="stretch"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": WELCOME_MESSAGE
            }
        ]
        st.rerun()

st.markdown(SHARED_CSS, unsafe_allow_html=True)
st.markdown("""
<style>
    .main .block-container {
        padding-top: 1.5rem !important;
    }
    h1 {
        margin-top: 0 !important;
        padding-top: 0 !important;
    }
</style>
""", unsafe_allow_html=True)



# init historique
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

if prompt := st.chat_input("Écrivez votre message ici..."):
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    ids, docs = query_rag(collection, prompt)
    print("[DEBUG] ids taken:", ids)

    user_query: str = f"""{st.session_state["messages"]}

    Utilise ces documents obtenus d'un RAG pour compléter ta réponse a l'utilisateur: {docs}

    La question de l'utilisateur est: {prompt}
    """

    st.session_state.messages.append({"role": "user", "content": prompt})
    print("[DEBUG] Num words in user query: ", len(user_query.split()))

    messages = [
        {"role": "system", "content": NETIQUETTE},
        {"role": "user", "content": user_query},
    ]



    # call API + réponse
    with st.chat_message("assistant", avatar="🤖"):
        try:
            req_response = call_llm(messages)
            assistant_response = stream_llm_response(req_response)
            out_stream_response = st.write_stream(assistant_response)
        except Exception as e:
            out_stream_response = f"❌ Erreur : {str(e)}"
            st.write(out_stream_response)

    st.session_state.messages.append({"role": "assistant", "content": out_stream_response})
