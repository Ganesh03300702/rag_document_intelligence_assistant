from vector_store import VectorStore
def test_search():
    s=VectorStore(); s.build([{'text':'Python programming','source':'a','page':None},{'text':'Cats animals','source':'b','page':None}]); r=s.search('Python',1); assert len(r)==1 and 'score' in r[0]
