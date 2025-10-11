import streamlit as st
from config.app import setup_sidebar

st.set_page_config(
    page_title="Pratique - IA LAB",
    #page_icon="📝",
    layout="wide"
)

# Configuration de la sidebar
setup_sidebar()

# Afficher les cards de sélection
st.title("Essaye les différents domaines de l'informatique")
st.write("Choisissez votre domaine")

st.write("---")

# Création des cards

# Espacement
st.write("")
st.write("")

# Première ligne de cards avec marges
empty1, col1, col2, empty2 = st.columns([0.5, 2, 2, 0.5], gap="large")

with col1:
    with st.container(border=True):
        st.markdown('<p style="font-size: 1.8em; font-weight: bold; color: #1e3a8a; margin-bottom: 15px; text-align: center;">🔒 Cybersécurité</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 1.05em; color: #4b5563; line-height: 1.7; text-align: justify; margin-bottom: 20px;">Explorez les concepts de sécurité informatique, apprenez à protéger les systèmes et découvrez les techniques de défense contre les cybermenaces.</p>', unsafe_allow_html=True)
        
        if st.button("Commencer la pratique", key="cyber", use_container_width=True, type="primary"):
            st.switch_page("pages/pratice_cyber.py")

with col2:
    with st.container(border=True):
        st.markdown('<p style="font-size: 1.8em; font-weight: bold; color: #1e3a8a; margin-bottom: 15px; text-align: center;">💻 Développement Backend</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 1.05em; color: #4b5563; line-height: 1.7; text-align: justify; margin-bottom: 20px;">Maîtrisez les technologies serveur, les bases de données, les APIs REST et GraphQL, et créez des architectures robustes et scalables.</p>', unsafe_allow_html=True)
        
        if st.button("Commencer la pratique", key="backend", use_container_width=True, type="primary"):
            st.switch_page("pages/pratice_backend.py")

# Deuxième ligne de cards avec marges
empty3, col3, col4, empty4 = st.columns([0.5, 2, 2, 0.5], gap="large")

with col3:
    with st.container(border=True):
        st.markdown('<p style="font-size: 1.8em; font-weight: bold; color: #1e3a8a; margin-bottom: 15px; text-align: center;">🎮 Développement de Jeux Vidéo</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 1.05em; color: #4b5563; line-height: 1.7; text-align: justify; margin-bottom: 20px;">Créez des expériences interactives captivantes, apprenez les moteurs de jeu, la conception de gameplay et le développement de jeux 2D et 3D.</p>', unsafe_allow_html=True)
        
        if st.button("Commencer la pratique", key="gamedev", use_container_width=True, type="primary"):
            st.switch_page("pages/pratice_gamedev.py")

with col4:
    with st.container(border=True):
        st.markdown('<p style="font-size: 1.8em; font-weight: bold; color: #1e3a8a; margin-bottom: 15px; text-align: center;">🌐 Développement Frontend</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 1.05em; color: #4b5563; line-height: 1.7; text-align: justify; margin-bottom: 20px;">Développez des interfaces utilisateur modernes et réactives, maîtrisez HTML, CSS, JavaScript et les frameworks populaires comme React et Vue.</p>', unsafe_allow_html=True)
        
        if st.button("Commencer la pratique", key="frontend", use_container_width=True, type="primary"):
            st.switch_page("pages/pratice_frontend.py")
