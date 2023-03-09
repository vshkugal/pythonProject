from ....src.base_element import BaseElement
from ....src.pages.saucedemo_base_page import SaucedemoBasePage
from ....src.pages.exceptions.custom_exceptions import BasePageException
from ....src.pages.locators.item_page_locators import ItemPageLocators as IPL


class ItemPage(SaucedemoBasePage):

    def __init__(self, driver, item_id):
        SaucedemoBasePage.__init__(self, driver, directory="inventory-item.html?id={}".format(item_id))
        self.item_id = item_id
        self.back_to_products_button = BaseElement(self.driver, *IPL.BACK_TO_PRODUCTS_BUTTON)
        self.item_img = BaseElement(self.driver, *IPL.ITEM_IMG)
        self.item_label = BaseElement(self.driver, *IPL.ITEM_LABEL)
        self.item_description = BaseElement(self.driver, *IPL.ITEM_DESCRIPTION)
        self.item_price = BaseElement(self.driver, *IPL.ITEM_PRICE)
        self.item_add_to_cart_button = BaseElement(self.driver, *IPL.ITEM_ADD_TO_CART_BUTTON)

    def click_back_to_products_button(self):
        self.back_to_products_button.click()
        from ....src.pages.all_pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)

    def is_correct_item_page(self, item_id, label, description, price):
        item_id1 = self.item_id
        label1 = self.item_label.get_text()
        description1 = self.item_description.get_text()
        price1 = self.item_price.get_text()
        if item_id != item_id1:
            raise BasePageException(f"Expected id: '{item_id}' Actual id: '{item_id1}'")
        if label != label1:
            raise BasePageException(f"Expected label: '{label}' Actual label: '{label1}'")
        if description != description1:
            raise BasePageException(f"Expected description: '{description}' Actual description: '{description1}'")
        if price != price1:
            raise BasePageException(f"Expected price: '{price}' Actual price: '{price1}'")
        return True
