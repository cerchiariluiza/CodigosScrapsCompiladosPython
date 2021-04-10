from openpyxl import load_workbook

arquivo = 'Precos.xlsx'
wb = load_workbook(arquivo)

origem = wb['Tabela de preços']
destino = wb.copy_worksheet(origem)
destino.title = 'Nova tabela de preços'

wb.save(arquivo)