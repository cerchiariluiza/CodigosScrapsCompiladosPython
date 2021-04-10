from urllib.request import urlretrieve
import csv

link = input("Informe o link do arquivo csv: ")
delimitador = input("Informe o delimitador: ")
urlretrieve(link, "arquivo_baixado.csv")
with open("arquivo_baixado.csv", 'r') as arquivo_csv:
    reader = csv.reader(arquivo_csv, delimiter=delimitador)
    for linha in reader:
        print(linha)
