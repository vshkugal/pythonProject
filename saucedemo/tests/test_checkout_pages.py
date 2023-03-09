from ..src.pages.components.page_constants import *

test_data = "test_data"
ERROR_MESSAGE_1 = "Error: First Name is required"
ERROR_MESSAGE_2 = "Error: Last Name is required"
ERROR_MESSAGE_3 = "Error: Postal Code is required"
CHECKOUT_STEP_1 = "CHECKOUT: YOUR INFORMATION"
CHECKOUT_STEP_2 = "CHECKOUT: OVERVIEW"
CHECKOUT_STEP_3 = "CHECKOUT: COMPLETE!"


class TestCheckoutPages:

    def test_checkout_step_one_page_title(self, checkout_page1):
        title = checkout_page1.header.page_section_title.get_text()
        checkout_page1.logger.logger.info("")
        checkout_page1.logger.logger.info(title)
        assert title.upper() == CHECKOUT_STEP_1

    def test_checkout_step_one_cancel_button(self, checkout_page1):
        page = checkout_page1.click_cancel_button()
        assert page.is_on_correct_page()
        page = page.click_checkout_button()
        assert page.is_on_correct_page()

    def test_checkout_error_message_1(self, checkout_page1):
        checkout_page1.continue_button.click()
        message = checkout_page1.get_error_message()
        assert message == ERROR_MESSAGE_1
        checkout_page1.error_close_button.click()

    def test_checkout_error_message_2(self, checkout_page1):
        checkout_page1.first_name_input.set_text(test_data)
        checkout_page1.continue_button.click()
        message = checkout_page1.get_error_message()
        assert message == ERROR_MESSAGE_2
        checkout_page1.error_close_button.click()

    def test_checkout_error_message_3(self, checkout_page1):
        checkout_page1.first_name_input.set_text(test_data)
        checkout_page1.last_name_input.set_text(test_data)
        checkout_page1.continue_button.click()
        message = checkout_page1.get_error_message()
        assert message == ERROR_MESSAGE_3
        checkout_page1.error_close_button.click()

    def test_checkout_step_two_page_title(self, checkout_page2):
        title = checkout_page2.header.page_section_title.get_text()
        checkout_page2.logger.logger.info("")
        checkout_page2.logger.logger.info(title)
        assert title.upper() == CHECKOUT_STEP_2

    def test_checkout_step_two_details(self, checkout_page2):
        info = checkout_page2.summary_info.get_all_elements()
        for line in info:
            checkout_page2.logger.logger.info(line.text)

    def test_checkout_step_two_cancel_button(self, checkout_page2):
        page = checkout_page2.click_cancel_button()
        assert page.is_on_correct_page()
        page = page.header.click_cart()
        page = page.click_checkout_button()
        page.first_name_input.set_text(test_data)
        page.last_name_input.set_text(test_data)
        page.postal_code_input.set_text(test_data)
        page = page.click_continue_button()
        assert page.is_on_correct_page()

    def test_checkout_step_three_page_title(self, checkout_page2):
        page = checkout_page2.click_finish_button()
        title = page.header.page_section_title.get_text()
        page.logger.logger.info("")
        page.logger.logger.info(title)
        page.logger.logger.info(page.info_label.get_text())
        page.logger.logger.info(page.info_text.get_text())
        assert title.upper() == CHECKOUT_STEP_3

    def test_checkout_step_three_back_home_button(self, checkout_page3):
        page = checkout_page3.click_back_home_button()
        assert page.is_on_correct_page()
        page.item_add_to_cart_button.click()

    def test_checkout_item_details(self, driver, checkout_page2):
        page = checkout_page2
        page.logger.logger.info("\nCheckout items:")
        quantity = page.item_quantity.get_text()
        page.logger.logger.info(f"Item quantity: '{quantity}'")
        label = page.item_name.get_text()
        page.logger.logger.info(f"Item label: '{label}'")
        description = page.item_description.get_text()
        page.logger.logger.info(f"Item description: '{description}'")
        price = page.item_price.get_text()
        page.logger.logger.info(f"Item price: '{price}'")
        link_id = page.item_link.get_attribute('id')
        mo = ID_REGEX.search(link_id)
        item_id = mo.group()
        page.logger.logger.info(f"Item id: '{item_id}'")
        page.item_link.click()
        from ..src.pages.all_pages.item_page import ItemPage
        page = ItemPage(driver, item_id)
        assert page.is_correct_item_page(item_id, label, description, price)
