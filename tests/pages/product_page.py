from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from pages.locators import BasePageLocators
import time


class ProductPage(BasePage):
    def add_to_cart(self):
        cart = self.browser.find_element(*ProductPageLocators.BASKET)
        cart.click()

    def name_book_in_cart(self):
        books = self.browser.find_element(*ProductPageLocators.BOOK)
        cart_book = self.browser.find_element(*ProductPageLocators.NAME)
        assert books.text == cart_book.text, f"expect {books.text} got {cart_book.text}"
        print(books.text, cart_book.text)

    def price_check(self):
        price = self.browser.find_element(*ProductPageLocators.COST)
        cart_price = self.browser.find_element(*ProductPageLocators.PRICE)
        assert price.text == cart_price.text, f"expect {price.text} got {cart_price.text}"
        print(price.text, cart_price.text)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def element_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "The message did not disappear"








