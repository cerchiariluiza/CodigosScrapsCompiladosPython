from openpyxl import load_workbook

wb = load_workbook('MeusNumeros.xlsx')

planilha = wb['Sheet']

planilha['B8'] = "=SUM(B2:B7)"
planilha['C8'] = "=SUM(C2:C7)"
planilha['D8'] = "=SUM(D2:D7)"
planilha['E8'] = "=SUM(E2:E7)"

planilha['F2'] = "=AVERAGE(B2:E2)"
planilha['F3'] = "=AVERAGE(B3:E3)"
planilha['F4'] = "=AVERAGE(B4:E4)"
planilha['F5'] = "=AVERAGE(B5:E5)"
planilha['F6'] = "=AVERAGE(B6:E6)"
planilha['F7'] = "=AVERAGE(B7:E7)"

planilha['G2'] = '=IF(E1>50,"LIKE","DISLIKE")'
planilha['G3'] = '=IF(E2>50,"LIKE","DISLIKE")'
planilha['G4'] = '=IF(E3>50,"LIKE","DISLIKE")'
planilha['G5'] = '=IF(E4>50,"LIKE","DISLIKE")'
planilha['G6'] = '=IF(E5>50,"LIKE","DISLIKE")'
planilha['G7'] = '=IF(E6>50,"LIKE","DISLIKE")'

wb.save('MeusNumeros.xlsx')