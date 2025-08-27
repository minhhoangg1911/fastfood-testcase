from pages.register_page import Register

def test_register(driver):
    
    register_page = Register(driver)
    register_page.register()