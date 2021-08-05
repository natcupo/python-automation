from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(Page):
    SEARCH_INPUT = (By.NAME, 'q')
    SEARCH_SUBMIT = (By.NAME, 'btnK')
    ORDERS_LINK = (By.ID, 'nav-orders')
    CART = (By.ID, 'nav-cart-count-container')
    ITEM = (By. CSS_SELECTOR, 'div.FourSalePromos__SectionHeading')
    ELEMENTS = (By.XPATH, "//ul[@role='listbox']//li//div[@class='wM6W7d']")

    def search_for_keyword(self, text):
        self.input_text(text, *self.SEARCH_INPUT)
        self.driver.wait.until(EC.element_to_be_clickable(self.SEARCH_SUBMIT))
        self.click(*self.SEARCH_SUBMIT)

    def select_orders_link(self):
        self.click(*self.ORDERS_LINK)

    def select_cart_icon(self):
        self.click(*self.CART)

    def item_selection(self):
        self.click(*self.ITEM)

    def google_dynamic(self, text):
        self.input_text(text, *self.SEARCH_INPUT)

    def google_dynamics(self):
        el = self.driver.find_elements(*self.ELEMENTS)
        if el[2].text == "sephoracuse ny":
            print(el[2].text)
        else:
            print('Provided text is NOT eligible')



