from pages.base_page import BasePage
import pytest
from locators import LoginPageLocators
from pages.main_page import MainPage


class LoginPage(BasePage):
    url = "https://target.my.com/"
    locators = LoginPageLocators()

    def login(self):
        self.driver.get(self.url)
        self.click(self.locators.ENTER_BUTTON_LOCATOR)
        self.send_keys(self.locators.EMAIL_FIELD_LOCATOR, "katerina_petrovich@bk.ru")
        self.send_keys(self.locators.PASSWORD_FIELD_LOCATOR, "135qwe")
        self.click(self.locators.ENTER_LOGIN_BUTTON_LOCATOR)
        return MainPage(self.driver)
