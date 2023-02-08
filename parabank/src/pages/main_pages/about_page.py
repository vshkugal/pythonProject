from .....parabank.src.pages.base_parabank_page import BaseParabankPage
from .....parabank.src.pages.locators.main_pages_locators.about_page_locators import AboutPageLocators


class AboutPage(BaseParabankPage):

    def __init__(self, driver):
        BaseParabankPage.__init__(self, driver,
                                  title="ParaBank | About Us",
                                  directory="/about.htm")

    def click_visit(self):
        return self.click_external_link(AboutPageLocators.VISIT_LINK)
