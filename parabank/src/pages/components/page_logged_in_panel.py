from .....parabank.src.base_element import BaseElement
from .....parabank.src.pages.locators.page_components_locators import LoggedInPanelLocators


class LoggedInPanel:

    def __init__(self, driver):
        self.driver = driver
        self.open_new_account = BaseElement(self.driver, *LoggedInPanelLocators.OPEN_NEW_ACCOUNT)
        self.accounts_overview = BaseElement(self.driver, *LoggedInPanelLocators.ACCOUNTS_OVERVIEW)
        self.transfer_funds = BaseElement(self.driver, *LoggedInPanelLocators.TRANSFER_FUNDS)
        self.bill_pay = BaseElement(self.driver, *LoggedInPanelLocators.BILL_PAY)
        self.find_transactions = BaseElement(self.driver, *LoggedInPanelLocators.FIND_TRANSACTIONS)
        self.update_contact_info = BaseElement(self.driver, *LoggedInPanelLocators.UPDATE_CONTACT_INFO)
        self.request_loan = BaseElement(self.driver, *LoggedInPanelLocators.REQUEST_LOAN)
        self.log_out = BaseElement(self.driver, *LoggedInPanelLocators.LOG_OUT)

    def click_log_out(self):
        self.log_out.click()
        from .....parabank.src.pages.main_pages.home_page import HomePage
        return HomePage(self.driver)

    def click_open_new_account(self):
        self.open_new_account.click()
        from .....parabank.src.pages.account_services_pages.open_new_account_page import OpenNewAccountPage
        return OpenNewAccountPage(self.driver)

    def click_accounts_overview(self):
        self.accounts_overview.click()
        from .....parabank.src.pages.account_services_pages.accounts_overview_page import AccountsOverviewPage
        return AccountsOverviewPage(self.driver)

    def click_transfer_funds(self):
        self.transfer_funds.click()
        from .....parabank.src.pages.account_services_pages.transfer_funds_page import TransferFundsPage
        return TransferFundsPage(self.driver)

    def click_bill_pay(self):
        self.bill_pay.click()
        from .....parabank.src.pages.account_services_pages.bill_pay_page import BillPayPage
        return BillPayPage(self.driver)

    def click_find_transactions(self):
        self.find_transactions.click()
        from .....parabank.src.pages.account_services_pages.find_transactions_page import FindTransactionsPage
        return FindTransactionsPage(self.driver)

    def click_update_contact_info(self):
        self.update_contact_info.click()
        from .....parabank.src.pages.account_services_pages.update_profile_page import UpdateProfilePage
        return UpdateProfilePage(self.driver)

    def click_request_loan(self):
        self.request_loan.click()
        from .....parabank.src.pages.account_services_pages.request_loan_page import LoanRequestPage
        return LoanRequestPage(self.driver)

    # -------------------------------------
    # Logged In Panel switch implementation
    # -------------------------------------
    panel_options = {
        'log_out': click_log_out,
        'open_new_account': click_open_new_account,
        'accounts_overview': click_accounts_overview,
        'transfer_funds': click_transfer_funds,
        'bill_pay': click_bill_pay,
        'find_transactions': click_find_transactions,
        'update_contact_info': click_update_contact_info,
        'request_loan': click_request_loan
    }

    def click_link(self, option):
        return self.panel_options.get(option)(self)
