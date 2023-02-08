from ...parabank.tests.conftest import test_user
import pytest

logged_in_links = ["open_new_account", "accounts_overview", "transfer_funds", "bill_pay", "find_transactions",
                   "update_contact_info", "request_loan"]


@pytest.mark.parametrize("logged_in_link", logged_in_links,
                         ids=[f"Test {i+1} with Account Service link '{logged_in_links[i]}'"
                              for i in range(len(logged_in_links))]
                         )
def test_logged_in_panel_navigation(user_login, logged_in_link):
    page = user_login.logged_in_panel.click_link(logged_in_link)
    assert page.is_on_correct_page()


def test_log_out(user_login):
    page = user_login.logged_in_panel.click_log_out()
    assert page.is_logged_out(), "User {} was not logged out".format(test_user)
