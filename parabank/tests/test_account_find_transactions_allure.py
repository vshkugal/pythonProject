# Test with allure. Please uncomment allure dir line in pytest.ini before running this test.
# This test must be executed after test_account_transfer_funds tests in order to work properly

from ...parabank.src.pages.account_services_pages.find_transactions_page import FindTransactionsPage
from datetime import date
import pytest
import allure

"""
!!! Please run 'test_account_transfer_funds.py' tests before executing this module !!!
"""

account_link = "find_transactions"
find_link = "https://parabank.parasoft.com/parabank/findtrans.htm"
find_name = "ParaBank | Find Transactions"

id_incorrect = ["00000", "aaa"]
date_incorrect = ["01-01-2020", "11-11-1111", str(date.today())]
date_incorrect_format = ["2020_01_01", "01.01.2020", "aaa"]
amount_incorrect = ["1.1", "-11", "0011"]
amount_incorrect_format = ["1_1", "aaa"]
transfer_data = ["10", "0", "-10"]


@allure.step("Find Transactions page fixture is used for this test")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.fixture(scope="function")
def find_page(driver, user_login) -> FindTransactionsPage:
    page = user_login.logged_in_panel.click_link(account_link)
    page.dropdown_account.wait_until_not_empty()
    return page


@allure.step("Fixture that finds last Transaction ID in main User's Account is used for this test")
@pytest.fixture(scope="function")
def transaction_id(user_login) -> str:
    page = user_login.logged_in_panel.click_accounts_overview()
    page = page.click_account_link()
    transaction_id = page.get_transaction_id()
    page.logged_in_panel.click_find_transactions()
    return transaction_id


@allure.step("Fixture that calculates current date and transforms it into required format is used for this test")
@pytest.fixture(scope="module")
def current_date() -> str:
    today = str(date.today())
    today_format = today[5:10] + '-' + today[0:4]
    return today_format


@allure.step("Find transaction by filling input with {value}, pressing button and waiting for result form to appear")
@allure.severity(allure.severity_level.CRITICAL)
def find_transaction(input1, button, form, value, input2=None):
    input1.set_text(value)
    if input2 is not None:
        input2.set_text(value)
    button.click()
    form.wait_to_appear()


@allure.story("Transaction_ID")
@allure.feature("Positive_test")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test with correct Transaction ID ({transaction_id})")
@allure.description("Positive test: Find Transaction by correct Transaction ID")
@allure.link(find_link, name=find_name)
@allure.step("Transaction ID = '{transaction_id}'")
def test_find_transaction_by_correct_transaction_id(find_page, transaction_id):
    find_transaction(find_page.input_by_id, find_page.button_by_id, find_page.success_form, transaction_id)
    assert find_page.is_success()
    assert find_page.get_transaction_id() == transaction_id
    find_page.print_transaction_results()
    page = find_page.click_transaction_link()
    page.print_transaction_details()
    assert page.is_on_correct_page()
    allure.dynamic.description(f"Positive test: Find Transaction by correct Transaction ID = '{transaction_id}'")


@allure.story("Transaction_ID")
@allure.feature("Negative_test")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.title("Test with incorrect Transaction ID = '{data}'")
@allure.description("Negative test: Find Transaction by incorrect Transaction ID")
@allure.link(find_link, name=find_name)
@allure.step("Transaction ID = '{data}'")
@pytest.mark.parametrize("data", id_incorrect,
                         ids=[f"Negative test {i+1} with id '{id_incorrect[i]}'"
                              for i in range(len(id_incorrect))]
                         )
def test_find_transaction_by_incorrect_transaction_id(find_page, data):
    find_transaction(find_page.input_by_id, find_page.button_by_id, find_page.error_form, data)
    assert not find_page.is_success()
    allure.dynamic.description(f"Negative test: Find Transaction by incorrect Transaction ID = '{data}'")


