from pages.base_page import Page
from selenium.webdriver.common.by import By


class ErrorVerificationPage(Page):

    FINANCING = (By.XPATH, "//a[contains(text(), 'Financing')]")
    SUBMIT_APPLY = (By.XPATH, "//span[contains(text(), 'Apply Now')]")
    SUBMIT_APPLICATION = (By.XPATH, "//span[contains(text(), 'Submit Application')]")

    def select_financing(self):
        self.click(*self.FINANCING)

    def submit_apply(self):
        self.click(*self.SUBMIT_APPLY)

    def submit_application(self):
        self.click(*self.SUBMIT_APPLICATION)



