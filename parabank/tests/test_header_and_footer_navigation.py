from ...parabank.src.pages.main_pages.about_page import AboutPage
from ...parabank.src.pages.components.page_constants import *
import pytest

pages = [AboutPage]
# pages = [AboutPage, AdminPage, ContactPage, HomePage, LookupPage, NewsPage, RegisterPage, ServicesPage, SitemapPage]

header_links = ["admin_top", "parabank_top", "about", "services", "admin", "home_button", "about_button",
                "contact_button"]
footer_links = ["home", "about", "services", "sitemap", "contact"]

external_header_links = {"1": {"click": "products", "link": PARASOFT_PRODUCTS},
                         "2": {"click": "locations", "link": PARASOFT_LOCATIONS}}

external_footer_links = {"1": {"click": "products", "link": PARASOFT_PRODUCTS},
                         "2": {"click": "locations", "link": PARASOFT_LOCATIONS},
                         "3": {"click": "forum", "link": PARASOFT_FORUM},
                         "4": {"click": "visit", "link": PARASOFT_MAIN}}


@pytest.fixture(params=pages)
def test_page(request):
    return request.param


@pytest.mark.parametrize("header_link", header_links,
                         ids=[f"Test {i+1} with header link '{header_links[i]}'"
                              for i in range(len(header_links))]
                         )
def test_header_navigation(driver, test_page, header_link):
    page = test_page(driver)
    page = page.header.click_link(header_link)
    assert page.is_on_correct_page()


@pytest.mark.parametrize("footer_link", footer_links,
                         ids=[f"Test {i+1} with footer link '{footer_links[i]}'"
                              for i in range(len(footer_links))]
                         )
def test_footer_navigation(driver, test_page, footer_link):
    page = test_page(driver)
    page = page.footer.click_link(footer_link)
    assert page.is_on_correct_page()


@pytest.mark.parametrize("click, link",
                         [i.values() for i in external_header_links.values()],
                         ids=[f"Test {i[1]} | Click external link: '{i[0]['click']}'"
                              for i in zip(external_header_links.values(), external_header_links.keys())]
                         )
def test_header_external_navigation(driver, test_page, click, link):
    page = test_page(driver)
    page = page.header.click_link(click)
    assert page.get_actual_url() == link, "Expected URL: '{}' Actual URL: '{}'".format(link, page.get_actual_url())


@pytest.mark.parametrize("click, link",
                         [i.values() for i in external_footer_links.values()],
                         ids=[f"Test {i[1]} | Click external link: '{i[0]['click']}'"
                              for i in zip(external_footer_links.values(), external_footer_links.keys())]
                         )
def test_footer_external_navigation(driver, test_page, click, link):
    page = test_page(driver)
    page = page.footer.click_link(click)
    assert page.get_actual_url() == link, "Expected URL: '{}' Actual URL: '{}'".format(link, page.get_actual_url())
