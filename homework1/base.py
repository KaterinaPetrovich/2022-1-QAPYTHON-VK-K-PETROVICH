import pytest
from selenium.common.exceptions import StaleElementReferenceException
import conftest


class Basecase:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        CLICK_RETRY = 3
        for i in range(CLICK_RETRY):
            try:
                elem = self.find(locator)
                elem.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise
