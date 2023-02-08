from selenium.webdriver.common.by import By


class BaseParabankPageLocators:

    DOMAIN = "https://parabank.parasoft.com/parabank"
    PAGE_SECTION_TITLE = (By.XPATH, "//div[@id = 'rightPanel']//h1[@class = 'title']")
    PAGE_SECTION_INFO = (By.XPATH, "//div[@id = 'rightPanel']//p")
    LEFT_PANEL_TITLE = (By.XPATH, "//div[@id = 'leftPanel']/h2")
    LOGGED_IN_TITLE = "Account Services"
    LOGGED_OUT_TITLE = "Customer Login"


class LoggedInPanelLocators:

    OPEN_NEW_ACCOUNT = (By.XPATH, "//div[@id = 'leftPanel']//a[text() = 'Open New Account']")
    ACCOUNTS_OVERVIEW = (By.XPATH, "//div[@id = 'leftPanel']//a[text() = 'Accounts Overview']")
    TRANSFER_FUNDS = (By.XPATH, "//div[@id = 'leftPanel']//a[text() = 'Transfer Funds']")
    BILL_PAY = (By.XPATH, "//div[@id = 'leftPanel']//a[text() = 'Bill Pay']")
    FIND_TRANSACTIONS = (By.XPATH, "//div[@id = 'leftPanel']//a[text() = 'Find Transactions']")
    UPDATE_CONTACT_INFO = (By.XPATH, "//div[@id = 'leftPanel']//a[text() = 'Update Contact Info']")
    REQUEST_LOAN = (By.XPATH, "//div[@id = 'leftPanel']//a[text() = 'Request Loan']")
    LOG_OUT = (By.XPATH, "//div[@id = 'leftPanel']//a[text() = 'Log Out']")


class LoginPanelLocators:

    INPUT_USERNAME = (By.XPATH, "//div[@id = 'loginPanel']//input[@name = 'username']")
    INPUT_PASSWORD = (By.XPATH, "//div[@id = 'loginPanel']//input[@name = 'password']")
    LOGIN_BUTTON = (By.XPATH, "//div[@id = 'loginPanel']//input[@class = 'button']")
    FORGOT_LINK = (By.XPATH, "//div[@id = 'loginPanel']//a[text() = 'Forgot login info?']")
    REGISTER_LINK = (By.XPATH, "//div[@id = 'loginPanel']//a[text() = 'Register']")


class PageFooterLocators:

    HOME_LINK = (By.XPATH, "//div[@id = 'footerPanel']//a[text() = 'Home']")
    ABOUT_LINK = (By.XPATH, "//div[@id = 'footerPanel']//a[text() = 'About Us']")
    SERVICES_LINK = (By.XPATH, "//div[@id = 'footerPanel']//a[text() = 'Services']")
    PRODUCTS_LINK = (By.XPATH, "//div[@id = 'footerPanel']//a[text() = 'Products']")
    LOCATIONS_LINK = (By.XPATH, "//div[@id = 'footerPanel']//a[text() = 'Locations']")
    FORUM_LINK = (By.XPATH, "//div[@id = 'footerPanel']//a[text() = 'Forum']")
    SITEMAP_LINK = (By.XPATH, "//div[@id = 'footerPanel']//a[text() = 'Site Map']")
    CONTACT_LINK = (By.XPATH, "//div[@id = 'footerPanel']//a[text() = 'Contact Us']")
    COPYRIGHT_MESSAGE = (By.XPATH, "//p[@class='copyright']")
    VISIT_LINK = (By.XPATH, "//a[text() = 'www.parasoft.com']")


class PageHeaderLocators:

    ADMIN_TOP_LINK = (By.XPATH, "//div[@id = 'topPanel']//a[contains(@href, 'admin')]/img")
    PARABANK_TOP_LINK = (By.XPATH, "//div[@id = 'topPanel']//a[contains(@href, 'index')]/img")

    SOLUTIONS_HEADER = (By.XPATH, "//LI[@class='Solutions'][text()='Solutions']")
    ABOUT_LINK = (By.XPATH, "//div[@id = 'headerPanel']//a[text() = 'About Us']")
    SERVICES_LINK = (By.XPATH, "//div[@id = 'headerPanel']//a[text() = 'Services']")
    PRODUCTS_LINK = (By.XPATH, "//div[@id = 'headerPanel']//a[text() = 'Products']")
    LOCATIONS_LINK = (By.XPATH, "//div[@id = 'headerPanel']//a[text() = 'Locations']")
    ADMIN_LINK = (By.XPATH, "//div[@id = 'headerPanel']//a[text() = 'Admin Page']")

    HOME_BUTTON = (By.XPATH, "//UL[@class = 'button']//a[text() = 'home']")
    ABOUT_BUTTON = (By.XPATH, "//UL[@class = 'button']//a[text() = 'about']")
    CONTACT_BUTTON = (By.XPATH, "//UL[@class = 'button']//a[text() = 'contact']")
