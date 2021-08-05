from pages.main_page import MainPage
from pages.search_results_page import SearchResults
from pages.menu_page import MenuPage
from pages.raymour_page import ErrorVerificationPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResults(self.driver)
        self.menu_page = MenuPage(self.driver)
        self.raymour_page = ErrorVerificationPage(self.driver)

