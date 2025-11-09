# 📁 Structure du projet Sparky

## 🚀 Lancer l'application

```bash
uv run streamlit run app.py
```

## 📂 Architecture

```
hackthon_start/
├── app.py                        # Point d'entrée principal
├── src/                          # Code source
│   ├── core/                     # Logique métier
│   │   ├── embeddings.py        # Classes d'embeddings ChromaDB
│   │   ├── llm.py               # Client API LLM
│   │   └── rag.py               # Gestion base vectorielle
│   ├── ui/                       # Interface utilisateur
│   │   ├── components/          # Composants réutilisables
│   │   │   └── sidebar.py
│   │   └── styles/              # Styles CSS
│   │       └── common.py
│   └── utils/                    # Utilitaires
│       ├── config.py            # Configuration centralisée
│       └── constants.py         # Constantes (prompts, etc.)
├── pages/                        # Pages Streamlit
│   ├── 1_🤖_chatbot.py
│   ├── 2_🎯_pratique.py
│   ├── 3_💻_backend.py
│   ├── 4_🌐_frontend.py
│   ├── 5_🔒_cyber.py
│   └── 6_🎮_gamedev.py
├── data/                         # Données et base vectorielle
├── assets/                       # Ressources statiques
│   └── images/
├── notebooks/                    # Scripts de création de données
└── scripts/                      # Scripts utilitaires
```

## 🔄 Retour en arrière (si besoin)

Si la nouvelle structure pose problème :

```bash
git checkout backup-old-structure
```
