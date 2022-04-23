from pages.base_page import BasePage
from pages.about_page import AboutPage
from pages.source_page import SourcePage
from locators import SettingsPageLocators



class SettingsPage(BasePage):
    locators = SettingsPageLocators()

    def open_about_page(self):
        self.click(self.locators.ABOUT_BUTTON)
        return AboutPage(self.driver)

    def open_source_page(self):
        self.click(self.locators.SOURCE_OF_NEWS)
        return SourcePage(self.driver)

