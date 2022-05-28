import pytest
from _pytest.fixtures import FixtureRequest

from pages.main_page import MainPage


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, request: FixtureRequest):
        self.driver = driver
        self.main_page: MainPage = (request.getfixturevalue('main_page'))
