from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
from pprint import pprint

driver: WebDriver = webdriver.Chrome()

def test_add_item_to_the_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    backpack_text = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]/div[@class="inventory_item_name "]').text

    add_to_cart_button = driver.find_element(By.XPATH, '//button[@data-test = "add-to-cart-sauce-labs-backpack"] ')
    add_to_cart_button.click()

    shopping_cart_link = driver.find_element(By.XPATH, '//a[@class = "shopping_cart_link"]')
    shopping_cart_link.click()

    item_text_in_cart = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]/div[@class="inventory_item_name"]').text

    assert backpack_text == item_text_in_cart

    time.sleep(3)
    driver.quit()

