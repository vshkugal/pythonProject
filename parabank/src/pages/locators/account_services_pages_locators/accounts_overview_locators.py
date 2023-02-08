from selenium.webdriver.common.by import By


class AccountsOverviewLocators:

    TABLE_COLUMN = (By.XPATH, "//div[@id='rightPanel']//table/thead//th")
    TABLE_DATA_LINE = (By.XPATH, "//div[@id='rightPanel']//table/tbody/tr")
    TABLE_DATA_CELL = "//div[@id='rightPanel']//table/tbody/tr[{}]/td[{}]"
    TABLE_DATA_FIRST_CELL = (By.XPATH, "//div[@id='rightPanel']//table/tbody/tr[1]/td[2]")
    ACCOUNT_LINK = (By.XPATH, "//div[@id='rightPanel']//table/tbody//td/a[contains(@href, 'activity.htm')]")
