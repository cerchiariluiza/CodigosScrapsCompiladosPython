from urllib.request import urlopen
html = urlopen("http://localhost:8000/exemplo2.php")
print(html.read().decode('utf-8'))

