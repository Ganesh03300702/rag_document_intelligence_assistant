from pathlib import Path
from pypdf import PdfReader

def load_document(path: Path):
    if path.suffix.lower()=='.txt':
        t=path.read_text(encoding='utf-8',errors='ignore').strip(); return [{'text':t,'source':path.name,'page':None}] if t else []
    if path.suffix.lower()=='.pdf':
        out=[]
        for n,p in enumerate(PdfReader(str(path)).pages,1):
            t=(p.extract_text() or '').strip()
            if t: out.append({'text':t,'source':path.name,'page':n})
        return out
    raise ValueError(f'Unsupported file type: {path.suffix}')
