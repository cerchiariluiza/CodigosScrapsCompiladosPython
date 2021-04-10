import csv

with open('FC_2016_05.csv') as arquivo_csv:
    reader = csv.reader(arquivo_csv, delimiter=';')
    for linha in reader:
        print(linha)