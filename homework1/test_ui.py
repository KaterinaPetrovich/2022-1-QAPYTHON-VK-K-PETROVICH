import pytest
import conftest
from base import Basecase
import locators
import selenium
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

email = "katerina_petrovich@bk.ru"
password = "135qwe"
fio = "adc"


class TestUI(Basecase):

    def login(self):
        wait = WebDriverWait(self.driver, timeout=10)
        self.driver.get("https://target.my.com/")

        enter_button = wait.until(
            EC.element_to_be_clickable(locators.ENTER_BUTTON_LOCATOR))
        enter_button.click()
        email_field = self.find(locators.EMAIL_FIELD_LOCATOR)
        email_field.send_keys(email)
        password_field = self.find(
            locators.PASSWORD_FIELD_LOCATOR)
        password_field.send_keys(password)
        enter_login_button = self.find(locators.enter_login_button_locator)
        enter_login_button.click()

    @pytest.mark.UI
    def test_login(self):
        wait = WebDriverWait(self.driver, timeout=10)
        self.login()
        assert wait.until(
            EC.presence_of_element_located(locators.instruction_locator))

    @pytest.mark.UI
    def test_logout(self):
        wait = WebDriverWait(self.driver, timeout=10)
        self.login()
        username_button = wait.until(
            EC.visibility_of_element_located(
                locators.username_button_locator))
        username_button = wait.until(
            EC.element_to_be_clickable(
                locators.username_button_locator))

        username_button.click()

        try:
            wait.until(
                  EC.visibility_of_element_located(locators.logout_button_locator))
        except selenium.common.exceptions.TimeoutException:
            username_button.click()
            wait.until(EC.visibility_of_element_located(
                    locators.logout_button_locator))
        self.click(locators.logout_button_locator)




    @pytest.mark.UI
    def test_edit_contact_info(self):
        wait = WebDriverWait(self.driver, timeout=10)
        self.login()
        self.driver.get("https://target.my.com/profile/contacts")
        fio_field = wait.until(
            EC.presence_of_element_located(locators.FIO_LOCATOR))
        fio_field = wait.until(
            EC.visibility_of_element_located(locators.FIO_LOCATOR))

        fio_field.send_keys(fio)
        self.find(locators.SAVE_BUTTON_LOCATOR).click()

        assert wait.until(
            EC.presence_of_element_located(locators.SUCCESS_SAVE))
        fio_field.clear()

    @pytest.mark.UI
    @pytest.mark.parametrize("button_locator, page_locator",
                             [(locators.BALANCE_BUTTON_LOCATOR, locators.DEPOSIT_FORM_LOCATOR),
                              (locators.STAT_BUTTON_LOCATOR, locators.STAT_PAGE_LOCATOR)])
    def test_parametrized(self, button_locator, page_locator):
        wait = WebDriverWait(self.driver, timeout=10)
        self.login()
        button = wait.until(
                 EC.visibility_of_element_located(button_locator))
        button = wait.until(
                 EC.element_to_be_clickable(button_locator))
        button.click()
        assert wait.until(
                 EC.visibility_of_element_located(page_locator))
