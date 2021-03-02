from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "[name='login_submit']")
    LOGIN_REGISTER = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    BASKET = (By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
    BOOK = (By.CSS_SELECTOR, ".product_page .product_main h1")
    NAME = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1) strong")
    COST = (By.CSS_SELECTOR, ".product_page .product_main .price_color")
    PRICE = (By.CSS_SELECTOR, "#messages>.alert:nth-child(3) strong")