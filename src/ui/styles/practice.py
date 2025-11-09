"""Styles CSS pour les pages de pratique"""


def get_practice_page_style() -> str:
    """Retourne le CSS commun pour toutes les pages de pratique"""
    return """
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
    
    /* Wrapper IDE - cibler tous les containers avec bordure sur cette page */
    section[data-testid="stVerticalBlock"] div[style*="border: 1px solid rgba(49, 51, 63, 0.2)"] {
        background: linear-gradient(135deg, rgba(222, 56, 142, 0.04), rgba(18, 170, 178, 0.04)) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        border-radius: 15px !important;
        border: 1px solid rgba(222, 56, 142, 0.2) !important;
        padding: 20px !important;
        box-shadow: 0 2px 8px 0 rgba(0, 0, 0, 0.08) !important;
    }
</style>
"""
