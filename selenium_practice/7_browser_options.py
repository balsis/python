import time

# Импортируем необходимые модули и классы из Selenium и webdriver_manager
from selenium import webdriver  # Импортируем класс webdriver из библиотеки Selenium для управления браузером
from webdriver_manager.chrome import ChromeDriverManager  # Импортируем ChromeDriverManager для автоматической установки и управления версией ChromeDriver
from selenium.webdriver.chrome.service import Service  # Импортируем класс Service для настройки службы ChromeDriver

# экземпляр класса ChromeOptions, который позволяет настроить параметры браузера перед его запуском
chrome_options = webdriver.ChromeOptions()
# Стратегия загрузки страницы
chrome_options.page_load_strategy = 'eager'
# Опции загрузки страницы
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--incognito')
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-cache")

#экземпляр класса Service, который используется для управления сервисом (в данном случае — браузером)
service = Service(executable_path=ChromeDriverManager().install())

#экземпляр класса webdriver.Chrome, который представляет собой браузер Google Chrome, управляемый с помощью Selenium
driver = webdriver.Chrome(service=service, options=chrome_options)
# driver.set_window_size(1920,1080)

start_time = time.time()
driver.get("https://practicetestautomation.com/practice-test-login/")
# driver.get("https://expired.badssl.com/") # URL for certificate errors
end_time = time.time()
result = end_time - start_time
print(result)