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
uv run streamlit run main.py
```

The app will open automatically in your browser at `http://localhost:8501`

## What is uv.lock?

`uv.lock` is automatically generated and contains exact versions of all dependencies and their sub-dependencies. It ensures reproducible builds across different environments.

- **Don't edit manually** - it's auto-generated
- **Commit to version control** for consistent installs
- **Regenerated** when you modify dependencies


## 📚 doc

- [Documentation Streamlit](https://docs.streamlit.io)
- [Documentation uv](https://github.com/astral-sh/uv)
