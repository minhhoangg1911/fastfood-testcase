from pages.user_page import User

def test_user(driver):

    user_page = User(driver)
    user_page.user()