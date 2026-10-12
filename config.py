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

OPENAI_API_KEY = _get("OPENAI_API_KEY")
OPENAI_BASE_URL = _get("OPENAI_BASE_URL")
OPENAI_MODEL = _get("OPENAI_MODEL", "gpt-4o-mini")
