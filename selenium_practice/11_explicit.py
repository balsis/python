# Явное ожидание - ожидание конкретного условия, появления элемента, исчезновения элемента, изменения текста

import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# WebDriverWait - нужен для того, чтобы мы могли указать общее время ожидания для всех условий в будущем.
from selenium.webdriver.support.ui import WebDriverWait
# expected_conditions - в дальнейшем EC, так и переводится “ожидаемые условия”,
# Данный модуль поможет нам выбрать необходимое условие, выполнения которого мы будем ожидать.
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# создается обьект wait:
# driver - Ну понятное дело, он же ждать то будет)
# 30 (любое число) - это количество секунд, в течение которого драйвер будет ждать выполнения того или иного условия
# poll_frequency=1 - определяет то, как часто делать новый запрос на проверку выполнения ожидаемого условия. В данном случае 1 секунда.
wait = WebDriverWait(driver, 15, poll_frequency=1)

# -----------------------------------------------------------------------------#
# driver.get("https://demoqa.com/dynamic-properties")
#
# button_after = ("xpath", "//button[@id='visibleAfter']")
# button_enable_in_seconds = ("xpath", "//button[@id='enableAfter']")
#
# wait.until(EC.visibility_of_element_located(button_after)).click()
# wait.until(EC.element_to_be_clickable(button_enable_in_seconds)).click()
# -----------------------------------------------------------------------------#
# driver.get("https://the-internet.herokuapp.com/dynamic_controls")
# REMOVE_BUTTON = ("xpath", "//button[text()='Remove']")
#
# driver.find_element(*REMOVE_BUTTON).click()
# wait.until(EC.invisibility_of_element_located(REMOVE_BUTTON)) # Ждем пока кнопка исчезнет
#
# print('Ok')
# -----------------------------------------------------------------------------#
driver.get("https://the-internet.herokuapp.com/dynamic_controls")
ENABLE_BUTTON = ("xpath", "//button[text()='Enable']")
TEXT_FIELD = ("xpath", "//input[@type='text']")

wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()
wait.until(EC.element_to_be_clickable(TEXT_FIELD)).send_keys("Hello")
wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD, "Hello"))
time.sleep(2)
print('Ok')

