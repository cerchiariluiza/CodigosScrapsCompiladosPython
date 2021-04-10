from openpyxl import load_workbook

wb = load_workbook('Precos.xlsx')

planilha = wb['Tabela de preços']

cells = planilha['A3:D12']

for c1, c2, c3, c4 in cells:
    print("{0:2} {1:90} {2:4} {3:10}".
          format(c1.value, c2.value, c3.value, c4.value))
