from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from ..src.pages.all_pages.login_page import LoginPage
from ..src.pages.components.page_constants import *
import pytest

supported_browsers = ["CHROME"]
# supported_browsers = ["FF"]
# supported_browsers = ["CHROME", "FF"]
test_data = "test_data"


@pytest.fixture(scope="module", params=supported_browsers)
def driver(request):
    """
    Universal webdriver that is going to be used in all tests
    """
    browser = request.param
    if browser == "CHROME":
        driver = webdriver.Chrome()
    elif browser == "FF":
        options = Options()
        options.binary_location = r'c:\Program Files\Mozilla Firefox\firefox.exe'
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


@pytest.fixture(scope="function")
def user_login(driver):
    """
    Universal login function that is going to be used in all tests where standard user must be logged in before action
    """
    page = LoginPage(driver).open()
    page.login_user(standard_user, user_password)
    return page


@pytest.fixture(scope="module")
def standard_user_login(driver):
    page = LoginPage(driver).open()
    page.login_user(standard_user, user_password)
    return page


@pytest.fixture(scope="function")
def inventory_page(standard_user_login):
    return standard_user_login.header.click_inventory()


@pytest.fixture(scope="function")
def cart_page(standard_user_login):
    return standard_user_login.header.click_cart()


@pytest.fixture(scope="function")
def checkout_page1(cart_page):
    return cart_page.click_checkout_button()


@pytest.fixture(scope="function")
def checkout_page2(checkout_page1):
    checkout_page1.first_name_input.set_text(test_data)
    checkout_page1.last_name_input.set_text(test_data)
    checkout_page1.postal_code_input.set_text(test_data)
    return checkout_page1.click_continue_button()


@pytest.fixture(scope="function")
def checkout_page3(checkout_page2):
    return checkout_page2.click_finish_button()
