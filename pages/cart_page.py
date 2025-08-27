from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time

class CartPage:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def cart(self, phone):
        time.sleep(1)
        add_cart_button = self.driver.find_element(By.XPATH, "//i[contains(@class, 'bi-cart-plus')]")
        
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_cart_button)
        time.sleep(1)
        add_cart_button.click()
        
        time.sleep(1)
        remove_toast = self.driver.find_element(By.XPATH, "//div[contains(text(),'Item added to cart successfully')]").click()

        link_cart_page = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", link_cart_page)
        time.sleep(1)
        link_cart_page.click()

        time.sleep(1)
        increase_item = self.driver.find_element(By.XPATH, "//i[contains(@class, 'bi bi-plus-circle-fill')]")
        increase_item.click()
        time.sleep(0.5) 
        increase_item.click()
        time.sleep(1)
        decrease_item = self.driver.find_element(By.XPATH, "//i[contains(@class, 'bi bi-dash-circle-fill')]").click()

        time.sleep(1)
        phoneNumber_input = self.driver.find_element(By.NAME, "phoneNumber").send_keys(phone)
        place_order_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        place_order_btn.click()
        time.sleep(3)