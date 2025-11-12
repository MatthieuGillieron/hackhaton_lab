import streamlit as st
from src.ui.components.sidebar import setup_sidebar
from src.utils.llm_helper import SHARED_CSS, create_two_column_info


st.set_page_config(
    page_title="Cybersécurité - Pratique",
    page_icon="🔒",
    layout="wide"
)

setup_sidebar()
st.markdown(SHARED_CSS, unsafe_allow_html=True)

if st.button("← Retour"):
    st.switch_page("pages/2_🎯_pratique.py")

st.title("🔒 Cybersécurité")
st.write("---")


#Les 2 widget info / doc
st.markdown(create_two_column_info([
    {
        "title": "📚 Mission de Cybersécurité",
        "items": [
            "Analyse l'image ci-dessous attentivement",
            "Trouve le <strong>flag</strong> caché dans l'image",
            "Entre le flag dans le champ de texte",
            "Valide ta réponse pour voir si tu as réussi !"
        ]
    },
    {
        "title": "💡 Qu'est-ce qu'un Flag ?",
        "items": [
            "Une preuve que tu as résolu le défi",
            "Souvent un mot ou une phrase secrète",
            "Il peut être caché dans du texte, des images, ou du code",
            "📝 <strong>Astuce</strong> : Cherche bien, le flag est quelque part dans l'image !"
        ]
    }
]), unsafe_allow_html=True)

st.write("")
st.write("")



# Wrapper pour l'image et le champ de flag
with st.container(border=True):
    col_image, col_validation = st.columns([1, 1])
    
    with col_image:
        st.subheader("🖼️ Image à analyser")
        try:
            st.image("assets/images/cyber.jpeg", use_container_width=True)
        except Exception:
            st.error("❌ Impossible de charger l'image. Vérifie que le fichier 'assets/images/cyber.jpeg' existe.")
    
    with col_validation:
        st.subheader("🔑 Validation du Flag")
        

        flag_input = st.text_input(
            "Entre le flag que tu as trouvé :",
            placeholder="Écris le flag ici...",
            key="flag_input",
            help="Le flag est caché dans l'image"
        )
        
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
