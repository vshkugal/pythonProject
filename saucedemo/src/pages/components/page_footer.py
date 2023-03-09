from ....src.base_element import BaseElement
from ....src.pages.locators.page_components_locators import PageFooterLocators


class PageFooter:

    def __init__(self, driver):
        self.driver = driver
        self.twitter_link = BaseElement(self.driver, *PageFooterLocators.TWITTER_LINK)
        self.facebook_link = BaseElement(self.driver, *PageFooterLocators.FACEBOOK_LINK)
        self.linkedin_link = BaseElement(self.driver, *PageFooterLocators.LINKEDIN_LINK)
        self.copyright = BaseElement(self.driver, *PageFooterLocators.COPYRIGHT)
        self.robot = BaseElement(self.driver, *PageFooterLocators.ROBOT)

    def get_copyright_msg(self):
        return self.copyright.get_text()

    def click_external_link(self, value):
        element = BaseElement(self.driver, *value)
        stripped = element.get_attribute("href").split("//")[-1].split("/")
        domain = stripped[0]
        directory = stripped[-1] if len(stripped) > 1 else ""
        element.click()
        from ....src.base_page import BasePage
        return BasePage(self.driver, domain=domain, directory=directory, title=None)

    def click_twitter(self):
        return self.click_external_link(PageFooterLocators.TWITTER_LINK)

    def click_facebook(self):
        return self.click_external_link(PageFooterLocators.FACEBOOK_LINK)

    def click_linkedin(self):
        return self.click_external_link(PageFooterLocators.LINKEDIN_LINK)

    # -------------------------------------
    # Footer Panel switch implementation
    # -------------------------------------
    panel_options = {
        'twitter': click_twitter,
        'facebook': click_facebook,
        'linkedin': click_linkedin
    }

    def click_link(self, option):
        return self.panel_options.get(option)(self)
