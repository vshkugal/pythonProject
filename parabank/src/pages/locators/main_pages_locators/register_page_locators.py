from selenium.webdriver.common.by import By


class RegisterPageLocators:

    FIRST_NAME = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='customer.firstName']")
    LAST_NAME = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='customer.lastName']")
    ADDRESS = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='customer.address.street']")
    CITY = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='customer.address.city']")
    STATE = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='customer.address.state']")
    ZIP_CODE = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='customer.address.zipCode']")
    PHONE = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='customer.phoneNumber']")
    SSN = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='customer.ssn']")
    USERNAME = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='customer.username']")
    PASSWORD = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='customer.password']")
    CONFIRM = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='repeatedPassword']")
    ERROR = (By.XPATH, "//div[@id = 'rightPanel']//span[@class='error']")
    REGISTER_BUTTON = (By.XPATH, "//div[@id = 'rightPanel']//input[@class = 'button']")
    INITIAL_MESSAGE = "Signing up is easy!"
