# Инициализация драйвера
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

# Создание экземпляра веб-драйвера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/radio-button")

YES_RADIO_BUTTON = ("xpath", "//input[@id='yesRadio']") # Для статуса
YES_RADIO_LABEL = ("xpath", "//label[@for='yesRadio']") # Для взаимодействия
NO_RADIO_BUTTON = ("xpath", "//input[@id='noRadio']")

assert driver.find_element(*NO_RADIO_BUTTON).is_enabled() is False, "Кнопка доступна"
driver.find_element(*YES_RADIO_LABEL).click()

assert driver.find_element(*YES_RADIO_BUTTON).is_selected() is True, "Радио-кнопка не выбрана"