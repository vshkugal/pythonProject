from .....parabank.src.base_element import BaseElement
from .....parabank.src.pages.locators.page_components_locators import LoginPanelLocators


class LoginPanel:

    def __init__(self, driver):
        self.driver = driver
        self.input_username = BaseElement(self.driver, *LoginPanelLocators.INPUT_USERNAME)
        self.input_password = BaseElement(self.driver, *LoginPanelLocators.INPUT_PASSWORD)
        self.login_button = BaseElement(self.driver, *LoginPanelLocators.LOGIN_BUTTON)
        self.forgot_link = BaseElement(self.driver, *LoginPanelLocators.FORGOT_LINK)
        self.register_link = BaseElement(self.driver, *LoginPanelLocators.REGISTER_LINK)

    def enter_username(self, username):
        self.input_username.set_text(username)

    def enter_password(self, password):
        self.input_password.set_text(password)

    def login_user_simplified(self, user_data):
        self.enter_username(user_data)
        self.enter_password(user_data)
        self.login_button.click()

    def click_forgot(self):
        self.forgot_link.click()
        from .....parabank.src.pages.main_pages.lookup_page import LookupPage
        return LookupPage(self.driver)

    def click_register(self):
        self.register_link.click()
        from .....parabank.src.pages.main_pages.register_page import RegisterPage
        return RegisterPage(self.driver)
