from pages.base_page import BasePage
from .locators import BasePageLocators



class BasketPage(BasePage):
    def go_to_cart(self):
        basket = self.browser.find_element(*BasePageLocators.BASKET)
        basket.click()

    def basked_is_empty(self):
        message = "Your basket is empty"
        basket = self.browser.find_element(*BasePageLocators.MESSAGE)
        assert message in basket.text, f"expected {message} got {basket.text}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*BasePageLocators.PRODUCT), \
            "Success message is presented, but should not be"

