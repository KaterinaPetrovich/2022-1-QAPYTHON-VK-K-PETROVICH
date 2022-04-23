from pages.base_page import BasePage
from locators import AboutPageLocators
from appium.webdriver.common.mobileby import By


class AboutPage(BasePage):
    locators = AboutPageLocators()

    def check_version(self, version):
        self.find((By.XPATH, f"//android.widget.TextView[contains(@text, 'Версия {version}')]"))
