from openpyxl import load_workbook

wb = load_workbook('Precos.xlsx')
planilha = wb['Tabela de preços']

qtd = 0

for linha in range(3, 13):
    qtd += planilha[f'C{linha}'].value

print(qtd)
