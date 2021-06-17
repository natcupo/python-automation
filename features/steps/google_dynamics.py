from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_WORD = (By.NAME, 'q')
ELEMENTS = (By.XPATH, "//ul[@role='listbox']//li//div[@class='wM6W7d']")


@when('Input {word} into text field')
def enter_search_word(context, word):
    search_word = context.driver.find_element(*SEARCH_WORD)
    search_word.send_keys(word)


#@then('Forth element is shown')
#def forth_element(context):
    #el = context.driver.find_elements(*ELEMENT)
    #print('Total elements are ' + str(len(el)))
    #for x in range(len(el)):
        #print(el[2].text)
        #if el[2].text == "sephora syracuse ny":
            #print(el[2].text)
            #el[0].click()
        #else:
            #print('wow')

@then('Second element is shown')
def second_element(context):
    el = context.driver.find_elements(*ELEMENTS)
    print('Total elements are ' + str(len(el)))
    #print(el[2].text)
    if el[2].text == "sephora syracuse ny":
        print(el[2].text)
    else:
        print('error')












