from selenium.webdriver.common.by import By
from behave import given, when, then

HAM_MENU = (By.ID, 'nav-hamburger-menu')
AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")


@when('Select hamburger menu')
def click_on_hamburger_menu(context):
    # context.driver.find_element(*HAM_MENU).click()
    context.application.menu_page.select_menu_icon()


@when('Select Amazon music menu item')
def click_on_amazon_music_menu_item(context):
    # context.driver.find_element(*AMAZON_MUSIC_MENU_ITEM).click()
    context.application.menu_page.select_amazon_menu()


@then('{expected_item_count} menu items are present')
def verify_amount_of_items(context, expected_item_count):
    """
    Converts string to integer
    :param context:
    :param expected_item_count
    """
    expected_item_count = int(expected_item_count)
    # count = len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS))
    # assert count == int(expected_item_count)
    context.application.menu_page.verify_item_count(expected_item_count)
