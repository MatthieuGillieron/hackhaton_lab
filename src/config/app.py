import streamlit as st

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
