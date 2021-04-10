from openpyxl import load_workbook

wb = load_workbook('Precos.xlsx')

planilha = wb['Tabela de preços']

for linha in range(3, 13):
    descricao = planilha[f'B{linha}']
    print(descricao.value)
