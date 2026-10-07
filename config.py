import os

from dotenv import load_dotenv
import streamlit as st

load_dotenv()


def _secret(name: str, default: str = "") -> str:
    """Read a value from Streamlit Secrets, falling back safely when secrets are unavailable."""
    try:
        value = st.secrets.get(name, default)
    except Exception:
        value = default
    return str(value).strip()


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip() or _secret("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "").strip() or _secret("OPENAI_BASE_URL")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "").strip() or _secret("OPENAI_MODEL", "gpt-4o-mini")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "").strip() or _secret("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "800"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "120"))
TOP_K = int(os.getenv("TOP_K", "4"))

if CHUNK_SIZE <= 0:
    raise ValueError("CHUNK_SIZE must be greater than 0.")
if CHUNK_OVERLAP < 0 or CHUNK_OVERLAP >= CHUNK_SIZE:
    raise ValueError("CHUNK_OVERLAP must be >= 0 and smaller than CHUNK_SIZE.")
