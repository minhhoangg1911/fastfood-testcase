import os
from pages.payment_page import PaymentPage

def test_payment(driver):
       card_number = os.getenv("TEST_NUMBERID")
       date = os.getenv("TEST_DATE")
       security = os.getenv("TEST_SECURITY")
       country = os.getenv("TEST_COUNTRY")
       
       payment_page = PaymentPage(driver)
       payment_page.payment(card_number,date,security,country)