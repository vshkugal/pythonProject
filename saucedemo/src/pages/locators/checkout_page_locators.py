from selenium.webdriver.common.by import By


class CheckoutPageLocators1:

    FIRST_NAME_INPUT = (By.XPATH, "//div[@class = 'checkout_info']//input[@id = 'first-name']")
    LAST_NAME_INPUT = (By.XPATH, "//div[@class = 'checkout_info']//input[@id = 'last-name']")
    POSTAL_CODE_INPUT = (By.XPATH, "//div[@class = 'checkout_info']//input[@id = 'postal-code']")
    ERROR_MESSAGE = (By.XPATH, "//div[@class = 'checkout_info']//h3[@data-test = 'error']")
    ERROR_CLOSE_BUTTON = (By.XPATH, "//div[@class = 'checkout_info']//button[@class = 'error-button']")
    CANCEL_BUTTON = (By.XPATH, "//div[@class = 'checkout_buttons']//button[@id = 'cancel']")
    CONTINUE_BUTTON = (By.XPATH, "//div[@class = 'checkout_buttons']//input[@id = 'continue']")


class CheckoutPageLocators2:

    ITEM_QUANTITY = (By.XPATH, "//div[@class = 'cart_item']//div[@class = 'cart_quantity']")
    ITEM_NAME = (By.XPATH, "//div[@class = 'cart_item']//div[@class = 'inventory_item_name']")
    ITEM_LINK = (By.XPATH, "//div[@class = 'cart_item']//a[contains(@id, 'title_link')]")
    ITEM_DESCRIPTION = (By.XPATH, "//div[@class = 'cart_item']//div[@class = 'inventory_item_desc']")
    ITEM_PRICE = (By.XPATH, "//div[@class = 'cart_item']//div[@class = 'inventory_item_price']")
    SUMMARY_INFO = (By.XPATH, "//div[@class = 'summary_info']/div[contains(@class, 'summary')]")
    CANCEL_BUTTON = (By.XPATH, "//div[@class = 'cart_footer']//button[@id = 'cancel']")
    FINISH_BUTTON = (By.XPATH, "//div[@class = 'cart_footer']//button[@id = 'finish']")


class CheckoutPageLocators3:

    INFO_LABEL = (By.XPATH, "//div[@class = 'checkout_complete_container']//h2[@class = 'complete-header']")
    INFO_TEXT = (By.XPATH, "//div[@class = 'checkout_complete_container']//div[@class = 'complete-text']")
    INFO_LOGO = (By.XPATH, "//div[@class = 'checkout_complete_container']//img[@class = 'pony_express']")
    BACK_HOME_BUTTON = (By.XPATH, "//div[@class = 'checkout_complete_container']//button[@id = 'back-to-products']")
