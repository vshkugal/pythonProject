from selenium import webdriver


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
        self.__expected_url = "{domain}{directory}".format(domain=domain, directory=directory)
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
