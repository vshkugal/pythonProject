from ..src.pages.components.page_constants import *


class TestCartPage:

    def test_page_title(self, cart_page):
        title = cart_page.header.page_section_title.get_text()
        assert title.upper() == "YOUR CART"

    def test_item_details(self, driver, cart_page):
        assert cart_page.header.get_cart_items_quantity() == '0'
        page = cart_page.click_continue_shopping_button()
        page.item_add_to_cart_button.click()
        page = page.header.click_cart()
        assert page.header.get_cart_items_quantity() == '1'
        page.logger.logger.info("\nCart contents:")
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
        page = page.header.click_cart()
        page.item_remove_button.click()
        assert page.header.get_cart_items_quantity() == '0'
