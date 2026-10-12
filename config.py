import os
from dotenv import load_dotenv

load_dotenv()


def _get(name, default=""):
    try:
        import streamlit as st
        if name in st.secrets:
            return st.secrets[name]
    except Exception:
        pass
    return os.getenv(name, default)


# LLM settings (Streamlit Secrets or .env)
OPENAI_API_KEY = _get("OPENAI_API_KEY")
OPENAI_BASE_URL = _get("OPENAI_BASE_URL")
OPENAI_MODEL = _get("OPENAI_MODEL", "openai/gpt-oss-20b")

# Chunking
CHUNK_SIZE = int(_get("CHUNK_SIZE", 900))
CHUNK_OVERLAP = int(_get("CHUNK_OVERLAP", 150))

# Retrieval and embeddings
EMBEDDING_MODEL = _get("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
TOP_K = int(_get("TOP_K", 4))
