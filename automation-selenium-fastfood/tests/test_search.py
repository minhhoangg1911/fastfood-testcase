from pages.search_page import SearchPage

def test_search(driver):

    test_search = SearchPage(driver)
    test_search.search()
