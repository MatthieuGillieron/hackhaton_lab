import streamlit as st
from config.app import setup_sidebar

st.set_page_config(
    page_title="IA LAB",
    page_icon="🚀",
    layout="wide"
)

def send_request(REQ):
    data = {
    #"model": "llama3",
    "model": "Qwen3-235B-A22B-Instruct-2507",
    "messages": [
    {"role": "system", "content": "You are a helpful assistant." },
    {"role": "user", "content": REQ}
    ],
    "temperature": 0.7
    }
    response = requests.post(BASE_URL, headers=HEADERS, json=data)
    res = response.json()
    print(res)
    print("################")
    content = res.get('choices', [{}])[0].get('message', {}).get('content', 'No content available')
    print(content)

def request_model():
    data = {
    "model": "llama3",
    "messages": [
    {"role": "system", "content": "You are a helpful assistant." },
    {"role": "user", "content": "quelle est la couleur du lac leman ?"}
    ],
    "temperature": 0.7
    }
    response = requests.post(BASE_URL, headers=HEADERS, json=data)

    #req = requests.request("POST", url = BASE_URL , data = data, headers = HEADERS)
    res = response.json()
    print(res)
    print("Salut")


# Configuration de la sidebar
setup_sidebar()

# Redirection vers la page chatbot
st.switch_page("pages/chatbot.py")
# Configuration de la sidebar

#request_model()
send_request("6*7")

#send_request("Quelle est la couleur du lac leman ?")