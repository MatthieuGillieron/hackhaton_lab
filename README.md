# AI Assistant

## Quick Start

You need to install `uv` to install the correct Python version and the libraries.
Follow the instruction bellow to install it:
```sh
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or via pip
pip install uv
```

You need an API key for the LLM. Copy `.env_template` into `.env` and add your key and product ID.
Then, install the dependencies and run the Streamlit app:
```sh
# install dependencies from pyproject.toml
uv sync
# create the vector store
uv run notebooks/create_vector_store.py # create the vector
# run the app
uv run streamlit run main.py
```

The app should open automatically in your browser at `http://localhost:8501`.

## Project Structure

```
hackathon_start/
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

## License

MIT.
