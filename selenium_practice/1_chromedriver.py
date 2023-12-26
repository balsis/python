# Импортируем необходимые модули и классы из Selenium и webdriver_manager
from selenium import webdriver  # Импортируем класс webdriver из библиотеки Selenium для управления браузером
from webdriver_manager.chrome import ChromeDriverManager  # Импортируем ChromeDriverManager для автоматической установки и управления версией ChromeDriver
from selenium.webdriver.chrome.service import Service  # Импортируем класс Service для настройки службы ChromeDriver

# Настраиваем службу ChromeDriver с использованием ChromeDriverManager
service = Service(executable_path=ChromeDriverManager().install())
# Создаем экземпляр Chrome WebDriver с настроенной службой
driver = webdriver.Chrome(service=service)
