from tests.UI.pages.base_page import BasePage
from tests.UI.locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    locators = RegistrationPageLocators()
    url = "http://app:8080/reg"

    def register(self, name, surname, middle_name, username, password, email, not_match=None):
        self.send_keys(self.locators.USER_NAME_FIELD, name)
        self.send_keys(self.locators.SURNAME_FIELD, surname)
        self.send_keys(self.locators.USERNAME_FIELD, username)
        self.send_keys(self.locators.MIDDLENAME_FIELD, middle_name)
        self.send_keys(self.locators.PASSWORD_FIELD, password)
        if not_match:
            self.send_keys(self.locators.REPEAT_PASSWORD_FIELD, "password")
        else:
            self.send_keys(self.locators.REPEAT_PASSWORD_FIELD, password)
        self.send_keys(self.locators.EMAIL_FIELD, email)
        self.click(self.locators.CHECKBOX)
        self.click(self.locators.REGISTER_BUTTON)
