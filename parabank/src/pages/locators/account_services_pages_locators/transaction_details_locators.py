from selenium.webdriver.common.by import By


class TransactionDetailsLocators:

    TRANSACTION_DETAILS_TABLE_LINE = (By.XPATH, "//div[@id='rightPanel']//table/tbody/tr")
    TRANSACTION_DETAILS_TABLE_CELL = "//tr[{}]/td[{}]"
    TRANSACTION_DETAILS_TABLE_FIRST_CELL = (By.XPATH, "//tr[1]/td[2]")
