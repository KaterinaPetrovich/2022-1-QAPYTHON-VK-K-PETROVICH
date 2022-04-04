import pytest
from base import Basecase
import locators
from helper import login


class TestUI(Basecase):

    @pytest.mark.UI
    def test_login(self):
        login(self)
        assert "dashboard" in self.driver.current_url

    @pytest.mark.UI
    def test_logout(self):
        login(self)
        self.find(locators.NOTIFICATION) or self.find(locators.LOGO)
        self.click(locators.USERNAME_BUTTON_LOCATOR)
        logout_button = self.find(locators.LOGOUT_BUTTON_LOCATOR)
        self.driver.execute_script("arguments[0].click();", logout_button)
        assert "https://target.my.com/" == self.driver.current_url

    @pytest.mark.UI
    def test_edit_contact_info(self):
        login(self)
        self.driver.get("https://target.my.com/profile/contacts")
        self.send_keys(locators.FIO_LOCATOR, "fio")
        self.click(locators.SAVE_BUTTON_LOCATOR)
        assert self.find(locators.SUCCESS_SAVE)

    @pytest.mark.UI
    @pytest.mark.parametrize("button_locator, key_word",
                             [(locators.BALANCE_BUTTON_LOCATOR, "billing"),
                              (locators.STAT_BUTTON_LOCATOR, "statistics")])
    def test_parametrized(self, button_locator, key_word):
        login(self)
        self.find(locators.NOTIFICATION) or self.find(locators.LOGO)
        self.click(button_locator)
        assert key_word in self.driver.current_url
