import streamlit as st
from config.app import setup_sidebar

st.set_page_config(
    page_title="Cybersécurité - Pratique",
    page_icon="🔒",
    layout="wide"
)

# Configuration de la sidebar
setup_sidebar()

# CSS pour styliser les boutons et réduire les marges
st.markdown("""
<style>
    /* Cacher/réduire le header blanc de Streamlit */
    header[data-testid="stHeader"] {
        background-color: transparent !important;
        height: 0 !important;
    }
    
    /* Réduire les marges en haut de la page */
    section.main > div {
        padding-top: 2rem !important;
    }
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 1rem !important;
        max-width: 100% !important;
    }
    
    /* Ajuster l'espacement du premier élément */
    section[data-testid="stVerticalBlock"] > div:first-child {
        padding-top: 0 !important;
    }
    
    /* Styliser les boutons Streamlit */
    button[kind="primary"] {
        background: linear-gradient(135deg, rgba(222, 56, 142, 0.15), rgba(18, 170, 178, 0.15)) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        border: 1px solid rgba(222, 56, 142, 0.3) !important;
        color: #de388e !important;
        font-weight: 600 !important;
        box-shadow: 0 2px 8px 0 rgba(0, 0, 0, 0.08) !important;
    }
    
    button[kind="primary"]:hover {
        background: linear-gradient(135deg, rgba(222, 56, 142, 0.25), rgba(18, 170, 178, 0.25)) !important;
        border: 1px solid rgba(222, 56, 142, 0.5) !important;
        box-shadow: 0 4px 12px rgba(222, 56, 142, 0.2) !important;
        transform: translateY(-1px) !important;
    }
    
    button[kind="secondary"] {
        background: white !important;
        border: 1px solid rgba(222, 56, 142, 0.5) !important;
        color: #de388e !important;
        box-shadow: 0 2px 8px 0 rgba(0, 0, 0, 0.05) !important;
    }
    
    button[kind="secondary"]:hover {
        background: rgba(222, 56, 142, 0.1) !important;
        border: 1px solid rgba(222, 56, 142, 0.8) !important;
    }
</style>
""", unsafe_allow_html=True)

# Bouton retour
if st.button("← Retour à la sélection"):
    st.switch_page("pages/pratice.py")

# Titre et sous-titre
st.title("🔒 Cybersécurité")
st.write("---")

# Sections avec effet glassmorphism subtil
st.markdown("""
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 20px;">
        <div style="
            background: linear-gradient(135deg, rgba(222, 56, 142, 0.08), rgba(18, 170, 178, 0.08));
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border-radius: 15px;
            border: 1px solid rgba(222, 56, 142, 0.2);
            padding: 20px;
            box-shadow: 0 2px 8px 0 rgba(0, 0, 0, 0.08);
        ">
            <h4 style="color: #c81e70; margin-top: 0; font-size: 1.1em; font-weight: 600;">📚 Mission de Cybersécurité</h4>
            <p style="color: #1a1a1a; font-weight: 500;">Voici ton défi :</p>
            <ul style="color: #1a1a1a;">
                <li>Analyse l'image ci-dessous attentivement</li>
                <li>Trouve le <strong>flag</strong> caché dans l'image</li>
                <li>Entre le flag dans le champ de texte</li>
                <li>Valide ta réponse pour voir si tu as réussi !</li>
            </ul>
        </div>
        <div style="
            background: linear-gradient(135deg, rgba(222, 56, 142, 0.08), rgba(18, 170, 178, 0.08));
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border-radius: 15px;
            border: 1px solid rgba(222, 56, 142, 0.2);
            padding: 20px;
            box-shadow: 0 2px 8px 0 rgba(0, 0, 0, 0.08);
        ">
            <h4 style="color: #c81e70; margin-top: 0; font-size: 1.1em; font-weight: 600;">💡 Qu'est-ce qu'un Flag ?</h4>
            <p style="color: #1a1a1a; font-weight: 500;">En cybersécurité, un <strong>flag</strong> est :</p>
            <ul style="color: #1a1a1a;">
                <li>Une preuve que tu as résolu le défi</li>
                <li>Souvent un mot ou une phrase secrète</li>
                <li>Il peut être caché dans du texte, des images, ou du code</li>
                <li>📝 <strong>Astuce</strong> : Cherche bien, le flag est quelque part dans l'image !</li>
            </ul>
        </div>
    </div>
""", unsafe_allow_html=True)

# Espace entre les sections
st.write("")
st.write("")

# Wrapper pour l'image et le champ de flag
with st.container(border=True):
    # Section Image (gauche) et Validation (droite)
    col_image, col_validation = st.columns([1, 1])
    
    with col_image:
        st.subheader("🖼️ Image à analyser")
        try:
            st.image("images/cyber.jpeg", use_container_width=True)
        except:
            st.error("❌ Impossible de charger l'image. Vérifie que le fichier 'images/cyber.jpeg' existe.")
    
    with col_validation:
        st.subheader("🔑 Validation du Flag")
        
        # Champ texte pour entrer le flag
        flag_input = st.text_input(
            "Entre le flag que tu as trouvé :",
            placeholder="Écris le flag ici...",
            key="flag_input",
            help="Le flag est caché dans l'image"
        )
        
        # Bouton de validation
        if st.button("Valider le Flag", use_container_width=True, type="primary"):
            if flag_input.strip().lower() == "cybersec":
                st.success("🎉 Bravo ! Tu as trouvé le bon flag !")
                st.balloons()
                st.markdown("""
                <div style="
                    background: linear-gradient(135deg, rgba(18, 170, 178, 0.1), rgba(222, 56, 142, 0.1));
                    padding: 20px;
                    border-radius: 10px;
                    margin-top: 20px;
                    border: 2px solid rgba(18, 170, 178, 0.3);
                ">
                    <h3 style="color: #12aab2; margin-top: 0;">✅ Mission accomplie !</h3>
                    <p style="color: #1a1a1a; font-size: 1.1em;">Tu as réussi ton premier défi de cybersécurité ! Continue comme ça ! 🚀</p>
                </div>
                """, unsafe_allow_html=True)
            elif flag_input.strip() == "":
                st.warning("⚠️ Le champ est vide. Entre un flag pour valider !")
            else:
                st.error("❌ Ce n'est pas le bon flag. Réessaye !")
                st.markdown("""
                <div style="
                    background: rgba(222, 56, 142, 0.05);
                    padding: 15px;
                    border-radius: 10px;
                    margin-top: 15px;
                    border-left: 4px solid #de388e;
                ">
                    <p style="color: #1a1a1a; margin: 0;"><strong>💡 Indice :</strong> Regarde attentivement l'image. Le flag est un mot en minuscules.</p>
                </div>
                """, unsafe_allow_html=True)
