from selenium.webdriver.common.by import By
import re


class FindTransactionsLocators:

    DROPDOWN_ACCOUNT = (By.XPATH, "//div[@id='rightPanel']//select[@id='accountId']")
    INPUT_BY_ID = (By.XPATH, "//div[@id='rightPanel']//input[@id='criteria.transactionId']")
    BUTTON_BY_ID = (By.XPATH, "//div[@id='rightPanel']//button[contains(@ng-click, 'ID')]")
    INPUT_BY_DATE = (By.XPATH, "//div[@id='rightPanel']//input[@id='criteria.onDate']")
    BUTTON_BY_DATE = (By.XPATH, "//div[@id='rightPanel']//button[contains(@ng-click, 'DATE')]")
    INPUT_FROM_DATE = (By.XPATH, "//div[@id='rightPanel']//input[@id='criteria.fromDate']")
    INPUT_TO_DATE = (By.XPATH, "//div[@id='rightPanel']//input[@id='criteria.toDate']")
    BUTTON_BY_DATE_RANGE = (By.XPATH, "//div[@id='rightPanel']//button[contains(@ng-click, 'DATE_RANGE')]")
    INPUT_BY_AMOUNT = (By.XPATH, "//div[@id='rightPanel']//input[@id='criteria.amount']")
    BUTTON_BY_AMOUNT = (By.XPATH, "//div[@id='rightPanel']//button[contains(@ng-click, 'AMOUNT')]")
    SUCCESS_MESSAGE = "Transaction Results"
    SUCCESS_FORM = (By.XPATH, "//div[@id = 'rightPanel']//div[@ng-if='showResult']")
    ERROR_FORM = (By.XPATH, "//div[@id = 'rightPanel']//div[@ng-if='showError']")
    TRANSACTIONS_TABLE_COLUMN = (By.XPATH, "//div[@id='rightPanel']//table[@id='transactionTable']/thead//th")
    TRANSACTIONS_TABLE_LINE = (By.XPATH, "//div[@id='rightPanel']//table[@id='transactionTable']/tbody/tr")
    TRANSACTIONS_TABLE_CELL = "//table[@id='transactionTable']//tr[{}]/td[{}]"
    TRANSACTIONS_TABLE_FIRST_CELL = (By.XPATH, "//table[@id='transactionTable']//tr[1]/td[1]")
    TRANSACTION_LINK = (By.XPATH, "//div[@id='rightPanel']//table[@id='transactionTable']/tbody/tr/td/"
                                  "a[contains(@href, 'transaction.htm')]")
    ID_REGEX = re.compile(r'\d\d\d\d\d')
