from .....parabank.src.base_element import BaseElement
from .....parabank.src.pages.locators.page_components_locators import PageFooterLocators


class PageFooter:

    def __init__(self, driver):
        self.driver = driver
        self.home_link = BaseElement(self.driver, *PageFooterLocators.HOME_LINK)
        self.about_link = BaseElement(self.driver, *PageFooterLocators.ABOUT_LINK)
        self.services_link = BaseElement(self.driver, *PageFooterLocators.SERVICES_LINK)
        self.products_link = BaseElement(self.driver, *PageFooterLocators.PRODUCTS_LINK)
        self.locations_link = BaseElement(self.driver, *PageFooterLocators.LOCATIONS_LINK)
        self.forum_link = BaseElement(self.driver, *PageFooterLocators.FORUM_LINK)
        self.sitemap_link = BaseElement(self.driver, *PageFooterLocators.SITEMAP_LINK)
        self.contact_link = BaseElement(self.driver, *PageFooterLocators.CONTACT_LINK)
        self.copyright_message = BaseElement(self.driver, *PageFooterLocators.COPYRIGHT_MESSAGE)
        self.visit_link = BaseElement(self.driver, *PageFooterLocators.VISIT_LINK)

    def click_home(self):
        self.home_link.click()
        from .....parabank.src.pages.main_pages.home_page import HomePage
        return HomePage(self.driver)

    def click_about(self):
        self.about_link.click()
        from .....parabank.src.pages.main_pages.about_page import AboutPage
        return AboutPage(self.driver)

    def click_services(self):
        self.services_link.click()
        from .....parabank.src.pages.main_pages.services_page import ServicesPage
        return ServicesPage(self.driver)

    def click_sitemap(self):
        self.sitemap_link.click()
        from .....parabank.src.pages.main_pages.sitemap_page import SitemapPage
        return SitemapPage(self.driver)

    def click_contact(self):
        self.contact_link.click()
        from .....parabank.src.pages.main_pages.contact_page import ContactPage
        return ContactPage(self.driver)

    def get_copyright_msg(self):
        return self.copyright_message.get_text()

    def click_external_link(self, value):
        element = BaseElement(self.driver, *value)
        stripped = element.get_attribute("href").split("//")[-1].split("/")
        domain = stripped[0]
        directory = stripped[-1] if len(stripped) > 1 else ""
        element.click()
        from .....parabank.src.base_page import BasePage
        return BasePage(self.driver, domain=domain, directory=directory, title=None)

    def click_products(self):
        return self.click_external_link(PageFooterLocators.PRODUCTS_LINK)

    def click_locations(self):
        return self.click_external_link(PageFooterLocators.LOCATIONS_LINK)

    def click_forum(self):
        return self.click_external_link(PageFooterLocators.FORUM_LINK)

    def click_visit(self):
        return self.click_external_link(PageFooterLocators.VISIT_LINK)

    # -------------------------------------
    # Footer Panel switch implementation
    # -------------------------------------
    panel_options = {
        'home': click_home,
        'about': click_about,
        'services': click_services,
        'sitemap': click_sitemap,
        'contact': click_contact,
        'products': click_products,
        'locations': click_locations,
        'forum': click_forum,
        'visit': click_visit
    }

    def click_link(self, option):
        return self.panel_options.get(option)(self)
