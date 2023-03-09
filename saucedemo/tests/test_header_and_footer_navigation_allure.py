from ..src.pages.components.page_constants import *
import pytest
import allure

header_links = ["cart", "inventory", "logout"]
external_header_links = {"1": {"click": "about", "link": SAUCELABS_MAIN}}
external_footer_links = {"1": {"click": "twitter", "link": TWITTER_LINK},
                         "2": {"click": "facebook", "link": FACEBOOK_LINK},
                         "3": {"click": "linkedin", "link": LINKEDIN_LINK}}


class TestBasicNavigation:

    @allure.feature("Menu Navigation Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Header Menu Navigation Test: {header_link}")
    @allure.description("Positive test: Header Menu Navigation")
    @pytest.mark.parametrize("header_link", header_links,
                             ids=[f"Test {i+1} with menu link '{header_links[i]}'"
                                  for i in range(len(header_links))]
                             )
    def test_header_navigation(self, user_login, header_link):
        with allure.step(f"Click header menu link: '{header_link}'"):
            page = user_login.header.click_link(header_link)
        with allure.step("Assert transition success"):
            assert page.is_on_correct_page()

    @allure.feature("Menu Navigation Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Header Menu Navigation Test: {click}")
    @allure.description("Positive test: Header Menu Navigation to External Link")
    @pytest.mark.parametrize("click, link",
                             [i.values() for i in external_header_links.values()],
                             ids=[f"Test {i[1]} | Click external menu link: '{i[0]['click']}'"
                                  for i in zip(external_header_links.values(), external_header_links.keys())]
                             )
    def test_header_external_navigation(self, user_login, click, link):
        with allure.step(f"Click header menu external link: '{click}'"):
            page = user_login.header.click_link(click)
        with allure.step("Assert transition success"):
            assert page.get_actual_url() == link, f"Expected URL: '{link}' Actual URL: '{page.get_actual_url()}'"

    @allure.feature("Menu Navigation Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Footer Menu Navigation Test: {click}")
    @allure.description("Positive test: Footer Menu Navigation to External Link")
    @pytest.mark.parametrize("click, link",
                             [i.values() for i in external_footer_links.values()],
                             ids=[f"Test {i[1]} | Click external link: '{i[0]['click']}'"
                                  for i in zip(external_footer_links.values(), external_footer_links.keys())]
                             )
    def test_footer_external_navigation(self, driver, user_login, click, link):
        with allure.step(f"Click footer menu external link: '{click}'"):
            page = user_login.footer.click_link(click)
        with allure.step("Switch to the new tab"):
            driver.switch_to.window(driver.window_handles[1])
        with allure.step("Assert transition success"):
            assert link in page.get_actual_url(), f"Expected URL: '{link}' Actual URL: '{page.get_actual_url()}'"
        with allure.step("Close the new tab"):
            driver.close()
        with allure.step("Switch to the main tab"):
            driver.switch_to.window(driver.window_handles[0])
