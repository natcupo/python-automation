from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open webpage')
def open_page(context):
    context.application.main_page.furniture_page()


@when('Select item')
def item_selection(context):
    context.application.main_page.item_selection()


@when('Select Price department')
def select_department(context):
    context.application.search_results_page.department_selection()


@then('{department} is selected')
def result(context, department):
    context.application.search_results_page.verify_selected_department(department)
