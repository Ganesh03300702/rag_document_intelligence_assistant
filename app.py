import tempfile
from pathlib import Path
import streamlit as st
from rag_pipeline import RAGPipeline

st.set_page_config(page_title='RAG Document Intelligence Assistant', page_icon='📚', layout='wide')
st.title('📚 RAG Document Intelligence Assistant')
st.caption('Upload documents, retrieve relevant context, and ask grounded questions with source references.')

@st.cache_resource
def get_pipeline(): return RAGPipeline()

pipeline = get_pipeline()
with st.sidebar:
    st.header('Settings')
    top_k = st.slider('Retrieved chunks', 2, 8, 4)
    st.info('Local Hugging Face embeddings + FAISS are used for retrieval. An OpenAI-compatible API key is required for answer generation.')

uploads = st.file_uploader('Upload PDF or TXT documents', type=['pdf','txt'], accept_multiple_files=True)
if uploads and st.button('Index Documents', type='primary'):
    try:
        with tempfile.TemporaryDirectory() as td:
            paths=[]
            for u in uploads:
                p=Path(td)/u.name; p.write_bytes(u.getvalue()); paths.append(p)
            r=pipeline.index_documents(paths)
        st.session_state['indexed']=True; st.session_state['document_count']=r['documents']; st.session_state['chunk_count']=r['chunks']
        st.success(f"Indexed {r['documents']} document(s) into {r['chunks']} chunks.")
    except Exception as e: st.error(f'Indexing failed: {e}')

if st.session_state.get('indexed'):
    c1,c2=st.columns(2); c1.metric('Indexed documents',st.session_state['document_count']); c2.metric('Indexed chunks',st.session_state['chunk_count'])

q=st.text_area('Ask a question about your indexed documents', placeholder='Example: What are the main recommendations mentioned in the documents?')
if st.button('Ask', disabled=not st.session_state.get('indexed')):
    if not q.strip(): st.warning('Please enter a question.')
    else:
        try:
            with st.spinner('Retrieving context and generating answer...'): r=pipeline.answer(q, top_k)
            st.subheader('Answer'); st.write(r['answer']); st.subheader('Sources')
            for i,s in enumerate(r['sources'],1):
                with st.expander(f"{i}. {s['source']} — page {s.get('page','N/A')}"):
                    st.write(s['text']); st.caption(f"Similarity score: {s['score']:.4f}")
        except Exception as e: st.error(f'Question answering failed: {e}')

st.divider(); st.caption('Python • Streamlit • Sentence Transformers • FAISS • OpenAI-compatible LLM API')
