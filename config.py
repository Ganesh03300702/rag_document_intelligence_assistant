import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY','').strip()
OPENAI_BASE_URL=os.getenv('OPENAI_BASE_URL','').strip()
OPENAI_MODEL=os.getenv('OPENAI_MODEL','gpt-4o-mini').strip()
EMBEDDING_MODEL=os.getenv('EMBEDDING_MODEL','sentence-transformers/all-MiniLM-L6-v2').strip()
CHUNK_SIZE=int(os.getenv('CHUNK_SIZE','800')); CHUNK_OVERLAP=int(os.getenv('CHUNK_OVERLAP','120'))
if CHUNK_OVERLAP >= CHUNK_SIZE: raise ValueError('CHUNK_OVERLAP must be smaller than CHUNK_SIZE.')
