import os

import pytest
from appium import webdriver

from pages.main_page import MainPage


@pytest.fixture()
def driver(capability):
    appium_url = 'http://127.0.0.1:4723/wd/hub'
    desired_caps = capability
    driver = webdriver.Remote(appium_url, desired_capabilities=desired_caps)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def capability(repo_root):
    capability = {"platformName": "Android",
                  "platformVersion": "8.1",
                  "automationName": "Appium",
                  "appPackage": "ru.mail.search.electroscope",
                  "appActivity": ".ui.activity.AssistantActivity",
                  "app": os.path.join(repo_root, 'stuff', "Marussia_v1.57.0.apk"),
                  "orientation": "PORTRAIT",
                  "autoGrantPermissions": True,
                  }
    return capability


@pytest.fixture(scope='session')
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))


@pytest.fixture
def main_page(driver):
    return MainPage(driver=driver)
