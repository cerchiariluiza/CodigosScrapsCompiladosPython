import csv


try:
    arq = open("pessoas.csv", "w", newline="")
    cabecalho = ["nome", "sobrenome"]
    writer = csv.DictWriter(arq, fieldnames=cabecalho)
    writer.writeheader()
    writer.writerow({"nome":"Evaldo", "sobrenome":"Wolkers"})
    writer.writerow({"nome":"Fulano", "sobrenome":"de Tal"})
    writer.writerow({"nome":"Cicrano", "sobrenome":"Souza"})
    writer.writerow({"nome":"Beltrano", "sobrenome":"Silva"})
finally:
    arq.close()