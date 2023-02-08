from selenium.webdriver.common.by import By


class UpdateProfileLocators:

    FIRST_NAME = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='customer.firstName']")
    LAST_NAME = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='customer.lastName']")
    ADDRESS = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='customer.address.street']")
    CITY = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='customer.address.city']")
    STATE = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='customer.address.state']")
    ZIP_CODE = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='customer.address.zipCode']")
    PHONE = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='customer.phoneNumber']")
    UPDATE_PROFILE_BUTTON = (By.XPATH, "//div[@id = 'rightPanel']//input[@class = 'button']")
    SUCCESS_MESSAGE = "Profile Updated"
    SUCCESS_HEADING = (By.XPATH, "//div[@id = 'rightPanel']//div[@ng-if='showResult']/h1[@class = 'title']")
    ERROR = (By.XPATH, "//div[@id = 'rightPanel']//span[contains(@class, 'error')]")
