from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SearchResults(Page):
    RESULTS_FOUND_MESSAGE = (By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]")
    SIGN_IN_RESULT = (By.CSS_SELECTOR, 'h1.a-spacing-small')
    EMPTY_CART = (By.CSS_SELECTOR, 'div.sc-your-amazon-cart-is-empty')
    SELECTION = (By.CSS_SELECTOR, 'select.ProductSearchSort__Select')
    BEST_SELLING = (By.XPATH, '//*[@id="product-search-content"]/div[1]/div[2]/label/div/select/option[1]')
    F = (By.ID, 'firstName-error')
    L = (By.ID, 'lastName-error')

    def verify_result_shown(self, expected_text):
        self.verify_text(expected_text, *self.RESULTS_FOUND_MESSAGE)

    def verify_sign_in_opened(self, expected_text):
        self.verify_text(expected_text, *self.SIGN_IN_RESULT)

    def cart_is_empty(self, expected_text):
        self.verify_text(expected_text, *self.EMPTY_CART)

    def department_selection(self):
        select_department_element = self.driver.find_element(*self.SELECTION)
        select = Select(select_department_element)
        select.select_by_value('rating')

    def verify_selected_department(self, expected_text):
        self.verify_text(expected_text, *self.BEST_SELLING)

    def verify_text_shown_pt1(self, expected_text_1):
        self.verify_text(expected_text_1, *self.F)







