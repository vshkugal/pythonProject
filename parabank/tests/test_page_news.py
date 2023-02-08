from random import randint
from ...parabank.src.pages.main_pages.news_page import NewsPage


class TestPageNews:

    def test_news_page_functionality(self, driver):
        page = NewsPage(driver)
        page.logger.logger.info('\n'+page.get_section_title())
        headlines = page.get_news_headlines()
        rand = randint(1, len(headlines)-1)
        page.logger.logger.info('Random news #{}'.format(len(headlines)-rand))
        page.logger.logger.info(headlines[rand])
        page.logger.logger.info(page.find_news_by_headline(headlines[rand]))
        headline = page.get_news_headline_by_id(len(headlines)-rand)
        assert headline == headlines[rand]
