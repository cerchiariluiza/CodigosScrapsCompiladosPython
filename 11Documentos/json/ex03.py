import json

with open('exemplo03.json', 'r', encoding='utf-8') as arq:
    conteudo = arq.read()
    print("*" * 50)
    print("Conteudo do arquivo:\n", conteudo)
    dados_json = json.loads(conteudo)
    print("*" * 50)
    print("JSON completo:\n", dados_json)
    print("*" * 50)
    print("Primeiro objeto (dados_json[0]):\n", dados_json[0])
    print("*" * 50)
    print("Loop em todos objetos:")
    for dados in dados_json:
        print("Curso:", dados["Curso"], "/", "Descrição da Aula:", dados['Descricao da Aula'])
    print("*" * 50)