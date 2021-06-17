from selenium.webdriver.common.by import By
from behave import given, when, then

FIND_STORE = (By.CSS_SELECTOR, 'a.GlobalHeaderMain__Item')
ASSERTION = (By. CSS_SELECTOR, 'h1.LocatorSearch__Heading')
ZIP_CODE = (By. ID, "enter-zip")
SEARCH_SUBMIT = (By. CSS_SELECTOR, "button.LocatorSearch__SearchButton")
STORE = (By. XPATH, "//*[contains(text(),'Syracuse Clearance Center')]")
STORE_SELECTION = (By.XPATH, "//*[contains(text(),'Select Store')]")
MY_STORE = (By. XPATH, "//*[contains(text(),'MY STORE')]")


@given('Open web page')
def open_google(context):
    context.driver.get('https://www.raymourflanigan.com/')


@when('Select Find Store')
def click_find_store(context):
    context.driver.find_element(*FIND_STORE).click()


@when('Verify {search} is available')
def verify_find_store(context, search):
    result = context.driver.find_element(*ASSERTION).text
    assert search in result, "Expected word '{}' in message, but got '{}'".format(search, result)
    if search == result:
        print("pass")
    else:
        print("fail")


@when("Enter {myword} into zip code field")
def enter_text(context, myword):
    search = context.driver.find_element(*ZIP_CODE)
    search.send_keys(myword)
    context.driver.find_element(*SEARCH_SUBMIT).click()


@when("{store} is available")
def store_available(context, store):
    stores = context.driver.find_element(*STORE)
    # store in stores, "Expected word '{}' in message, but got '{}'".format(store, stores)


@when("Select Store")
def selection(context):
    select = context.driver.find_element(*STORE_SELECTION)
    select.click()


@then("{mystore} is available")
def my_store(context, mystore):
    mystore = context.driver.find_element(*MY_STORE)
    # assert mystore in mystore, "Expected word '{}' in message, but got '{}'".format(mystore, mystore)
