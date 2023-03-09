from ....src.base_element import BaseElement
from ....src.pages.saucedemo_base_page import SaucedemoBasePage
from ....src.pages.locators.cart_page_locators import CartPageLocators as CPL


class CartPage(SaucedemoBasePage):

    def __init__(self, driver):
        SaucedemoBasePage.__init__(self, driver, directory="cart.html")
        self.cart_quantity_label = BaseElement(self.driver, *CPL.CART_QUANTITY_LABEL)
        self.cart_desc_label = BaseElement(self.driver, *CPL.CART_DESC_LABEL)
        self.item_quantity = BaseElement(self.driver, *CPL.ITEM_QUANTITY)
        self.item_name = BaseElement(self.driver, *CPL.ITEM_NAME)
        self.item_link = BaseElement(self.driver, *CPL.ITEM_LINK)
        self.item_description = BaseElement(self.driver, *CPL.ITEM_DESCRIPTION)
        self.item_price = BaseElement(self.driver, *CPL.ITEM_PRICE)
        self.item_remove_button = BaseElement(self.driver, *CPL.ITEM_REMOVE_BUTTON)
        self.continue_shopping_button = BaseElement(self.driver, *CPL.CONTINUE_SHOPPING_BUTTON)
        self.checkout_button = BaseElement(self.driver, *CPL.CHECKOUT_BUTTON)

    def click_continue_shopping_button(self):
        self.continue_shopping_button.click()
        from ....src.pages.all_pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)

    def click_checkout_button(self):
        self.checkout_button.click()
        from ....src.pages.all_pages.checkout_page_1 import CheckoutPage1
        return CheckoutPage1(self.driver)
