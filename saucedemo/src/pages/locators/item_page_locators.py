from selenium.webdriver.common.by import By


class ItemPageLocators:

    BACK_TO_PRODUCTS_BUTTON = (By.XPATH, "//button[@id = 'back-to-products']")
    ITEM_IMG = (By.XPATH, "//div[@class = 'inventory_details_img_container']/img")
    ITEM_LABEL = (By.XPATH, "//DIV[@class='inventory_details_name large_size']/self::DIV")
    ITEM_DESCRIPTION = (By.XPATH, "//DIV[@class='inventory_details_desc large_size']/self::DIV")
    ITEM_PRICE = (By.XPATH, "//div[@class = 'inventory_details_price']")
    ITEM_ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(@class, 'btn_inventory')]")
