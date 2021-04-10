import csv
import sys

if len(sys.argv)>1:
    with open(sys.argv[1], 'r') as arquivo_csv:
        reader = csv.reader(arquivo_csv, delimiter=';')
        print(reader)
        for linha in reader:
            print(linha)
else:
    print("Informe o nome do arquivo.")
    print("Sintaxe:")
    print("$ python exemplo_csv4.py arquivo.csv")