from .....parabank.src.base_element import BaseElement
from .....parabank.src.pages.base_parabank_page import BaseParabankPage
from .....parabank.src.pages.locators.account_services_pages_locators.update_profile_locators import UpdateProfileLocators
from .....parabank.src.pages.exceptions.custom_exceptions import BaseElementException


class UpdateProfilePage(BaseParabankPage):

    def __init__(self, driver):
        BaseParabankPage.__init__(self, driver,
                                  title="ParaBank | Update Profile",
                                  directory="/updateprofile.htm")
        self.input_first_name = BaseElement(self.driver, *UpdateProfileLocators.FIRST_NAME)
        self.input_last_name = BaseElement(self.driver, *UpdateProfileLocators.LAST_NAME)
        self.input_address = BaseElement(self.driver, *UpdateProfileLocators.ADDRESS)
        self.input_city = BaseElement(self.driver, *UpdateProfileLocators.CITY)
        self.input_state = BaseElement(self.driver, *UpdateProfileLocators.STATE)
        self.input_zip_code = BaseElement(self.driver, *UpdateProfileLocators.ZIP_CODE)
        self.input_phone = BaseElement(self.driver, *UpdateProfileLocators.PHONE)
        self.inputs = [self.input_first_name, self.input_last_name, self.input_address, self.input_city,
                       self.input_state, self.input_zip_code, self.input_phone]
        self.update_profile_button = BaseElement(self.driver, *UpdateProfileLocators.UPDATE_PROFILE_BUTTON)

    @staticmethod
    def _update_field(field: BaseElement, value):
        field.wait_until_not_empty()
        field.set_text(value)

    def update_profile(self, values):
        for i in range(len(self.inputs)):
            self._update_field(self.inputs[i], values[i])
        self.update_profile_button.click()

    def update_profile_simplified(self, value):
        for item in self.inputs:
            self._update_field(item, value)
        self.update_profile_button.click()

    def is_updated(self):
        try:
            return bool(BaseElement(self.driver, *UpdateProfileLocators.SUCCESS_HEADING).get_text() ==
                        UpdateProfileLocators.SUCCESS_MESSAGE)
        except BaseElementException:
            return False

    def print_update_profile_errors(self):
        try:
            errors = BaseElement(self.driver, *UpdateProfileLocators.ERROR).get_all_elements()
            if errors:
                self.logger.logger.warning('\nUpdate Profile form errors:')
                for error in errors:
                    self.logger.logger.warning(error.text)
        except BaseElementException:
            pass
