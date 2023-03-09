from ....src.base_element import BaseElement
from ....src.pages.saucedemo_base_page import SaucedemoBasePage
from ....src.pages.locators.checkout_page_locators import CheckoutPageLocators3 as CPL3


class CheckoutPage3(SaucedemoBasePage):

    def __init__(self, driver):
        SaucedemoBasePage.__init__(self, driver, directory="checkout-complete.html")
        self.info_label = BaseElement(self.driver, *CPL3.INFO_LABEL)
        self.info_text = BaseElement(self.driver, *CPL3.INFO_TEXT)
        self.info_logo = BaseElement(self.driver, *CPL3.INFO_LOGO)
        self.back_home_button = BaseElement(self.driver, *CPL3.BACK_HOME_BUTTON)

    def click_back_home_button(self):
        self.back_home_button.click()
        from ....src.pages.all_pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)
