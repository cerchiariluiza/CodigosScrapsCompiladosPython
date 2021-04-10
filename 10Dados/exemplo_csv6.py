import csv


estado = []
with open("estados.csv", encoding="utf-8") as arq:
    reader = csv.DictReader(arq)
    for linha in reader:
        print(linha['Nome'] + " - " + linha['Capital'])