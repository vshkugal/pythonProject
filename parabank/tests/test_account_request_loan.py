from ...parabank.src.pages.account_services_pages.request_loan_page import LoanRequestPage
from ...parabank.src.pages.exceptions.custom_exceptions import BaseElementException
import pytest

account_link = "request_loan"
loan_data = ["10", "100"]
loan_data_negative = ["100000", "aaa", ""]


@pytest.fixture(scope="function")
def loan_page(driver, user_login) -> LoanRequestPage:
    page = user_login.logged_in_panel.click_link(account_link)
    return page


@pytest.mark.parametrize("data", loan_data,
                         ids=[f"Positive test {i+1} with input '{loan_data[i]}'"
                              for i in range(len(loan_data))]
                         )
def test_request_loan_page(loan_page, data):
    loan_page.logger.logger.info('\n'+loan_page.get_section_title())
    page = loan_page.request_loan(data, 1)
    page.success_form.wait_to_appear()
    assert page.is_processed() and page.is_approved()
    page.print_loan_details()
    page.print_section_info()
    page = page.click_new_account_link()
    page.print_account_details()
    page.print_account_transactions()
    assert page.is_on_correct_page()


@pytest.mark.parametrize("data", loan_data_negative,
                         ids=[f"Negative test {i+1} with input '{loan_data_negative[i]}'"
                              for i in range(len(loan_data_negative))]
                         )
def test_request_loan_page_incorrect(loan_page, data):
    loan_page.logger.logger.info('\n'+loan_page.get_section_title())
    page = loan_page.request_loan(data, 1)
    try:
        page.success_form.wait_to_appear()
        page.print_loan_details()
    except BaseElementException:
        pass
    page.print_section_info()
    assert not page.is_processed() or page.is_processed() and not page.is_approved()


def test_accounts_overview_activity_and_transaction_tables(transaction_details):
    assert transaction_details.is_on_correct_page()
