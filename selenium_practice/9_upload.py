import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://demoqa.com/upload-download")
time.sleep(2)

# загрузка файлов на сайтах реализована тегом <input> cо специальным атрибутом <input type=”file”/> .
# os.getcwd() - возвращает путь до текущей директории
driver.find_element("xpath", "//input[@type='file']").send_keys(f"{os.getcwd()}/downloads/TextDoc.txt")
time.sleep(2)
driver.find_element("xpath", "//a[@id='downloadButton']").click()
time.sleep(2)

