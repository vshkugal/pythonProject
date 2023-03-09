from selenium.webdriver.common.by import By


class CartPageLocators:

    CART_QUANTITY_LABEL = (By.XPATH, "//div[@class = 'cart_quantity_label']")
    CART_DESC_LABEL = (By.XPATH, "//div[@class = 'cart_desc_label']")

    ITEM_QUANTITY = (By.XPATH, "//div[@class = 'cart_item']//div[@class = 'cart_quantity']")
    ITEM_NAME = (By.XPATH, "//div[@class = 'cart_item']//div[@class = 'inventory_item_name']")
    ITEM_LINK = (By.XPATH, "//div[@class = 'cart_item']//a[contains(@id, 'title_link')]")
    ITEM_DESCRIPTION = (By.XPATH, "//div[@class = 'cart_item']//div[@class = 'inventory_item_desc']")
    ITEM_PRICE = (By.XPATH, "//div[@class = 'cart_item']//div[@class = 'inventory_item_price']")
    ITEM_REMOVE_BUTTON = (By.XPATH, "//div[@class = 'cart_item']//button[contains(@id, 'remove')]")

    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//div[@class = 'cart_footer']//button[@id = 'continue-shopping']")
    CHECKOUT_BUTTON = (By.XPATH, "//div[@class = 'cart_footer']//button[@id = 'checkout']")
