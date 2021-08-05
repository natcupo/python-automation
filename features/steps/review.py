from selenium.webdriver.common.by import By
from behave import given, when, then

ITEM_SELECTION = By.XPATH("//*[text()='MacBook Pro 13-inch']")
PAGE_OPENS = By.CSS_SELECTOR('h1.entry-title')
REVIEWS = By.XPATH("//li[@id='tab-title-reviews']")
NO_REVIEWS_AVAILABLE = By.CSS_SELECTOR('p.woocommerce-noreviews')
NAME_FIELD = By.ID('author')
EMAIL_FIELD = By.ID('email')
COMMENT_WINDOW = By. ID('comment')
RATING = By.CSS_SELECTOR('a.star-5')
SUBMIT =By.CSS_SELECTOR('input.submit')
REVIEW_SUBMITTED = By. CSS_SELECTOR('em.woocommerce-review__awaiting-approval')


@given('Open Gettop page')
def open_gettopp(context):
    context.driver.get('https://gettop.us/')


@when('Select MacBook Pro 13-inch')
def selection(context):
    selection = context.driver.find_element(*ITEM_SELECTION)
    selection.click()


@when('{search_word} opens')
def open_macbook_page(context, search_word):
    result_msg = context.driver.find_element(*PAGE_OPENS).text
    assert search_word in result_msg, "Expected word '{}' in message, but got '{}'".format(search_word, result_msg)


@when('Select Reviews link')
def no_reviews(context):
    reviews = context.driver.find_element(*REVIEWS)
    reviews.click()


@when('Item has no {reviews}')
def no_reviews(context, reviews):
    no_reviews = context.driver.find_element(*NO_REVIEWS_AVAILABLE).text
    assert reviews in no_reviews, "Expected word '{}' in message, but got '{}'".format(reviews, no_reviews)


@when('Submit {comment_field}, {name_field} and {email_field}')
def review_submission(context, comment_field, name_field, email_field):
    rating = context.driver.find_element(*RATING)
    rating.click()
    comment_field = context.driver.find_element(*COMMENT_WINDOW)
    comment_field.send_keys(comment_field)
    name_field = context.driver.find_element(*NAME_FIELD)
    name_field.send_keys(name_field)
    email_field = context.driver.find_element(*EMAIL_FIELD)
    email_field.send_keys(email_field)
    submit_button = context.driver.find_element(*SUBMIT)
    submit_button.click()


@then('Review was submitted')
def review_submission(context):
    submission = context.driver.find_element(*REVIEW_SUBMITTED).text
