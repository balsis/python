import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")
options.page_load_strategy = "normal"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

# 1 способ
driver.get("https://demoqa.com/select-menu")

SELECT_TITLE = ("xpath", "//input[@id='react-select-3-input']") # Локатор нашего dropdown

driver.find_element(*SELECT_TITLE).send_keys("MS." + Keys.ENTER) # Вводим текст в dropdown
time.sleep(5)

# 2 способ
# setTimeout(function() { debugger; }, 5000); - включит отложенный старт дебаг-режима в devtools.

driver.get("https://demoqa.com/select-menu")

driver.find_element("xpath", "//div[@id='withOptGroup']").click() # Открываем dropdown
driver.find_element("xpath", "//div[@id='withOptGroup']//div[text()='A root option']").click() # Кликаем на элемент внутри

time.sleep(5)