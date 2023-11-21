import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

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

