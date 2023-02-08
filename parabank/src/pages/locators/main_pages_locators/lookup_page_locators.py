from selenium.webdriver.common.by import By


class LookupPageLocators:

    FIRST_NAME = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='firstName']")
    LAST_NAME = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='lastName']")
    ADDRESS = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='address.street']")
    CITY = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='address.city']")
    STATE = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='address.state']")
    ZIP_CODE = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='address.zipCode']")
    SSN = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='ssn']")
    ERROR = (By.XPATH, "//div[@id = 'rightPanel']//span[@class='error']")
    LOOKUP_BUTTON = (By.XPATH, "//div[@id = 'rightPanel']//input[@class = 'button']")
    MESSAGE_SUCCESS = "Your login information was located successfully. You are now logged in."
    MESSAGE_ERROR = "Error!"
