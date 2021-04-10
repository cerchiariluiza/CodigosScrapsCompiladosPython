"""
    Simulando o formulario.html, que envia os dados
    via POST para formulario_pythonwebscraping1.php
    Este funciona porque o User Agent foi definido
"""
import requests

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) " \
             "AppleWebKit/537.36 (KHTML, like Gecko)" \
             "Chrome/35.0.1916.47 Safari/537.36"

params = {'nome':'Evaldo', 'email':'evaldowolkers@gmail.com', 'celular':'(28)99948-3074'}
r = requests.post('http://www.pythonparatodos.com.br/formulario_pythonwebscraping1.php',
                  headers={'User-Agent': user_agent},
                  data=params)
print(r.text)
