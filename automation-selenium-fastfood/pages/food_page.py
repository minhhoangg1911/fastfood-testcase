from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
import time

class FoodPage:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def food(self):
        time.sleep(5)
        food_span = self.driver.find_element(By.XPATH, "//span[@class='ant-menu-title-content' and text()='Food']").click()
        time.sleep(1)
        name_input = self.driver.find_element(By.NAME, "name").send_keys("Burgur")
        time.sleep(1)
        description_textarea = self.driver.find_element(By.XPATH, "//textarea[@name='description']").send_keys("Món Ăn Ngon")
        time.sleep(1)
        specialTag_input = self.driver.find_element(By.NAME, "specialTag").send_keys("XXX")
        time.sleep(1)
        category_select = self.driver.find_element(By.NAME, "category")
        select = Select(category_select)
        select.select_by_value("Dessert")
        time.sleep(1)
        file_path = r"C:\Users\Admin\Downloads\airplane_0005.jpg"
        time.sleep(1)
        price_input = self.driver.find_element(By.NAME, "price").send_keys("20")
        time.sleep(1)
        upload_input = self.driver.find_element(By.ID, "file")
        time.sleep(1)   
        upload_input.send_keys(file_path)
        time.sleep(1)
        button_create = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Create')]")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button_create)
        time.sleep(1)
        button_create.click()
        time.sleep(6)
        list_food_span = self.driver.find_element(By.XPATH, "//span[@class='ant-menu-title-content' and text()='List Food']")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", list_food_span)
        time.sleep(1)
        list_food_span.click()
        time.sleep(2)
        delete_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button.btn-danger")
        last_button = delete_buttons[-1]
        time.sleep(3)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", last_button)
        time.sleep(2)
        last_button.click()
        time.sleep(5)