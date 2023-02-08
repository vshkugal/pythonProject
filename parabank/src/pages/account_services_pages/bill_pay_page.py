from .....parabank.src.base_element import BaseElement
from .....parabank.src.pages.base_parabank_page import BaseParabankPage
from .....parabank.src.pages.locators.account_services_pages_locators.bill_pay_locators import BillPayLocators
from .....parabank.src.pages.exceptions.custom_exceptions import BaseElementException


class BillPayPage(BaseParabankPage):

    def __init__(self, driver):
        BaseParabankPage.__init__(self, driver,
                                  title="ParaBank | Bill Pay",
                                  directory="/billpay.htm")
        self.input_name = BaseElement(self.driver, *BillPayLocators.INPUT_NAME)
        self.input_address = BaseElement(self.driver, *BillPayLocators.INPUT_ADDRESS)
        self.input_city = BaseElement(self.driver, *BillPayLocators.INPUT_CITY)
        self.input_state = BaseElement(self.driver, *BillPayLocators.INPUT_STATE)
        self.input_zip_code = BaseElement(self.driver, *BillPayLocators.INPUT_ZIP_CODE)
        self.input_phone = BaseElement(self.driver, *BillPayLocators.INPUT_PHONE)
        self.input_account = BaseElement(self.driver, *BillPayLocators.INPUT_ACCOUNT)
        self.input_account_verify = BaseElement(self.driver, *BillPayLocators.INPUT_ACCOUNT_VERIFY)
        self.input_amount = BaseElement(self.driver, *BillPayLocators.INPUT_AMOUNT)
        self.dropdown_from_account = BaseElement(self.driver, *BillPayLocators.DROPDOWN_FROM_ACCOUNT)
        self.send_payment_button = BaseElement(self.driver, *BillPayLocators.SEND_PAYMENT_BUTTON)
        self.success_form = BaseElement(self.driver, *BillPayLocators.SUCCESS_FORM)
        self.error = BaseElement(self.driver, *BillPayLocators.ERROR)

    def input_payee_information_full(self, name, street, city, state, zip_code, phone, acc1, acc2, amount):
        self.dropdown_from_account.wait_until_not_empty()
        self.input_name.set_text(name)
        self.input_address.set_text(street)
        self.input_city.set_text(city)
        self.input_state.set_text(state)
        self.input_zip_code.set_text(zip_code)
        self.input_phone.set_text(phone)
        self.input_account.set_text(acc1)
        self.input_account_verify.set_text(acc2)
        self.input_amount.set_text(amount)
        self.send_payment_button.click()

    def is_success(self):
        return bool(BaseElement(self.driver, *BillPayLocators.SUCCESS_HEADING).get_text()
                    == BillPayLocators.SUCCESS_MESSAGE)

    def print_bill_pay_form_errors(self):
        try:
            errors = self.error.get_all_elements()
            if errors:
                self.logger.logger.warning('\nBill Pay form errors:')
                for error in errors:
                    self.logger.logger.warning(error.text)
        except BaseElementException:
            pass
