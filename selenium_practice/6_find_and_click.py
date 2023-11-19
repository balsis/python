import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.freeconferencecall.com/global/')

login_button = driver.find_element("xpath","//a[@id='login-desktop']")
login_button.click()
time.sleep(3)

email = driver.find_element("xpath", "//input[@id='login_email']")
email.send_keys('test@ya.ru')
time.sleep(1)
email.clear()
time.sleep(1)
email.send_keys('test2@ya.ru')
print(email.get_attribute('value'))
time.sleep(3)