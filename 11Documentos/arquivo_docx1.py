import docx

doc = docx.Document('ArquivoWord.docx')

for a in doc.paragraphs:
    print(a.text)