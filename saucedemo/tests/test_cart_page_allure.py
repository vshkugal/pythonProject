from ..src.pages.components.page_constants import *
import allure


class TestCartPage:

    @allure.feature("Cart Page Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Cart Page Title Test")
    @allure.description("Positive test: Cart Page Title")
    def test_page_title(self, cart_page):
        with allure.step("Get page title"):
            title = cart_page.header.page_section_title.get_text()
        with allure.step("Verify page title"):
            assert title.upper() == "YOUR CART"

    @allure.feature("Cart Page Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Cart Page Item Details Test")
    @allure.description("Positive test: Item Details")
    def test_item_details(self, driver, cart_page):
        with allure.step("Verify that cart is empty"):
            assert cart_page.header.get_cart_items_quantity() == '0'
        with allure.step("Navigate to the inventory page"):
            page = cart_page.click_continue_shopping_button()
        with allure.step("Add item to the cart"):
            page.item_add_to_cart_button.click()
        with allure.step("Navigate to the cart page"):
            page = page.header.click_cart()
        with allure.step("Verify that item is in the cart"):
            assert page.header.get_cart_items_quantity() == '1'
        with allure.step("Get cart item details"):
            page.logger.logger.info("\nCart contents:")
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
        with allure.step("Navigate to the cart page"):
            page = page.header.click_cart()
        with allure.step("Remove item from the cart"):
            page.item_remove_button.click()
        with allure.step("Verify that cart is empty"):
            assert page.header.get_cart_items_quantity() == '0'
