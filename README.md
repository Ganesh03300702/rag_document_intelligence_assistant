# RAG Document Intelligence Assistant

A practical Retrieval-Augmented Generation application: PDF/TXT ingestion → chunking → Sentence-Transformer embeddings → FAISS semantic retrieval → context-grounded LLM answers with source/page references.

## Stack
Python, Streamlit, Sentence Transformers (Hugging Face), FAISS, PyPDF, OpenAI-compatible API, PyTest.

## Run
1. `python -m venv .venv`
2. Windows: `.venv\\Scripts\\activate` | macOS/Linux: `source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. Copy `.env.example` to `.env` and set `OPENAI_API_KEY`.
5. `pytest -q`
6. `streamlit run app.py`

## Deployment
Push to GitHub, create a Streamlit Community Cloud app using `app.py`, and add `OPENAI_API_KEY` in Streamlit Secrets. The embedding model downloads automatically on first start.

## Notes
Text-based PDFs are supported. Scanned/image-only PDFs need OCR. The FAISS index is in memory for the current session. Production hardening would include persistent vector storage, auth, rate limiting, monitoring, and document access controls.
