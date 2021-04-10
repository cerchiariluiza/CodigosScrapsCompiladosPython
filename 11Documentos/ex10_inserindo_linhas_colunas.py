from openpyxl import load_workbook

wb = load_workbook('MeusNumeros.xlsx')

planilha = wb['Sheet']

planilha.insert_rows(1)
planilha.insert_cols(1)

wb.save('MeusNumeros.xlsx')