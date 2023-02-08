from .....parabank.src.base_element import BaseElement
from .....parabank.src.pages.locators.page_components_locators import PageHeaderLocators


class PageHeader:

    def __init__(self, driver):
        self.driver = driver
        self.admin_top_link = BaseElement(self.driver, *PageHeaderLocators.ADMIN_TOP_LINK)
        self.parabank_top_link = BaseElement(self.driver, *PageHeaderLocators.PARABANK_TOP_LINK)
        self.about_link = BaseElement(self.driver, *PageHeaderLocators.ABOUT_LINK)
        self.services_link = BaseElement(self.driver, *PageHeaderLocators.SERVICES_LINK)
        self.products_link = BaseElement(self.driver, *PageHeaderLocators.PRODUCTS_LINK)
        self.locations_link = BaseElement(self.driver, *PageHeaderLocators.LOCATIONS_LINK)
        self.admin_link = BaseElement(self.driver, *PageHeaderLocators.ADMIN_LINK)
        self.home_button = BaseElement(self.driver, *PageHeaderLocators.HOME_BUTTON)
        self.about_button = BaseElement(self.driver, *PageHeaderLocators.ABOUT_BUTTON)
        self.contact_button = BaseElement(self.driver, *PageHeaderLocators.CONTACT_BUTTON)

    def click_admin_top(self):
        self.admin_top_link.click()
        from .....parabank.src.pages.main_pages.admin_page import AdminPage
        return AdminPage(self.driver)

    def click_parabank_top(self):
        self.parabank_top_link.click()
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

    def click_admin(self):
        self.admin_link.click()
        from .....parabank.src.pages.main_pages.admin_page import AdminPage
        return AdminPage(self.driver)

    def click_home_button(self):
        self.contact_button.click()
        from .....parabank.src.pages.main_pages.home_page import HomePage
        return HomePage(self.driver)

    def click_about_button(self):
        self.about_button.click()
        from .....parabank.src.pages.main_pages.about_page import AboutPage
        return AboutPage(self.driver)

    def click_contact_button(self):
        self.contact_button.click()
        from .....parabank.src.pages.main_pages.contact_page import ContactPage
        return ContactPage(self.driver)

    def click_external_link(self, value):
        element = BaseElement(self.driver, *value)
        stripped = element.get_attribute("href").split("//")[-1].split("/")
        domain = stripped[0]
        directory = stripped[-1] if len(stripped) > 1 else ""
        element.click()
        from .....parabank.src.base_page import BasePage
        return BasePage(self.driver, domain=domain, directory=directory, title=None)

    def click_products(self):
        return self.click_external_link(PageHeaderLocators.PRODUCTS_LINK)

    def click_locations(self):
        return self.click_external_link(PageHeaderLocators.LOCATIONS_LINK)

    # -------------------------------------
    # Header Panel switch implementation
    # -------------------------------------
    panel_options = {
        'admin_top': click_admin_top,
        'parabank_top': click_parabank_top,
        'about': click_about,
        'services': click_services,
        'admin': click_admin,
        'home_button': click_home_button,
        'about_button': click_about_button,
        'contact_button': click_contact_button,
        'products': click_products,
        'locations': click_locations
    }

    def click_link(self, option):
        return self.panel_options.get(option)(self)
