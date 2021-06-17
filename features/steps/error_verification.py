from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('User selects Financing')
def select_financing(context):
    context.application.raymour_page.select_financing()


@when('User selects Apply')
def submit_app(context):
    context.application.raymour_page.submit_apply()


@when('User submits application')
def submit_application(context):
    context.application.raymour_page.submit_application()


@then('User verifies {F}')
def verification(context, F):
    context.application.search_results_page.verify_text_shown_pt1(F)





