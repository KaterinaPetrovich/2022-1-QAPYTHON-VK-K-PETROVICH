from tests.UI.pages.base_page import BasePage
from tests.UI.locators import LoginPageLocators


class LoginPage(BasePage):
    locators = LoginPageLocators()
    url = "http://app:8080/login"

    def login(self, username, password):
        self.send_keys(self.locators.USERNAME_FIELD, username)
        self.send_keys(self.locators.PASSWORD_FIELD, password)
        self.click(self.locators.LOGIN_BUTTON)