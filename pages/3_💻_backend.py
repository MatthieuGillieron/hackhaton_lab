import streamlit as st
from io import StringIO
from contextlib import redirect_stdout
from src.ui.components.sidebar import setup_sidebar
from src.utils.llm_helper import (
    explain_error_with_llm,
    format_error_explanation,
    SHARED_CSS,
    create_two_column_info,
)


st.set_page_config(page_title="Backend - Pratique", page_icon="💻", layout="wide")

setup_sidebar()

if st.button("← Retour"):
    st.switch_page("pages/2_🎯_pratique.py")

st.title("💻 Développement Backend")
st.write("---")

# Les 2 widget (doc + tuto)

st.markdown(
    create_two_column_info(
        [
            {
                "title": "📚 Documentation",
                "items": [
                    "<code style='background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;'>personnage_1</code> est une variable : tu peux lui donner une valeur",
                    "<code style='background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;'>print</code> est une fonction qui permet d'afficher un message à l'écran",
                    "Pour afficher du texte avec <code style='background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;'>print()</code>, il faut le mettre entre guillemets: <code style='background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;'>print(\"exemple\")</code>",
                    "Pour récuperer la valeur d'une variable, il faut l'appeler sans les guillemets: <code style='background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;'>print(var)</code>",
                ],
            },
            {
                "title": "💡 Guide de pratique",
                "items": [
                    "Lis la documentation et essaie de comprendre comment afficher du texte",
                    "Ensuite, rend toi dans l'éditeur de code en dessous",
                    "Essaie de comprendre le code et éxecute le en appuyant sur <i>Exécuter</i>",
                    "Modifie une variable, lance le code et regarde ce qu'il se passe",
                ],
            },
        ]
    ),
    unsafe_allow_html=True,
)

st.write("")
st.write("")


# Init le code (defaut)
if "backend_code" not in st.session_state:
    st.session_state["backend_code"] = """
personnage_1 = "Christophe"
personnage_2 = "Julie"

print("Salut, je m'appelle", personnage_1)
print("Salut", personnage_1, ", je m'appelle", personnage_2)
"""

if "backend_last_executed" not in st.session_state:
    st.session_state["backend_last_executed"] = None

st.markdown(SHARED_CSS, unsafe_allow_html=True)


# Wrapper pour IDE et résultat
with st.container(border=True):
    col_ide, col_output = st.columns(2)

    with col_ide:
        st.subheader("🖥️ Éditeur de Code Python")

        current_code = st.text_area(
            "Code Python",
            value=st.session_state["backend_code"],
            height=300,
            key="code_editor",
            help="Écrivez votre code Python ici",
            label_visibility="collapsed",
        )

        # Boutons en dessous de l'IDE
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button(
                "Exécuter", use_container_width=True, type="primary", key="exec_btn"
            ):
                st.session_state["backend_code"] = current_code
                st.session_state["backend_last_executed"] = current_code
                st.rerun()
        with btn_col2:
            if st.button("Réinitialiser", use_container_width=True):
                st.session_state["backend_code"] = """# Écrivez votre code Python ici
personnage_1 = "Christophe"
personnage_2 = "Frederic"

print("Salut, je m'appelle", personnage_1, "et toi ?")
print("Salut", personnage_1, "je m'appelle", personnage_2)
"""
                st.session_state["backend_last_executed"] = None
                st.rerun()

    with col_output:
        st.subheader("📤 Résultat de l'exécution")

        with st.container(border=True):
            if st.session_state["backend_last_executed"] is not None:
                output_buffer = StringIO()

                try:
                    with redirect_stdout(output_buffer):
                        exec(st.session_state["backend_last_executed"])

                    output = output_buffer.getvalue()

                    if output:
                        st.code(output, language="text")
                        st.success("✅ Code exécuté avec succès !")
                    else:
                        st.info(
                            "ℹ️ Le code s'est exécuté mais n'a rien affiché (pas de print())"
                        )

                except Exception as e:
                    st.error("❌ Erreur lors de l'exécution :")
                    st.code(str(e), language="text")

                    st.write("---")
                    with st.spinner("Sparky analyse votre erreur..."):
                        explanation = explain_error_with_llm(
                            st.session_state["backend_last_executed"], str(e)
                        )
                    st.markdown(
                        format_error_explanation(explanation), unsafe_allow_html=True
                    )
            else:
                st.markdown(
                    """
                    <div style="height: 342px; display: flex; align-items: center; justify-content: center; color: #888;">
                        <p style="text-align: center;">Aucun résultat pour le moment.<br>Exécutez votre code pour voir le résultat ici.</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
