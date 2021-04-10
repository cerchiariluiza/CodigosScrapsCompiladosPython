"""
Neste exemplo vamos trabalhar com os dados obtidos
no portal da Câmara dos Deputados:
http://www.camara.leg.br/cotas/Ano-2017.json.zip
"""
import json

with open('Ano-2017/Ano-2017_exemplo.json', 'r', encoding='utf-8') as arq:
    dados_json = json.load(arq)
    print("Objeto índice zero:\n", dados_json["DESPESA"][0])
    print("Valor líquido do objeto de índice zero:\n",dados_json["DESPESA"][0]["vlrLiquido"])



