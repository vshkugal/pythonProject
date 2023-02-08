from ...parabank.src.pages.main_pages.about_page import AboutPage
import pytest

pages = [AboutPage]
# pages = [AboutPage, AdminPage, ContactPage, HomePage, LookupPage, NewsPage, RegisterPage, ServicesPage, SitemapPage]

header_links = ["admin_top", "parabank_top", "about", "services", "admin", "home_button", "about_button",
                "contact_button"]
footer_links = ["home", "about", "services", "sitemap", "contact"]

external_header_links = ["products", "locations"]
external_footer_links = ["products", "locations", "forum", "visit"]


@pytest.fixture(params=pages)
def test_page(request):
    return request.param


@pytest.fixture(params=header_links)
def header_link(request):
    return request.param


@pytest.fixture(params=footer_links)
def footer_link(request):
    return request.param


class TestNavigation:

    @staticmethod
    def __validate_page_properties(page):
        """
        There are common validation steps in this suite,
        thus it was unified under this method.
        This method validates:
        - expected and actual page URL
        - expected and actual page Title
        Based on the Page Object definitions
        :param page: Object, any page object
        :return: None
        """
        expected_url, actual_url = page.expected_url, page.get_actual_url()
        assert expected_url in actual_url, "Expected URL: '{}' Actual URL: '{}'".format(expected_url, actual_url)
        expected_title, actual_title = page.expected_title, page.get_actual_title()
        assert expected_title in actual_title, "Expected Title: '{}' Actual Title: '{}'".format(expected_title,
                                                                                                actual_title)

    def test_header_navigation(self, driver, test_page, header_link):
        page = test_page(driver).open()
        page = getattr(page.header, "click_{}".format(header_link))()
        TestNavigation.__validate_page_properties(page)

    def test_footer_navigation(self, driver, test_page, footer_link):
        page = test_page(driver).open()
        page = getattr(page.footer, "click_{}".format(footer_link))()
        TestNavigation.__validate_page_properties(page)
