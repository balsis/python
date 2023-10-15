from selenium import webdriver
from selenium.webdriver.common.by import By
import math

link = 'http://suninjuly.github.io/find_link_text'
link_value = str(math.ceil(math.pow(math.pi, math.e)*10000))
try:
    browser = webdriver.Chrome()
    browser.get(link)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла