from openpyxl import load_workbook

arquivo = 'Precos.xlsx'
wb = load_workbook(arquivo)

planilha = wb['Nova tabela de preços']
planilha['A1'] = 'Tabela de Preços Dez/2018'

wb.save(arquivo)