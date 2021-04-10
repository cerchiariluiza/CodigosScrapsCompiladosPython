import json

dados = {'Curso': 'Python Web Scraping',
         'Secao':'12',
         'Nome Secao': 'Lendo documentos',
         'Numero da Aula':'05',
         'Descricao da Aula':'Arquivos JSON'}

dados_json = json.dumps(dados)
print(dados_json)
with open('exemplo01.json', 'w') as arq:
    arq.write(json.dumps(dados))