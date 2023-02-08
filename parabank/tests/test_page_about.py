from ...parabank.src.pages.main_pages.about_page import AboutPage
from ...parabank.src.pages.main_pages.admin_page import AdminPage
from ...parabank.src.pages.components.page_constants import PARASOFT_MAIN
import pytest


class TestPageAbout:

    @pytest.fixture(scope="function")
    def about_page(self, driver) -> AboutPage:
        try:
            page = AboutPage(driver)
            yield page
        finally:
            page = AboutPage(driver)
            page.open()

    def test_top_panel_link_on_about_page(self, driver, about_page):
        assert about_page.header.admin_top_link.exists()
        assert about_page.header.admin_top_link.wait_to_be_clickable()
        assert about_page.header.admin_top_link.is_clickable()
        page = about_page.header.click_admin_top()
        assert AdminPage(driver).expected_url in page.get_actual_url()

    def test_about_page_functionality(self, about_page):
        about_page.print_section_info()
        page = about_page.click_visit()
        assert page.get_actual_url() == PARASOFT_MAIN
