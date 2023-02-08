from ...parabank.src.pages.main_pages.home_page import HomePage
import pytest


class TestPageHome:

    @pytest.fixture(scope="function")
    def home_page(self, driver) -> HomePage:
        page = HomePage(driver)
        return page

    def test_click_services(self, home_page):
        page = home_page.click_services()
        assert page.is_on_correct_page()

    def test_click_news(self, home_page):
        page = home_page.click_news()
        assert page.is_on_correct_page()

    def test_home_page_latest_news(self, home_page):
        page = home_page.print_latest_news()
        assert page.is_on_correct_page()
