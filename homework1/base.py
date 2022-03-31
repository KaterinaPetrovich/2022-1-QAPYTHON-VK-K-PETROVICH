import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Basecase:
    driver = None

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        self.driver = driver

    def find(self, locator, timeout=15):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 15
        return WebDriverWait(self.driver, timeout=timeout)

    def click(self, locator, timeout=None):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def send_keys(self, locator, text, timeout=None):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)
