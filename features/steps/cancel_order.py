from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ORDER_TEXT = (By.ID, 'twotabsearchtextbox')
SEARCH_SUBMIT = (By. ID, 'nav-search-submit-button')
RESULTS_FOUND_MESSAGE = (By. XPATH, "//*[@id='question-answer']//div[1]//span/span[2]")


@when('Input Cancel order into text field')
def input_text(context):
    search = context.driver.find_element(*ORDER_TEXT)
    search.clear()
    search.send_keys("Cancel Order")


@when('Select search button')
def verify_cancel_order(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()


@then('Word {search_word} is available')
def verify_found_results_text(context, search_word):
    results_msg = context.driver.find_element(*RESULTS_FOUND_MESSAGE).text
    assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)



