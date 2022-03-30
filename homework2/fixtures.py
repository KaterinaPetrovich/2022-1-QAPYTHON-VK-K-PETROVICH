import pytest
import os
from _pytest.fixtures import FixtureRequest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.segment_page import SegmentPage
from pages.main_page import MainPage
from pages.campaign_page import CampaignPage


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture()
def file_path(repo_root):
    return os.path.join(repo_root, 'files', 'file.json')


@pytest.fixture()
def login(request: FixtureRequest):
    login_page = (request.getfixturevalue('login_page'))
    return login_page.login()


@pytest.fixture
def get_driver():
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    browser.maximize_window()
    return browser


@pytest.fixture
def login_page(driver):
    return LoginPage(driver=driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)


@pytest.fixture
def segment_page(driver):
    return SegmentPage(driver=driver)


@pytest.fixture
def campaign_page(driver):
    return CampaignPage(driver=driver)
