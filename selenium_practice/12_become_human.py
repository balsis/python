import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
# Запуск браузера с заданным разрешением
options.add_argument("--window-size=1920,1080")
# options.add_argument("--headless")
# Запуск браузера с игнорированием ssl сертификатов
options.add_argument("--ignore-certificate-errors")
# Отключение средства автоматизации т.е. браузером управляет человек
options.add_argument("--disable-blink-features=AutomationControlled")
# добавить user-agent
options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
driver.save_screenshot("screen.png")

time.sleep(3)
