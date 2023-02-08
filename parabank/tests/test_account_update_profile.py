from ...parabank.src.pages.account_services_pages.update_profile_page import UpdateProfilePage
import pytest

account_link = "update_contact_info"
update_data = ["abc", "123", "0", "-e-"]
update_data_negative = ""
update_data_full = ["first_name", "last_name", "address", "city", "state", "zip_code", "phone"]


@pytest.fixture(scope="function")
def update_page(driver, user_login) -> UpdateProfilePage:
    page = user_login.logged_in_panel.click_link(account_link)
    return page


@pytest.mark.parametrize("data", update_data,
                         ids=[f"Positive test {i+1} with input '{update_data[i]}'"
                              for i in range(len(update_data))]
                         )
def test_update_profile_page(update_page, data):
    update_page.logger.logger.info('\n'+update_page.get_section_title())
    update_page.update_profile_simplified(data)
    assert update_page.is_updated(), update_page.print_update_profile_errors()
    update_page.print_section_info()


def test_update_profile_page_negative(update_page):
    update_page.logger.logger.info('\n'+update_page.get_section_title())
    update_page.update_profile_simplified(update_data_negative)
    update_page.print_update_profile_errors()
    assert not update_page.is_updated()


def test_update_profile_page_full(update_page):
    update_page.update_profile(update_data_full)
    assert update_page.is_updated(), update_page.print_update_profile_errors()
