import csv


telefones = [['Nome', 'Telefone', 'Celular'],
             ['Fulano', '(11)1111-1111', '(11)99999-9999'],
             ['Cicrano', '(22)2222-2222', '(27)88888-8888'],
             ['Beltrano', '(33)3333-3333', '(31)77777-7777']]
try:
    with open('exemplo2.csv', 'w', newline="") as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerows(telefones)
finally:
    arquivo_csv.close()
