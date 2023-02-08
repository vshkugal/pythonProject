from selenium.webdriver.common.by import By
from .....parabank.src.base_element import BaseElement
from .....parabank.src.pages.base_parabank_page import BaseParabankPage
from .....parabank.src.pages.locators.account_services_pages_locators.accounts_overview_locators import AccountsOverviewLocators


class AccountsOverviewPage(BaseParabankPage):

    def __init__(self, driver):
        BaseParabankPage.__init__(self, driver,
                                  title="ParaBank | Accounts Overview",
                                  directory="/overview.htm")

        self.table_column = BaseElement(self.driver, *AccountsOverviewLocators.TABLE_COLUMN)
        self.table_data_line = BaseElement(self.driver, *AccountsOverviewLocators.TABLE_DATA_LINE)
        self.table_data_first_cell = BaseElement(self.driver, *AccountsOverviewLocators.TABLE_DATA_FIRST_CELL)
        self.account_link = BaseElement(self.driver, *AccountsOverviewLocators.ACCOUNT_LINK)

    def get_accounts_overview_table_column_info(self):
        column_info = []
        columns = self.table_column.get_all_elements()
        for column in columns:
            column_info.append(str(column.text))
        return column_info

    def get_accounts_overview_table_data(self):
        self.table_data_first_cell.wait_until_content_not_empty()
        columns = self.get_accounts_overview_table_column_info()
        data = {}
        elements = self.table_data_line.get_all_elements()
        for element in elements:
            current_index = elements.index(element) + 1
            parsed_data = {}
            for column in columns:
                value = element.find_element(By.XPATH, AccountsOverviewLocators.TABLE_DATA_CELL
                                             .format(current_index, columns.index(column) + 1)).text
                parsed_data.update({column: str(value)})
            data.update({current_index: parsed_data})
        return data

    def print_accounts_overview(self):
        self.logger.logger.info('\n'+self.get_section_title())
        for item in self.get_accounts_overview_table_data().values():
            self.logger.logger.info(item)

    def get_account_id(self):
        return self.account_link.get_text()

    def click_account_link(self):
        account_id = self.get_account_id()
        self.account_link.click()
        from .....parabank.src.pages.account_services_pages.account_activity_page import AccountActivityPage
        return AccountActivityPage(self.driver, account_id)
