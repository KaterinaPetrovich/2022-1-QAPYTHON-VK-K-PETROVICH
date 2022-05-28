from pages.base_page import BasePage
from pages.settings_page import SettingsPage
from locators import MainPageLocators
import time


class MainPage(BasePage):
    locators = MainPageLocators()

    def send_question(self, text):
        self.click(self.locators.KEYBOARD_BUTTON)
        self.send_keys(self.locators.TEXT_FIELD, text)
        self.send_keys(self.locators.TEXT_FIELD, text)
        self.click(self.locators.SEND_BUTTON)

    def open_settings_page(self):
        self.click(self.locators.BURGER_MENU_BUTTON)
        return SettingsPage(self.driver)
