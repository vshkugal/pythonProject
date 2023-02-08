from .....parabank.src.base_element import BaseElement
from .....parabank.src.pages.base_parabank_page import BaseParabankPage
from .....parabank.src.pages.locators.main_pages_locators.sitemap_page_locators import SitemapPageLocators


class SitemapPage(BaseParabankPage):

    def __init__(self, driver):
        BaseParabankPage.__init__(self, driver,
                                  title="ParaBank | Site Map",
                                  directory="/sitemap.htm")

        self.about_link = BaseElement(self.driver, *SitemapPageLocators.ABOUT_LINK)
        self.services_link = BaseElement(self.driver, *SitemapPageLocators.SERVICES_LINK)
        self.admin_link = BaseElement(self.driver, *SitemapPageLocators.ADMIN_LINK)

        self.open_new_account = BaseElement(self.driver, *SitemapPageLocators.OPEN_NEW_ACCOUNT)
        self.accounts_overview = BaseElement(self.driver, *SitemapPageLocators.ACCOUNTS_OVERVIEW)
        self.transfer_funds = BaseElement(self.driver, *SitemapPageLocators.TRANSFER_FUNDS)
        self.bill_pay = BaseElement(self.driver, *SitemapPageLocators.BILL_PAY)
        self.find_transactions = BaseElement(self.driver, *SitemapPageLocators.FIND_TRANSACTIONS)
        self.update_contact_info = BaseElement(self.driver, *SitemapPageLocators.UPDATE_CONTACT_INFO)
        self.request_loan = BaseElement(self.driver, *SitemapPageLocators.REQUEST_LOAN)
        self.log_out = BaseElement(self.driver, *SitemapPageLocators.LOG_OUT)

    def click_about(self):
        self.about_link.click()
        from .....parabank.src.pages.main_pages.about_page import AboutPage
        return AboutPage(self.driver)

    def click_services(self):
        self.services_link.click()
        from .....parabank.src.pages.main_pages.services_page import ServicesPage
        return ServicesPage(self.driver)

    def click_admin(self):
        self.admin_link.click()
        from .....parabank.src.pages.main_pages.admin_page import AdminPage
        return AdminPage(self.driver)

    def click_products(self):
        return self.click_external_link(SitemapPageLocators.PRODUCTS_LINK)

    def click_locations(self):
        return self.click_external_link(SitemapPageLocators.LOCATIONS_LINK)

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

    def click_log_out(self):
        self.log_out.click()
        from .....parabank.src.pages.main_pages.home_page import HomePage
        return HomePage(self.driver)

    # -------------------------------------
    # Sitemap Page switch implementation
    # -------------------------------------
    panel_options = {
        'about': click_about,
        'services': click_services,
        'products': click_products,
        'locations': click_locations,
        'admin': click_admin,
        'open_new_account': click_open_new_account,
        'accounts_overview': click_accounts_overview,
        'transfer_funds': click_transfer_funds,
        'bill_pay': click_bill_pay,
        'find_transactions': click_find_transactions,
        'update_contact_info': click_update_contact_info,
        'request_loan': click_request_loan,
        'log_out': click_log_out
    }

    def click_link(self, option):
        return self.panel_options.get(option)(self)
