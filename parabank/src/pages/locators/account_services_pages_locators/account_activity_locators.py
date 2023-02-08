from selenium.webdriver.common.by import By
import re


class AccountActivityLocators:

    ACCOUNT_DETAILS_TABLE_LINE = (By.XPATH, "//div[@id='rightPanel']"
                                            "//div[@ng-controller='AccountDetailsCtrl']/table/tbody/tr")
    ACCOUNT_DETAILS_TABLE_CELL = "//div[@ng-controller='AccountDetailsCtrl']//tr[{}]/td[{}]"
    ACCOUNT_DETAILS_TABLE_FIRST_CELL = (By.XPATH, "//div[@ng-controller='AccountDetailsCtrl']//tr[1]/td[2]")
    ACCOUNT_ACTIVITY_TITLE = (By.XPATH, "//div[@id = 'rightPanel']//div[@ng-if='showActivity']//h1[@class = 'title']")
    ACCOUNT_ACTIVITY_TABLE_COLUMN = (By.XPATH, "//div[@id='rightPanel']//table[@id='transactionTable']/thead//th")
    ACCOUNT_ACTIVITY_TABLE_LINE = (By.XPATH, "//div[@id='rightPanel']//table[@id='transactionTable']/tbody/tr")
    ACCOUNT_ACTIVITY_TABLE_CELL = "//table[@id='transactionTable']//tr[{}]/td[{}]"
    ACCOUNT_ACTIVITY_TABLE_FIRST_CELL = (By.XPATH, "//table[@id='transactionTable']//tr[1]/td[1]")
    DROPDOWN_MONTH = (By.XPATH, "//div[@id='rightPanel']//select[@id='month']")
    DROPDOWN_TYPE = (By.XPATH, "//div[@id='rightPanel']//select[@id='transactionType']")
    GO_BUTTON = (By.XPATH, "//div[@id='rightPanel']//input[@class='button'][@value='Go']")
    STATUS_MESSAGE = (By.XPATH, "//div[@id='rightPanel']//p[@class='ng-scope']/b")
    NO_TRANSACTIONS_MESSAGE = "No transactions found."
    TRANSACTION_LINK = (By.XPATH, "//div[@id='rightPanel']//table[@id='transactionTable']/tbody/tr/td/"
                                  "a[contains(@href, 'transaction.htm')]")
    ID_REGEX = re.compile(r'\d\d\d\d\d')
