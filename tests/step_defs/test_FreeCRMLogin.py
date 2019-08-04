# coding=utf-8
"""Free CRM Login Feature feature tests."""

from pytest_bdd import given,scenario,then,when,parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture
def browser():
    path = 'F:\\selenium-java-3.141.59\\geckodriver.exe'
    driver = webdriver.Firefox(executable_path=path)
    driver.implicitly_wait(10)
    yield driver
    time.sleep(5)
    driver.quit()


@scenario('../features/FreeCRMLogin.feature', 'Free CRM Login Test Scenario')
def test_add1():
    pass

@scenario('../features/FreeCRMLogin.feature','Free CRM Login Test Scenario1 using parameter')
def test_add2():
    pass

@scenario('../features/FreeCRMLogin.feature','Free CRM Login Test Scenario2')
def test_add3():
    pass


@given('User is already on login page')
def user_is_already_on_login_page(browser):

    browser.maximize_window()
    browser.implicitly_wait(10)
    browser.get("https://classic.crmpro.com/index.html")




@when('title of Login page is Free CRM')
def title_of_login_page_is_free_crm(browser):
    title = browser.title
    print(title)
    assert title == title



@when('user clicks on login button')
def user_clicks_on_login_button(browser):
    login_btn = browser.find_element(By.XPATH,"//input[@type='submit']")
    browser.execute_script("arguments[0].click();", login_btn)




@when('user enters username and password')
def user_enters_username_and_password(browser):
    browser.find_element(By.NAME,"username").send_keys("Dranadheer")
    browser.find_element(By.NAME,"password").send_keys('"test@1234"')

@when(parsers.parse('user enters "{username}" and "{password}"'))
def user_enter_details(browser,username, password):
    browser.find_element(By.NAME, "username").send_keys(username)
    browser.find_element(By.NAME, "password").send_keys(password)

@when('user enters "<username>" and "<password>"')
def user_enter_details(browser,username, password):
    browser.find_element(By.NAME, "username").send_keys(username)
    browser.find_element(By.NAME, "password").send_keys(password)

#above 3 can be combined into single as below
# @when('user enters username and password')
# @when(parsers.parse('user enters "{username}" and "{password}"'))
# @when("user enters <username> and <password>")
# def user_enter_details(browser,username, password):
#     browser.find_element(By.NAME, "username").send_keys(username)
#     browser.find_element(By.NAME, "password").send_keys(password)

@then('Close the browser')
def close_the_browser(browser):
    pass


@then('user is on home page')
def user_is_on_home_page(browser):
    title = browser.title
    print(title)
    assert title == "CRMPRO - CRM software for customer relationship management, sales, and support."


