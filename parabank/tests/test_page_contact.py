from ...parabank.src.pages.main_pages.contact_page import ContactPage
import pytest

contact_data = ["test", "123", "@#$%^"]
contact_data_negative = ""
contact_data_full = ["Name", "E-mail", "Phone", "Message"]


class TestPageContact:

    INITIAL_MESSAGE = "Email support is available by filling out the following form."
    SUCCESS_MESSAGE = ["Thank you {}", "A Customer Care Representative will be contacting you."]

    @pytest.fixture(scope="function")
    def contact_page(self, driver) -> ContactPage:
        try:
            page = ContactPage(driver)
            yield page
        finally:
            page = ContactPage(driver)
            page.open()

    @pytest.mark.parametrize("data", contact_data,
                             ids=[f"Positive test {i+1} with contact info '{contact_data[i]}'"
                                  for i in range(len(contact_data))]
                             )
    def test_contact_page_functionality(self, contact_page, data):
        contact_page.input_contact_information_simplified(data)
        contact_page.send_button.click()
        info = contact_page.get_section_info()
        assert self.SUCCESS_MESSAGE[0].format(data) in info[0], contact_page.print_contact_errors()
        contact_page.print_section_info()
        assert info[1] == self.SUCCESS_MESSAGE[1]

    def test_contact_page_errors(self, contact_page):
        contact_page.print_section_info()
        contact_page.input_contact_information_simplified(contact_data_negative)
        contact_page.send_button.click()
        contact_page.print_contact_errors()
        assert contact_page.get_section_info()[0] == self.INITIAL_MESSAGE

    def test_contact_page_full(self, contact_page):
        contact_page.input_contact_information(*contact_data_full)
        contact_page.send_button.click()
        info = contact_page.get_section_info()
        assert self.SUCCESS_MESSAGE[0].format(contact_data_full[0]) in info[0], contact_page.print_contact_errors()
        contact_page.print_section_info()
        assert info[1] == self.SUCCESS_MESSAGE[1]
