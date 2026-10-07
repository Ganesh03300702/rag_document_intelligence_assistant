from chunker import chunk_text
from document_loader import load_document
from llm_client import LLMClient
from vector_store import VectorStore
class RAGPipeline:
    def __init__(self): self.vector_store=VectorStore(); self.llm_client=None
    def index_documents(self,paths):
        records=[]
        for p in paths: records.extend(load_document(p))
        chunks=chunk_text(records); self.vector_store.build(chunks); return {'documents':len(paths),'chunks':len(chunks)}
    def answer(self,question,top_k=4):
        contexts=self.vector_store.search(question,top_k)
        if self.llm_client is None: self.llm_client=LLMClient()
        return {'answer':self.llm_client.generate(question,contexts),'sources':contexts}
