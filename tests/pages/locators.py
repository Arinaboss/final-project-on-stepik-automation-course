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
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1) .alertinner")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, ".btn-group a")
    MESSAGE = (By.CSS_SELECTOR, "#content_inner")
    PRODUCT = (By.CSS_SELECTOR, "[class='basket-items']")
    EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    PASSWORD = (By.CSS_SELECTOR, "[name='registration-password1']")
    DBLEPASSWORD = (By.CSS_SELECTOR, "[name='registration-password2']")
    BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")