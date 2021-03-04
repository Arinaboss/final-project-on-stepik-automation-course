from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
import time
from pages.locators import BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
        assert "login" in self.browser.current_url, "Login link is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "not login"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER), "not register"

    def register_new_user(self, email, password):
        address = self.browser.find_element(*BasePageLocators.EMAIL)
        address.click()
        address.send_keys(email)
        parol = self.browser.find_element(*BasePageLocators.PASSWORD)
        parol.click()
        parol.send_keys(password)
        dblpassword = self.browser.find_element(*BasePageLocators.DBLEPASSWORD)
        dblpassword.click()
        dblpassword.send_keys(password)
        button = self.browser.find_element(*BasePageLocators.BUTTON)
        button.click()


