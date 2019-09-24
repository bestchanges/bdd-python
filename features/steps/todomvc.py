from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver


@given("list of tasks is empty")
def step_impl(context):
    pass


@when("user add task '{task_name}'")
def step_impl(context, task_name):
    browser: WebDriver = context.browser
    input = browser.find_element_by_xpath("//input[@class='new-todo']")
    input.send_keys(task_name)
    input.send_keys(Keys.RETURN)


@step("there is todo-item '{todo_item}' in the list")
def step_impl(context, todo_item):
    elements = find_todo_items_by_name(context, todo_item)
    assert len(elements) > 0


def find_todo_items_by_name(context, todo_item):
    browser: WebDriver = context.browser
    elements = browser.find_elements_by_xpath(f'//label[text()="{todo_item}"]')
    return elements


@given("user open webpage {url}")
def step_impl(context, url):
    browser: WebDriver = context.browser
    browser.get(url)


@step("there are no todo-item '{todo_item}' in the list")
def step_impl(context, todo_item):
    elements = find_todo_items_by_name(context, todo_item)
    assert len(elements) == 0
