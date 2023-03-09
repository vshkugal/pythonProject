from selenium.webdriver.common.by import By


class LoginPageLocators:

    INPUT_USERNAME = (By.XPATH, "//div[@class = 'login-box']//input[@id = 'user-name']")
    INPUT_PASSWORD = (By.XPATH, "//div[@class = 'login-box']//input[@id = 'password']")
    LOGIN_BUTTON = (By.XPATH, "//div[@class = 'login-box']//input[@id = 'login-button']")
    ERROR_MESSAGE = (By.XPATH, "//div[@class = 'login-box']//h3[@data-test = 'error']")
    ERROR_BUTTON = (By.XPATH, "//div[@class = 'login-box']//button[@class = 'error-button']")
