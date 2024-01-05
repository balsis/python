import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Добавление настроек является экспериментальной фичей,
# поэтому мы явно указываем add_experimental_option, а “prefs” - это ключевое слово в качестве первого аргумента,
# оно не меняется, вторым же аргументом идет наш словарь настроек.
chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}\downloads"
}
chrome_options.add_experimental_option("prefs", prefs)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/download")
time.sleep(2)
driver.find_elements("xpath", "//a")[5].click()
time.sleep(2)
