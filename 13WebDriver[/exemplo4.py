from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.pythonparatodos.com.br")
# current_url: Retorna a URL corrente
print(driver.current_url)
driver.get("http://www.pythonparatodos.com.br/cursos")
sleep(3)
# Pressiona o botão Voltar
driver.back()
sleep(3)
# Pressiona o botão Avançar
driver.forward()
sleep(3)
# Recarrega a página
driver.refresh()
# Retorna o título da página
print(driver.title)
# Salvar uma imagem (screenshot) com a página atual
driver.save_screenshot('teste.png')
driver.close()
