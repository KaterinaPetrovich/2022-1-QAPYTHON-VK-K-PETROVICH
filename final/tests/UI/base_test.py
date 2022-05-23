import os

import allure
import pytest
import requests
from _pytest.fixtures import FixtureRequest

from mysql.builder import MysqlBuilder
from tests.UI.pages.login_page import LoginPage
from tests.UI.pages.main_page import MainPage
from tests.UI.pages.registration_page import RegistrationPage


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, request: FixtureRequest, mysql_client):
        self.driver = driver
        self.mysql = mysql_client
        self.builder = MysqlBuilder(self.mysql)
        self.def_user = self.builder.add_default_user()
        self.login_page: LoginPage = (request.getfixturevalue('login_page'))
        self.main_page: MainPage = (request.getfixturevalue('main_page'))
        self.registration_page: RegistrationPage = (request.getfixturevalue('registration_page'))

    def get_vk_id(self, username):
        res = requests.get(f'http://mock:8082/vk_id/{username}')
        return res.json()['vk_id']

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
            self.driver.get_screenshot_as_file(screenshot_path)
            allure.attach.file(screenshot_path, 'failed.png', allure.attachment_type.PNG)
            with open(browser_logs, 'r') as f:
                allure.attach(f.read(), 'test.log', allure.attachment_type.TEXT)


class ApiBase:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, api_client, mysql_client):
        self.api_client = api_client
        self.mysql = mysql_client
        self.builder = MysqlBuilder(self.mysql)
