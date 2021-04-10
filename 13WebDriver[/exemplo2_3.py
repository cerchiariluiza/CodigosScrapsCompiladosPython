from selenium import webdriver

def aguardar(driver):
    while True:
        try:
            if driver.find_element_by_id("enviar"):
                print(driver.find_element_by_id("enviar").get_attribute('value'))
                return
        except:
            print('Deu erro')
            pass


print("Início")
driver = webdriver.Firefox()
driver.get("http://localhost:8000/exemplo2.php")
aguardar(driver)
driver.close()
print("Fim")