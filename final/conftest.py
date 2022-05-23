import os
import logging
import shutil
import sys

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from mysql.client import MysqlClient
from tests.API.client import ApiClient
from tests.API.helper import get_user
from tests.UI.pages.login_page import LoginPage
from tests.UI.pages.main_page import MainPage
from tests.UI.pages.registration_page import RegistrationPage


@pytest.fixture()
def driver():
    #browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    capabilities = {
        'browserName': 'chrome',
        'version': "98.0"
    }
    browser = webdriver.Remote(
        command_executor='http://selenoid:4444/wd/hub', options=Options(),
        desired_capabilities=capabilities)
    browser.maximize_window()
    yield browser
    browser.quit()


# @pytest.fixture(scope='session')
# def base_temp_dir():
#     if sys.platform.startswith('win'):
#         base_dir = 'C:\\tests\vk'
#     else:
#         base_dir = '/tmp/tests'
#     if os.path.exists(base_dir):
#         shutil.rmtree(base_dir)
#     return base_dir
#
#
@pytest.fixture(scope='function')
def temp_dir(repo_root):
    test_dir = os.path.join(repo_root, "temp")
    #os.makedirs(test_dir)
    return test_dir


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


@pytest.fixture(scope="session")
def api_client():
    api_client = ApiClient()
    return api_client


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver=driver)


@pytest.fixture(scope='session')
def mysql_client():
    mysql_client = MysqlClient(user='test_qa', port=3306, password='qa_test',
                               host='mysql', db_name='vkeducation')
    mysql_client.connect()
    yield mysql_client

    mysql_client.connection.close()


@pytest.fixture(scope='function')
def logger(temp_dir):
    log_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    log_file = os.path.join(temp_dir, 'test.log')
    log_level = logging.INFO

    file_handler = logging.FileHandler(log_file, 'w')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(log_level)

    log = logging.getLogger('test')
    log.propagate = False
    log.setLevel(log_level)
    log.handlers.clear()
    log.addHandler(file_handler)

    yield log

    for handler in log.handlers:
        handler.close()


@pytest.fixture()
def user():
    return get_user()
