"""Validation de code pour environnement pédagogique (12-16 ans)"""
import re

MAX_LINES = 20
DANGEROUS_KEYWORDS = ['import', 'exec', 'eval', 'open', '__', 'compile', 'globals', 'locals', 'vars', 'dir']

def validate_code_security(code: str, max_lines: int = MAX_LINES) -> tuple[bool, str]:
    """Valide uniquement la sécurité (pas la syntaxe)"""
    if not code.strip():
        return False, "Le code est vide"
    
    lines = [line for line in code.split('\n') if line.strip() and not line.strip().startswith('#')]
    if len(lines) > max_lines:
        return False, f"Trop de lignes de code (max {max_lines})"
    
    # Bloquer mots-clés dangereux
    code_lower = code.lower()
    for keyword in DANGEROUS_KEYWORDS:
        if keyword in code_lower:
            return False, f"Le mot '{keyword}' n'est pas autorisé"
    
    return True, ""


def validate_backend_code(code: str) -> tuple[bool, str]:
    """Valide code Python backend (sécurité uniquement)"""
    return validate_code_security(code)


def validate_frontend_code(code: str) -> tuple[bool, str]:
    """Valide code Streamlit frontend (sécurité uniquement)"""
    return validate_code_security(code)


def validate_gamedev_code(code: str) -> tuple[bool, str]:
    """Valide commandes JavaScript gamedev (whitelist stricte)"""
    if not code.strip():
        return False,
    
    lines = [line for line in code.split('\n') if line.strip() and not line.strip().startswith('//')]
    if len(lines) > MAX_LINES:
        return False,
    
    # Whitelist stricte: seulement haut/bas/gauche/droite
    allowed_pattern = r'^(haut|bas|gauche|droite)\(\d+\)$'
    for line in lines:
        if not re.match(allowed_pattern, line.strip()):
            return False, f"Commande non autorisée: {line.strip()[:50]}. Utilise: haut(n), bas(n), gauche(n), droite(n)"
    
    return True, ""


def safe_exec_python(code: str, allowed_globals: dict) -> tuple[bool, str, any]:
    """
    Exécute du code Python dans un environnement restreint
    
    Args:
        code: Code à exécuter
        allowed_globals: Dict des fonctions/variables autorisées
    
    Returns:
        (success, error_message, output)
    """
    try:
        restricted_globals = {'__builtins__': {}}
        restricted_globals.update(allowed_globals)
        
        exec(code, restricted_globals)
        return True, "", None
    except Exception as e:
        return False, str(e), None
