from selenium import webdriver
from ..src.pages.exceptions.custom_exceptions import BasePageException


class BasePage:
    def __init__(self, driver, domain, directory, title):
        """
        This class will be inherited by all the Page Objects
        :param domain: STRING, Base domain of the website aka "https://parabank.parasoft.com/parabank"
                               Base domain & expected URL will be used to open this page
        :param directory: STRING, expected URL of the page that is inheriting this class aka:
                                  "/index.htm" or "/about.htm"
        :param title: STRING, expected Title of the page that is inheriting this class
        """
        self.__title = title
        self.__directory = directory
        self.__domain = domain
        self.__expected_url = f"{domain}{directory}"
        self.driver: webdriver = driver

    @property
    def expected_directory(self):
        return self.__directory

    @property
    def expected_domain(self):
        return self.__domain

    @property
    def expected_title(self):
        return self.__title

    @property
    def expected_url(self):
        return self.__expected_url

    def get_actual_title(self):
        return self.driver.title

    def get_actual_url(self):
        return self.driver.current_url

    def open(self):
        """
        This method will open the page which inherited BasePage
        :return: self (Page Object which inherited BasePage will be returned)
        """
        self.driver.get(self.expected_url)
        return self

    def is_on_correct_page(self):
        """
            There are common validation steps for any site page,
            thus they were unified under this method.
            This method validates:
            - expected and actual page URL
            - expected and actual page Title
            Based on the Page Object definitions
            :return: bool
        """
        expected_url, actual_url = self.expected_url, self.get_actual_url()
        if expected_url not in actual_url:
            raise BasePageException(f"Expected URL: '{expected_url}' Actual URL: '{actual_url}'")
        expected_title, actual_title = self.expected_title, self.get_actual_title()
        if expected_title not in actual_title:
            raise BasePageException(f"Expected Title: '{expected_title}' Actual Title: '{actual_title}'")
        return True
