import docx

doc = docx.Document('ArquivoWord.docx')

for a in doc.paragraphs:
    with open('resultado.txt', 'a') as arquivo:
        arquivo.write(a.text)