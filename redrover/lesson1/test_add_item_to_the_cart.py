from selenium import webdriver  # Импортируем класс webdriver из библиотеки Selenium для управления браузером
from webdriver_manager.chrome import ChromeDriverManager  # Импортируем ChromeDriverManager для автоматической установки и управления версией ChromeDriver
from selenium.webdriver.chrome.service import Service  # Импортируем класс Service для настройки службы ChromeDriver

# Настраиваем службу ChromeDriver с использованием ChromeDriverManager
service = Service(executable_path=ChromeDriverManager().install())
# Создаем экземпляр Chrome WebDriver с настроенной службой
driver = webdriver.Chrome(service=service)

def test_add_item_to_the_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element("xpath", '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element("xpath", '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element("xpath", '//input[@data-test="login-button"]')
    login_button.click()

    backpack_text = driver.find_element("xpath", '//a[@id="item_4_title_link"]/div[@class="inventory_item_name "]').text

    add_to_cart_button = driver.find_element("xpath", '//button[@data-test = "add-to-cart-sauce-labs-backpack"] ')
    add_to_cart_button.click()

    shopping_cart_link = driver.find_element("xpath", '//a[@class = "shopping_cart_link"]')
    shopping_cart_link.click()

    item_text_in_cart = driver.find_element("xpath", '//a[@id="item_4_title_link"]/div[@class="inventory_item_name"]').text

    assert backpack_text == item_text_in_cart

    driver.quit()

