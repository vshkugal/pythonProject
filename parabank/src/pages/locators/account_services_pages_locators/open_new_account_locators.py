from selenium.webdriver.common.by import By


class OpenNewAccountLocators:

    DROPDOWN_TYPE = (By.XPATH, "//div[@id='rightPanel']//select[@id='type']")
    DROPDOWN_FROM_ACCOUNT = (By.XPATH, "//div[@id='rightPanel']//select[@id='fromAccountId']")
    OPEN_BUTTON = (By.XPATH, "//div[@id = 'rightPanel']//input[@class = 'button']")
    SUCCESS_MESSAGE = "Account Opened!"
    SUCCESS_HEADING = (By.XPATH, "//div[@id = 'rightPanel']//div[@ng-if='showResult']/h1[@class = 'title']")
    ERROR = (By.XPATH, "//div[@id = 'rightPanel']//p[@class='error ng-scope']")
    ACCOUNT_LINK = (By.XPATH, "//div[@id='rightPanel']//a[@id='newAccountId']")
