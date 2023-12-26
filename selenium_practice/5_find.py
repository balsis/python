import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://practicetestautomation.com/practice-test-login/')

time.sleep(10)
# Найдем обьект с типом WebElement "login_button"
submit_button = driver.find_element('id', 'submit') # Поиск по id атрибуту
submit_button.click() # клик по найденному элементу

time.sleep(5)