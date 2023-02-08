# This test must be executed after test_account_transfer_funds tests in order to work properly
from ...parabank.src.base_element import BaseElement
from ...parabank.src.pages.account_services_pages.find_transactions_page import FindTransactionsPage
# from web.parabank.tests.test_account_transfer_funds import transfer_data
from datetime import date
from typing import List, Union
import pytest

"""
!!! Please run 'test_account_transfer_funds.py' tests before executing this module !!!
"""

account_link = "find_transactions"

id_incorrect = ["00000", "aaa"]
date_incorrect = ["01-01-2020", "11-11-1111", str(date.today())]
date_incorrect_format = ["2020_01_01", "01.01.2020", "aaa"]
amount_incorrect = ["1.1", "-11", "0011"]
amount_incorrect_format = ["1_1", "aaa"]
transfer_data = ["10", "0", "-10"]


@pytest.fixture(scope="function")
def find_page(driver, user_login) -> FindTransactionsPage:
    page = user_login.logged_in_panel.click_link(account_link)
    page.dropdown_account.wait_until_not_empty()
    return page


@pytest.fixture(scope="function")
def transaction_id(user_login) -> str:
    page = user_login.logged_in_panel.click_accounts_overview()
    page = page.click_account_link()
    transaction_id = page.get_transaction_id()
    page.logged_in_panel.click_find_transactions()
    return transaction_id


@pytest.fixture(scope="module")
def current_date() -> str:
    today = str(date.today())
    today_format = today[5:10] + '-' + today[0:4]
    return today_format


def submit_form_with_params(fields: Union[BaseElement, List[BaseElement]], button: BaseElement, form: BaseElement,
                            values: Union[str, List[str]]):
    if isinstance(fields, BaseElement) and isinstance(values, str):
        fields.set_text(values)
    elif isinstance(fields, List) and isinstance(values, str):
        for field in fields:
            field.set_text(values)
    elif isinstance(fields, List) and isinstance(values, List):
        for field, value in zip(fields, values):
            field.set_text(value)
    else:
        raise Exception("You can't assign the list of values to the single input field")
    button.click()
    form.wait_to_appear()


def test_find_transaction_by_correct_transaction_id(find_page, transaction_id):
    submit_form_with_params(find_page.input_by_id, find_page.button_by_id, find_page.success_form, transaction_id)
    assert find_page.is_success()
    assert find_page.get_transaction_id() == transaction_id
    find_page.print_transaction_results()
    page = find_page.click_transaction_link()
    page.print_transaction_details()
    assert page.is_on_correct_page()


@pytest.mark.parametrize("data", id_incorrect,
                         ids=[f"Negative test {i+1} with id '{id_incorrect[i]}'"
                              for i in range(len(id_incorrect))]
                         )
def test_find_transaction_by_incorrect_transaction_id(find_page, data):
    submit_form_with_params(find_page.input_by_id, find_page.button_by_id, find_page.error_form, data)
    assert not find_page.is_success()


def test_find_transaction_by_correct_date(find_page, current_date):
    submit_form_with_params(find_page.input_by_date, find_page.button_by_date, find_page.success_form, current_date)
    assert find_page.is_success()
    find_page.print_transaction_results()
    page = find_page.click_transaction_link()
    assert page.is_on_correct_page()


@pytest.mark.parametrize("data", date_incorrect,
                         ids=[f"Negative test {i+1} with date '{date_incorrect[i]}'"
                              for i in range(len(date_incorrect))]
                         )
def test_find_transaction_by_incorrect_date(find_page, data):
    submit_form_with_params(find_page.input_by_date, find_page.button_by_date, find_page.success_form, data)
    assert find_page.is_success() and not find_page.transactions_table_line.exists()


@pytest.mark.parametrize("data", date_incorrect_format,
                         ids=[f"Negative test {i+1} with date '{date_incorrect_format[i]}'"
                              for i in range(len(date_incorrect_format))]
                         )
def test_find_transaction_by_incorrect_date_format(find_page, data):
    submit_form_with_params(find_page.input_by_date, find_page.button_by_date, find_page.error_form, data)
    assert not find_page.is_success()


def test_find_transaction_by_correct_dates(find_page, current_date):
    submit_form_with_params([find_page.input_from_date, find_page.input_to_date], find_page.button_by_date_range,
                            find_page.success_form, current_date)
    assert find_page.is_success()
    find_page.print_transaction_results()
    page = find_page.click_transaction_link()
    assert page.is_on_correct_page()


@pytest.mark.parametrize("data", date_incorrect,
                         ids=[f"Negative test {i+1} with date '{date_incorrect[i]}'"
                              for i in range(len(date_incorrect))]
                         )
def test_find_transaction_by_incorrect_dates(find_page, data):
    submit_form_with_params([find_page.input_from_date, find_page.input_to_date], find_page.button_by_date_range,
                            find_page.success_form, data)
    assert find_page.is_success() and not find_page.transactions_table_line.exists()


@pytest.mark.parametrize("data", date_incorrect_format,
                         ids=[f"Negative test {i+1} with date '{date_incorrect_format[i]}'"
                              for i in range(len(date_incorrect_format))]
                         )
def test_find_transaction_by_incorrect_dates_format(find_page, data):
    submit_form_with_params([find_page.input_from_date, find_page.input_to_date], find_page.button_by_date_range,
                            find_page.error_form, data)
    assert not find_page.is_success()


@pytest.mark.parametrize("data", transfer_data,
                         ids=[f"Positive test {i+1} with amount '{transfer_data[i]}'"
                              for i in range(len(transfer_data))]
                         )
def test_find_transaction_by_correct_amount(find_page, data):
    submit_form_with_params(find_page.input_by_amount, find_page.button_by_amount, find_page.success_form, data)
    assert find_page.is_success()
    find_page.print_transaction_results()
    page = find_page.click_transaction_link()
    assert page.is_on_correct_page()


@pytest.mark.parametrize("data", amount_incorrect,
                         ids=[f"Negative test {i+1} with amount '{amount_incorrect[i]}'"
                              for i in range(len(amount_incorrect))]
                         )
def test_find_transaction_by_incorrect_amount(find_page, data):
    submit_form_with_params(find_page.input_by_amount, find_page.button_by_amount, find_page.success_form, data)
    assert find_page.is_success() and not find_page.transactions_table_line.exists()


@pytest.mark.parametrize("data", amount_incorrect_format,
                         ids=[f"Negative test {i+1} with amount '{amount_incorrect_format[i]}'"
                              for i in range(len(amount_incorrect_format))]
                         )
def test_find_transaction_by_incorrect_amount_format(find_page, data):
    submit_form_with_params(find_page.input_by_amount, find_page.button_by_amount, find_page.error_form, data)
    assert not find_page.is_success()


def test_find_transaction_with_blank_inputs(find_page):
    find_page.button_by_id.click()
    assert find_page.is_on_correct_page() and not find_page.is_success()
    find_page.button_by_date.click()
    assert find_page.is_on_correct_page() and not find_page.is_success()
    find_page.button_by_date_range.click()
    assert find_page.is_on_correct_page() and not find_page.is_success()
    find_page.button_by_amount.click()
    assert find_page.is_on_correct_page() and not find_page.is_success()
