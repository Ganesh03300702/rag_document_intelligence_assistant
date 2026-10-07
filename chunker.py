from config import CHUNK_SIZE, CHUNK_OVERLAP

def chunk_text(records):
    out=[]
    for r in records:
        text=' '.join(r['text'].split())
        start=0
        while start<len(text):
            end=min(start+CHUNK_SIZE,len(text)); chunk=text[start:end].strip()
            if chunk: out.append({'text':chunk,'source':r['source'],'page':r['page']})
            if end>=len(text): break
            start=end-CHUNK_OVERLAP
    return out
