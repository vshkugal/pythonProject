from selenium.webdriver.common.by import By


class SitemapPageLocators:

    ABOUT_LINK = (By.XPATH, "//div[@id = 'rightPanel']//a[text() = 'About Us']")
    SERVICES_LINK = (By.XPATH, "//div[@id = 'rightPanel']//a[text() = 'Services']")
    PRODUCTS_LINK = (By.XPATH, "//div[@id = 'rightPanel']//a[text() = 'Products']")
    LOCATIONS_LINK = (By.XPATH, "//div[@id = 'rightPanel']//a[text() = 'Locations']")
    ADMIN_LINK = (By.XPATH, "//div[@id = 'rightPanel']//a[text() = 'Admin Page']")

    OPEN_NEW_ACCOUNT = (By.XPATH, "//div[@id = 'rightPanel']//a[text() = 'Open New Account']")
    ACCOUNTS_OVERVIEW = (By.XPATH, "//div[@id = 'rightPanel']//a[text() = 'Accounts Overview']")
    TRANSFER_FUNDS = (By.XPATH, "//div[@id = 'rightPanel']//a[text() = 'Transfer Funds']")
    BILL_PAY = (By.XPATH, "//div[@id = 'rightPanel']//a[text() = 'Bill Pay']")
    FIND_TRANSACTIONS = (By.XPATH, "//div[@id = 'rightPanel']//a[text() = 'Find Transactions']")
    UPDATE_CONTACT_INFO = (By.XPATH, "//div[@id = 'rightPanel']//a[text() = 'Update Contact Info']")
    REQUEST_LOAN = (By.XPATH, "//div[@id = 'rightPanel']//a[text() = 'Request Loan']")
    LOG_OUT = (By.XPATH, "//div[@id = 'rightPanel']//a[text() = 'Log Out']")
