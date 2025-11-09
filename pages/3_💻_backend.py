import streamlit as st
import re
from io import StringIO
from contextlib import redirect_stdout
from src.ui.components.sidebar import setup_sidebar
from src.ui.styles.practice import get_practice_page_style
from src.core.llm import explain_error_with_llm

st.set_page_config(
    page_title="Backend - Pratique",
    page_icon="💻",
    layout="wide"
)

setup_sidebar()

# Bouton retour
if st.button("← Retour à la sélection"):
    st.switch_page("pages/2_🎯_pratique.py")

# Titre et sous-titre
st.title("💻 Développement Backend")
#st.write(" Module de pratique en Développement Backend")
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
            <h4 style="color: #c81e70; margin-top: 0; font-size: 1.1em; font-weight: 600;">📚 Documentation</h4>
            <p style="color: #1a1a1a; font-weight: 500;">Voici quelque points clés à connaitre :</p>
            <ul style="color: #1a1a1a;">
                <li><code style="background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;">personage_1</code> est une variable : on peut lui donner une valeur</li>
                <li><code style="background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;">print</code> est une fonction qui permet d'afficher un message à l'écran</li>
                <li>Pour afficher du texte avec <code style="background-color: rgba(222, 56, 142, 0.1); padding: 2px 6px; border-radius: 4px;">print()</code>, on doit le mettre entre guillemets</li>
                <li>Pour recuperer la valeur d'une variable, on doit l'appeler sans les guillemets</li>
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
            <h4 style="color: #c81e70; margin-top: 0; font-size: 1.1em; font-weight: 600;">💡 Guide de pratique</h4>
            <p style="color: #1a1a1a; font-weight: 500;">Lis bien la documentation et essaie de comprendre les points clés.</p>
            <ul style="color: #1a1a1a;">
                <li>Ensuite rend toi dans l'éditeur de code en dessous</li>
                <li>Essaie de comprendre le code</li>
                <li>Modifie, regarde ce qu'il se passe</li>
                <li>Et essaie de finir l'exercice</li>
            </ul>
        </div>
    </div>
""", unsafe_allow_html=True)

# Espace entre les sections
st.write("")
st.write("")

# Initialiser le code par défaut
if 'backend_code' not in st.session_state:
    st.session_state['backend_code'] = """# Écrivez votre code Python ici
personnage_1 = "Christophe"
personnage_2 = "Frederic"

#print est une fonction qui permet d'afficher un message à l'écran
print("Salut, je m'appelle", personnage_1, "et toi ?")
print("Salut", personnage_1, "je m'appelle", personnage_2)
"""

# Initialiser le dernier code exécuté
if 'backend_last_executed' not in st.session_state:
    st.session_state['backend_last_executed'] = None

st.markdown(get_practice_page_style(), unsafe_allow_html=True)

# Wrapper pour IDE et résultat
with st.container(border=True):
    # Section IDE (gauche) et Output (droite)
    col_ide, col_output = st.columns(2)
    
    with col_ide:
        st.subheader("🖥️ Éditeur de Code Python")
        
        # Utiliser text_area pour une édition stable
        current_code = st.text_area(
            "Code Python",
            value=st.session_state['backend_code'],
            height=300,
            key="code_editor",
            help="Écrivez votre code Python ici",
            label_visibility="collapsed"
        )
        
        # Boutons en dessous de l'éditeur
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("Exécuter", use_container_width=True, type="primary", key="exec_btn"):
                # Sauvegarder le code et marquer comme devant être exécuté
                st.session_state['backend_code'] = current_code
                st.session_state['backend_last_executed'] = current_code
                st.rerun()
        with btn_col2:
            if st.button("Réinitialiser", use_container_width=True):
                st.session_state['backend_code'] = """# Écrivez votre code Python ici
personnage_1 = "Christophe"
personnage_2 = "Frederic"

#print est une fonction qui permet d'afficher un message à l'écran
print("Salut, je m'appelle", personnage_1, "et toi ?")
print("Salut", personnage_1, "je m'appelle", personnage_2)
"""
                st.session_state['backend_last_executed'] = None
                st.rerun()
    
    with col_output:
        st.subheader("📤 Résultat de l'exécution")
        
        # Conteneur avec bordure et hauteur fixe
        with st.container(border=True):
            # Zone de résultat avec hauteur fixe
            if st.session_state['backend_last_executed'] is not None:
                # Capturer la sortie avec contextlib
                output_buffer = StringIO()
                
                try:
                    # Exécuter le dernier code validé
                    with redirect_stdout(output_buffer):
                        exec(st.session_state['backend_last_executed'])
                    
                    output = output_buffer.getvalue()
                    
                    if output:
                        st.code(output, language="text")
                        st.success("✅ Code exécuté avec succès !")
                    else:
                        st.info("ℹ️ Le code s'est exécuté mais n'a rien affiché (pas de print())")
                        
                except Exception as e:
                    st.error(f"❌ Erreur lors de l'exécution :")
                    st.code(str(e), language="text")
                    
                    # Demander au LLM d'expliquer l'erreur
                    st.write("---")
                    
                    with st.spinner("Sparky analyse votre erreur..."):
                        explanation = explain_error_with_llm(
                            st.session_state['backend_last_executed'], 
                            str(e)
                        )
                    
                    # Convertir le markdown en HTML <strong> de manière plus robuste
                    # Remplacer les paires de ** par <strong>...</strong>
                    explanation_html = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', explanation)
                    # Remplacer les single backticks ` par des guillemets + gras
                    explanation_html = re.sub(r'`([^`]+)`', r'"<strong>\1</strong>"', explanation_html)
                    
                    # Remplacer les retours à la ligne par des <br>
                    explanation_html = explanation_html.replace("\n", "<br>")
                    
                    # Afficher l'explication avec le style glassmorphism
                    st.markdown(f"""
                    <div style="
                        background: linear-gradient(135deg, rgba(222, 56, 142, 0.08), rgba(18, 170, 178, 0.08));
                        backdrop-filter: blur(8px);
                        -webkit-backdrop-filter: blur(8px);
                        border-radius: 15px;
                        border: 1px solid rgba(222, 56, 142, 0.2);
                        padding: 20px;
                        box-shadow: 0 2px 8px 0 rgba(0, 0, 0, 0.08);
                        margin-top: 10px;
                    ">
                        <h4 style="color: #c81e70; margin-top: 0; font-size: 1.1em; font-weight: 600; margin-bottom: 15px;">🧠 Explication de l'erreur par Sparky</h4>
                        <p style="color: #1a1a1a; line-height: 1.6; margin-bottom: 0;">{explanation_html}</p>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                # Message par défaut centré avec hauteur fixe
                st.markdown(
                    """
                    <div style="height: 342px; display: flex; align-items: center; justify-content: center; color: #888;">
                        <p style="text-align: center;">Aucun résultat pour le moment.<br>Exécutez votre code pour voir le résultat ici.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
