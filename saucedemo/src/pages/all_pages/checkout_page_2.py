from ....src.base_element import BaseElement
from ....src.pages.saucedemo_base_page import SaucedemoBasePage
from ....src.pages.locators.checkout_page_locators import CheckoutPageLocators2 as CPL2


class CheckoutPage2(SaucedemoBasePage):

    def __init__(self, driver):
        SaucedemoBasePage.__init__(self, driver, directory="checkout-step-two.html")
        self.item_quantity = BaseElement(self.driver, *CPL2.ITEM_QUANTITY)
        self.item_name = BaseElement(self.driver, *CPL2.ITEM_NAME)
        self.item_link = BaseElement(self.driver, *CPL2.ITEM_LINK)
        self.item_description = BaseElement(self.driver, *CPL2.ITEM_DESCRIPTION)
        self.item_price = BaseElement(self.driver, *CPL2.ITEM_PRICE)
        self.summary_info = BaseElement(self.driver, *CPL2.SUMMARY_INFO)
        self.cancel_button = BaseElement(self.driver, *CPL2.CANCEL_BUTTON)
        self.finish_button = BaseElement(self.driver, *CPL2.FINISH_BUTTON)

    def click_cancel_button(self):
        self.cancel_button.click()
        from ....src.pages.all_pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)

    def click_finish_button(self):
        self.finish_button.click()
        from ....src.pages.all_pages.checkout_page_3 import CheckoutPage3
        return CheckoutPage3(self.driver)
