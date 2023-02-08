from selenium.webdriver.common.by import By
from .....parabank.src.base_element import BaseElement, Dropdown
from .....parabank.src.pages.base_parabank_page import BaseParabankPage
from .....parabank.src.pages.locators.account_services_pages_locators.request_loan_locators import LoanRequestLocators


class LoanRequestPage(BaseParabankPage):

    def __init__(self, driver):
        BaseParabankPage.__init__(self, driver,
                                  title="ParaBank | Loan Request",
                                  directory="/requestloan.htm")
        self.input_amount = BaseElement(self.driver, *LoanRequestLocators.INPUT_AMOUNT)
        self.input_down_payment = BaseElement(self.driver, *LoanRequestLocators.INPUT_DOWN_PAYMENT)
        self.dropdown_account = Dropdown(self.driver, *LoanRequestLocators.DROPDOWN_ACCOUNT, "fromAccountId")
        self.apply_button = BaseElement(self.driver, *LoanRequestLocators.APPLY_BUTTON)
        self.success_form = BaseElement(self.driver, *LoanRequestLocators.SUCCESS_FORM)
        self.loan_request_table_line = BaseElement(self.driver, *LoanRequestLocators.LOAN_REQUEST_TABLE_LINE)
        self.new_account_link = BaseElement(self.driver, *LoanRequestLocators.NEW_ACCOUNT_LINK)

    def request_loan(self, amount, down_payment):
        self.dropdown_account.wait_until_not_empty()
        self.input_amount.set_text(amount)
        self.input_down_payment.set_text(down_payment)
        self.apply_button.click()
        return self

    def is_processed(self):
        return bool(self.get_section_title() == LoanRequestLocators.SUCCESS_MESSAGE)

    def is_approved(self):
        return bool(self.get_section_info()[0] == LoanRequestLocators.APPROVE_MESSAGE)

    def get_loan_request_table_data(self):
        data = {}
        elements = self.loan_request_table_line.get_all_elements()
        for element in elements:
            current_index = elements.index(element) + 1
            parsed_data = {}
            name = element.find_element(By.XPATH, LoanRequestLocators.LOAN_REQUEST_TABLE_CELL
                                        .format(current_index, 1)).text
            value = element.find_element(By.XPATH, LoanRequestLocators.LOAN_REQUEST_TABLE_CELL
                                         .format(current_index, 2)).text
            parsed_data.update({str(name).strip(':'): str(value)})
            data.update({current_index: parsed_data})
        return data

    def print_loan_details(self):
        self.logger.logger.info('\n'+self.get_section_title())
        for item in self.get_loan_request_table_data().values():
            self.logger.logger.info(item)

    def get_new_account_id(self):
        return self.new_account_link.get_text()

    def click_new_account_link(self):
        account_id = self.get_new_account_id()
        self.new_account_link.click()
        from .....parabank.src.pages.account_services_pages.account_activity_page import AccountActivityPage
        return AccountActivityPage(self.driver, account_id)
