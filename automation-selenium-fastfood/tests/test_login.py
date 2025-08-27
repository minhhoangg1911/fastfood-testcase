import os
from pages.login_page import LoginPage

def test_login(driver):
    username = os.getenv("TEST_USERNAME")
    password = os.getenv("TEST_PASSWORD")

    login_page = LoginPage(driver)
    login_page.login(username,password)