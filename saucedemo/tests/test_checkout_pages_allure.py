from ..src.pages.components.page_constants import *
import allure

test_data = "test_data"
ERROR_MESSAGE_1 = "Error: First Name is required"
ERROR_MESSAGE_2 = "Error: Last Name is required"
ERROR_MESSAGE_3 = "Error: Postal Code is required"
CHECKOUT_STEP_1 = "CHECKOUT: YOUR INFORMATION"
CHECKOUT_STEP_2 = "CHECKOUT: OVERVIEW"
CHECKOUT_STEP_3 = "CHECKOUT: COMPLETE!"


class TestCheckoutPages:

    @allure.feature("Checkout Page Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Checkout Step One Page Title Test")
    @allure.description("Positive test: Checkout Step One Page Title")
    def test_checkout_step_one_page_title(self, checkout_page1):
        with allure.step("Get page title"):
            title = checkout_page1.header.page_section_title.get_text()
            checkout_page1.logger.logger.info("")
            checkout_page1.logger.logger.info(title)
        with allure.step("Verify page title"):
            assert title.upper() == CHECKOUT_STEP_1

    @allure.feature("Checkout Page Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Checkout Step One Cancel Button Test")
    @allure.description("Positive test: Checkout Step One Cancel Button")
    def test_checkout_step_one_cancel_button(self, checkout_page1):
        with allure.step("Click cancel button"):
            page = checkout_page1.click_cancel_button()
        with allure.step("Verify navigation"):
            assert page.is_on_correct_page()
        with allure.step("Click checkout button"):
            page = page.click_checkout_button()
            assert page.is_on_correct_page()

    @allure.feature("Checkout Page Test")
    @allure.story("Negative Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Checkout Step One Fill The Form Test: Blank First Name")
    @allure.description("Negative test: Blank First Name")
    def test_checkout_error_message_1(self, checkout_page1):
        with allure.step("Leave all fields blank and click continue button"):
            checkout_page1.continue_button.click()
        with allure.step("Check error message"):
            message = checkout_page1.get_error_message()
            assert message == ERROR_MESSAGE_1
        with allure.step("Close error message"):
            checkout_page1.error_close_button.click()

    @allure.feature("Checkout Page Test")
    @allure.story("Negative Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Checkout Step One Fill The Form Test: Blank Last Name")
    @allure.description("Negative test: Blank Last Name")
    def test_checkout_error_message_2(self, checkout_page1):
        with allure.step("Input first name and leave other fields blank"):
            checkout_page1.first_name_input.set_text(test_data)
        with allure.step("Click continue button"):
            checkout_page1.continue_button.click()
        with allure.step("Check error message"):
            message = checkout_page1.get_error_message()
            assert message == ERROR_MESSAGE_2
        with allure.step("Close error message"):
            checkout_page1.error_close_button.click()

    @allure.feature("Checkout Page Test")
    @allure.story("Negative Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Checkout Step One Fill The Form Test: Blank Postal Code")
    @allure.description("Negative test: Blank Postal Code")
    def test_checkout_error_message_3(self, checkout_page1):
        with allure.step("Input first and last names and leave postal code blank"):
            checkout_page1.first_name_input.set_text(test_data)
            checkout_page1.last_name_input.set_text(test_data)
        with allure.step("Click continue button"):
            checkout_page1.continue_button.click()
        with allure.step("Check error message"):
            message = checkout_page1.get_error_message()
            assert message == ERROR_MESSAGE_3
        with allure.step("Close error message"):
            checkout_page1.error_close_button.click()

    @allure.feature("Checkout Page Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Checkout Step Two Page Title Test")
    @allure.description("Positive test: Checkout Step Two Page Title")
    def test_checkout_step_two_page_title(self, checkout_page2):
        with allure.step("Get page title"):
            title = checkout_page2.header.page_section_title.get_text()
            checkout_page2.logger.logger.info("")
            checkout_page2.logger.logger.info(title)
        with allure.step("Verify page title"):
            assert title.upper() == CHECKOUT_STEP_2

    @allure.feature("Checkout Page Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Checkout Step Two Page Details")
    @allure.description("Positive test: Checkout Step Two Page Details")
    def test_checkout_step_two_details(self, checkout_page2):
        with allure.step("Get summary info"):
            info = checkout_page2.summary_info.get_all_elements()
        with allure.step("Print summary info"):
            for line in info:
                checkout_page2.logger.logger.info(line.text)

    @allure.feature("Checkout Page Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Checkout Step Two Cancel Button Test")
    @allure.description("Positive test: Checkout Step Two Cancel Button")
    def test_checkout_step_two_cancel_button(self, checkout_page2):
        with allure.step("Click cancel button"):
            page = checkout_page2.click_cancel_button()
        with allure.step("Verify navigation"):
            assert page.is_on_correct_page()
        with allure.step("Navigate to cart page"):
            page = page.header.click_cart()
        with allure.step("Navigate to checkout page"):
            page = page.click_checkout_button()
        with allure.step("Fill checkout form"):
            page.first_name_input.set_text(test_data)
            page.last_name_input.set_text(test_data)
            page.postal_code_input.set_text(test_data)
        with allure.step("Continue checkout"):
            page = page.click_continue_button()
        with allure.step("Verify navigation"):
            assert page.is_on_correct_page()

    @allure.feature("Checkout Page Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Checkout Step Three Page Title Test")
    @allure.description("Positive test: Checkout Step Three Page Title")
    def test_checkout_step_three_page_title(self, checkout_page2):
        with allure.step("Navigate to the final checkout page"):
            page = checkout_page2.click_finish_button()
        with allure.step("Get page title"):
            title = page.header.page_section_title.get_text()
            page.logger.logger.info("")
            page.logger.logger.info(title)
        with allure.step("Get final details"):
            page.logger.logger.info(page.info_label.get_text())
            page.logger.logger.info(page.info_text.get_text())
        with allure.step("Verify page title"):
            assert title.upper() == CHECKOUT_STEP_3

    @allure.feature("Checkout Page Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Checkout Step Three Back Home Button Test")
    @allure.description("Positive test: Checkout Step Three Back Home Button")
    def test_checkout_step_three_back_home_button(self, checkout_page3):
        with allure.step("Click back home button"):
            page = checkout_page3.click_back_home_button()
        with allure.step("Verify navigation"):
            assert page.is_on_correct_page()
        with allure.step("Add item to the cart"):
            page.item_add_to_cart_button.click()

    @allure.feature("Checkout Page Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Checkout Step Two Page Item Details")
    @allure.description("Positive test: Checkout Step Two Page Item Details")
    def test_checkout_item_details(self, driver, checkout_page2):
        page = checkout_page2
        with allure.step("Get checkout item details"):
            page.logger.logger.info("\nCheckout items:")
            quantity = page.item_quantity.get_text()
            page.logger.logger.info(f"Item quantity: '{quantity}'")
            label = page.item_name.get_text()
            page.logger.logger.info(f"Item label: '{label}'")
            description = page.item_description.get_text()
            page.logger.logger.info(f"Item description: '{description}'")
            price = page.item_price.get_text()
            page.logger.logger.info(f"Item price: '{price}'")
        with allure.step("Get item ID"):
            link_id = page.item_link.get_attribute('id')
            mo = ID_REGEX.search(link_id)
            item_id = mo.group()
            page.logger.logger.info(f"Item id: '{item_id}'")
        with allure.step("Navigate to the item page"):
            page.item_link.click()
            from ..src.pages.all_pages.item_page import ItemPage
            page = ItemPage(driver, item_id)
        with allure.step("Verify item details"):
            assert page.is_correct_item_page(item_id, label, description, price)
