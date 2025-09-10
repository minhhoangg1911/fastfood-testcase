from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time
class User:
    def __init__(self,driver: WebDriver):
        self.driver = driver

    def user(self):
        time.sleep(5)
        user_link = self.driver.find_element(By.XPATH, "//span[contains(text(), 'List User')]")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", user_link)
        time.sleep(2)
        user_link.click()
        time.sleep(2)
        delete_button = self.driver.find_element(By.XPATH,
        "//div[@class='row border' and .//div[text()='customer1@gmail.com']]//button[contains(@class,'btn-danger')]"
        )
        delete_button.click()
        time.sleep(2)
        time.sleep(5)
    