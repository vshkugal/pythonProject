from selenium.webdriver.common.by import By
from .....parabank.src.base_element import BaseElement, Dropdown
from .....parabank.src.pages.base_parabank_page import BaseParabankPage
from .....parabank.src.pages.locators.account_services_pages_locators.account_activity_locators import AccountActivityLocators
from .....parabank.src.pages.exceptions.custom_exceptions import BaseElementException


class AccountActivityPage(BaseParabankPage):

    def __init__(self, driver, account_id):
        BaseParabankPage.__init__(self, driver,
                                  title="ParaBank | Account Activity",
                                  directory="/activity.htm?id={}".format(account_id))
        self.account_id = account_id
        self.account_details_table_line = BaseElement(self.driver, *AccountActivityLocators.ACCOUNT_DETAILS_TABLE_LINE)
        self.account_details_table_first_cell = BaseElement(self.driver,
                                                            *AccountActivityLocators.ACCOUNT_DETAILS_TABLE_FIRST_CELL)
        self.account_activity_table_line = BaseElement(self.driver,
                                                       *AccountActivityLocators.ACCOUNT_ACTIVITY_TABLE_LINE)
        self.account_activity_table_first_cell = BaseElement(self.driver,
                                                             *AccountActivityLocators.ACCOUNT_ACTIVITY_TABLE_FIRST_CELL)
        self.account_activity_table_column = BaseElement(self.driver,
                                                         *AccountActivityLocators.ACCOUNT_ACTIVITY_TABLE_COLUMN)
        self.dropdown_month = Dropdown(self.driver, *AccountActivityLocators.DROPDOWN_MONTH, "month")
        self.dropdown_type = Dropdown(self.driver, *AccountActivityLocators.DROPDOWN_TYPE, "transactionType")
        self.dropdowns = [self.dropdown_month, self.dropdown_type]
        self.go_button = BaseElement(self.driver, *AccountActivityLocators.GO_BUTTON)
        self.status_message = BaseElement(self.driver, *AccountActivityLocators.STATUS_MESSAGE)
        self.transaction_link = BaseElement(self.driver, *AccountActivityLocators.TRANSACTION_LINK)

    def get_account_details_table_data(self):
        data = {}
        self.account_details_table_first_cell.wait_until_content_not_empty()
        elements = self.account_details_table_line.get_all_elements()
        for element in elements:
            current_index = elements.index(element) + 1
            parsed_data = {}
            name = element.find_element(By.XPATH, AccountActivityLocators.ACCOUNT_DETAILS_TABLE_CELL
                                        .format(current_index, 1)).text
            value = element.find_element(By.XPATH, AccountActivityLocators.ACCOUNT_DETAILS_TABLE_CELL
                                         .format(current_index, 2)).text
            parsed_data.update({str(name).strip(':'): str(value)})
            data.update({current_index: parsed_data})
        return data

    def print_account_details(self):
        self.logger.logger.info('\n'+self.get_section_title())
        for item in self.get_account_details_table_data().values():
            self.logger.logger.info(item)

    def get_account_activity_table_column_info(self):
        column_info = []
        columns = self.account_activity_table_column.get_all_elements()
        for column in columns:
            column_info.append(str(column.text))
        return column_info

    def get_account_activity_table_data(self):
        if self.get_status_message() != "":
            return self.get_status_message()
        self.account_activity_table_first_cell.wait_until_content_not_empty()
        columns = self.get_account_activity_table_column_info()
        data = {}
        elements = self.account_activity_table_line.get_all_elements()
        for element in elements:
            current_index = elements.index(element) + 1
            parsed_data = {}
            for column in columns:
                value = element.find_element(By.XPATH, AccountActivityLocators.ACCOUNT_ACTIVITY_TABLE_CELL
                                             .format(current_index, columns.index(column) + 1)).text
                parsed_data.update({column: str(value)})
            data.update({current_index: parsed_data})
        return data

    def print_account_transactions(self):
        self.logger.logger.info('\n'+BaseElement(self.driver, *AccountActivityLocators.ACCOUNT_ACTIVITY_TITLE).get_text())
        if self.no_transactions():
            self.logger.logger.info(self.get_status_message())
        else:
            for item in self.get_account_activity_table_data().values():
                self.logger.logger.info(item)

    def get_status_message(self):
        try:
            return self.status_message.get_text()
        except BaseElementException:
            return ""

    def no_transactions(self):
        self.dropdown_month.wait_until_not_empty()
        self.dropdown_type.wait_until_not_empty()
        return bool(self.get_status_message() == AccountActivityLocators.NO_TRANSACTIONS_MESSAGE)

    def get_transaction_id(self):
        self.account_activity_table_first_cell.wait_until_content_not_empty()
        mo = AccountActivityLocators.ID_REGEX.search(self.transaction_link.get_all_elements()[-1].get_attribute("href"))
        return mo.group()

    def click_transaction_link(self):
        transaction_id = self.get_transaction_id()
        self.transaction_link.get_all_elements()[-1].click()
        from .....parabank.src.pages.account_services_pages.transaction_details_page import TransactionDetailsPage
        return TransactionDetailsPage(self.driver, transaction_id)
