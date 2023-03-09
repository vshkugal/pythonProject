from ..src.pages.components.page_constants import *
import allure


class TestInventoryPage:

    @allure.feature("Inventory Page Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Inventory Page Title Test")
    @allure.description("Positive test: Inventory Page Title")
    def test_page_title(self, inventory_page):
        with allure.step("Get page title"):
            title = inventory_page.header.page_section_title.get_text()
        with allure.step("Verify page title"):
            assert title.upper() == "PRODUCTS"

    @allure.feature("Inventory Page Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Inventory Page Dropdown Test")
    @allure.description("Positive test: Dropdown Options List")
    def test_dropdown_descriptions(self, inventory_page):
        with allure.step("Get inventory page dropdown"):
            dropdown = inventory_page.sort_items_dropdown
        with allure.step("Print inventory page dropdown options"):
            inventory_page.logger.logger.info(f"\nDropdown '{dropdown.dropdown_id}' options:\n")
            for option in dropdown.get_dropdown_options():
                inventory_page.logger.logger.info(option)

    @allure.feature("Inventory Page Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Inventory Page Dropdown Options Test")
    @allure.description("Positive test: Dropdown Options Navigation")
    def test_dropdown_selections(self, inventory_page):
        with allure.step("Get inventory page dropdown options"):
            dropdown = inventory_page.sort_items_dropdown
            values = dropdown.get_dropdown_options()
        inventory_page.logger.logger.info(f"\nDropdown '{dropdown.dropdown_id}' selections:")
        for i in range(len(values), 0, -1):
            with allure.step("Check current dropdown option"):
                inventory_page.logger.logger.info(f"\nSelected value: {dropdown.get_selected()}")
            with allure.step("Navigate to the next dropdown option"):
                inventory_page.logger.logger.info(f"Select: {values[i-1]}")
                dropdown.select(values[i-1])
            with allure.step("Verify new dropdown option"):
                inventory_page.logger.logger.info(f"Selected value: {dropdown.get_selected()}")
                assert values[i-1].upper() == dropdown.get_selected().upper()

    @allure.feature("Inventory Page Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Inventory Page Item Details Test")
    @allure.description("Positive test: Item Details")
    def test_item_details(self, driver, inventory_page):
        with allure.step("Get item details"):
            label = inventory_page.item_label.get_text()
            inventory_page.logger.logger.info(f"\nItem label: '{label}'")
            description = inventory_page.item_description.get_text()
            inventory_page.logger.logger.info(f"Item description: '{description}'")
            price = inventory_page.item_price.get_text()
            inventory_page.logger.logger.info(f"Item price: '{price}'")
        with allure.step("Get item ID"):
            link_id = inventory_page.item_label_link.get_attribute('id')
            mo = ID_REGEX.search(link_id)
            item_id = mo.group()
            inventory_page.logger.logger.info(f"Item id: '{item_id}'")
        with allure.step("Navigate to the item page"):
            inventory_page.item_label_link.click()
            from ..src.pages.all_pages.item_page import ItemPage
            page = ItemPage(driver, item_id)
        with allure.step("Verify item details"):
            assert page.is_correct_item_page(item_id, label, description, price)
        with allure.step("Return to the inventory page"):
            page = page.click_back_to_products_button()
            assert page.is_on_correct_page()

    @allure.feature("Inventory Page Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Inventory Page Add Item To Cart Test")
    @allure.description("Positive test: Add Item To Cart")
    def test_add_item_to_cart(self, driver, inventory_page):
        with allure.step("Verify that cart is empty"):
            assert inventory_page.header.get_cart_items_quantity() == '0'
        with allure.step("Verify that item is not in the cart yet"):
            assert inventory_page.item_add_to_cart_button.get_text().upper() == "ADD TO CART"
        with allure.step("Add item to the cart"):
            inventory_page.item_add_to_cart_button.click()
        with allure.step("Verify that item is in the cart"):
            assert inventory_page.item_add_to_cart_button.get_text().upper() == "REMOVE"
            assert inventory_page.header.get_cart_items_quantity() == '1'
        with allure.step("Get item ID"):
            link_id = inventory_page.item_label_link.get_attribute('id')
            mo = ID_REGEX.search(link_id)
            item_id = mo.group()
        with allure.step("Navigate to the item page"):
            inventory_page.item_label_link.click()
            from ..src.pages.all_pages.item_page import ItemPage
            page = ItemPage(driver, item_id)
        with allure.step("Confirm that item is in the cart"):
            assert page.header.get_cart_items_quantity() == '1'
            assert page.item_add_to_cart_button.get_text().upper() == "REMOVE"
        with allure.step("Remove item from the cart"):
            page.item_add_to_cart_button.click()
        with allure.step("Verify that item is not in the cart anymore"):
            assert inventory_page.item_add_to_cart_button.get_text().upper() == "ADD TO CART"
            assert page.header.get_cart_items_quantity() == '0'
        with allure.step("Navigate to the inventory page"):
            page = page.click_back_to_products_button()
            assert page.is_on_correct_page()
        with allure.step("Confirm that item is not in the cart anymore"):
            assert page.header.get_cart_items_quantity() == '0'
            assert page.item_add_to_cart_button.get_text().upper() == "ADD TO CART"

    @allure.feature("Inventory Page Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Inventory Page Add All Items To Cart Test")
    @allure.description("Positive test: Add All Items To Cart")
    def test_add_all_items_to_cart(self, inventory_page):
        with allure.step("Verify that cart is empty"):
            assert inventory_page.header.get_cart_items_quantity() == '0'
            items = 0
        with allure.step("Get all items on the page"):
            buttons = inventory_page.item_add_to_cart_button.get_all_elements()
        for button in buttons:
            with allure.step(f"Add item {items+1} to the cart"):
                assert button.text.upper() == "ADD TO CART"
                button.click()
                items += 1
            with allure.step(f"Verify that the number of items in the cart is {items} now"):
                assert inventory_page.header.get_cart_items_quantity() == str(items)
        inventory_page.logger.logger.info(f"\nTotal of {str(items)} items were added to cart")

    @allure.feature("Inventory Page Test")
    @allure.story("Positive Test")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Inventory Page Remove All Items From Cart Test")
    @allure.description("Positive test: Remove All Items From Cart")
    def test_remove_all_items_from_cart(self, inventory_page):
        with allure.step("Get number of items in the cart"):
            items = qty = int(inventory_page.header.get_cart_items_quantity())
        with allure.step(f"Get all {items} items on the page"):
            buttons = inventory_page.item_add_to_cart_button.get_all_elements()
        for button in buttons:
            with allure.step(f"Remove item {items} from the cart"):
                assert button.text.upper() == "REMOVE"
                button.click()
                items -= 1
            with allure.step(f"Verify that the number of items in the cart is {items} now"):
                assert inventory_page.header.get_cart_items_quantity() == str(items)
        with allure.step("Confirm that cart is empty"):
            assert inventory_page.header.get_cart_items_quantity() == '0'
            inventory_page.logger.logger.info(f"All {str(qty)} items were removed from cart")
