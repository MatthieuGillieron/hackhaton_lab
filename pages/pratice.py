import streamlit as st

st.set_page_config(
    page_title="Pratique - IA LAB",
    page_icon="📝",
    layout="wide"
)

import sys
import os

# Ajouter le chemin du dossier pages au path Python
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from config.app import setup_sidebar, apply_practice_cards_style

# Imports des modules de pratique
from practice_modules.cyber import render_cyber_content
from practice_modules.backend import render_backend_content
from practice_modules.gamedev import render_gamedev_content
from practice_modules.frontend import render_frontend_content

# Configuration de la sidebar
setup_sidebar()

# Application du style des cards
apply_practice_cards_style()

# Initialiser le state
if 'selected_practice' not in st.session_state:
    st.session_state['selected_practice'] = None

# Vérifier si un module est sélectionné
if st.session_state['selected_practice'] is None:
    # Afficher les cards de sélection
    st.title("📝 Pratique")
    st.write("Bienvenue sur la page de pratique")
    
    st.write("---")
    
    # Création des cards
    st.subheader("Choisissez votre domaine de pratique")
    
    # Première ligne de cards
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        with st.container(border=True):
            st.image("images/cyber.jpeg", use_container_width=True)
            st.markdown('<div class="card-title">🔒 Cybersécurité</div>', unsafe_allow_html=True)
            st.markdown('<div class="card-description">Explorez les concepts de sécurité informatique, apprenez à protéger les systèmes et découvrez les techniques de défense contre les cybermenaces.</div>', unsafe_allow_html=True)
            
            if st.button("Commencer la pratique", key="cyber", use_container_width=True, type="primary"):
                st.session_state['selected_practice'] = 'cyber'
                st.rerun()
    
    with col2:
        with st.container(border=True):
            st.image("images/cyber.jpeg", use_container_width=True)
            st.markdown('<div class="card-title">💻 Développement Backend</div>', unsafe_allow_html=True)
            st.markdown('<div class="card-description">Maîtrisez les technologies serveur, les bases de données, les APIs REST et GraphQL, et créez des architectures robustes et scalables.</div>', unsafe_allow_html=True)
            
            if st.button("Commencer la pratique", key="backend", use_container_width=True, type="primary"):
                st.session_state['selected_practice'] = 'backend'
                st.rerun()
    
    # Deuxième ligne de cards
    col3, col4 = st.columns(2, gap="large")
    
    with col3:
        with st.container(border=True):
            st.image("images/cyber.jpeg", use_container_width=True)
            st.markdown('<div class="card-title">🎮 Développement de Jeux Vidéo</div>', unsafe_allow_html=True)
            st.markdown('<div class="card-description">Créez des expériences interactives captivantes, apprenez les moteurs de jeu, la conception de gameplay et le développement de jeux 2D et 3D.</div>', unsafe_allow_html=True)
            
            if st.button("Commencer la pratique", key="gamedev", use_container_width=True, type="primary"):
                st.session_state['selected_practice'] = 'gamedev'
                st.rerun()
    
    with col4:
        with st.container(border=True):
            st.image("images/cyber.jpeg", use_container_width=True)
            st.markdown('<div class="card-title">🌐 Développement Frontend</div>', unsafe_allow_html=True)
            st.markdown('<div class="card-description">Développez des interfaces utilisateur modernes et réactives, maîtrisez HTML, CSS, JavaScript et les frameworks populaires comme React et Vue.</div>', unsafe_allow_html=True)
            
            if st.button("Commencer la pratique", key="frontend", use_container_width=True, type="primary"):
                st.session_state['selected_practice'] = 'frontend'
                st.rerun()

else:
    # Afficher le contenu du module sélectionné
    module = st.session_state['selected_practice']
    
    # Bouton de retour en haut
    if st.button("← Retour aux modules", type="secondary"):
        st.session_state['selected_practice'] = None
        st.rerun()
    
    st.write("---")
    
    # Afficher le contenu selon le module
    if module == 'cyber':
        render_cyber_content()
        
    elif module == 'backend':
        render_backend_content()
        
    elif module == 'gamedev':
        render_gamedev_content()
        
    elif module == 'frontend':
        render_frontend_content()

