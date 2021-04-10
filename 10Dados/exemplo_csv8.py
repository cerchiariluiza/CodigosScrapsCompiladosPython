from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

html = urlopen("https://www.techtudo.com.br/noticias/2017/10/confira-a-lista-completa-de-carros-para-need-for-speed-payback.ghtml")
bsObj = BeautifulSoup(html, "html.parser")
tabela = bsObj.find("table")
linhas = tabela.findAll("tr")
arquivo_csv = open("carros.csv", "w", newline="")

for linha in linhas:
    colunas = linha.findAll("td")
    lista = []
    for coluna in colunas:
        lista.append(coluna.text)

    writer = csv.writer(arquivo_csv, delimiter=";")
    writer.writerow(lista)

arquivo_csv.close()