import os
from dotenv import load_dotenv
from utils.driver_setup import init_driver
from tests.test_register import test_register
from tests.test_login import test_login
from tests.test_cart import test_cart 
from tests.test_payment import test_payment
from tests.test_food import test_food
from tests.test_user import test_user
from tests.test_search import test_search

if __name__ == "__main__":
    load_dotenv()

    driver = init_driver()
    driver.get("http://localhost:3000/")
    test_register(driver)
    test_login(driver)
    test_cart(driver)
    test_payment(driver)
    driver.get("http://localhost:3000/admin")
    test_food(driver)
    test_user(driver)
    test_search(driver)
    input("\n Press Enter to finish...")
    driver.quit()