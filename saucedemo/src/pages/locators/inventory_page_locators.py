from selenium.webdriver.common.by import By


class InventoryPageLocators:

    SORT_ITEMS_DROPDOWN = (By.XPATH, "//span[@class = 'select_container']//select[@class = 'product_sort_container']")
    ITEM_IMG = (By.XPATH, "//div[@class = 'inventory_item_img']//img")
    ITEM_IMG_LINK = (By.XPATH, "//div[@class = 'inventory_item_img']//a")
    ITEM_LABEL = (By.XPATH, "//div[@class = 'inventory_item_name']")
    ITEM_LABEL_LINK = (By.XPATH, "//div[@class = 'inventory_item_label']//a")
    ITEM_DESCRIPTION = (By.XPATH, "//div[@class = 'inventory_item_label']//div[@class = 'inventory_item_desc']")
    ITEM_PRICE = (By.XPATH, "//div[@class = 'inventory_item']//div[@class = 'inventory_item_price']")
    ITEM_ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(@class, 'btn_inventory')]")
