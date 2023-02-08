from random import randint
from ...parabank.src.pages.account_services_pages.open_new_account_page import OpenNewAccountPage
import pytest

account_link = "open_new_account"
account_type = ["CHECKING", "SAVINGS"]


@pytest.fixture(scope="function")
def open_page(driver, user_login) -> OpenNewAccountPage:
    page = user_login.logged_in_panel.click_link(account_link)
    return page


def test_dropdowns_descriptions(open_page):
    for dropdown in open_page.dropdowns:
        open_page.logger.logger.info("\nDropdown '{}':".format(dropdown.dropdown_id))
        dropdown.wait_until_not_empty()
        for option in dropdown.get_dropdown_options():
            open_page.logger.logger.info(option)


@pytest.mark.parametrize("data", account_type,
                         ids=[f"Test {i+1} with account type '{account_type[i]}'"
                              for i in range(len(account_type))]
                         )
def test_open_new_account_page(open_page, data):
    open_page.logger.logger.info('\n'+open_page.get_section_title())
    open_page.dropdown_from_account.wait_until_not_empty()
    open_page.dropdown_type.select(data)
    acc = open_page.dropdown_from_account.get_dropdown_options()
    rand = randint(0, len(acc)-1)
    open_page.dropdown_from_account.select(acc[rand])
    page = open_page.open_new_account()
    assert page.is_success(), page.print_open_new_account_form_error()
    page.print_section_info()
    page = page.click_account_link()
    page.print_account_details()
    page.print_account_transactions()
    assert page.is_on_correct_page()
    page = page.click_transaction_link()
    page.print_transaction_details()
    assert page.is_on_correct_page()
