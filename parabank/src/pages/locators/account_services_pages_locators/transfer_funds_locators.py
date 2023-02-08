from selenium.webdriver.common.by import By


class TransferFundsLocators:

    INPUT_AMOUNT = (By.XPATH, "//div[@id='rightPanel']//input[@id='amount']")
    DROPDOWN_FROM_ACCOUNT = (By.XPATH, "//div[@id='rightPanel']//select[@id='fromAccountId']")
    DROPDOWN_TO_ACCOUNT = (By.XPATH, "//div[@id='rightPanel']//select[@id='toAccountId']")
    TRANSFER_BUTTON = (By.XPATH, "//div[@id='rightPanel']//input[@value='Transfer']")
    SUCCESS_MESSAGE = "Transfer Complete!"
    SUCCESS_HEADING = (By.XPATH, "//div[@id = 'rightPanel']//div[@ng-if='showResult']/h1[@class = 'title']")
    ERROR = (By.XPATH, "//div[@id = 'rightPanel']//p[@class='error ng-scope']")
