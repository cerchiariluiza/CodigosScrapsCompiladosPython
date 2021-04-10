import json

with open('exemplo01.json', 'r') as arq:
    conteudo = arq.read()
    dados_json = json.loads(conteudo)
    print(dados_json['Curso'])