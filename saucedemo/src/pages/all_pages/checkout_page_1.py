from ....src.base_element import BaseElement
from ....src.pages.saucedemo_base_page import SaucedemoBasePage
from ....src.pages.exceptions.custom_exceptions import BaseElementException
from ....src.pages.locators.checkout_page_locators import CheckoutPageLocators1 as CPL1


class CheckoutPage1(SaucedemoBasePage):

    def __init__(self, driver):
        SaucedemoBasePage.__init__(self, driver, directory="checkout-step-one.html")
        self.first_name_input = BaseElement(self.driver, *CPL1.FIRST_NAME_INPUT)
        self.last_name_input = BaseElement(self.driver, *CPL1.LAST_NAME_INPUT)
        self.postal_code_input = BaseElement(self.driver, *CPL1.POSTAL_CODE_INPUT)
        self.error_message = BaseElement(self.driver, *CPL1.ERROR_MESSAGE)
        self.error_close_button = BaseElement(self.driver, *CPL1.ERROR_CLOSE_BUTTON)
        self.cancel_button = BaseElement(self.driver, *CPL1.CANCEL_BUTTON)
        self.continue_button = BaseElement(self.driver, *CPL1.CONTINUE_BUTTON)

    def click_cancel_button(self):
        self.cancel_button.click()
        from ....src.pages.all_pages.cart_page import CartPage
        return CartPage(self.driver)

    def click_continue_button(self):
        self.continue_button.click()
        from ....src.pages.all_pages.checkout_page_2 import CheckoutPage2
        return CheckoutPage2(self.driver)

    def get_error_message(self):
        try:
            error = self.error_message.get_element()
            if error:
                self.logger.logger.warning('\nCheckout Step One form error message:')
                self.logger.logger.warning(error.text)
                return error.text
        except BaseElementException:
            return ""
