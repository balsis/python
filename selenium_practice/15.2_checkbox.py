# Инициализация драйвера
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

# Создание экземпляра веб-драйвера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/checkbox")

# чек-бокс для проверки статуса
HOME_CHECKBOX = ("xpath", "//input[@id='tree-node-home']")

# Элемент для клика, чтобы выставить флажок
HOME_BUTTON = ("xpath", "//span[text()='Home']")

# Кликаем на элемент, который выставляет чек-бокс
driver.find_element(*HOME_BUTTON).click()

# Выведем статус чек-бокса, так как он меняется при клике на элемент, отвечающий за выставление флажка
assert driver.find_element(*HOME_CHECKBOX).is_selected() is True