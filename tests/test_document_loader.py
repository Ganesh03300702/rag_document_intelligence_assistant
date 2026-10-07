from document_loader import load_document
def test_txt(tmp_path):
    p=tmp_path/'x.txt'; p.write_text('Hello RAG',encoding='utf-8'); assert load_document(p)==[{'text':'Hello RAG','source':'x.txt','page':None}]