@allure.story("Date")
@allure.feature("Positive_test")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test with Date equal to today's date ({current_date})")
@allure.description("Positive test: Find Transaction by correct Date")
@allure.link(find_link, name=find_name)
@allure.step("Date = '{current_date}'")
def test_find_transaction_by_correct_date(find_page, current_date):
    find_transaction(find_page.input_by_date, find_page.button_by_date, find_page.success_form, current_date)
    assert find_page.is_success()
    find_page.print_transaction_results()
    page = find_page.click_transaction_link()
    assert page.is_on_correct_page()
    allure.dynamic.description(f"Positive test: Find Transaction by correct Date = '{current_date}'")


@allure.story("Date")
@allure.feature("Negative_test")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.title("Test with incorrect Date = '{data}'")
@allure.description("Negative test: Find Transaction by incorrect Date")
@allure.link(find_link, name=find_name)
@allure.step("Date = '{data}'")
@pytest.mark.parametrize("data", date_incorrect,
                         ids=[f"Negative test {i+1} with date '{date_incorrect[i]}'"
                              for i in range(len(date_incorrect))]
                         )
def test_find_transaction_by_incorrect_date(find_page, data):
    find_transaction(find_page.input_by_date, find_page.button_by_date, find_page.success_form, data)
    assert find_page.is_success() and not find_page.transactions_table_line.exists()
    allure.dynamic.description(f"Negative test: Find Transaction by incorrect Date = '{data}'")


@allure.story("Date")
@allure.feature("Negative_test")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.title("Test with incorrect Date format = '{data}'")
@allure.description("Negative test: Find Transaction by incorrect Date format")
@allure.link(find_link, name=find_name)
@allure.step("Date = '{data}'")
@pytest.mark.parametrize("data", date_incorrect_format,
                         ids=[f"Negative test {i+1} with date '{date_incorrect_format[i]}'"
                              for i in range(len(date_incorrect_format))]
                         )
def test_find_transaction_by_incorrect_date_format(find_page, data):
    find_transaction(find_page.input_by_date, find_page.button_by_date, find_page.error_form, data)
    assert not find_page.is_success()
    allure.dynamic.description(f"Negative test: Find Transaction by incorrect Date format = '{data}'")


@allure.story("Date_Range")
@allure.feature("Positive_test")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test with Date Range equal to today's date ({current_date})")
@allure.description("Positive test: Find Transaction by correct Date Range")
@allure.link(find_link, name=find_name)
@allure.step("Date Range is from '{current_date}' to '{current_date}'")
def test_find_transaction_by_correct_dates(find_page, current_date):
    find_transaction(find_page.input_from_date, find_page.button_by_date_range, find_page.success_form, current_date,
                     find_page.input_to_date)
    assert find_page.is_success()
    find_page.print_transaction_results()
    page = find_page.click_transaction_link()
    assert page.is_on_correct_page()
    allure.dynamic.description(f"Positive test: Find Transaction by correct Date Range = '{current_date}'")


@allure.story("Date_Range")
@allure.feature("Negative_test")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.title("Test with incorrect Date Range = '{data}'")
@allure.description("Negative test: Find Transaction by incorrect Date Range")
@allure.link(find_link, name=find_name)
@allure.step("Date Range is from '{data}' to '{data}'")
@pytest.mark.parametrize("data", date_incorrect,
                         ids=[f"Negative test {i+1} with date '{date_incorrect[i]}'"
                              for i in range(len(date_incorrect))]
                         )
def test_find_transaction_by_incorrect_dates(find_page, data):
    find_transaction(find_page.input_from_date, find_page.button_by_date_range, find_page.success_form, data,
                     find_page.input_to_date)
    assert find_page.is_success() and not find_page.transactions_table_line.exists()
    allure.dynamic.description(f"Negative test: Find Transaction by incorrect Date Range = '{data}'")


