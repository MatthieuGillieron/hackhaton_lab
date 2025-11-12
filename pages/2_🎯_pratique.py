import streamlit as st
from src.ui.components.sidebar import setup_sidebar
from src.utils.llm_helper import SHARED_CSS


st.set_page_config(
    page_title="Pratique - IA LAB",
    # page_icon="📝",
    layout="wide",
)

setup_sidebar()

st.markdown(SHARED_CSS, unsafe_allow_html=True)

st.title("Essaye les différents domaines de l'informatique")
st.write("Amuse-toi ici, tu seras aidé-e par Sparky !")

st.write("---")
st.write("")
st.write("")


# Première ligne de cards avec marges
empty1, col1, col2, empty2 = st.columns([0.5, 2, 2, 0.5], gap="large")

with col1:
    with st.container(border=True):
        st.markdown(
            '<p style="font-size: 1.8em; font-weight: bold; color: #c81e70; margin-bottom: 15px; text-align: center;">🔒 Cybersécurité</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p style="font-size: 1.05em; color: #4b5563; line-height: 1.7; text-align: justify; margin-bottom: 20px;">Protège les systèmes informatiques contre les cyberattaques. Tu détectes les failles de sécurité, analyses les menaces et mets en place des solutions pour sécuriser les données sensibles des entreprises et des utilisateurs.</p>',
            unsafe_allow_html=True,
        )

        if st.button(
            "Commencer la pratique",
            key="cyber",
            use_container_width=True,
            type="primary",
        ):
            st.switch_page("pages/5_🔒_cyber.py")

with col2:
    with st.container(border=True):
        st.markdown(
            '<p style="font-size: 1.8em; font-weight: bold; color: #c81e70; margin-bottom: 15px; text-align: center;">💻 Développement Backend</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p style="font-size: 1.05em; color: #4b5563; line-height: 1.7; text-align: justify; margin-bottom: 20px;">Développe la partie invisible des applications : bases de données, serveurs, APIs. Tu gères la logique métier, le stockage et le traitement sécurisé des données, et tu assures que tout fonctionne correctement côté serveur.</p>',
            unsafe_allow_html=True,
        )

        if st.button(
            "Commencer la pratique",
            key="backend",
            use_container_width=True,
            type="primary",
        ):
            st.switch_page("pages/3_💻_backend.py")


# Deuxième ligne de cards avec marges
empty3, col3, col4, empty4 = st.columns([0.5, 2, 2, 0.5], gap="large")

with col3:
    with st.container(border=True):
        st.markdown(
            '<p style="font-size: 1.8em; font-weight: bold; color: #c81e70; margin-bottom: 15px; text-align: center;">🎮 Développement de Jeux</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p style="font-size: 1.05em; color: #4b5563; line-height: 1.7; text-align: justify; margin-bottom: 20px;">Crée des jeux vidéo en programmant le gameplay, les graphismes et les interactions. Tu donnes vie à des univers virtuels, développes des mécaniques de jeu et optimises les performances pour une expérience fluide.</p>',
            unsafe_allow_html=True,
        )

        if st.button(
            "Commencer la pratique",
            key="gamedev",
            use_container_width=True,
            type="primary",
        ):
            st.switch_page("pages/6_🎮_gamedev.py")

with col4:
    with st.container(border=True):
        st.markdown(
            '<p style="font-size: 1.8em; font-weight: bold; color: #c81e70; margin-bottom: 15px; text-align: center;">🌐 Développement Frontend</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style=\"font-size: 1.05em; color: #4b5563; line-height: 1.7; text-align: justify; margin-bottom: 20px;\">Conçoit l'interface visuelle des sites web et applications. Tu transformes les maquettes en code, crées des animations et tu t'assures que l'expérience utilisateur soit intuitive et responsive sur tous les appareils.</p>",
            unsafe_allow_html=True,
        )

        if st.button(
            "Commencer la pratique",
            key="frontend",
            use_container_width=True,
            type="primary",
        ):
            st.switch_page("pages/4_🌐_frontend.py")
