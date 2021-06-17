from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BUTTON = (By. CSS_SELECTOR, 'a.button-type-secondary-light')
PRODUCTS = (By.XPATH, "//*[@id = 'wfm-pmd_deals_section']/div[6]//li")
REGULAR_WORD = (By. CSS_SELECTOR, 'span.wfm-sales-item-card__regular-price')
PRODUCT_DESCRIPTION = (By.CSS_SELECTOR, 'span.wfm-sales-item-card__product-name')


@given('Open Amazon Whole Foods page')
def open_page(context):
    context.driver.get('https://www.amazon.com/fmc/storedeals/?almBrandId=VUZHIFdob2xlIEZvb2Rz&ref_=US_MER_ALL_UFG_WFM_MERCH_0432906')


@then("Verify every product on the page has a text {expected_word}")
def verify_regular_price(context, expected_word):
    product_elements = context.driver.find_elements(*PRODUCTS)

    for product_element in product_elements:
        assert expected_word in product_element.text, f"Expected, {expected_word}, to be in: {product_element.text}"
        print('Product element: ',  product_element.text, ';')

        product_description = product_element.find_element(*PRODUCT_DESCRIPTION).text
        print('\n', product_description, ';')
        assert '' != product_description, f'Expected non-empty product name'


