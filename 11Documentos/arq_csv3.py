from urllib.request import urlopen
from bs4 import BeautifulSoup
from io import StringIO
import csv

html = urlopen("https://evaldowolkers.wordpress.com/python-web-scraping-csv-sample/")
soup = BeautifulSoup(html, "html.parser")

for link in soup.findAll('a'):
    if link.get('href'):
        if ".csv" in link.get('href'):
            print("Encontrou um link para um CSV.")
            dados = urlopen(link.get('href')).read().decode(encoding='utf-8', errors='ignore')
            arqDados = StringIO(dados)
            csvReader = csv.reader(arqDados)

            for linha in csvReader:
                print(linha)
            print("Fim arquivo.")