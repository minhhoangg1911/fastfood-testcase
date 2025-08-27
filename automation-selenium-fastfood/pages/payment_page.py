from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class PaymentPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def payment(self, card_number, expiry, cvc, country):

        iframe = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[title='Secure payment input frame']"))
        )
        self.driver.switch_to.frame(iframe)

        self.wait.until(EC.presence_of_element_located((By.ID, "Field-numberInput"))).send_keys(card_number)

        self.wait.until(EC.presence_of_element_located((By.ID, "Field-expiryInput"))).send_keys(expiry)

        self.wait.until(EC.presence_of_element_located((By.ID, "Field-cvcInput"))).send_keys(cvc)

        dropdown = Select(self.wait.until(EC.presence_of_element_located((By.ID, "Field-countryInput"))))
        dropdown.select_by_visible_text(country)

        self.wait.until(EC.presence_of_element_located((By.ID, "Field-postalCodeInput"))).send_keys("44444")

        self.driver.switch_to.default_content()

        submit_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Submit Order']]"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
        time.sleep(1)
        submit_btn.click()
