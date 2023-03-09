from selenium.webdriver.common.by import By


class PageHeaderLocators:

    SHOPPING_CART_LINK = (By.XPATH, "//div[@class = 'primary_header']//a[@class = 'shopping_cart_link']")
    SHOPPING_CART_BADGE = (By.XPATH, "//div[@class = 'primary_header']//a[@class = 'shopping_cart_link']"
                                     "/span[@class = 'shopping_cart_badge']")
    OPEN_MENU_BUTTON = (By.XPATH, "//div[@class = 'primary_header']//button[@id = 'react-burger-menu-btn']")
    # OPEN_MENU_BUTTON = (By.XPATH, "//div[@class = 'primary_header']//button[text() = 'Open Menu']")
    CLOSE_MENU_BUTTON = (By.XPATH, "//div[@class = 'primary_header']//button[@id = 'react-burger-cross-btn']")
    # CLOSE_MENU_BUTTON = (By.XPATH, "//div[@class = 'primary_header']//button[text() = 'Close Menu']")

    ALL_ITEMS_LINK = (By.XPATH, "//div[@class = 'bm-menu']//a[@id = 'inventory_sidebar_link']")
    ABOUT_LINK = (By.XPATH, "//div[@class = 'bm-menu']//a[@id = 'about_sidebar_link']")
    LOGOUT_LINK = (By.XPATH, "//div[@class = 'bm-menu']//a[@id = 'logout_sidebar_link']")
    RESET_LINK = (By.XPATH, "//div[@class = 'bm-menu']//a[@id = 'reset_sidebar_link']")

    PAGE_SECTION_TITLE = (By.XPATH, "//div[@class = 'header_secondary_container']//span[@class = 'title']")


class PageFooterLocators:

    TWITTER_LINK = (By.XPATH, "//footer[@class = 'footer']//li[@class = 'social_twitter']/a")
    # TWITTER_LINK = (By.XPATH, "//footer[@class = 'footer']//a[text() = 'Twitter']")
    FACEBOOK_LINK = (By.XPATH, "//footer[@class = 'footer']//li[@class = 'social_facebook']/a")
    # FACEBOOK_LINK = (By.XPATH, "//footer[@class = 'footer']//a[text() = 'Facebook']")
    LINKEDIN_LINK = (By.XPATH, "//footer[@class = 'footer']//li[@class = 'social_linkedin']/a")
    # LINKEDIN_LINK = (By.XPATH, "//footer[@class = 'footer']//a[text() = 'LinkedIn']")
    COPYRIGHT = (By.XPATH, "//footer[@class = 'footer']//div[@class = 'footer_copy']")
    ROBOT = (By.XPATH, "//footer[@class = 'footer']//img[@class = 'footer_robot']")
