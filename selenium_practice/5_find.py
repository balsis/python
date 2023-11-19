import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# from selenium.webdriver.common.by import By


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://practicetestautomation.com/practice-test-login/')

time.sleep(10)
login_button = driver.find_element('id', 'submit')
login_button.click()

time.sleep(5)