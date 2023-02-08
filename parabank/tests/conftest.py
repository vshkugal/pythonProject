from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from ...parabank.src.pages.main_pages.home_page import HomePage
from ...parabank.src.pages.exceptions.custom_exceptions import BasePageException
import pytest

# Universal username and password that is going to be used in all tests except login, registration and lookup
test_user = "ParaBankUser8"

# supported_browsers = ["CHROME"]
# supported_browsers = ["FF"]
supported_browsers = ["CHROME", "FF"]


@pytest.fixture(scope="module", params=supported_browsers)
def driver(request):
    """
    Universal webdriver that is going to be used in all tests
    """
    browser = request.param
    if browser == "CHROME":
        driver = webdriver.Chrome()
    elif browser == "FF":
        # driver = webdriver.Firefox()
        options = Options()
        options.binary_location = r'c:\Program Files\Mozilla Firefox\firefox.exe'
        # driver = webdriver.Firefox(executable_path=r'c:\webdrivers\geckodriver.exe', options=options)
        service = Service(r'c:\webdrivers\geckodriver.exe')
        driver = webdriver.Firefox(service=service, options=options)
    elif browser == "OPERA":
        driver = webdriver.Opera()
    elif browser == "IE":
        driver = webdriver.Ie()
    elif browser == "EDGE":
        driver = webdriver.Edge()
    elif browser == "SAFARI":
        driver = webdriver.Safari()
    else:
        raise Exception("There is no support for browser: {}".format(browser))
    yield driver
    driver.close()


@pytest.fixture(scope="module")
def user_login(driver):
    """
    Universal login function that is going to be used in all tests where user must be logged in before action
    """
    page = HomePage(driver)
    # If no user is logged in, try to log in universal user "test_user"
    # by filling Customer Login form
    if page.is_logged_out():
        page.login_panel.login_user_simplified(test_user)
    # If "test_user" was not logged in, try to register "test_user"
    # by clicking 'Register' link and filling Customer Registration form
    if page.is_logged_out():
        page = page.login_panel.click_register()
        page.register_user_simplified(test_user)
    # If registration failed because "test_user" exists in the system, try to look up "test_user"
    # by clicking 'Forgot login info?' link and filling Customer Lookup form
    if page.is_logged_out():
        page = page.login_panel.click_forgot()
        page.lookup_user_simplified(test_user)
    return page


@pytest.fixture(scope="function")
def transaction_details(user_login):
    """
    Universal test function verifying account pages (Account Activity, Transaction Details)
    that become available only after certain transactions with account
    """
    # Navigate to Accounts Overview page and check Accounts Overview table
    page = user_login.logged_in_panel.click_accounts_overview()
    page.print_accounts_overview()
    # Navigate to Account Activity page of the main account (first in the list of available accounts)
    # and check Account Details and Account Activity (all account transactions) tables
    page = page.click_account_link()
    page.print_account_details()
    if page.no_transactions():
        raise BasePageException("The are no transactions in this account yet. "
                                "Please create transaction before using this fixture.")
    page.print_account_transactions()
    # Navigate to Transaction Details page of the last transaction in the list of account's transactions
    # and check Transaction Details table
    page = page.click_transaction_link()
    page.print_transaction_details()
    # Return Transaction Details page for further assessment
    return page
