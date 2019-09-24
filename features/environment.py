# Take from: https://github.com/StephenDavidson/python-bdd-behave/blob/master/features/environment.py
from behave import fixture, use_fixture

from selenium.webdriver import Firefox

@fixture
def browser_firefox(context):
    browser = Firefox()
    browser.implicitly_wait(1)

    context.browser = browser

    yield context.browser

    context.browser.quit()

def before_all(context):
    use_fixture(browser_firefox, context)
