from lxml import etree

"""
    Arquivo Ano-2017.xml baixado em:
    http://www2.camara.leg.br/transparencia/cota-para-exercicio-da-atividade-parlamentar/dados-abertos-cota-parlamentar
    http://www.camara.leg.br/cotas/Ano-2017.xml.zip
    
    Pegando despesas de um parlamentar especificado diretamente no código
    O objetivo deste exemplo é mostrar a facilidade de uso do lxml e sua velocidade
"""

dados = etree.parse("Ano-2017.xml")
todas_despesas = dados.findall("DESPESAS")
parlamentar = 'ABEL MESQUITA JR.'

for despesas in todas_despesas:
    for despesa in despesas:
        desp = despesa.getchildren()

        if desp[0].text == parlamentar:
            print("Despesa:", desp[8].text, "- Valor:", desp[18].text)