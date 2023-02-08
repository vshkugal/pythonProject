from ...parabank.src.pages.main_pages.register_page import RegisterPage
import pytest

user_data = {"1": "User1", "2": "aaa", "3": "test1", "4": "@@@"}
# user_data = {"1": "User2", "2": "bbb", "3": "test2", "4": "###"}
# user_data = {"1": "User3", "2": "ccc", "3": "test3", "4": "$$$"}
user_data_negative = {"1": "", "2": user_data['1'], "3": user_data['2']}
user_data_full = ["first_name1", "last_name1", "address1", "city", "state", "zip_code", "phone", "ssn1",
                  "username1", "password", "password"]


@pytest.fixture(scope="function")
def register_page(driver) -> RegisterPage:
    page = RegisterPage(driver)
    return page


def test_initial_state(register_page):
    assert register_page.is_not_registered()


@pytest.mark.parametrize("user",
                         [i for i in user_data.values()],
                         ids=[f"Positive test {i[1]} with username '{i[0]}'"
                              for i in zip(user_data.values(), user_data.keys())]
                         )
def test_new_customer_registration(register_page, user):
    register_page.register_user_simplified(user)
    assert register_page.is_registered(), register_page.print_registration_errors()


@pytest.mark.parametrize("user",
                         [i for i in user_data_negative.values()],
                         ids=[f"Negative test {i[1]} with username '{i[0]}'"
                              for i in zip(user_data_negative.values(), user_data_negative.keys())]
                         )
def test_incorrect_customer_registration(register_page, user):
    register_page.register_user_simplified(user)
    assert register_page.is_not_registered(), "User '{}' was miraculously registered".format(user)


def test_new_customer_registration_full(register_page):
    register_page.register_user(user_data_full)
    assert register_page.is_registered(), register_page.print_registration_errors()
