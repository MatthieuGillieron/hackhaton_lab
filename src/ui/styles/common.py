"""Styles CSS communs"""


def get_sidebar_style() -> str:
    """Retourne le CSS pour la sidebar"""
    return """
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
    """


def get_button_style() -> str:
    """Retourne le CSS pour les boutons"""
    return """
    <style>
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
    </style>
    """
