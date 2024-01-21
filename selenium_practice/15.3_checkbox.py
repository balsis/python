# Инициализация драйвера
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep

# Создание экземпляра веб-драйвера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/selectable")

# Записываем локатор первого чек-бокса
FIRST_CHECKBOX = ("xpath", "(//ul[@id='verticalListContainer']/li)[1]")

# Кликаем на него
driver.find_element(*FIRST_CHECKBOX).click()

# Проверяем, что после клика, к нему добавился класс active
assert "active" in driver.find_element(*FIRST_CHECKBOX).get_attribute("class"), "Чек-бокс не выбран"