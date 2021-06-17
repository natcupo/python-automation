from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class MenuPage(Page):
    HAM_MENU = (By.ID, 'nav-hamburger-menu')
    AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
    AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")

    def select_menu_icon(self):
        self.click(*self.HAM_MENU)

    def select_amazon_menu(self):
        sleep(4)
        self.click(*self.AMAZON_MUSIC_MENU_ITEM)
        sleep(1)

    def verify_item_count(self, expected_item_count: int):
        count = len(self.driver.find_elements(*self.AMAZON_MUSIC_MENU_ITEM_RESULTS))
        assert count == int(expected_item_count)
