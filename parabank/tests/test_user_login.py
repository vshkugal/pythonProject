from selenium import webdriver
from ...parabank.src.pages.main_pages.home_page import HomePage
import pytest

user = "User0"


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()


def user_login(driver):
    page = HomePage(driver).open()
    assert page.is_logged_out(), "Some user is already logged in"
    page.login_panel.login_user_simplified(user)
    return page


def test_unregistered_user_login(driver):
    page = user_login(driver)
    assert page.is_logged_out(), "User '{}' was logged in".format(user)
    assert page.get_section_title() == 'Error!'


def test_new_user_registration_and_login(driver):
    page = HomePage(driver).open()
    assert page.is_logged_out(), "Some user is already logged in"
    page = page.login_panel.click_register()
    page.register_user_simplified(user)
    assert page.is_logged_in(), "User '{}' was not registered".format(user)


def test_registered_user_login(driver):
    page = user_login(driver)
    assert page.is_logged_in(), "User '{}' was not logged in".format(user)
    assert page.get_section_title() == 'Accounts Overview'
