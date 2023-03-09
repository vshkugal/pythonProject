from ..src.pages.components.page_constants import *
from ..src.pages.all_pages.login_page import LoginPage
import pytest
import allure


class TestUserLogin:

    @pytest.fixture(scope="function")
    def login_page(self, driver) -> LoginPage:
        with allure.step("Open Login Page"):
            page = LoginPage(driver).open()
        return page

    @allure.feature("User Login Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Standard User Login Test")
    @allure.description("Positive test: Standard User Login")
    def test_standard_user_login(self, login_page):
        with allure.step("Login standard user"):
            login_page.login_user(standard_user, user_password)
        with allure.step("Assert login success"):
            assert login_page.get_actual_url() == SAUCEDEMO_INVENTORY

    @allure.feature("User Login Test")
    @allure.story("Negative Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Incorrect User Login Test")
    @allure.description("Negative test: Incorrect User Login")
    def test_incorrect_user_login(self, login_page):
        with allure.step("Login incorrect user"):
            login_page.login_user(incorrect_user, incorrect_password)
        with allure.step("Assert login failure"):
            assert login_page.get_actual_url() == SAUCEDEMO_MAIN
        with allure.step("Print login error"):
            login_page.print_login_error()
        with allure.step("Check login error message"):
            assert login_page.error_message.get_text() == INCORRECT_MESSAGE
        with allure.step("Close error message"):
            login_page.error_button.click()

    @allure.feature("User Login Test")
    @allure.story("Negative Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Locked Out User Login Test")
    @allure.description("Negative test: Locked Out User Login")
    def test_locked_out_user_login(self, login_page):
        with allure.step("Login locked out user"):
            login_page.login_user(locked_out_user, user_password)
        with allure.step("Assert login failure"):
            assert login_page.get_actual_url() == SAUCEDEMO_MAIN
        with allure.step("Print login error"):
            login_page.print_login_error()
        with allure.step("Check login error message"):
            assert login_page.error_message.get_text() == LOCKED_OUT_MESSAGE
        with allure.step("Close error message"):
            login_page.error_button.click()

    @allure.feature("User Login Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Problem User Login Test")
    @allure.description("Positive test: Problem User Login")
    def test_problem_user_login(self, login_page):
        with allure.step("Login problem user"):
            login_page.login_user(problem_user, user_password)
        with allure.step("Assert login success"):
            assert login_page.get_actual_url() == SAUCEDEMO_INVENTORY

    @allure.feature("User Login Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Glitch User Login Test")
    @allure.description("Positive test: Glitch User Login")
    def test_performance_glitch_user_login(self, login_page):
        with allure.step("Login glitch user"):
            login_page.login_user(performance_glitch_user, user_password)
        with allure.step("Assert login success"):
            assert login_page.get_actual_url() == SAUCEDEMO_INVENTORY
