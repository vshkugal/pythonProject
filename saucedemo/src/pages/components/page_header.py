from ....src.base_element import BaseElement
from ....src.pages.exceptions.custom_exceptions import BaseElementException
from ....src.pages.locators.page_components_locators import PageHeaderLocators


class PageHeader:

    def __init__(self, driver):
        self.driver = driver
        self.shopping_cart_link = BaseElement(self.driver, *PageHeaderLocators.SHOPPING_CART_LINK)
        self.shopping_cart_badge = BaseElement(self.driver, *PageHeaderLocators.SHOPPING_CART_BADGE)
        self.open_menu_button = BaseElement(self.driver, *PageHeaderLocators.OPEN_MENU_BUTTON)
        self.close_menu_button = BaseElement(self.driver, *PageHeaderLocators.CLOSE_MENU_BUTTON)
        self.all_items_link = BaseElement(self.driver, *PageHeaderLocators.ALL_ITEMS_LINK)
        self.about_link = BaseElement(self.driver, *PageHeaderLocators.ABOUT_LINK)
        self.logout_link = BaseElement(self.driver, *PageHeaderLocators.LOGOUT_LINK)
        self.reset_link = BaseElement(self.driver, *PageHeaderLocators.RESET_LINK)
        self.page_section_title = BaseElement(self.driver, *PageHeaderLocators.PAGE_SECTION_TITLE)

    def get_cart_items_quantity(self):
        try:
            return self.shopping_cart_badge.get_text()
        except BaseElementException:
            return '0'

    def click_cart(self):
        self.shopping_cart_link.click()
        from ....src.pages.all_pages.cart_page import CartPage
        return CartPage(self.driver)

    def click_inventory(self):
        self.open_menu_button.click()
        self.all_items_link.click()
        from ....src.pages.all_pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)

    def click_about(self):
        self.open_menu_button.click()
        element = BaseElement(self.driver, *PageHeaderLocators.ABOUT_LINK)
        stripped = element.get_attribute("href").split("//")[-1].split("/")
        domain = stripped[0]
        directory = stripped[-1] if len(stripped) > 1 else ""
        element.click()
        from ....src.base_page import BasePage
        return BasePage(self.driver, domain=domain, directory=directory, title=None)

    def click_logout(self):
        self.open_menu_button.click()
        self.logout_link.click()
        from ....src.pages.all_pages.login_page import LoginPage
        return LoginPage(self.driver)

    # -------------------------------------
    # Header Panel switch implementation
    # -------------------------------------
    panel_options = {
        'cart': click_cart,
        'inventory': click_inventory,
        'about': click_about,
        'logout': click_logout
    }

    def click_link(self, option):
        return self.panel_options.get(option)(self)
