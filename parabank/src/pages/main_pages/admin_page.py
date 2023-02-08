from .....parabank.src.base_element import BaseElement, Dropdown
from .....parabank.src.pages.base_parabank_page import BaseParabankPage
from .....parabank.src.pages.exceptions.custom_exceptions import BaseElementException
from .....parabank.src.pages.locators.main_pages_locators.admin_page_locators import AdminPageLocators


class AdminPage(BaseParabankPage):

    def __init__(self, driver):
        BaseParabankPage.__init__(self, driver,
                                  title="ParaBank | Administration",
                                  directory="/admin.htm")

        self.status_message = BaseElement(self.driver, *AdminPageLocators.STATUS_MESSAGE)
        self.database_initialize_button = BaseElement(self.driver, *AdminPageLocators.DATABASE_INITIALIZE_BUTTON)
        self.database_clean_button = BaseElement(self.driver, *AdminPageLocators.DATABASE_CLEAN_BUTTON)

        self.jms_service_status_message = BaseElement(self.driver, *AdminPageLocators.JMS_SERVICE_STATUS_MESSAGE)
        self.jms_service_button = BaseElement(self.driver, *AdminPageLocators.JMS_SERVICE_BUTTON)

        self.radio_button_soap = BaseElement(self.driver, *AdminPageLocators.RADIO_BUTTON_SOAP)
        self.radio_button_rest_xml = BaseElement(self.driver, *AdminPageLocators.RADIO_BUTTON_REST_XML)
        self.radio_button_rest_json = BaseElement(self.driver, *AdminPageLocators.RADIO_BUTTON_REST_JSON)
        self.radio_button_jdbc = BaseElement(self.driver, *AdminPageLocators.RADIO_BUTTON_JDBC)
        self.radio_buttons = [self.radio_button_soap, self.radio_button_rest_xml, self.radio_button_rest_json,
                              self.radio_button_jdbc]

        self.link_wsdl = BaseElement(self.driver, *AdminPageLocators.LINK_WSDL)
        self.link_wadl = BaseElement(self.driver, *AdminPageLocators.LINK_WADL)
        self.link_swagger = BaseElement(self.driver, *AdminPageLocators.LINK_SWAGGER)
        self.link_loan_wsdl = BaseElement(self.driver, *AdminPageLocators.LINK_LOAN_WSDL)

        self.dropdown_provider = Dropdown(self.driver, *AdminPageLocators.DROPDOWN_LOAN_PROVIDER, "loanProvider")
        self.dropdown_processor = Dropdown(self.driver, *AdminPageLocators.DROPDOWN_LOAN_PROCESSOR, "loanProcessor")
        self.dropdowns = [self.dropdown_provider, self.dropdown_processor]

        self.input_soap_endpoint = BaseElement(self.driver, *AdminPageLocators.INPUT_SOAP_ENDPOINT)
        self.input_rest_endpoint = BaseElement(self.driver, *AdminPageLocators.INPUT_REST_ENDPOINT)
        self.input_endpoint = BaseElement(self.driver, *AdminPageLocators.INPUT_ENDPOINT)

        self.input_init_balance = BaseElement(self.driver, *AdminPageLocators.INPUT_INIT_BALANCE)
        self.input_min_balance = BaseElement(self.driver, *AdminPageLocators.INPUT_MIN_BALANCE)
        self.input_threshold = BaseElement(self.driver, *AdminPageLocators.INPUT_THRESHOLD)
        self.error = BaseElement(self.driver, *AdminPageLocators.ERROR)

        self.submit_button = BaseElement(self.driver, *AdminPageLocators.SUBMIT_BUTTON)

    def get_status_message(self):
        try:
            return self.status_message.get_text()
        except BaseElementException:
            return ""

    def is_success(self):
        return bool(self.get_status_message() == AdminPageLocators.SUCCESS_MESSAGE)

    def get_jms_service_status_message(self):
        return self.jms_service_status_message.get_text()

    def get_jms_service_button_name(self):
        return self.jms_service_button.get_attribute("value")

    def get_selected_radio_button(self):
        for radio_button in self.radio_buttons:
            if radio_button.is_selected():
                return radio_button.get_attribute("value").upper()

    def click_link_wsdl(self):
        return self.click_external_link(AdminPageLocators.LINK_WSDL)

    def click_link_wadl(self):
        return self.click_external_link(AdminPageLocators.LINK_WADL)

    def click_link_swagger(self):
        return self.click_external_link(AdminPageLocators.LINK_SWAGGER)

    def click_link_loan_wsdl(self):
        return self.click_external_link(AdminPageLocators.LINK_LOAN_WSDL)

    # ---------------------------------------------------
    # Admin Page switch implementation for external links
    # ---------------------------------------------------
    panel_options = {
        'wsdl': click_link_wsdl,
        'wadl': click_link_wadl,
        'swagger': click_link_swagger,
        'loan_wsdl': click_link_loan_wsdl
    }

    def click_link(self, option):
        return self.panel_options.get(option)(self)

    def input_web_form_data(self, soap, rest, loan):
        self.input_soap_endpoint.set_text(soap)
        self.input_rest_endpoint.set_text(rest)
        self.input_endpoint.set_text(loan)

    def input_web_form_data_simplified(self, value):
        self.input_web_form_data(value, value, value)

    def input_app_form_data(self, init, min, threshold):
        self.input_init_balance.set_text(init)
        self.input_min_balance.set_text(min)
        self.input_threshold.set_text(threshold)

    def input_app_form_data_simplified(self, value):
        self.input_app_form_data(value, value, value)

    def print_admin_form_errors(self):
        try:
            errors = self.error.get_all_elements()
            if errors:
                self.logger.logger.warning('\nApplication Settings form errors:')
                for error in errors:
                    self.logger.logger.warning(f"{error.get_attribute('id')} : {error.text}")
        except BaseElementException:
            pass
