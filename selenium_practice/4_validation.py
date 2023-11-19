from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://en.wikipedia.org/wiki/Wikipedia')

url = driver.current_url
print(url)
assert url == 'https://en.wikipedia.org/wiki/Wikipedia', 'Wrong URL'

current_title = driver.title
print(current_title)
assert current_title == 'Wikipedia - Wikipedia', 'Wrong Title'

print(driver.page_source)