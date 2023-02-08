from ...parabank.src.pages.account_services_pages.account_activity_page import AccountActivityPage
from datetime import date
import pytest

account_link = "accounts_overview"
dropdown_names = ["Month", "Transaction Type"]
dropdown_test_values = [["All", "January", "February", "March", "April", "May", "June", "July", "August", "September",
                         "October", "November", "December"], ["All", "Credit", "Debit"]]


@pytest.fixture(scope="module")
def activity_page(driver, user_login) -> AccountActivityPage:
    page = user_login.logged_in_panel.click_link(account_link)
    account_id = page.get_account_id()
    page = AccountActivityPage(driver, account_id)
    return page


def test_account_activity_page_basics(activity_page):
    activity_page.print_account_details()
    activity_page.print_account_transactions()
    assert activity_page.is_on_correct_page()


def test_dropdowns_descriptions(activity_page):
    for dropdown in activity_page.dropdowns:
        activity_page.logger.logger.info("\nDropdown '{}':".format(dropdown.dropdown_id))
        for option in dropdown.get_dropdown_options():
            activity_page.logger.logger.info(option)


@pytest.mark.parametrize("dropdown_type, value",
                         [(dropdown_type, value) for dropdown_type in range(len(dropdown_test_values))
                          for value in dropdown_test_values[dropdown_type]],
                         ids=[f"Dropdown '{dropdown_names[dropdown_type]}' with option '{value}'"
                              for dropdown_type in range(len(dropdown_test_values))
                              for value in dropdown_test_values[dropdown_type]]
                         )
def test_dropdowns_selections(activity_page, dropdown_type, value):
    activity_page.logger.logger.info("\nDropdown: '{}', value to select: '{}'"
                                     .format(activity_page.dropdowns[dropdown_type].dropdown_id, value))
    activity_page.dropdowns[dropdown_type].select(value)
    activity_page.go_button.click()
    activity_page.logger.logger.info("Selected value: '{}'"
                                     .format(activity_page.dropdowns[dropdown_type].get_attribute("value")))
    if value != dropdown_test_values[0][date.today().month] and value != 'All':
        assert activity_page.no_transactions(), \
            f"There are transactions for '{dropdown_names[dropdown_type]}' = '{value}'"
