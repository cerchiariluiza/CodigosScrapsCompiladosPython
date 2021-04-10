from selenium import webdriver

print("Início")
driver = webdriver.Firefox()
driver.get("http://localhost:8000/exemplo2.php")
print(driver.find_element_by_id("enviar").get_attribute('value'))
driver.close()
print("Fim")