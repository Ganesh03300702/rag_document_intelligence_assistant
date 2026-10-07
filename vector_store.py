import faiss, numpy as np
from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL

class VectorStore:
    def __init__(self): self.model=SentenceTransformer(EMBEDDING_MODEL); self.index=None; self.metadata=[]
    def build(self,chunks):
        if not chunks: raise ValueError('No text chunks were produced from the uploaded documents.')
        emb=np.asarray(self.model.encode([x['text'] for x in chunks],normalize_embeddings=True,show_progress_bar=False),dtype='float32')
        self.index=faiss.IndexFlatIP(emb.shape[1]); self.index.add(emb); self.metadata=chunks
    def search(self,query,top_k=4):
        if self.index is None: raise RuntimeError('No documents are indexed.')
        q=np.asarray(self.model.encode([query],normalize_embeddings=True,show_progress_bar=False),dtype='float32'); k=min(top_k,len(self.metadata)); scores,idx=self.index.search(q,k)
        return [{**self.metadata[int(i)],'score':float(s)} for s,i in zip(scores[0],idx[0]) if i>=0]
