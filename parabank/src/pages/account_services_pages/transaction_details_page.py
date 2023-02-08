from selenium.webdriver.common.by import By
from .....parabank.src.base_element import BaseElement
from .....parabank.src.pages.base_parabank_page import BaseParabankPage
from .....parabank.src.pages.locators.account_services_pages_locators.transaction_details_locators import TransactionDetailsLocators


class TransactionDetailsPage(BaseParabankPage):

    def __init__(self, driver, transaction_id):
        BaseParabankPage.__init__(self, driver,
                                  title="ParaBank | Transaction Details",
                                  directory="/transaction.htm?id={}".format(transaction_id))
        self.transaction_id = transaction_id
        self.transaction_details_table_line = \
            BaseElement(self.driver, *TransactionDetailsLocators.TRANSACTION_DETAILS_TABLE_LINE)
        self.transaction_details_table_first_cell = \
            BaseElement(self.driver, *TransactionDetailsLocators.TRANSACTION_DETAILS_TABLE_FIRST_CELL)

    def get_transaction_details_table_data(self):
        data = {}
        self.transaction_details_table_first_cell.wait_until_content_not_empty()
        elements = self.transaction_details_table_line.get_all_elements()
        for element in elements:
            current_index = elements.index(element) + 1
            parsed_data = {}
            name = element.find_element(By.XPATH, TransactionDetailsLocators.TRANSACTION_DETAILS_TABLE_CELL
                                        .format(current_index, 1)).text
            value = element.find_element(By.XPATH, TransactionDetailsLocators.TRANSACTION_DETAILS_TABLE_CELL
                                         .format(current_index, 2)).text
            parsed_data.update({str(name).strip(':'): str(value)})
            data.update({current_index: parsed_data})
        return data

    def print_transaction_details(self):
        self.logger.logger.info('\n'+self.get_section_title())
        for item in self.get_transaction_details_table_data().values():
            self.logger.logger.info(item)
