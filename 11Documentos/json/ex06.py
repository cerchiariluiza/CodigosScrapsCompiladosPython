"""
Neste exemplo vamos trabalhar com os dados obtidos
no portal da Câmara dos Deputados:
http://www.camara.leg.br/cotas/Ano-2017.json.zip
"""
import json

soma_valor_liquido = 0.0

with open('Ano-2017/Ano-2017.json', 'r', encoding='utf-8') as arq:
    dados_json = json.load(arq)
    for x in range(0, len(dados_json["DESPESA"])):
        valor_liquido = float(dados_json["DESPESA"][x]["vlrLiquido"].replace(",","."))
        soma_valor_liquido += valor_liquido
print("Soma do valor líquido: %.2f" % soma_valor_liquido)



