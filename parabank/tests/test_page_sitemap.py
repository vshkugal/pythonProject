from ...parabank.src.pages.main_pages.sitemap_page import SitemapPage
from ...parabank.src.pages.components.page_constants import *
import pytest

sitemap_links = ["about", "services", "admin", "open_new_account", "accounts_overview", "transfer_funds", "bill_pay",
                 "find_transactions", "update_contact_info", "request_loan", "log_out"]
external_sitemap_links = {"1": {"click": "products", "link": PARASOFT_PRODUCTS},
                          "2": {"click": "locations", "link": PARASOFT_LOCATIONS}}


class TestPageSitemap:

    @pytest.fixture(scope="function")
    def sitemap_page(self, driver) -> SitemapPage:
        page = SitemapPage(driver)
        return page

    @pytest.mark.parametrize("sitemap_link", sitemap_links,
                             ids=[f"Test {i+1} with sitemap link '{sitemap_links[i]}'"
                                  for i in range(len(sitemap_links))]
                             )
    def test_sitemap_navigation(self, user_login, sitemap_page, sitemap_link):
        page = user_login
        page = sitemap_page.click_link(sitemap_link)
        assert page.is_on_correct_page()

    @pytest.mark.parametrize("click, link",
                             [i.values() for i in external_sitemap_links.values()],
                             ids=[f"Test {i[1]} | Click external link: '{i[0]['click']}'"
                                  for i in zip(external_sitemap_links.values(), external_sitemap_links.keys())]
                             )
    def test_sitemap_external_navigation(self, sitemap_page, click, link):
        page = sitemap_page.click_link(click)
        assert page.get_actual_url() == link, "Expected URL: '{}' Actual URL: '{}'".format(link, page.get_actual_url())
