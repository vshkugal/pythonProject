from ...parabank.src.pages.account_services_pages.transfer_funds_page import TransferFundsPage
import pytest

account_link = "transfer_funds"
transfer_data = ["10", "100", "10000", "0", "-10"]
transfer_data_negative = ["aaa", ""]


@pytest.fixture(scope="function")
def transfer_page(driver, user_login) -> TransferFundsPage:
    page = user_login.logged_in_panel.click_link(account_link)
    return page


@pytest.mark.parametrize("data", transfer_data,
                         ids=[f"Positive test {i+1} with input '{transfer_data[i]}'"
                              for i in range(len(transfer_data))]
                         )
def test_transfer_funds_page(transfer_page, data):
    transfer_page.logger.logger.info('\n'+transfer_page.get_section_title())
    page = transfer_page.transfer_funds(data)
    assert page.is_success()
    page.print_section_info()


@pytest.mark.parametrize("data", transfer_data_negative,
                         ids=[f"Negative test {i+1} with input '{transfer_data_negative[i]}'"
                              for i in range(len(transfer_data_negative))]
                         )
def test_transfer_funds_page_incorrect(transfer_page, data):
    transfer_page.logger.logger.info('\n'+transfer_page.get_section_title())
    page = transfer_page.transfer_funds(data)
    page.print_transfer_funds_form_error()
    assert not page.is_success()


def test_accounts_overview_activity_and_transaction_tables(transaction_details):
    assert transaction_details.is_on_correct_page()
