from .....parabank.src.base_element import BaseElement
from .....parabank.src.pages.base_parabank_page import BaseParabankPage
from .....parabank.src.pages.exceptions.custom_exceptions import BaseElementException
from .....parabank.src.pages.locators.main_pages_locators.lookup_page_locators import LookupPageLocators


class LookupPage(BaseParabankPage):

    def __init__(self, driver):
        BaseParabankPage.__init__(self, driver,
                                  title="ParaBank | Customer Lookup",
                                  directory="/lookup.htm")
        self.input_first_name = BaseElement(self.driver, *LookupPageLocators.FIRST_NAME)
        self.input_last_name = BaseElement(self.driver, *LookupPageLocators.LAST_NAME)
        self.input_address = BaseElement(self.driver, *LookupPageLocators.ADDRESS)
        self.input_city = BaseElement(self.driver, *LookupPageLocators.CITY)
        self.input_state = BaseElement(self.driver, *LookupPageLocators.STATE)
        self.input_zip_code = BaseElement(self.driver, *LookupPageLocators.ZIP_CODE)
        self.input_ssn = BaseElement(self.driver, *LookupPageLocators.SSN)
        self.inputs = [self.input_first_name, self.input_last_name, self.input_address, self.input_city,
                       self.input_state, self.input_zip_code, self.input_ssn]
        self.error = BaseElement(self.driver, *LookupPageLocators.ERROR)
        self.lookup_button = BaseElement(self.driver, *LookupPageLocators.LOOKUP_BUTTON)

    def lookup_user(self, values):
        for i in range(len(self.inputs)):
            self.inputs[i].set_text(values[i])
        self.lookup_button.click()

    def lookup_user_simplified(self, value):
        for item in self.inputs:
            item.set_text(value)
        self.lookup_button.click()

    def print_lookup_errors(self):
        try:
            errors = self.error.get_all_elements()
            if errors:
                self.logger.logger.warning('\nLookup form errors:')
                for error in errors:
                    self.logger.logger.warning(error.text)
        except BaseElementException:
            pass

    def is_found(self):
        return bool(LookupPageLocators.MESSAGE_SUCCESS in self.get_section_info())

    def is_not_found(self):
        self.print_lookup_errors()
        return bool(self.get_section_title() == LookupPageLocators.MESSAGE_ERROR)
