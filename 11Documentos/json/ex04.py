from urllib.request import urlopen
import json

dados = urlopen('http://dados.iffarroupilha.edu.br/api/v1/projetos.json').read()
dados = json.loads(dados)
print(dados)

