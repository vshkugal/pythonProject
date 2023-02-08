account_link = "accounts_overview"


def test_accounts_overview_page(user_login):
    page = user_login.logged_in_panel.click_link(account_link)
    page.print_accounts_overview()
    page = page.click_account_link()
    page.print_account_details()
    assert page.is_on_correct_page()
