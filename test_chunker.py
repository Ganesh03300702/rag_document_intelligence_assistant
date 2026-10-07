from chunker import chunk_text
def test_chunker():
    r=chunk_text([{'text':'a'*1700,'source':'x.txt','page':None}]); assert len(r)>=2; assert all(x['source']=='x.txt' for x in r)
