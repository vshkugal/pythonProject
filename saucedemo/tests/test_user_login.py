from ..src.pages.components.page_constants import *
from ..src.pages.all_pages.login_page import LoginPage
import pytest


class TestUserLogin:

    @pytest.fixture(scope="function")
    def login_page(self, driver) -> LoginPage:
        page = LoginPage(driver).open()
        return page

    def test_standard_user_login(self, login_page):
        login_page.login_user(standard_user, user_password)
        assert login_page.get_actual_url() == SAUCEDEMO_INVENTORY

    def test_incorrect_user_login(self, login_page):
        login_page.login_user(incorrect_user, incorrect_password)
        assert login_page.get_actual_url() == SAUCEDEMO_MAIN
        login_page.print_login_error()
        assert login_page.error_message.get_text() == INCORRECT_MESSAGE
        login_page.error_button.click()

    def test_locked_out_user_login(self, login_page):
        login_page.login_user(locked_out_user, user_password)
        assert login_page.get_actual_url() == SAUCEDEMO_MAIN
        login_page.print_login_error()
        assert login_page.error_message.get_text() == LOCKED_OUT_MESSAGE
        login_page.error_button.click()

    def test_problem_user_login(self, login_page):
        login_page.login_user(problem_user, user_password)
        assert login_page.get_actual_url() == SAUCEDEMO_INVENTORY

    def test_performance_glitch_user_login(self, login_page):
        login_page.login_user(performance_glitch_user, user_password)
        assert login_page.get_actual_url() == SAUCEDEMO_INVENTORY
