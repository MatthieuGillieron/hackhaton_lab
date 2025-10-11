import streamlit as st
import sys
from io import StringIO

def render_backend_content():
    """Affiche le contenu du module Développement Backend"""
    st.title("💻 Développement Backend")
    st.write("### Module de pratique en Développement Backend")
    
    st.write("---")
    
    # Contenu du module
    st.info("💡 Bienvenue dans le module de Développement Backend !")
    
    # Exemple de contenu à développer
    with st.expander("📚 Introduction", expanded=True):
        st.write("""
        Ce module couvre les technologies backend modernes :
        - Développement serveur avec Python, Node.js, etc.
        - Gestion des bases de données (SQL, NoSQL)
        - Création d'APIs REST et GraphQL
        - Architecture et scalabilité
        """)
    
    # Éditeur de code interactif
    st.write("---")
    st.subheader("🖥️ Éditeur de Code Python")
    st.write("Écrivez et testez votre code Python directement ici !")
    
    # Initialiser le code par défaut
    if 'backend_code' not in st.session_state:
        st.session_state['backend_code'] = """# Écrivez votre code Python ici
def saluer(nom):
    return f"Bonjour, {nom}!"

# Testez votre fonction
resultat = saluer("Développeur")
print(resultat)
"""
    
    # Créer deux colonnes pour l'éditeur et les options
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Éditeur de code
        code = st.text_area(
            "Code Python",
            value=st.session_state['backend_code'],
            height=300,
            key="code_editor",
            help="Écrivez votre code Python ici"
        )
        st.session_state['backend_code'] = code
    
    with col2:
        st.write("**Actions**")
        
        # Bouton pour réinitialiser
        if st.button("🔄 Réinitialiser", use_container_width=True):
            st.session_state['backend_code'] = """# Écrivez votre code Python ici
def saluer(nom):
    return f"Bonjour, {nom}!"

# Testez votre fonction
resultat = saluer("Développeur")
print(resultat)
"""
            st.rerun()
        
        # Bouton pour exécuter
        run_code = st.button("▶️ Exécuter", use_container_width=True, type="primary")
        
        st.write("---")
        st.write("**Exemples**")
        
        example = st.selectbox(
            "Charger un exemple",
            ["Aucun", "Hello World", "Fonction somme", "Liste et boucle", "API Flask"],
            label_visibility="collapsed"
        )
    
    # Charger l'exemple sélectionné
    if example != "Aucun":
        examples = {
            "Hello World": """# Hello World en Python
print("Hello, World!")
print("Bienvenue dans le Backend!")
""",
            "Fonction somme": """# Fonction pour additionner deux nombres
def additionner(a, b):
    return a + b

# Test
resultat = additionner(5, 3)
print(f"5 + 3 = {resultat}")
""",
            "Liste et boucle": """# Manipulation de listes
langages = ["Python", "JavaScript", "Java", "Go"]

print("Langages backend populaires:")
for i, langage in enumerate(langages, 1):
    print(f"{i}. {langage}")
""",
            "API Flask": """# Exemple simple d'API Flask
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Bonjour depuis l'API!"})

# Note: Cet exemple montre la structure
# Pour exécuter Flask, utilisez un environnement adapté
print("Structure API Flask créée!")
"""
        }
        st.session_state['backend_code'] = examples[example]
        st.rerun()
    
    # Zone de résultat
    if run_code:
        st.write("---")
        st.subheader("📤 Résultat de l'exécution")
        
        # Capturer la sortie
        old_stdout = sys.stdout
        redirected_output = StringIO()
        sys.stdout = redirected_output
        
        try:
            # Exécuter le code
            exec(code)
            output = redirected_output.getvalue()
            
            if output:
                st.code(output, language="text")
                st.success("✅ Code exécuté avec succès !")
            else:
                st.info("ℹ️ Le code s'est exécuté sans afficher de résultat.")
                
        except Exception as e:
            st.error(f"❌ Erreur lors de l'exécution :\n```\n{str(e)}\n```")
        
        finally:
            # Restaurer stdout
            sys.stdout = old_stdout
    
    st.write("---")
    
    with st.expander("🎯 Exercices pratiques"):
        st.write("""
        ### Exercice 1 : Créer une fonction
        Créez une fonction qui prend un nombre en paramètre et retourne son carré.
        
        ### Exercice 2 : Manipulation de dictionnaires
        Créez un dictionnaire représentant un utilisateur (nom, email, age) et affichez ses informations.
        
        ### Exercice 3 : API simple
        Écrivez une fonction qui simule une réponse d'API (retourne un dictionnaire JSON).
        """)
    
    with st.expander("📝 Quiz"):
        st.write("Le quiz d'évaluation sera ajouté ici.")

