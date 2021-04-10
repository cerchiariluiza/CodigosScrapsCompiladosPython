"""
    Simulando o formulario_get.html, que envia os dados
    via POST para formulario_pythonwebscraping2.php
    Utilizando o servidor PHP local na porta 8000
"""
import requests

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) " \
             "AppleWebKit/537.36 (KHTML, like Gecko)" \
             "Chrome/35.0.1916.47 Safari/537.36"

params = {'nome':'Evaldo', 'email':'evaldowolkers@gmail.com', 'celular':'(28)99948-3074'}
r = requests.get('http://localhost:8000/formulario_pythonwebscraping2.php',
                  headers={'User-Agent': user_agent},
                  params=params)
print(r.text)
