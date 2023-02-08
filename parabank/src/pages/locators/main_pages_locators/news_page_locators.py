from selenium.webdriver.common.by import By


class NewsPageLocators:

    HEADLINE = (By.XPATH, "//div[@id = 'rightPanel']//a[@class = 'headline']")
    HEADLINE_BY_ID = "//div[@id = 'rightPanel']//a[@class = 'headline'][@id = '{}']"
