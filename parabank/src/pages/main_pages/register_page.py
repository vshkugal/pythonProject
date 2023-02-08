from .....parabank.src.base_element import BaseElement
from .....parabank.src.pages.base_parabank_page import BaseParabankPage
from .....parabank.src.pages.exceptions.custom_exceptions import BaseElementException
from .....parabank.src.pages.locators.main_pages_locators.register_page_locators import RegisterPageLocators


class RegisterPage(BaseParabankPage):

    def __init__(self, driver):
        BaseParabankPage.__init__(self, driver,
                                  title="ParaBank | Register for Free Online Account Access",
                                  directory="/register.htm")
        self.input_first_name = BaseElement(self.driver, *RegisterPageLocators.FIRST_NAME)
        self.input_last_name = BaseElement(self.driver, *RegisterPageLocators.LAST_NAME)
        self.input_address = BaseElement(self.driver, *RegisterPageLocators.ADDRESS)
        self.input_city = BaseElement(self.driver, *RegisterPageLocators.CITY)
        self.input_state = BaseElement(self.driver, *RegisterPageLocators.STATE)
        self.input_zip_code = BaseElement(self.driver, *RegisterPageLocators.ZIP_CODE)
        self.input_phone = BaseElement(self.driver, *RegisterPageLocators.PHONE)
        self.input_ssn = BaseElement(self.driver, *RegisterPageLocators.SSN)
        self.input_username = BaseElement(self.driver, *RegisterPageLocators.USERNAME)
        self.input_password = BaseElement(self.driver, *RegisterPageLocators.PASSWORD)
        self.input_confirm = BaseElement(self.driver, *RegisterPageLocators.CONFIRM)
        self.inputs = [self.input_first_name, self.input_last_name, self.input_address, self.input_city,
                       self.input_state, self.input_zip_code, self.input_phone, self.input_ssn,
                       self.input_username, self.input_password, self.input_confirm]
        self.error = BaseElement(self.driver, *RegisterPageLocators.ERROR)
        self.register_button = BaseElement(self.driver, *RegisterPageLocators.REGISTER_BUTTON)

    def register_user(self, values):
        for i in range(len(self.inputs)):
            self.inputs[i].set_text(values[i])
        self.register_button.click()

    def register_user_simplified(self, value):
        for item in self.inputs:
            item.set_text(value)
        self.register_button.click()

    def print_registration_errors(self):
        try:
            errors = self.error.get_all_elements()
            if errors:
                self.logger.logger.warning('\nRegistration form errors:')
                for error in errors:
                    self.logger.logger.warning(error.text)
        except BaseElementException:
            pass

    def is_registered(self):
        return bool('Welcome' in self.get_section_title())

    def is_not_registered(self):
        self.print_registration_errors()
        return bool(self.get_section_title() == RegisterPageLocators.INITIAL_MESSAGE)
