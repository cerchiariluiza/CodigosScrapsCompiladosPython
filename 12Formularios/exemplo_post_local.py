"""
    Simulando o formulario.html, que envia os dados
    via POST para formulario_pythonwebscraping1.php
    Utilizando o servidor PHP local na porta 8000
"""
import requests

params = {'nome':'Evaldo', 'email':'evaldowolkers@gmail.com',
          'celular':'(28)99948-3074'}
r = requests.post('http://localhost:8000/'
                  'formulario_pythonwebscraping1.php', data=params)
print(r.text)