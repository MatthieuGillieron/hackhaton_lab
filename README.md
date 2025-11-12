# Project Setup with uv

## Installation

Install uv (Python package manager):
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.sh | iex"

# Or via pip
pip install uv
```

## Quick Start

```bash
# Install dependencies from pyproject.toml
uv sync

# Run the Streamlit app
add token in .env
uv run notebooks/create_vector_store.py
uv run streamlit run main.py
```

The app will open automatically in your browser at `http://localhost:8501`

## What is uv.lock?

`uv.lock` is automatically generated and contains exact versions of all dependencies and their sub-dependencies. It ensures reproducible builds across different environments.

- **Don't edit manually** - it's auto-generated
- **Commit to version control** for consistent installs
- **Regenerated** when you modify dependencies


## 📁 Project Structure

```
hackthon_start/
├── app.py                      # Main application entry point
├── pages/                      # Streamlit multi-page app
│   ├── 1_🤖_chatbot.py        # RAG chatbot with AI
│   ├── 2_🎯_pratique.py       # Practice modules selection
│   ├── 3_💻_backend.py        # Interactive Python editor
│   ├── 4_🌐_frontend.py       # Interactive Streamlit editor
│   ├── 5_🔒_cyber.py          # Cybersecurity challenge
│   └── 6_🎮_gamedev.py        # Interactive JavaScript game
├── src/
│   ├── core/                   # Business logic
│   │   ├── embeddings.py      # Embeddings management
│   │   ├── llm.py             # LLM integration (Bedrock)
│   │   └── rag.py             # RAG pipeline
│   ├── ui/                     # UI components
│   │   ├── components/        # Reusable components (sidebar, etc.)
│   │   └── styles/            # Custom CSS styles
│   └── utils/                  # Utilities
│       ├── config.py          # Configuration
│       └── constants.py       # Constants
├── data/                       # Data and vector database
│   ├── chroma.sqlite3         # ChromaDB database
│   └── links.csv              # Source data
├── notebooks/                  # Jupyter notebooks
│   └── create_vector_store.py # Vector store creation script
├── assets/                     # Static resources
│   └── images/                # Application images
├── .streamlit/                 # Streamlit configuration
│   └── config.toml            # Theme and settings
└── pyproject.toml             # Dependencies and project configuration
```

## 📚 Documentation

- [Documentation Streamlit](https://docs.streamlit.io)
- [Documentation uv](https://github.com/astral-sh/uv)