@allure.story("Date_Range")
@allure.feature("Negative_test")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.title("Test with incorrect Date Range format = '{data}'")
@allure.description("Negative test: Find Transaction by incorrect Date Range format")
@allure.link(find_link, name=find_name)
@allure.step("Date Range is from '{data}' to '{data}'")
@pytest.mark.parametrize("data", date_incorrect_format,
                         ids=[f"Negative test {i+1} with date '{date_incorrect_format[i]}'"
                              for i in range(len(date_incorrect_format))]
                         )
def test_find_transaction_by_incorrect_dates_format(find_page, data):
    find_transaction(find_page.input_from_date, find_page.button_by_date_range, find_page.error_form, data,
                     find_page.input_to_date)
    assert not find_page.is_success()
    allure.dynamic.description(f"Negative test: Find Transaction by incorrect Date Range format = '{data}'")


@allure.story("Amount")
@allure.feature("Positive_test")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Test with Amount = '{data}'")
@allure.description("Positive test: Find Transaction by correct Amount")
@allure.link(find_link, name=find_name)
@allure.step("Amount = '{data}'")
@pytest.mark.parametrize("data", transfer_data,
                         ids=[f"Positive test {i+1} with amount '{transfer_data[i]}'"
                              for i in range(len(transfer_data))]
                         )
def test_find_transaction_by_correct_amount(find_page, data):
    find_transaction(find_page.input_by_amount, find_page.button_by_amount, find_page.success_form, data)
    assert find_page.is_success()
    find_page.print_transaction_results()
    page = find_page.click_transaction_link()
    assert page.is_on_correct_page()
    allure.dynamic.description(f"Positive test: Find Transaction by correct Amount = '{data}'")


@allure.story("Amount")
@allure.feature("Negative_test")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.title("Test with incorrect Amount = '{data}'")
@allure.description("Negative test: Find Transaction by incorrect Amount")
@allure.link(find_link, name=find_name)
@allure.step("Amount = '{data}'")
@pytest.mark.parametrize("data", amount_incorrect,
                         ids=[f"Negative test {i+1} with amount '{amount_incorrect[i]}'"
                              for i in range(len(amount_incorrect))]
                         )
def test_find_transaction_by_incorrect_amount(find_page, data):
    find_transaction(find_page.input_by_amount, find_page.button_by_amount, find_page.success_form, data)
    assert find_page.is_success() and not find_page.transactions_table_line.exists()
    allure.dynamic.description(f"Negative test: Find Transaction by incorrect Amount = '{data}'")


@allure.story("Amount")
@allure.feature("Negative_test")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.title("Test with incorrect Amount format = '{data}'")
@allure.description("Negative test: Find Transaction by incorrect Amount format")
@allure.link(find_link, name=find_name)
@allure.step("Amount = '{data}'")
@pytest.mark.parametrize("data", amount_incorrect_format,
                         ids=[f"Negative test {i+1} with amount '{amount_incorrect_format[i]}'"
                              for i in range(len(amount_incorrect_format))]
                         )
def test_find_transaction_by_incorrect_amount_format(find_page, data):
    find_transaction(find_page.input_by_amount, find_page.button_by_amount, find_page.error_form, data)
    assert not find_page.is_success()
    allure.dynamic.description(f"Negative test: Find Transaction by incorrect Amount format = '{data}'")


@allure.story("Blank")
@allure.feature("Negative_test")
@allure.severity(allure.severity_level.TRIVIAL)
@allure.title("Test with blank inputs")
@allure.description("Negative test: Find Transaction with blank input")
@allure.link(find_link, name=find_name)
@allure.step("All input values are blank")
def test_find_transaction_with_blank_inputs(find_page):
    find_page.button_by_id.click()
    assert find_page.is_on_correct_page() and not find_page.is_success()
    find_page.button_by_date.click()
    assert find_page.is_on_correct_page() and not find_page.is_success()
    find_page.button_by_date_range.click()
    assert find_page.is_on_correct_page() and not find_page.is_success()
    find_page.button_by_amount.click()
    assert find_page.is_on_correct_page() and not find_page.is_success()
    allure.dynamic.title("Test where all inputs are blank")
