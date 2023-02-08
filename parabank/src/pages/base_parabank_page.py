from ....parabank.src.base_element import BaseElement
from ....parabank.src.base_page import BasePage
from ....parabank.src.pages.components.page_header import PageHeader
from ....parabank.src.pages.components.page_footer import PageFooter
from ....parabank.src.pages.components.page_login_panel import LoginPanel
from ....parabank.src.pages.components.page_logged_in_panel import LoggedInPanel
from ....parabank.src.pages.exceptions.custom_exceptions import BaseElementException, BasePageException
from ....parabank.src.pages.locators.page_components_locators import BaseParabankPageLocators
from ....parabank.src.pages.components.logger import ParabankLogger


class BaseParabankPage(BasePage):

    def __init__(self, driver, directory, title):
        BasePage.__init__(self, driver,
                          domain=BaseParabankPageLocators.DOMAIN,
                          title=title,
                          directory=directory)
        self.driver.get(self.expected_url)
        self.header = PageHeader(self.driver)
        self.footer = PageFooter(self.driver)
        self.login_panel = LoginPanel(self.driver)
        self.logged_in_panel = LoggedInPanel(self.driver)
        self.logger = ParabankLogger("parabank.log")

    def get_section_title(self):
        return BaseElement(self.driver, *BaseParabankPageLocators.PAGE_SECTION_TITLE).get_text()

    def get_section_info(self):
        text = []
        try:
            paragraphs = BaseElement(self.driver, *BaseParabankPageLocators.PAGE_SECTION_INFO).get_all_elements()
            for paragraph in paragraphs:
                text.append(paragraph.text)
        except BaseElementException:
            pass
        return text

    def print_section_info(self):
        self.logger.logger.info('\n'+self.get_section_title())
        text = self.get_section_info()
        for paragraph in text:
            if paragraph != "":
                self.logger.logger.info(paragraph)

    def get_left_panel_title(self):
        return BaseElement(self.driver, *BaseParabankPageLocators.LEFT_PANEL_TITLE).get_text()

    def is_logged_in(self):
        return bool(self.get_left_panel_title() == BaseParabankPageLocators.LOGGED_IN_TITLE)

    def is_logged_out(self):
        return bool(self.get_left_panel_title() == BaseParabankPageLocators.LOGGED_OUT_TITLE)

    def click_external_link(self, locator):
        element = BaseElement(self.driver, *locator)
        stripped = element.get_attribute("href").split("//")[-1].split("/")
        domain = stripped[0]
        directory = stripped[-1] if len(stripped) > 1 else ""
        element.click()
        return BasePage(self.driver, domain=domain, directory=directory, title=None)

    def is_on_correct_page(self):
        """
            There are common validation steps for any site page,
            thus they were unified under this method.
            This method validates:
            - expected and actual page URL
            - expected and actual page Title
            Based on the Page Object definitions
            :return: bool
        """
        expected_url, actual_url = self.expected_url, self.get_actual_url()
        if expected_url not in actual_url:
            raise BasePageException("Expected URL: '{}' Actual URL: '{}'".format(expected_url, actual_url))
        expected_title, actual_title = self.expected_title, self.get_actual_title()
        if expected_title not in actual_title:
            raise BasePageException("Expected Title: '{}' Actual Title: '{}'".format(expected_title, actual_title))
        return True
