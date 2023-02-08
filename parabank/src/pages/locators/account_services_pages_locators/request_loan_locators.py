from selenium.webdriver.common.by import By


class LoanRequestLocators:

    INPUT_AMOUNT = (By.XPATH, "//div[@id='rightPanel']//input[@id='amount']")
    INPUT_DOWN_PAYMENT = (By.XPATH, "//div[@id='rightPanel']//input[@id='downPayment']")
    DROPDOWN_ACCOUNT = (By.XPATH, "//div[@id='rightPanel']//select[@id='fromAccountId']")
    APPLY_BUTTON = (By.XPATH, "//div[@id='rightPanel']//input[@class='button'][@value='Apply Now']")
    SUCCESS_FORM = (By.XPATH, "//div[@id = 'rightPanel']//div[@ng-if='showResult']")
    LOAN_REQUEST_TABLE_LINE = (By.XPATH, "//div[@ng-controller='RequestLoanAppCtrl']//table/tbody/tr")
    LOAN_REQUEST_TABLE_CELL = "//tr[{}]/td[{}]"
    NEW_ACCOUNT_LINK = (By.XPATH, "//div[@id='rightPanel']//a[@id='newAccountId']")
    SUCCESS_MESSAGE = "Loan Request Processed"
    APPROVE_MESSAGE = "Congratulations, your loan has been approved."
