import pytest
import allure
import os
from _pytest.fixtures import FixtureRequest
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.segment_page import SegmentPage
from pages.main_page import MainPage
from pages.campaign_page import CampaignPage


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, logger, request: FixtureRequest):
        self.driver = driver
        self.logger = logger
        self.base_page:BasePage = (request.getfixturevalue('base_page'))
        self.login_page:LoginPage = (request.getfixturevalue('login_page'))
        self.main_page: MainPage = (request.getfixturevalue('main_page'))
        self.segment_page: SegmentPage = (request.getfixturevalue('segment_page'))
        self.campaign_page: CampaignPage = (request.getfixturevalue('campaign_page'))

    @pytest.fixture(scope='function', autouse=True)
    def ui_report(self, driver, request, temp_dir):
        failed_test_count = request.session.testsfailed
        yield
        if request.session.testsfailed > failed_test_count:
            browser_logs = os.path.join(temp_dir, 'browser.log')
            with open(browser_logs, 'w') as f:
                for i in driver.get_log('browser'):
                    f.write(f"{i['level']} - {i['source']}\n{i['message']}\n")
            screenshot_path = os.path.join(temp_dir, 'failed.png')
            allure.attach.file(screenshot_path, 'failed.png', allure.attachment_type.PNG)
            with open(browser_logs, 'r') as f:
                allure.attach(f.read(), 'test.log', allure.attachment_type.TEXT)