from openpyxl import load_workbook

arquivo = 'Precos.xlsx'
wb = load_workbook(arquivo)

wb.remove(wb['Planilha de carros'])

wb.save(arquivo)