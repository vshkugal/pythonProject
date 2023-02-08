from .....parabank.src.base_element import BaseElement
from .....parabank.src.pages.base_parabank_page import BaseParabankPage
from .....parabank.src.pages.exceptions.custom_exceptions import BaseElementException
from .....parabank.src.pages.locators.main_pages_locators.services_page_locators import ServicesPageLocators


class ServicesPage(BaseParabankPage):

    def __init__(self, driver):
        BaseParabankPage.__init__(self, driver,
                                  title="ParaBank | Services",
                                  directory="/services.htm")

        self.table_heading = BaseElement(self.driver, *ServicesPageLocators.TABLE_HEADING)

    def get_service_tables_headings(self):
        text = []
        try:
            headings = self.table_heading.get_all_elements()
            for heading in headings:
                text.append(heading.text)
        except BaseElementException:
            pass
        return text
