from .....parabank.src.base_element import BaseElement, Dropdown
from .....parabank.src.pages.base_parabank_page import BaseParabankPage
from .....parabank.src.pages.locators.account_services_pages_locators.transfer_funds_locators import TransferFundsLocators
from .....parabank.src.pages.exceptions.custom_exceptions import BaseElementException


class TransferFundsPage(BaseParabankPage):

    def __init__(self, driver):
        BaseParabankPage.__init__(self, driver,
                                  title="ParaBank | Transfer Funds",
                                  directory="/transfer.htm")
        self.input_amount = BaseElement(self.driver, *TransferFundsLocators.INPUT_AMOUNT)
        self.dropdown_from_account = Dropdown(self.driver, *TransferFundsLocators.DROPDOWN_FROM_ACCOUNT, "fromAccountId")
        self.dropdown_to_account = Dropdown(self.driver, *TransferFundsLocators.DROPDOWN_TO_ACCOUNT, "toAccountId")
        self.transfer_button = BaseElement(self.driver, *TransferFundsLocators.TRANSFER_BUTTON)

    def transfer_funds(self, amount):
        self.dropdown_from_account.wait_until_not_empty()
        self.dropdown_to_account.wait_until_not_empty()
        self.input_amount.set_text(amount)
        self.transfer_button.click()
        return self

    def is_success(self):
        try:
            return bool(BaseElement(self.driver, *TransferFundsLocators.SUCCESS_HEADING).get_text() ==
                        TransferFundsLocators.SUCCESS_MESSAGE)
        except BaseElementException:
            return False

    def print_transfer_funds_form_error(self):
        try:
            error = BaseElement(self.driver, *TransferFundsLocators.ERROR)
            self.logger.logger.warning('\nTransfer Funds form error: {}'.format(error.get_text()))
        except BaseElementException:
            pass
