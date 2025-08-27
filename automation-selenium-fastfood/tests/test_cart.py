import os
from pages.cart_page import CartPage

def test_cart(driver):
    phoneNumber = os.getenv("TEST_PHONENUMBER")

    cart_page = CartPage(driver)
    cart_page.cart(phoneNumber)