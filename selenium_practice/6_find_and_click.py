import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://practicetestautomation.com/practice-test-login/')


# Записываем найденный элемент (button) в переменную
submit_button = driver.find_element("xpath", "//button[@id='submit']")

# Записываем найденные элементы (input) в переменную
username_field = driver.find_element("xpath", "//input[@id='username']")
password_field = driver.find_element("xpath", "//input[@id='password']")
time.sleep(5)

# Проверим, что input пустые и очистим
if username_field.get_attribute('value'):
    username_field.clear()
if password_field.get_attribute('value'):
    password_field.clear()

# Обращаясь к переменным с найденными элементами вызываем метод send_keys(), вписывая в input текст
username_field.send_keys('student')
password_field.send_keys('Password123')
time.sleep(1)

print(username_field.get_attribute('value'))
print(password_field.get_attribute('value'))

time.sleep(1)

#Кликаем по кнопочке
submit_button.click()
time.sleep(1)

