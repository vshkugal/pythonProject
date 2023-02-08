# This test must be executed after test_user_registration tests in order to work properly

from ...parabank.src.pages.main_pages.lookup_page import LookupPage
from ...parabank.tests.test_user_registration import user_data
import pytest

user_data_negative = {"1": "@#$%^&*", "2": "-new-", "3": "dhfjgkyuhd"}
user_blank = ""
user_data_full = ["first_name1", "last_name1", "address1", "city", "state", "zip_code", "ssn1"]


@pytest.fixture(scope="function")
def lookup_page(driver) -> LookupPage:
    page = LookupPage(driver)
    return page


@pytest.mark.parametrize("user",
                         [i for i in user_data.values()],
                         ids=[f"Positive test {i[1]} with user '{i[0]}'"
                              for i in zip(user_data.values(), user_data.keys())]
                         )
def test_registered_customer_lookup(lookup_page, user):
    lookup_page.lookup_user_simplified(user)
    lookup_page.print_section_info()
    assert lookup_page.is_found(), "User '{}' was not found".format(user)


@pytest.mark.parametrize("user",
                         [i for i in user_data_negative.values()],
                         ids=[f"Negative test {i[1]} with user '{i[0]}'"
                              for i in zip(user_data_negative.values(), user_data_negative.keys())]
                         )
def test_unregistered_customer_lookup(lookup_page, user):
    lookup_page.lookup_user_simplified(user)
    lookup_page.print_section_info()
    assert lookup_page.is_not_found(), "User '{}' was found".format(user)


def test_blank_customer_lookup(lookup_page):
    lookup_page.lookup_user_simplified(user_blank)
    lookup_page.print_section_info()
    assert lookup_page.get_section_title() == "Customer Lookup" and not lookup_page.is_not_found(), "Blank user found"


def test_registered_customer_lookup_full(lookup_page):
    lookup_page.lookup_user(user_data_full)
    lookup_page.print_section_info()
    assert lookup_page.is_found(), "User '{}' was not found".format(user_data_full[0])
