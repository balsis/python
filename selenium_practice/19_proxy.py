import time
from selenium import webdriver

PROXY = "195.246.109.42:3128"  # Указываем адрес прокси-сервера

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--proxy-server={PROXY}")  # Добавляем прокси через опции

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://2ip.ru")  # Проверяем IP-адрес

time.sleep(5)