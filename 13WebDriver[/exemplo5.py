from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://localhost:8000/exemplo1.html")
driver.execute_script('window.alert("Script Executado")')

# Não vou fechar para ver o script na tela
#driver.close()
