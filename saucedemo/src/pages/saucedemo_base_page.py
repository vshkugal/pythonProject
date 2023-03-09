from ...src.base_element import BaseElement
from ...src.base_page import BasePage
from ...src.pages.components.logger import SaucedemoLogger
from ...src.pages.components.page_constants import *
from ...src.pages.components.page_footer import PageFooter
from ...src.pages.components.page_header import PageHeader


class SaucedemoBasePage(BasePage):

    def __init__(self, driver, directory):
        BasePage.__init__(self, driver,
                          domain=SAUCEDEMO_MAIN,
                          title=SAUCEDEMO_TITLE,
                          directory=directory)
        self.driver.get(self.expected_url)
        self.header = PageHeader(self.driver)
        self.footer = PageFooter(self.driver)
        self.logger = SaucedemoLogger(SAUCEDEMO_LOG)

    def get_section_title(self):
        return self.header.page_section_title.get_text()

    def click_external_link(self, locator):
        element = BaseElement(self.driver, *locator)
        stripped = element.get_attribute("href").split("//")[-1].split("/")
        domain = stripped[0]
        directory = stripped[-1] if len(stripped) > 1 else ""
        element.click()
        return BasePage(self.driver, domain=domain, directory=directory, title=None)
