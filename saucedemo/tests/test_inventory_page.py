from ..src.pages.components.page_constants import *


class TestInventoryPage:

    def test_page_title(self, inventory_page):
        title = inventory_page.header.page_section_title.get_text()
        assert title.upper() == "PRODUCTS"

    def test_dropdown_descriptions(self, inventory_page):
        dropdown = inventory_page.sort_items_dropdown
        inventory_page.logger.logger.info(f"\nDropdown '{dropdown.dropdown_id}' options:\n")
        for option in dropdown.get_dropdown_options():
            inventory_page.logger.logger.info(option)

    def test_dropdown_selections(self, inventory_page):
        dropdown = inventory_page.sort_items_dropdown
        values = dropdown.get_dropdown_options()
        inventory_page.logger.logger.info(f"\nDropdown '{dropdown.dropdown_id}' selections:")
        for i in range(len(values), 0, -1):
            inventory_page.logger.logger.info(f"\nSelected value: {dropdown.get_selected()}")
            inventory_page.logger.logger.info(f"Select: {values[i-1]}")
            dropdown.select(values[i-1])
            inventory_page.logger.logger.info(f"Selected value: {dropdown.get_selected()}")
            assert values[i-1].upper() == dropdown.get_selected().upper()

    def test_item_details(self, driver, inventory_page):
        label = inventory_page.item_label.get_text()
        inventory_page.logger.logger.info(f"\nItem label: '{label}'")
        description = inventory_page.item_description.get_text()
        inventory_page.logger.logger.info(f"Item description: '{description}'")
        price = inventory_page.item_price.get_text()
        inventory_page.logger.logger.info(f"Item price: '{price}'")
        link_id = inventory_page.item_label_link.get_attribute('id')
        mo = ID_REGEX.search(link_id)
        item_id = mo.group()
        inventory_page.logger.logger.info(f"Item id: '{item_id}'")
        inventory_page.item_label_link.click()
        from ..src.pages.all_pages.item_page import ItemPage
        page = ItemPage(driver, item_id)
        assert page.is_correct_item_page(item_id, label, description, price)
        page = page.click_back_to_products_button()
        assert page.is_on_correct_page()

    def test_add_item_to_cart(self, driver, inventory_page):
        assert inventory_page.header.get_cart_items_quantity() == '0'
        assert inventory_page.item_add_to_cart_button.get_text().upper() == "ADD TO CART"
        inventory_page.item_add_to_cart_button.click()
        assert inventory_page.item_add_to_cart_button.get_text().upper() == "REMOVE"
        assert inventory_page.header.get_cart_items_quantity() == '1'
        link_id = inventory_page.item_label_link.get_attribute('id')
        mo = ID_REGEX.search(link_id)
        item_id = mo.group()
        inventory_page.item_label_link.click()
        from ..src.pages.all_pages.item_page import ItemPage
        page = ItemPage(driver, item_id)
        assert page.header.get_cart_items_quantity() == '1'
        assert page.item_add_to_cart_button.get_text().upper() == "REMOVE"
        page.item_add_to_cart_button.click()
        assert inventory_page.item_add_to_cart_button.get_text().upper() == "ADD TO CART"
        assert page.header.get_cart_items_quantity() == '0'
        page = page.click_back_to_products_button()
        assert page.is_on_correct_page()
        assert page.header.get_cart_items_quantity() == '0'
        assert page.item_add_to_cart_button.get_text().upper() == "ADD TO CART"

    def test_add_all_items_to_cart(self, inventory_page):
        assert inventory_page.header.get_cart_items_quantity() == '0'
        items = 0
        buttons = inventory_page.item_add_to_cart_button.get_all_elements()
        for button in buttons:
            assert button.text.upper() == "ADD TO CART"
            button.click()
            items += 1
            assert inventory_page.header.get_cart_items_quantity() == str(items)
        inventory_page.logger.logger.info(f"\nTotal of {str(items)} items were added to cart")

    def test_remove_all_items_from_cart(self, inventory_page):
        items = qty = int(inventory_page.header.get_cart_items_quantity())
        buttons = inventory_page.item_add_to_cart_button.get_all_elements()
        for button in buttons:
            assert button.text.upper() == "REMOVE"
            button.click()
            items -= 1
            assert inventory_page.header.get_cart_items_quantity() == str(items)
        assert inventory_page.header.get_cart_items_quantity() == '0'
        inventory_page.logger.logger.info(f"All {str(qty)} items were removed from cart")
