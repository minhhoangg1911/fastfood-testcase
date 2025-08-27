from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time
class SearchPage:
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def search(self):
        time.sleep(5)
        link_search = self.driver.find_element(By.XPATH, "//span[contains(text(), 'All Orders')]").click()
        time.sleep(1)
        search_input = self.driver.find_element(By.NAME, "searchString").send_keys("customer")
        time.sleep(1)
        button_search = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Filters')]").click()