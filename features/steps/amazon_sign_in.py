from selenium.webdriver.common.by import By
from behave import given, when, then

ORDERS_LINK = (By. ID, 'nav-orders')
SIGN_IN_RESULT = (By. CSS_SELECTOR, 'h1.a-spacing-small')


@when('Select Orders link')
def select_order(context):
    context.application.main_page.select_orders_link()


@then('Verify {search_word} is opened')
def verify_sign_in_opened(context, search_word):
    context.application.search_results_page.verify_sign_in_opened(search_word)

