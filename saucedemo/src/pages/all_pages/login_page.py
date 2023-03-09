from ....src.base_element import BaseElement
from ....src.pages.saucedemo_base_page import SaucedemoBasePage
from ....src.pages.exceptions.custom_exceptions import BaseElementException
from ....src.pages.locators.login_page_locators import LoginPageLocators as LPL


class LoginPage(SaucedemoBasePage):

    def __init__(self, driver):
        SaucedemoBasePage.__init__(self, driver, directory="")
        self.input_username = BaseElement(self.driver, *LPL.INPUT_USERNAME)
        self.input_password = BaseElement(self.driver, *LPL.INPUT_PASSWORD)
        self.login_button = BaseElement(self.driver, *LPL.LOGIN_BUTTON)
        self.error_message = BaseElement(self.driver, *LPL.ERROR_MESSAGE)
        self.error_button = BaseElement(self.driver, *LPL.ERROR_BUTTON)

    def login_user(self, username, password):
        self.input_username.set_text(username)
        self.input_password.set_text(password)
        self.login_button.click()

    def print_login_error(self):
        try:
            error = self.error_message.get_element()
            if error:
                self.logger.logger.warning('\nLogin form error:')
                self.logger.logger.warning(error.text)
        except BaseElementException:
            pass
