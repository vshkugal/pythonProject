from .....parabank.src.base_element import BaseElement
from .....parabank.src.pages.base_parabank_page import BaseParabankPage
from .....parabank.src.pages.exceptions.custom_exceptions import BaseElementException
from .....parabank.src.pages.locators.main_pages_locators.contact_page_locators import ContactPageLocators


class ContactPage(BaseParabankPage):

    def __init__(self, driver):
        BaseParabankPage.__init__(self, driver,
                                  title="ParaBank | Customer Care",
                                  directory="/contact.htm")

        self.input_name = BaseElement(self.driver, *ContactPageLocators.NAME)
        self.input_email = BaseElement(self.driver, *ContactPageLocators.EMAIL)
        self.input_phone = BaseElement(self.driver, *ContactPageLocators.PHONE)
        self.input_message = BaseElement(self.driver, *ContactPageLocators.MESSAGE)
        self.inputs = [self.input_name, self.input_email, self.input_phone, self.input_message]
        self.error = BaseElement(self.driver, *ContactPageLocators.ERROR)
        self.send_button = BaseElement(self.driver, *ContactPageLocators.SEND_BUTTON)

    def input_contact_information(self, name, email, phone, message):
        self.input_name.set_text(name)
        self.input_email.set_text(email)
        self.input_phone.set_text(phone)
        self.input_message.set_text(message)

    def input_contact_information_simplified(self, value):
        for item in self.inputs:
            item.set_text(value)

    def print_contact_errors(self):
        try:
            errors = self.error.get_all_elements()
            if errors:
                self.logger.logger.warning('\nContact form errors:')
                for error in errors:
                    self.logger.logger.warning(error.text)
        except BaseElementException:
            pass
