from .....parabank.src.base_element import BaseElement
from .....parabank.src.pages.base_parabank_page import BaseParabankPage
from .....parabank.src.pages.locators.main_pages_locators.home_page_locators import HomePageLocators


class HomePage(BaseParabankPage):

    def __init__(self, driver):
        BaseParabankPage.__init__(self, driver,
                                  title="ParaBank | Welcome | Online Banking",
                                  directory="/index.htm")

        self.services_link = BaseElement(self.driver, *HomePageLocators.SERVICES_LINK)
        self.news_main_link = BaseElement(self.driver, *HomePageLocators.NEWS_MAIN_LINK)
        self.news_links = BaseElement(self.driver, *HomePageLocators.NEWS_LINK).get_all_elements()

    def click_services(self):
        self.services_link.click()
        from .....parabank.src.pages.main_pages.services_page import ServicesPage
        return ServicesPage(self.driver)

    def click_news(self):
        self.news_main_link.click()
        from .....parabank.src.pages.main_pages.news_page import NewsPage
        return NewsPage(self.driver)

    def print_latest_news(self):
        headlines = []
        for link in self.news_links:
            headlines.append(link.text)
        from .....parabank.src.pages.main_pages.news_page import NewsPage
        page = NewsPage(self.driver)
        self.logger.logger.info('')
        for headline in headlines:
            self.logger.logger.info(headline)
            self.logger.logger.info(page.find_news_by_headline(headline))
        return page
