from selenium.common.exceptions import TimeoutException
from base import BaseCase
from appium.webdriver.common.mobileby import By
import pytest
from helper import get_version


class TestAndroid(BaseCase):

    @pytest.mark.Android
    def test_russia(self):
        self.main_page.send_question("Russia")
        try:
            self.main_page.swipe_element_lo_left(self.main_page.locators.SUGGESTION)
        except TimeoutException:
            self.main_page.send_keys(self.main_page.locators.TEXT_FIELD, "Russia")
            self.main_page.click(self.main_page.locators.SEND_BUTTON)
            self.main_page.swipe_element_lo_left(self.main_page.locators.SUGGESTION)
        self.main_page.click(self.main_page.locators.POPULATION)
        assert self.main_page.find((By.XPATH, self.main_page.locators.ELEMENT.format("146 млн.")))

    @pytest.mark.Android
    def test_calculator(self):
        self.main_page.send_question("2+3")
        assert self.main_page.find((By.XPATH, self.main_page.locators.ELEMENT.format("5")))

    @pytest.mark.Android
    def test_news_source(self):
        settingsPage = self.main_page.open_settings_page()
        settingsPage.swipe_up()
        settingsPage.swipe_up()
        sourcePage = settingsPage.open_source_page()
        sourcePage.click(sourcePage.locators.MAIL_RU)
        assert sourcePage.find(sourcePage.locators.SELECTED)
        sourcePage.click(sourcePage.locators.BACK_BUTTON)
        settingsPage.click(settingsPage.locators.CLOSE_BUTTON)
        self.main_page.send_question("News")
        assert self.main_page.find((By.XPATH, self.main_page.locators.ELEMENT.format("Включаю новости")))

    @pytest.mark.Android
    def test_settings(self):
        version = get_version()
        settingsPage = self.main_page.open_settings_page()
        settingsPage.swipe_up()
        settingsPage.swipe_up()
        aboutPage = settingsPage.open_about_page()
        assert aboutPage.check_version(version)
        assert aboutPage.find(aboutPage.locators.TRADE_MARK)
