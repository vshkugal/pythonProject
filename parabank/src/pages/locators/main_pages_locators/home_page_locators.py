from selenium.webdriver.common.by import By


class HomePageLocators:

    SERVICES_LINK = (By.XPATH, "//div[@id = 'rightPanel']//a[contains(@href, 'services')][text()='Read More']")
    NEWS_MAIN_LINK = (By.XPATH, "//div[@id = 'rightPanel']//a[contains(@href, 'news')][text()='Read More']")
    NEWS_LINK = (By.XPATH, "//div[@id = 'rightPanel']//a[contains(@href, 'news')][contains(@href, '#')]")
