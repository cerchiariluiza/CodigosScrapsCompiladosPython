from openpyxl import Workbook

wb = Workbook()
planilha = wb.active

linhas = (
    (14, 11, 44, 48),
    (12, 21, 12, 136),
    (55, 22, 58, 125),
    (98, 66, 47, 66),
    (14, 18, 36, 84),
    (78, 18, 67, 75)
)

for linha in linhas:
    planilha.append(linha)

wb.save('MeusNumeros.xlsx')