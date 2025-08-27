from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time

class LoginPage:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def login(self, username, password):
        time.sleep(5)
        remove_toast = self.driver.find_element(By.XPATH, "//div[contains(text(),'Register successful! Please login to continue')]").click()
        time.sleep(1)
        account_setting = self.driver.find_element(By.XPATH, "//a[text()='Setting']").click()
        time.sleep(1)
        account_login = self.driver.find_element(By.XPATH, "//a[text()='Login']").click()
        time.sleep(1)
        username_input = self.driver.find_element(By.NAME, "userName").send_keys(username)
        time.sleep(1)
        password_input = self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        time.sleep(1)
        login_button = self.driver.find_element(By.XPATH, "//button[contains(text(),'Login')]").click()
        time.sleep(3)