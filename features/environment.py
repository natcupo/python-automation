from selenium import webdriver
from features.application import Application

# bs_user = 'natalia_GCDipd'
# bs_pw = 'UHhJomFpy3mmonpKYr1G'


def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome(executable_path='drivers/chromedriver')

    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    # url = f'http://{bs_user}:{bs_pw}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.application = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()


#desired_cap = {
      #'browser': 'Chrome',
      #'browser_version': '78.0',
      #'os': 'Windows',
      #'os_version': '10',
      #'#name': 'User gets verification errors without co-applicant'
    #}


