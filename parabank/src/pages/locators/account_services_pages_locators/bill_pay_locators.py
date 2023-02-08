from selenium.webdriver.common.by import By


class BillPayLocators:

    INPUT_NAME = (By.XPATH, "//div[@id='rightPanel']//input[@name='payee.name']")
    INPUT_ADDRESS = (By.XPATH, "//div[@id='rightPanel']//input[@name='payee.address.street']")
    INPUT_CITY = (By.XPATH, "//div[@id='rightPanel']//input[@name='payee.address.city']")
    INPUT_STATE = (By.XPATH, "//div[@id='rightPanel']//input[@name='payee.address.state']")
    INPUT_ZIP_CODE = (By.XPATH, "//div[@id='rightPanel']//input[@name='payee.address.zipCode']")
    INPUT_PHONE = (By.XPATH, "//div[@id='rightPanel']//input[@name='payee.phoneNumber']")
    INPUT_ACCOUNT = (By.XPATH, "//div[@id='rightPanel']//input[@name='payee.accountNumber']")
    INPUT_ACCOUNT_VERIFY = (By.XPATH, "//div[@id='rightPanel']//input[@name='verifyAccount']")
    INPUT_AMOUNT = (By.XPATH, "//div[@id='rightPanel']//input[@name='amount']")
    DROPDOWN_FROM_ACCOUNT = (By.XPATH, "//div[@id='rightPanel']//select[@name='fromAccountId']")
    SEND_PAYMENT_BUTTON = (By.XPATH, "//div[@id='rightPanel']//input[@value='Send Payment']")
    SUCCESS_FORM = (By.XPATH, "//div[@id = 'rightPanel']//div[@ng-show='showResult']")
    SUCCESS_HEADING = (By.XPATH, "//div[@id = 'rightPanel']//div[@ng-show='showResult']/h1[@class = 'title']")
    SUCCESS_MESSAGE = "Bill Payment Complete"
    ERROR = (By.XPATH, "//div[@id = 'rightPanel']//span[@class='error']")
