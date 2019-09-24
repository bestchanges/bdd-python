from typing import List, Optional

from behave import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def find_tasks(browser: WebDriver) -> List[WebElement]:
    elements = browser.find_elements_by_xpath(f'//ul[@class="todo-list"]/*')
    return elements


def find_task_by_name(browser: WebDriver, task_name) -> Optional[WebElement]:
    tasks = find_tasks(browser)
    for task in tasks:
        found_label = task.find_element_by_xpath(f'//label[text()="{task_name}"]')
        if found_label:
            return task
    return None


def get_complete_control_for_task_li(task_li):
    return task_li.find_element_by_xpath('//input[@class="toggle"]')


def get_task_completed(task_li: WebElement):
    return task_li.get_attribute('class')


@step("list of tasks is empty")
def step_impl(context):
    tasks = find_tasks(context.browser)
    assert len(tasks) == 0


@step("user add task '{task_name}'")
def step_impl(context, task_name):
    browser: WebDriver = context.browser
    input = browser.find_element_by_xpath("//input[@class='new-todo']")
    input.send_keys(task_name)
    input.send_keys(Keys.RETURN)


@step("there is todo-item '{task_name}' in the list")
def step_impl(context, task_name):
    task = find_task_by_name(context.browser, task_name)
    assert task


@given("user open webpage {url}")
def step_impl(context, url):
    browser: WebDriver = context.browser
    browser.get(url)


@step("there are no todo-item '{task_name}' in the list")
def step_impl(context, task_name):
    task = find_task_by_name(context.browser, task_name)
    assert task is None


@when("user click checkbox before task '{task_name}'")
def step_impl(context, task_name):
    task_li = find_task_by_name(context.browser, task_name)
    complete_control = get_complete_control_for_task_li(task_li)
    complete_control.click()


@step("todo-item '{task_name}' is completed")
def step_impl(context, task_name):
    task_li = find_task_by_name(context.browser, task_name)
    assert get_task_completed(task_li) == 'completed'
