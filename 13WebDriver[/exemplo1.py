from selenium import webdriver


# webdriver representa o Browser
driver = webdriver.Firefox()
# Navegar até a página exemplo1
driver.get("http://localhost:8000/exemplo1.php")

# Find Element By retorna um objeto WebElement
objeto = driver.find_element_by_id("enviar")
# Pegando o atributo value para obter o texto do botão
print('Texto do botão:', objeto.get_attribute('value'))
driver.close()

