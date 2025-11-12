import streamlit as st
from src.ui.components.sidebar import setup_sidebar
from src.utils.llm_helper import (
    explain_error_with_llm,
    format_error_explanation,
    SHARED_CSS,
    create_two_column_info,
)

st.set_page_config(page_title="Frontend - Pratique", page_icon="🌐", layout="wide")

setup_sidebar()
st.markdown(SHARED_CSS, unsafe_allow_html=True)

if st.button("← Retour"):
    st.switch_page("pages/2_🎯_pratique.py")

st.title("🌐 Développement Frontend")
st.write("---")


# Les 2 widget doc / info
st.markdown(
    create_two_column_info(
        [
            {
                "title": "📚 Documentation Streamlit",
                "items": [
                    "<code style='background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;'>st.title(\"Mon titre\")</code> : Affiche un titre principal",
                    "<code style='background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;'>st.header(\"Mon en-tête\")</code> : Affiche un sous-titre",
                    "<code style='background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;'>st.write(\"Mon texte\")</code> : Affiche du texte simple",
                    "<code style='background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;'>st.balloons()</code> : Déclenche l'effet des ballons 🎈",
                ],
            },
            {
                "title": "💡 Exercice pratique",
                "items": [
                    "<strong>Objectif</strong> : Créer une page web simple",
                    "Utilise <code style='background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;'>st.title()</code> pour créer un titre",
                    "Ajoute du texte avec <code style='background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;'>st.write()</code>",
                    "Déclenche l'effet des ballons avec <code style='background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;'>st.balloons()</code>",
                    "Clique sur Exécuter pour voir le résultat !",
                ],
            },
        ]
    ),
    unsafe_allow_html=True,
)

st.write("")
st.write("")


# init du code
if "frontend_code" not in st.session_state:
    st.session_state["frontend_code"] = """
st.title("Yo c'est Matthieu")
st.write("Bienvenue dans le monde du développement frontend !")
st.balloons()
"""

if "frontend_last_executed" not in st.session_state:
    st.session_state["frontend_last_executed"] = None

with st.container(border=True):
    col_ide, col_output = st.columns([45, 55])

    with col_ide:
        st.subheader("🖥️ Éditeur de Code Streamlit")

        current_code = st.text_area(
            "Code Streamlit",
            value=st.session_state["frontend_code"],
            height=300,
            key="code_editor_frontend",
            help="Écrivez votre code Streamlit ici",
            label_visibility="collapsed",
        )

        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button(
                "Exécuter", use_container_width=True, type="primary", key="exec_btn"
            ):
                st.session_state["frontend_code"] = current_code
                st.session_state["frontend_last_executed"] = current_code
                st.rerun()
        with btn_col2:
            if st.button("Réinitialiser", use_container_width=True):
                st.session_state["frontend_code"] = """
st.title("Yo c'est Matthieu")
st.write("Bienvenue dans le monde du développement frontend !")
st.balloons()
"""
                st.session_state["frontend_last_executed"] = None
                st.rerun()

    with col_output:
        st.subheader("📤 Aperçu de votre page")

        with st.container(border=True, height=500):
            if st.session_state["frontend_last_executed"] is not None:
                try:
                    exec(st.session_state["frontend_last_executed"])

                except Exception as e:
                    st.error("❌ Erreur lors de l'exécution :")
                    st.code(str(e), language="text")
                    st.write("---")
                    with st.spinner("Sparky analyse votre erreur..."):
                        explanation = explain_error_with_llm(
                            st.session_state["frontend_last_executed"],
                            str(e),
                            "Streamlit",
                        )
                    st.markdown(
                        format_error_explanation(explanation), unsafe_allow_html=True
                    )
            else:
                st.markdown(
                    """
                    <div style="height: 400px; display: flex; align-items: center; justify-content: center; color: #888;">
                        <p style="text-align: center;">Aucun aperçu pour le moment.<br>Exécutez votre code pour voir le résultat ici.</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
