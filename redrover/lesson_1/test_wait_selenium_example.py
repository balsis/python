import time
from selenium import webdriver  # Импортируем класс webdriver из библиотеки Selenium для управления браузером
from webdriver_manager.chrome import ChromeDriverManager  # Импортируем ChromeDriverManager для автоматической установки и управления версией ChromeDriver
from selenium.webdriver.chrome.service import Service  # Импортируем класс Service для настройки службы ChromeDriver

# Настраиваем службу ChromeDriver с использованием ChromeDriverManager
service = Service(executable_path=ChromeDriverManager().install())
# Создаем экземпляр Chrome WebDriver с настроенной службой
driver = webdriver.Chrome(service=service)


def test_load_button_without_wait():
    driver.get("https://victoretc.github.io/waitSeleniumexample/")

    load_content_button = driver.find_element("xpath", "//button")
    load_content_button.click()

    welcome_message = driver.find_element("xpath", "//h2")

    assert welcome_message.text == "Welcome to the Unstable Load Site!"


def test_load_with_wait():
    driver.get("https://victoretc.github.io/waitSeleniumexample/")

    load_content_button = driver.find_element("xpath", "//button")
    load_content_button.click()

    welcome_message = driver.find_element("xpath", "//h2")

    time.sleep(6)
    assert welcome_message.text == "Welcome to the Unstable Load Site!"