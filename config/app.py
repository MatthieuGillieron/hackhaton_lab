import streamlit as st

def apply_practice_cards_style():
    """Applique le style personnalisé pour les cards de pratique"""
    st.markdown("""
        <style>
        /* Styles UNIQUEMENT pour la page de sélection des cards */
        #practice-cards-page div.card-title {
            font-size: 1.8em;
            font-weight: bold;
            color: #1e3a8a;
            margin-bottom: 15px;
            text-align: center;
        }
        
        #practice-cards-page div.card-description {
            font-size: 1.05em;
            color: #4b5563;
            line-height: 1.7;
            text-align: justify;
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

def apply_sidebar_style():
    """Applique le style personnalisé à la sidebar"""
    st.markdown("""
    <style>
        /* Dégradé de couleur pour la sidebar */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #de388e 0%, #12aab2 100%) !important;
        }
        
        /* Ajuster la couleur du texte pour qu'il soit lisible sur le dégradé */
        [data-testid="stSidebar"] * {
            color: white !important;
        }
        
        /* Style des titres dans la sidebar */
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {
            color: white !important;
        }
        
        /* Style des séparateurs */
        [data-testid="stSidebar"] hr {
            border-color: rgba(255, 255, 255, 0.3) !important;
        }
    </style>
    """, unsafe_allow_html=True)

def setup_sidebar():
    """Configure la sidebar complète avec logo, navigation et style"""
    # Appliquer le style
    apply_sidebar_style()
    
    # Logo
    st.sidebar.image("images/42.png", use_container_width=True)
    
    # Titre Navigation
    st.sidebar.markdown('<p style="margin-bottom: -40px; margin-top: 75px; padding: 0;"><b>Navigation</b></p>', unsafe_allow_html=True)
    st.sidebar.write("---")
    
    # Menu de navigation
    st.sidebar.page_link("pages/chatbot.py", label="Chatbot", use_container_width=True)
    st.sidebar.page_link("pages/pratice.py", label="Pratique", use_container_width=True)
    
    st.sidebar.write("---")
    
    # Texte en bas de la sidebar
    st.sidebar.markdown('''
    <div style="position: fixed; bottom: 20px; left: 20px; text-align: left; font-size: 14px; font-weight: bold;">
    	Cité des Métiers 2025
    </div>
    ''', unsafe_allow_html=True)
