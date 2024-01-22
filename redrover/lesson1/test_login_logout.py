from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
from pprint import pprint

driver: WebDriver = webdriver.Chrome()

def test_add_item_to_the_cart():
    driver.get("https://www.saucedemo.com/")
    url_before = driver.current_url
    username_field = driver.find_element("xpath", '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element("xpath", '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element("xpath", '//input[@data-test="login-button"]')
    login_button.click()

    burger_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
    burger_menu.click()
    time.sleep(1)
    logout = driver.find_element(By.ID, 'logout_sidebar_link')
    logout.click()

    url_after = driver.current_url

    assert url_after == url_before
    time.sleep(3)
    driver.quit()