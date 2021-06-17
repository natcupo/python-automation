from selenium.webdriver.common.by import By
from behave import given, when, then
import datetime

DURATION_LOCATOR = (By.CSS_SELECTOR, 'css_selector_locator')
LOCATOR_BLACK_FRAME = (By.CSS_SELECTOR, 'black_frame_locator')
LOCATOR_PLUS_BUTTON = (By.CSS_SELECTOR, 'plus_button_locator')
TIME_COLUMN = (By.XPATH, 'plus_button_locator')
FIRST_ROW = (By. XPATH, 'first_row_locator')


@given('Open Target Delivery page')
def open_page(context):
    context.driver.get('https://www.websitename.com/')


@when('Increase {duration} in Black Frame')
def increase_black_frame(context, duration):
    # finds an original duration of 00:00:30,00
    duration = context.driver.find_element(*DURATION_LOCATOR).text
    # finds a whole Black Frame block
    black_frame = context.driver.find_element(*LOCATOR_BLACK_FRAME)
    # selects plus button and increases video clip duration
    plus_button = context.driver.find_element(*LOCATOR_PLUS_BUTTON)
    for plus_button in black_frame:
        plus_button.click()
    actual_result = datetime.datetime(duration)
    expected_result = actual_result + datetime.timedelta(2, 15)
    assert actual_result in duration, "Expected word '{}' in message, but got '{}'".format(actual_result, duration)
    if expected_result == '00:00:32,15':
        print('Duration increased by 2 minutes 15 seconds')
    else:
        print('Duration did not increase')


@then('Time is adjusted')
def adjust_time(context):
    time_column = context.driver.find_element(*TIME_COLUMN)
    # selects the first row duration result in Time column
    first_row = context.driver.find_element(*FIRST_ROW).text
    assert first_row in time_column, "Expected word '{}' in message, but got '{}'".format(first_row, time_column)
    if first_row == '13:15:43,01':
        print('The video clip time has been increased')
    else:
        print('The video clip time did not increase')








