from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
driver = webdriver.Chrome()

action = ActionChains(driver)
action.context_click()

# maximizam fereastra
driver.maximize_window()


# navigam catre un url
driver.get('https://demoqa.com/buttons')
sleep(2)

# double click
double_click = driver.find_element(By.ID, 'doubleClickBtn')
action.double_click(double_click).perform()
sleep(2)

# right click
right_click = driver.find_element(By.ID, 'rightClickBtn')
action.context_click(right_click).perform()
sleep(2)

# dynamic click
dynamic_click = driver.find_element(By.XPATH, '//*[text()="Click Me"]')
action.click(dynamic_click).perform()

sleep(2)

# inchidem chrome
driver.quit()

# daca a trecut testul, printam in consola un mesaj de succes
print('SUCCESS - TEST PASSED')