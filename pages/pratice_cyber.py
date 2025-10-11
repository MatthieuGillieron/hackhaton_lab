import streamlit as st
from config.app import setup_sidebar

st.set_page_config(
    page_title="Cybersécurité - Pratique",
    page_icon="🔒",
    layout="wide"
)

# Configuration de la sidebar
setup_sidebar()

# Bouton retour
if st.button("← Retour à la sélection"):
    st.switch_page("pages/pratice.py")

# Titre et sous-titre
st.title("🔒 Cybersécurité")
st.write("### Module de pratique en Cybersécurité")

st.write("---")

# Contenu du module
st.info("💡 Bienvenue dans le module de Cybersécurité !")

# Exemple de contenu à développer
with st.expander("📚 Introduction"):
    st.write("""
    Ce module couvre les concepts fondamentaux de la cybersécurité :
    - Protection des systèmes et des données
    - Techniques de défense contre les cybermenaces
    - Analyse des vulnérabilités
    - Bonnes pratiques de sécurité
    """)

with st.expander("🎯 Exercices pratiques"):
    st.write("Les exercices pratiques seront ajoutés ici.")

with st.expander("📝 Quiz"):
    st.write("Le quiz d'évaluation sera ajouté ici.")
