from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

site = "http://www.destemperados.com.br/"
html = urlopen(site + "receitas")
bsObj = BeautifulSoup(html)
imageLocation = bsObj.find("a", {"title": "Destemperados"}).find("img")["src"]
urlretrieve(site+imageLocation, "teste.jpg")

# <a href="http://www.destemperados.com.br/" title="Destemperados" class="hidden-sm hidden-xs"><img src="Content/img/logo-destemperados.png"></a>