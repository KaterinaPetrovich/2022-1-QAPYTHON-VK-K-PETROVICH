from base import BaseCase
import pytest

email = "katerina_petrovich@bk.ru"
wrong_password = "123"
password = "135qwe"


class TestUI(BaseCase):

    @pytest.mark.UI
    def test_wrong_password_login(self):
        self.logger.info("start")
        self.driver.get("https://target.my.com/")
        self.login_page.click(self.login_page.locators.ENTER_BUTTON_LOCATOR)
        self.login_page.send_keys(self.login_page.locators.EMAIL_FIELD_LOCATOR, email)
        self.logger.info("entering wrong password")
        self.login_page.send_keys(self.login_page.locators.PASSWORD_FIELD_LOCATOR, wrong_password)
        self.login_page.click(self.login_page.locators.ENTER_LOGIN_BUTTON_LOCATOR)
        self.logger.info("asserting")
        assert "error" in self.driver.current_url

    @pytest.mark.UI
    def test_invalid_login(self):
        self.logger.info("start")
        self.logger.info("going to login page")
        self.driver.get("https://target.my.com/")
        self.logger.info("entering credentials")
        self.login_page.click(self.login_page.locators.ENTER_BUTTON_LOCATOR)
        self.login_page.send_keys(self.login_page.locators.EMAIL_FIELD_LOCATOR, "email")
        self.login_page.send_keys(self.login_page.locators.PASSWORD_FIELD_LOCATOR, wrong_password)
        self.login_page.click(self.login_page.locators.ENTER_LOGIN_BUTTON_LOCATOR)
        self.logger.info("asserting")
        assert self.login_page.find(self.login_page.locators.WRONG_LOGIN_NOTIFY)

    @pytest.mark.UI
    def test_segment_creation(self, login, random_str):
        self.logger.info("start")
        self.logger.info("logging in")
        main_page = login
        main_page.find(self.main_page.locators.NOTIFICATION) or \
        main_page.find(self.main_page.locators.LOGO)
        main_page.click(self.main_page.locators.SEGMENTS_BUTTON)
        self.logger.info("creating segment with random generated name")
        self.segment_page.create_segment(random_str)
        self.logger.info("asserting")
        assert self.segment_page.find(
            self.segment_page.locators.get_created_segment_locator(random_str))

    @pytest.mark.UI
    def test_segment_deletion(self, login, random_str):
        self.logger.info("start")
        self.logger.info("logging in")
        main_page = login
        main_page.find(self.main_page.locators.NOTIFICATION) or \
        main_page.find(self.main_page.locators.LOGO)
        main_page.click(self.main_page.locators.SEGMENTS_BUTTON)
        self.logger.info("creating segment with random generated name")
        self.segment_page.create_segment(random_str)
        self.logger.info("deleting segment")
        self.segment_page.click(self.segment_page.locators.get_delete_icon_locator(random_str))
        self.segment_page.click(self.segment_page.locators.DELETE_BUTTON)
        self.segment_page.send_keys(self.segment_page.locators.SEARCH_INPUT, random_str)
        self.logger.info("asserting")
        assert self.segment_page.find(self.segment_page.locators.NOTHING_NOTIFICATION)

    @pytest.mark.UI
    def test_campaign_creation(self, login, file_path, random_str):
        self.logger.info("start")
        self.logger.info("logging in")
        main_page = login
        main_page.find(self.main_page.locators.LOGO)
        main_page.click(self.main_page.locators.CREATE_CAMPAIGN_BUTTON)
        self.campaign_page.find(self.campaign_page.locators.TITLE)
        self.logger.info("creating campaign from file")
        self.campaign_page.click(self.campaign_page.locators.IMPORT_FROM_FILE_BUTTON)
        self.campaign_page.click(self.campaign_page.locators.MY_TARGET_RADIOBUTTON)
        self.campaign_page.find(self.campaign_page.locators.INPUT_FILE).send_keys(file_path)
        self.campaign_page.click(self.campaign_page.locators.INPUT_SUBMIT_BUTTON)
        self.campaign_page.send_keys(self.campaign_page.locators.CAMPAIGN_NAME_INPUT, random_str)
        self.campaign_page.click(self.campaign_page.locators.CREATE_CAMPAIGN_BUTTON)
        self.logger.info("asserting")
        assert self.campaign_page.find(self.campaign_page.locators.CREATED_NOTIFY)
