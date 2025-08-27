from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
import time

class Register:
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def register(self):
        time.sleep(5)
        account_setting = self.driver.find_element(By.XPATH, "//a[text()='Setting']").click()
        time.sleep(1)
        account_register = self.driver.find_element(By.XPATH, "//a[text()='Register']").click()
        time.sleep(1)
        username_input = self.driver.find_element(By.NAME, "userName").send_keys("customer1@gmail.com")
        time.sleep(1)
        name_input = self.driver.find_element(By.NAME, "name").send_keys("customer1")
        time.sleep(1)
        password_input = self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys("123456")
        time.sleep(1)
        dropdown = Select(self.driver.find_element(By.NAME, "role"))
        # dropdown.select_by_index(1)   # chọn Customer
        # dropdown.select_by_value("customer")   # chọn Customer
        dropdown.select_by_visible_text("Customer")
        time.sleep(1)
        register_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Register')]").click()
