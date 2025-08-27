from pages.food_page import FoodPage

def test_food(driver):

    food_page = FoodPage(driver)
    food_page.food()