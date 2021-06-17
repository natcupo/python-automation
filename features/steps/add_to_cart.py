from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')
CART_ICON = (By.ID, 'nav-cart-count-container')
AMOUNT = (By. ID, 'nav-cart-count')
WORD_SEARCH = (By.ID, 'twotabsearchtextbox')
ELEMENT = (By.XPATH, "//span[@class='a-price-whole']//ancestor::a")
ELEMENT_AVAILABLE = (By.CSS_SELECTOR, 'span.a-color-state')


@when('Put {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*WORD_SEARCH)
    search.clear()
    search.send_keys(search_word)


@when('Verify {search_element} is there')
def element_verify(context, search_element):
    message = context.driver.find_element(*ELEMENT_AVAILABLE).text
    assert search_element in message, "Expected word '{}' in message, but got '{}'".format(search_element, message)


@when('Select a product')
def item_select(context):
    context.driver.find_element(*ELEMENT).click()


@when('Select Add to Cart')
def add_to_cart_icon(context):
    icon = context.driver.find_element(*ADD_TO_CART_BUTTON)
    icon.click()


@when('Select Cart Icon')
def cart_icon_selected(context):
    cart_icon = context.driver.find_element(*CART_ICON)
    cart_icon.click()
    sleep(4)


@then('Verify {amount} of items is one')
def one_item(context, amount):
    cart_number_count = context.driver.find_element(*AMOUNT).text
    print(cart_number_count)
    assert int(cart_number_count) == 1



