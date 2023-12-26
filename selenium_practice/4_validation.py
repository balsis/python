from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://practicetestautomation.com/practice-test-login/')

# Получить текущий URL
url = driver.current_url
print(url)
assert url == 'https://practicetestautomation.com/practice-test-login/', 'Wrong URL'

# Получить текущий title страницы
current_title = driver.title
print(current_title)
assert current_title == 'Test Login | Practice Test Automation', 'Wrong Title'

#print(driver.page_source)