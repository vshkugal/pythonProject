from selenium.webdriver.common.by import By
from .....parabank.src.base_element import BaseElement, Dropdown
from .....parabank.src.pages.base_parabank_page import BaseParabankPage
from .....parabank.src.pages.locators.account_services_pages_locators.find_transactions_locators import FindTransactionsLocators


class FindTransactionsPage(BaseParabankPage):

    def __init__(self, driver):
        BaseParabankPage.__init__(self, driver,
                                  title="ParaBank | Find Transactions",
                                  directory="/findtrans.htm")
        self.dropdown_account = Dropdown(self.driver, *FindTransactionsLocators.DROPDOWN_ACCOUNT, "accountId")
        self.input_by_id = BaseElement(self.driver, *FindTransactionsLocators.INPUT_BY_ID)
        self.button_by_id = BaseElement(self.driver, *FindTransactionsLocators.BUTTON_BY_ID)
        self.input_by_date = BaseElement(self.driver, *FindTransactionsLocators.INPUT_BY_DATE)
        self.button_by_date = BaseElement(self.driver, *FindTransactionsLocators.BUTTON_BY_DATE)
        self.input_from_date = BaseElement(self.driver, *FindTransactionsLocators.INPUT_FROM_DATE)
        self.input_to_date = BaseElement(self.driver, *FindTransactionsLocators.INPUT_TO_DATE)
        self.button_by_date_range = BaseElement(self.driver, *FindTransactionsLocators.BUTTON_BY_DATE_RANGE)
        self.input_by_amount = BaseElement(self.driver, *FindTransactionsLocators.INPUT_BY_AMOUNT)
        self.button_by_amount = BaseElement(self.driver, *FindTransactionsLocators.BUTTON_BY_AMOUNT)
        self.success_form = BaseElement(self.driver, *FindTransactionsLocators.SUCCESS_FORM)
        self.error_form = BaseElement(self.driver, *FindTransactionsLocators.ERROR_FORM)
        self.transactions_table_line = BaseElement(self.driver, *FindTransactionsLocators.TRANSACTIONS_TABLE_LINE)
        self.transactions_table_first_cell = BaseElement(self.driver,
                                                         *FindTransactionsLocators.TRANSACTIONS_TABLE_FIRST_CELL)
        self.transactions_table_column = BaseElement(self.driver, *FindTransactionsLocators.TRANSACTIONS_TABLE_COLUMN)
        self.transaction_link = BaseElement(self.driver, *FindTransactionsLocators.TRANSACTION_LINK)

    def is_success(self):
        return bool(self.get_section_title() == FindTransactionsLocators.SUCCESS_MESSAGE)

    def get_transactions_table_column_info(self):
        column_info = []
        columns = self.transactions_table_column.get_all_elements()
        for column in columns:
            column_info.append(str(column.text))
        return column_info

    def get_transactions_table_data(self):
        self.transactions_table_first_cell.wait_until_content_not_empty()
        columns = self.get_transactions_table_column_info()
        data = {}
        elements = self.transactions_table_line.get_all_elements()
        for element in elements:
            current_index = elements.index(element) + 1
            parsed_data = {}
            for column in columns:
                value = element.find_element(By.XPATH, FindTransactionsLocators.TRANSACTIONS_TABLE_CELL
                                             .format(current_index, columns.index(column) + 1)).text
                parsed_data.update({column: str(value)})
            data.update({current_index: parsed_data})
        return data

    def print_transaction_results(self):
        self.logger.logger.info('\n'+self.get_section_title())
        if self.transactions_table_line.exists():
            for item in self.get_transactions_table_data().values():
                self.logger.logger.info(item)

    def get_transaction_id(self):
        self.transactions_table_first_cell.wait_until_content_not_empty()
        mo = FindTransactionsLocators.ID_REGEX.search(self.transaction_link.get_all_elements()[-1].get_attribute("href"))
        return mo.group()

    def click_transaction_link(self):
        transaction_id = self.get_transaction_id()
        self.transaction_link.get_all_elements()[-1].click()
        from .....parabank.src.pages.account_services_pages.transaction_details_page import TransactionDetailsPage
        return TransactionDetailsPage(self.driver, transaction_id)
