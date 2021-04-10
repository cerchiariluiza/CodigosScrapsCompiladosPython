import csv


arquivo_csv = open("exemplo.csv", "w", newline="")
try:
    writer = csv.writer(arquivo_csv)
    writer.writerow(['Nome', 'Telefone', 'Celular'])
    writer.writerow(['Fulano', '(11)1111-1111', '(11)99999-9999'])
    writer.writerow(['Cicrano', '(22)2222-2222', '(27)88888-8888'])
    writer.writerow(['Beltrano', '(33)3333-3333', '(31)77777-7777'])
finally:
    arquivo_csv.close()
