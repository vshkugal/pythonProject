from ....src.base_element import BaseElement, Dropdown
from ....src.pages.saucedemo_base_page import SaucedemoBasePage
from ....src.pages.locators.inventory_page_locators import InventoryPageLocators as IPL


class InventoryPage(SaucedemoBasePage):

    def __init__(self, driver):
        SaucedemoBasePage.__init__(self, driver, directory="inventory.html")
        self.sort_items_dropdown = Dropdown(self.driver, *IPL.SORT_ITEMS_DROPDOWN, 'product_sort_container')
        self.item_img = BaseElement(self.driver, *IPL.ITEM_IMG)
        self.item_img_link = BaseElement(self.driver, *IPL.ITEM_IMG_LINK)
        self.item_label = BaseElement(self.driver, *IPL.ITEM_LABEL)
        self.item_label_link = BaseElement(self.driver, *IPL.ITEM_LABEL_LINK)
        self.item_description = BaseElement(self.driver, *IPL.ITEM_DESCRIPTION)
        self.item_price = BaseElement(self.driver, *IPL.ITEM_PRICE)
        self.item_add_to_cart_button = BaseElement(self.driver, *IPL.ITEM_ADD_TO_CART_BUTTON)
