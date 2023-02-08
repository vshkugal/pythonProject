from ...parabank.src.pages.main_pages.about_page import AboutPage
from ...parabank.src.pages.main_pages.admin_page import AdminPage
from ...parabank.src.pages.main_pages.contact_page import ContactPage
from ...parabank.src.pages.main_pages.home_page import HomePage
from ...parabank.src.pages.main_pages.lookup_page import LookupPage
from ...parabank.src.pages.main_pages.news_page import NewsPage
from ...parabank.src.pages.main_pages.register_page import RegisterPage
from ...parabank.src.pages.main_pages.services_page import ServicesPage
from ...parabank.src.pages.main_pages.sitemap_page import SitemapPage
import pytest

pages = [AboutPage, AdminPage, ContactPage, HomePage, LookupPage, NewsPage, RegisterPage, ServicesPage, SitemapPage]


@pytest.fixture(params=pages)
def test_page(request):
    return request.param


def test_page_url(driver, test_page):
    page = test_page(driver)
    expected_url, actual_url = page.expected_url, page.get_actual_url()
    assert expected_url == actual_url, "Expected URL: '{}' Actual URL: '{}'".format(expected_url, actual_url)


def test_page_title(driver, test_page):
    page = test_page(driver)
    expected_title, actual_title = page.expected_title, page.get_actual_title()
    assert expected_title == actual_title, "Expected Title: '{}' Actual Title: '{}'".format(expected_title,
                                                                                            actual_title)


# Combined test function in order to avoid Service Unavailable error
# due to too many connections to the site in short time
def test_page_url_and_title(driver, test_page):
    page = test_page(driver)
    assert page.is_on_correct_page()
