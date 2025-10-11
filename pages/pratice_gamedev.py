import streamlit as st
from config.app import setup_sidebar

st.set_page_config(
    page_title="Game Dev - Pratique",
    page_icon="🎮",
    layout="wide"
)

# Configuration de la sidebar
setup_sidebar()

# Bouton retour
if st.button("← Retour à la sélection"):
    st.switch_page("pages/pratice.py")

# Titre et sous-titre
st.title("🎮 Développement de Jeux Vidéo")
st.write("### Module de pratique en Développement de Jeux Vidéo")

st.write("---")

# Contenu du module
st.info("💡 Bienvenue dans le module de Développement de Jeux Vidéo !")

# Exemple de contenu à développer
with st.expander("📚 Introduction"):
    st.write("""
    Ce module couvre le développement de jeux vidéo :
    - Moteurs de jeu (Unity, Unreal, Godot)
    - Conception de gameplay
    - Développement de jeux 2D et 3D
    - Animation et physique
    """)

with st.expander("🎯 Exercices pratiques"):
    st.write("Les exercices pratiques seront ajoutés ici.")

with st.expander("📝 Quiz"):
    st.write("Le quiz d'évaluation sera ajouté ici.")
