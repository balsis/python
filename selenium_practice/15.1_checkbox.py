# Инициализация драйвера
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

# Создание экземпляра веб-драйвера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/checkboxes")

# Находим выбранные чек-боксы и записываем в переменные
CHECKBOX_1 = ("xpath", "//input[@type='checkbox'][1]")
CHECKBOX_2 = ("xpath", "//input[@type='checkbox'][2]")

# Выполняем клики по чек-боксам
driver.find_element(*CHECKBOX_1).click()
assert driver.find_element(*CHECKBOX_1).is_selected() is True, "Чек-бокс не выбран"

driver.find_element(*CHECKBOX_2).click()
assert driver.find_element(*CHECKBOX_2).is_selected() is False, "Чек-бокс до сих пор выбран"

time.sleep(2)