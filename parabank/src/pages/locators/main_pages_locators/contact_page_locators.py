from selenium.webdriver.common.by import By


class ContactPageLocators:

    NAME = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='name']")
    EMAIL = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='email']")
    PHONE = (By.XPATH, "//div[@id = 'rightPanel']//input[@id='phone']")
    MESSAGE = (By.XPATH, "//div[@id = 'rightPanel']//textarea[@id='message']")
    ERROR = (By.XPATH, "//div[@id = 'rightPanel']//span[@class='error']")
    SEND_BUTTON = (By.XPATH, "//div[@id = 'rightPanel']//input[@class = 'button']")
