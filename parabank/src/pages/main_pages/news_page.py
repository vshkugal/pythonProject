from selenium.webdriver.common.by import By
from .....parabank.src.base_element import BaseElement
from .....parabank.src.pages.base_parabank_page import BaseParabankPage
from .....parabank.src.pages.locators.main_pages_locators.news_page_locators import NewsPageLocators


class NewsPage(BaseParabankPage):

    def __init__(self, driver):
        BaseParabankPage.__init__(self, driver,
                                  title="ParaBank | News",
                                  directory="/news.htm")
        self.headline = BaseElement(self.driver, *NewsPageLocators.HEADLINE)

    def get_news_headlines(self):
        text = []
        headlines = self.headline.get_all_elements()
        for headline in headlines:
            text.append(headline.text)
        return text

    def get_news_headline_by_id(self, news_id):
        return BaseElement(self.driver, By.XPATH, NewsPageLocators.HEADLINE_BY_ID.format(news_id)).get_text()

    def print_news_headlines(self):
        headlines = self.get_news_headlines()
        for headline in headlines:
            self.logger.logger.info(headline)

    def find_news_by_headline(self, headline):
        info = self.get_section_info()
        for i in range(len(info)):
            if info[i] == headline:
                return info[i+1]
