from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

TOP_LINKS = (By. CSS_SELECTOR, 'div.GlobalHeaderTier1Desktop__Inner')


@then('User can go through top links and verify page has opened')
def click_through_top(context):
    link_element = context.driver.find_element(*TOP_LINKS)
    for link in link_element:
        link_element = context.driver.find_element(*TOP_LINKS)
        link_element.click()
