# ----------------------------------------------------------------------------------------------------------------------
# Create universal wrapper for any web element on the page with Python Selenium WebDriver
# ----------------------------------------------------------------------------------------------------------------------

import time

from selenium.common import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ..src.pages.exceptions.custom_exceptions import BaseElementException


class BaseElement:

    DEFAULT_WAITING_TIME = 5

    def __init__(self, driver, by, locator):
        self.driver = driver
        self.by = by
        self.locator = locator

    def get_element(self, wait=DEFAULT_WAITING_TIME):
        self.wait_to_appear(wait)
        return self.driver.find_element(self.by, self.locator)

    def get_all_elements(self, wait=DEFAULT_WAITING_TIME):
        self.wait_to_appear(wait)
        return self.driver.find_elements(self.by, self.locator)

    def get_locator(self):
        return self.locator

    def get_text(self, encoding=None):
        text = self.get_element().text
        return text.encode(encoding) if encoding else text

    def get_attribute(self, value):
        return self.get_element().get_attribute(value)

    def is_selected(self):
        return self.get_element().is_selected()

    def is_checked(self):
        return self.driver.execute_script("return arguments[0].checked;", self.get_element())

    def exists(self):
        try:
            WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((self.by, self.locator)))
            return True
        except WebDriverException:
            return False

    def is_clickable(self):
        def is_clickable(by, locator):
            try:
                WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((by, locator)))
                return True
            except WebDriverException:
                return False

        return self.exists() and is_clickable(self.by, self.locator)

    def wait_to_be_clickable(self, seconds=DEFAULT_WAITING_TIME):
        start = time.time()
        while (time.time() - start) < seconds:
            if self.is_clickable():
                return self
            time.sleep(1)
        if self.exists():
            raise BaseElementException("Locator in the DOM: {} but did not become click-able in {} seconds"
                                       .format(self.locator, seconds))
        raise BaseElementException("Locator is not in the DOM and so not click-able: {}".format(self.locator))

    def is_not_empty_attribute(self, attr="class"):
        try:
            WebDriverWait(self.driver, 1).until(EC.text_to_be_present_in_element_attribute(
                (self.by, self.locator), attr, "not-empty"))
            return True
        except WebDriverException:
            return False

    def wait_until_not_empty(self, seconds=DEFAULT_WAITING_TIME, attr="class"):
        start = time.time()
        while (time.time() - start) < seconds:
            # if "not-empty" in self.get_attribute(attr):
            if self.is_not_empty_attribute(attr):
                return self
        raise BaseElementException("Locator: {} remained empty for {} seconds!".format(self.locator, seconds))

    def wait_until_content_not_empty(self, seconds=DEFAULT_WAITING_TIME):
        start = time.time()
        while (time.time() - start) < seconds:
            if self.get_text() != "":
                return self
        raise BaseElementException("Locator: {} remained empty for {} seconds!".format(self.locator, seconds))

    def is_not_visible(self, attr="class"):
        try:
            WebDriverWait(self.driver, 1).until(EC.text_to_be_present_in_element_attribute(
                (self.by, self.locator), attr, "ng-hide"))
            return True
        except WebDriverException:
            return False

    def wait_until_visible(self, seconds=DEFAULT_WAITING_TIME, attr="class"):
        start = time.time()
        while (time.time() - start) < seconds:
            # if "ng-hide" not in self.get_attribute(attr):
            if not self.is_not_visible(attr):
                return self
        raise BaseElementException("Locator: {} remained invisible for {} seconds!".format(self.locator, seconds))

    def wait_to_appear(self, seconds=DEFAULT_WAITING_TIME):
        start = time.time()
        while (time.time() - start) < seconds:
            if self.exists():
                return self
        raise BaseElementException("Locator: {} did not appear in {} seconds!".format(self.locator, seconds))

    def wait_to_disappear(self, seconds=DEFAULT_WAITING_TIME):
        start = time.time()
        while (time.time() - start) < seconds:
            try:
                WebDriverWait(self.driver, seconds).until(
                    EC.invisibility_of_element_located((self.by, self.locator)))
            except WebDriverException:
                raise BaseElementException("Locator: {} did not disappear in {} seconds!".format(self.locator, seconds))
        return self

    def click(self, wait=DEFAULT_WAITING_TIME, use_action_chains=False):
        self.wait_to_be_clickable(wait)
        if use_action_chains:
            ui_object = self.get_element()
            ActionChains(self.driver).move_to_element(ui_object).click().perform()
        else:
            try:
                self.get_element().click()
            except WebDriverException as error:
                try:
                    self.scroll_into_center()
                    self.get_element().click()
                except WebDriverException:
                    raise error
        return self

    def set_text(self, value, loose_focus=False):
        self.get_element().clear()
        self.get_element().send_keys(str(value))
        if loose_focus:
            self.press_key(Keys.TAB)
        return self

    def set_text_without_clear(self, value):
        self.get_element().send_keys(value)
        return self

    def scroll_into_center(self):
        scroll_element_into_middle = "var viewPortHeight = Math.max(document.documentElement.clientHeight, " \
                                     "window.innerHeight || 0); " \
                                     "var elementTop = arguments[0].getBoundingClientRect().top;" \
                                     "window.scrollBy(0, elementTop-(viewPortHeight/2));"
        self.driver.execute_script(scroll_element_into_middle, self.get_element())

    def scroll_into_view(self):
        self.driver.execute_script("arguments[0].scrollIntoView()", self.get_element())
        return self

    def press_key(self, key, use_action_chains=False):
        if not use_action_chains:
            self.get_element().send_keys(key)
        else:
            chains = ActionChains(driver=self.driver)
            chains.send_keys(key).perform()
        return self

    def mouse_over(self):
        ui_object = self.get_element()
        ActionChains(self.driver).move_to_element(ui_object).perform()
        return self


class Dropdown(BaseElement):

    OPTION = "//select[@class = '{}']/option[text() = '{}']"
    ALL_OPTIONS = "//select[@class = '{}']/option"
    ACTIVE_OPTION = "//span[@class = 'select_container']/span[@class = 'active_option']"

    def __init__(self, driver, by, locator, dropdown_id):
        BaseElement.__init__(self, driver, by, locator)
        self.dropdown_id = dropdown_id

    def select(self, value):
        self.get_element().click()
        try:
            self.driver.find_element(By.XPATH, Dropdown.OPTION.format(self.dropdown_id, value)).click()
        except WebDriverException:
            print("Value '{}' is not selectable in dropdown '{}'".format(value, self.dropdown_id))
        return self

    def get_dropdown_options(self):
        data = []
        options = self.driver.find_elements(By.XPATH, Dropdown.ALL_OPTIONS.format(self.dropdown_id))
        for option in options:
            data.append(str(option.text))
        return data

    def get_selected(self):
        return str(self.driver.find_element(By.XPATH, Dropdown.ACTIVE_OPTION).text)
