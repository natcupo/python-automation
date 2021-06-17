from selenium.webdriver.common.by import By
from behave import given, when, then

CART = (By. ID, 'nav-cart-count-container')
EMPTY_CART = (By.CSS_SELECTOR, 'div.sc-your-amazon-cart-is-empty')


@when('Select Cart')
def select_cart(context):
    # context.driver.find_element(*CART).click()
    context.application.main_page.select_cart_icon()


@then('Verify {search_text} text is present')
def cart_empty(context, search_text):
    # result = context.driver.find_element(*EMPTY_CART).text
    # assert search_text in result, "Expected word '{}' in message, but got '{}'".format(search_text, result)
    context.application.search_results_page.cart_is_empty(search_text)
