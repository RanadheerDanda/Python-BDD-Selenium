import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Constants



DUCKDUCKGO_HOME = 'https://duckduckgo.com/'

# Scenarios

scenarios('../features/DuckDuckGoWebBrowsing.feature')


# Fixtures

@pytest.fixture
def browser():
    path = 'F:\\selenium-java-3.141.59\\geckodriver.exe'
    driver = webdriver.Firefox(executable_path=path)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# Given Steps

@given('the DuckDuckGo home page is displayed')
def ddg_home(browser):
    browser.get(DUCKDUCKGO_HOME)


# When Steps

@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase(browser, phrase):
    search_input = browser.find_element_by_name('q')
    search_input.send_keys(phrase + Keys.RETURN)


# Then Steps

@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    links_div = browser.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    search_input = browser.find_element_by_name('q')
    assert search_input.get_attribute('value') == phrase