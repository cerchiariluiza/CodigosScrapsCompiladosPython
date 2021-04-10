from openpyxl import load_workbook
from openpyxl.styles import Font
from openpyxl.styles.colors import BLUE, RED

wb = load_workbook('MeusNumeros.xlsx')

planilha = wb['Sheet']

fonte_titulo = Font(bold=True, size=12, color=RED)
fonte_total = Font(bold=True, color=BLUE)

planilha['B1'].font = fonte_titulo
planilha['B8'].font = fonte_total
planilha['C8'].font = fonte_total
planilha['D8'].font = fonte_total
planilha['E8'].font = fonte_total

wb.save('MeusNumeros.xlsx')