from openai import OpenAI
from config import OPENAI_API_KEY,OPENAI_BASE_URL,OPENAI_MODEL
class LLMClient:
    def __init__(self):
        if not OPENAI_API_KEY: raise RuntimeError('OPENAI_API_KEY is not configured. Add it to .env before asking questions.')
        kw={'api_key':OPENAI_API_KEY}
        if OPENAI_BASE_URL: kw['base_url']=OPENAI_BASE_URL
        self.client=OpenAI(**kw); self.model=OPENAI_MODEL
    def generate(self,question,contexts):
        ctx='\n\n'.join(f"[Source: {x['source']}; Page: {x.get('page','N/A')}]\n{x['text']}" for x in contexts)
        r=self.client.chat.completions.create(model=self.model,temperature=0.1,messages=[{'role':'system','content':'Answer only from supplied context. If unsupported, say you cannot find it in the documents. Do not invent facts.'},{'role':'user','content':f'Context:\n{ctx}\n\nQuestion: {question}'}])
        return r.choices[0].message.content or 'No answer was generated.'
