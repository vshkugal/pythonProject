from .....parabank.src.base_element import BaseElement, Dropdown
from .....parabank.src.pages.base_parabank_page import BaseParabankPage
from .....parabank.src.pages.locators.account_services_pages_locators.open_new_account_locators import OpenNewAccountLocators
from .....parabank.src.pages.exceptions.custom_exceptions import BaseElementException


class OpenNewAccountPage(BaseParabankPage):

    def __init__(self, driver):
        BaseParabankPage.__init__(self, driver,
                                  title="ParaBank | Open Account",
                                  directory="/openaccount.htm")
        self.dropdown_type = Dropdown(self.driver, *OpenNewAccountLocators.DROPDOWN_TYPE, "type")
        self.dropdown_from_account = Dropdown(self.driver, *OpenNewAccountLocators.DROPDOWN_FROM_ACCOUNT, "fromAccountId")
        self.dropdowns = [self.dropdown_type, self.dropdown_from_account]
        self.open_button = BaseElement(self.driver, *OpenNewAccountLocators.OPEN_BUTTON)
        self.account_link = BaseElement(self.driver, *OpenNewAccountLocators.ACCOUNT_LINK)

    def open_new_account(self):
        self.open_button.click()
        return self

    def is_success(self):
        return bool(BaseElement(self.driver, *OpenNewAccountLocators.SUCCESS_HEADING).get_text() ==
                    OpenNewAccountLocators.SUCCESS_MESSAGE)

    def print_open_new_account_form_error(self):
        try:
            error = BaseElement(self.driver, *OpenNewAccountLocators.ERROR)
            self.logger.logger.warning('\nOpen New Account form error: {}'.format(error.get_text()))
        except BaseElementException:
            pass

    def get_account_id(self):
        return self.account_link.get_text()

    def click_account_link(self):
        account_id = self.get_account_id()
        self.account_link.click()
        from .....parabank.src.pages.account_services_pages.account_activity_page import AccountActivityPage
        return AccountActivityPage(self.driver, account_id)
