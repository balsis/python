# Прописываются все импорты
import pickle
import os
import time

# Инициализация драйвера
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создание экземпляра веб-драйвера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, poll_frequency=1)
driver.get("https://www.freeconferencecall.com/en/us/login")

# Вернет куку name или любую другую указанную в качестве аргумента
#driver.get_cookie("name")
# Вернет список словарей, все куки
#driver.get_cookies()

# # Создадим куку с именем Example и значением Kukushka:
# driver.add_cookie({
#     'name': 'Example',
#     'value': 'Kukushka'
# })
# print(driver.get_cookie('Example'))
#
# # Замена Cookies
# driver.delete_cookie("Example")
# driver.add_cookie({
#     'name': 'Example',
#     'value': 'More'
# })

LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")

# Логинимся в аккаунт
driver.get("https://www.freeconferencecall.com/en/us/login")
driver.find_element(*LOGIN_FIELD).send_keys("autocheck@ya.ru")
driver.find_element(*PASSWORD_FIELD).send_keys("123")
driver.find_element(*SUBMIT_BUTTON).click()

# Сохраняем куки в файл
# open(os.getcwd() + "/cookies/cookies.pkl") - указатель места для записи или чтения.
# “wb” (write binary) - запись в бинарном формате.
pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))

# Открываем страницу логина
driver.get("https://www.freeconferencecall.com/profile")
time.sleep(3)
# Чистим все куки
driver.delete_all_cookies()
time.sleep(3)
# Записываем куки из файла в переменную
# open(os.getcwd() + "/cookies/cookies.pkl") - указываем путь к файлу с ранее записанными куками.
# “rb” (read binaries) - прочитать данные в бинарном формате.
cookies = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))
time.sleep(3)
# Добавляем по одной куке из списка
for cookie in cookies:
    driver.add_cookie(cookie)
time.sleep(3)
driver.get("https://www.freeconferencecall.com/profile")
time.sleep(3)