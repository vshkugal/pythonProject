from ...parabank.src.pages.account_services_pages.bill_pay_page import BillPayPage
import pytest

account_link = "bill_pay"
bill_data = [["name", "street", "city", "state", "zip_code", "phone", "11111", "11111", "10"],
             ["name", "street", "city", "state", "zip_code", "phone", "222", "222", "0"],
             ["name", "street", "city", "state", "zip_code", "phone", "0", "0", "10000"],
             ["name", "street", "city", "state", "zip_code", "phone", "-5", "-5", "-10000"]]
bill_data_negative = [["name", "street", "city", "state", "", "", "11111", "22222", "5"],
                      ["name", "street", "city", "state", "zip_code", "phone", "a", "a", "a"],
                      ["", "", "", "", "", "", "", "", ""]]


@pytest.fixture(scope="function")
def bill_page(driver, user_login) -> BillPayPage:
    page = user_login.logged_in_panel.click_link(account_link)
    return page


@pytest.mark.parametrize("data", bill_data,
                         ids=[f"Positive test {i+1} with input '{bill_data[i]}'"
                              for i in range(len(bill_data))]
                         )
def test_bill_pay_page_correct_input(bill_page, data):
    bill_page.input_payee_information_full(*data)
    bill_page.success_form.wait_until_visible()
    bill_page.print_section_info()
    assert bill_page.is_success()


@pytest.mark.parametrize("data", bill_data_negative,
                         ids=[f"Negative test {i+1} with input '{bill_data_negative[i]}'"
                              for i in range(len(bill_data_negative))]
                         )
def test_bill_pay_page_incorrect_input(bill_page, data):
    bill_page.input_payee_information_full(*data)
    bill_page.print_bill_pay_form_errors()
    bill_page.print_section_info()
    assert not bill_page.is_success()


def test_accounts_overview_activity_and_transaction_tables(transaction_details):
    assert transaction_details.is_on_correct_page()
