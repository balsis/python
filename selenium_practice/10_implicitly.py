#Неявное ожидание - это количество времени (которое указывается нами) в течение которого, WebDriver будет опрашивать DOM. Неявным оно называется,
#так как мы не указываем чего ждать, изменения текста, размера и т.д…

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# Задается время в секундах, в течение которого WebDriver
# опрашивать страницу на наличие элемента.
driver.implicitly_wait(10)

driver.get("https://demoqa.com/dynamic-properties")
button_after = ("xpath", "//button[@id='visibleAfter']")
driver.find_element(*button_after).click()