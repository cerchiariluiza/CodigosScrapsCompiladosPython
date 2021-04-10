from selenium import webdriver


driver = webdriver.Firefox()
driver.get("http://localhost:8000/exemplo1.php")
nome = driver.find_element_by_name("nome")
email = driver.find_element_by_name("email")
celular = driver.find_element_by_name("celular")
enviar = driver.find_element_by_name("enviar")
# send_keys: Digita uma sequência de teclas
nome.send_keys("Evaldo Wolkers")
email.send_keys("evaldowolkers@gmail.com")
celular.send_keys("(28)99948-3074")

enviar.click()

print(driver.page_source)
driver.close()