from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

# Coloque o caminho correto onde o arquivo html foi salvo
html = urlopen('file:///C:/Pastas/www2.aneel.gov.br.html')
bsObj = BeautifulSoup(html.read(), "html.parser")

for link in bsObj.find_all('a'):
    if "href" in link.attrs:
        try:
            link_completo = link.get('href')
            link_partes = link_completo.split("/")
            nome_arquivo = link_partes[-1]
            print("Link: " + link_completo)
            print("Nome Arquivo: " + nome_arquivo)
            urlretrieve(link_completo, filename=nome_arquivo)
        except Exception as e:
            print(f"Erro arquivo: {link.get('href')}: ", e)