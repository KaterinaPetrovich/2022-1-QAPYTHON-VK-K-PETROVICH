from base import BaseCase
import pytest

email = "katerina_petrovich@bk.ru"
wrong_password = "123"
password = "135qwe"


class TestUI(BaseCase):

    @pytest.mark.UI
    @pytest.mark.skip("skip")
    def test_wrong_password_login(self):
        self.driver.get("https://target.my.com/")
        self.login_page.click(self.login_page.locators.ENTER_BUTTON_LOCATOR)
        self.login_page.send_keys(self.login_page.locators.EMAIL_FIELD_LOCATOR, email)
        self.login_page.send_keys(self.login_page.locators.PASSWORD_FIELD_LOCATOR, wrong_password)
        self.login_page.click(self.login_page.locators.ENTER_LOGIN_BUTTON_LOCATOR)

        assert self.login_page.find(self.login_page.locators.REGISTRATION_BUTTON)

    @pytest.mark.UI
    @pytest.mark.skip("skip")
    def test_invalid_login(self):

        self.driver.get("https://target.my.com/")

        self.login_page.click(self.login_page.locators.ENTER_BUTTON_LOCATOR)
        self.login_page.send_keys(self.login_page.locators.EMAIL_FIELD_LOCATOR, "email")
        self.login_page.send_keys(self.login_page.locators.PASSWORD_FIELD_LOCATOR, wrong_password)
        self.login_page.click(self.login_page.locators.ENTER_LOGIN_BUTTON_LOCATOR)

        assert self.login_page.find(self.login_page.locators.WRONG_LOGIN_NOTIFY)

    @pytest.mark.UI
    @pytest.mark.skip("skip")
    def test_segment_creation(self, login, random_str):

        main_page = login
        main_page.find(self.main_page.locators.NOTIFICATION) or \
        main_page.find(self.main_page.locators.LOGO)
        main_page.click(self.main_page.locators.SEGMENTS_BUTTON)

        self.segment_page.create_segment(random_str)

        assert self.segment_page.find(
            self.segment_page.locators.get_created_segment_locator(random_str))

    @pytest.mark.UI
    def test_segment_deletion(self, login, random_str):

        main_page = login
        main_page.find(self.main_page.locators.NOTIFICATION) or \
        main_page.find(self.main_page.locators.LOGO)
        main_page.click(self.main_page.locators.SEGMENTS_BUTTON)

        self.segment_page.create_segment(random_str)
        self.segment_page.delete_segment(random_str)

        self.segment_page.send_keys(self.segment_page.locators.SEARCH_INPUT, random_str)

        assert self.segment_page.find(self.segment_page.locators.NOTHING_NOTIFICATION)

    @pytest.mark.skip("skip")
    def test_campaign_creation(self, login, path_to_campaign_data_file, random_str):

        main_page = login
        main_page.find(self.main_page.locators.LOGO)
        main_page.click(self.main_page.locators.CREATE_CAMPAIGN_BUTTON)
        self.campaign_page.find(self.campaign_page.locators.TITLE)

        self.campaign_page.click(self.campaign_page.locators.IMPORT_FROM_FILE_BUTTON)
        self.campaign_page.click(self.campaign_page.locators.MY_TARGET_RADIOBUTTON)
        self.campaign_page.find(self.campaign_page.locators.INPUT_FILE).send_keys(path_to_campaign_data_file)
        self.campaign_page.click(self.campaign_page.locators.INPUT_SUBMIT_BUTTON)
        self.campaign_page.send_keys(self.campaign_page.locators.CAMPAIGN_NAME_INPUT, random_str)
        self.campaign_page.click(self.campaign_page.locators.CREATE_CAMPAIGN_BUTTON)

        assert self.campaign_page.find(self.campaign_page.locators.CREATED_NOTIFY)
