from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=20):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 20
        return WebDriverWait(self.driver, timeout=timeout)

    def click(self, locator, timeout=None):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def send_keys(self, locator, text, timeout=None):
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(
            EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)

    def click_on_hidden_element(self, visible_locator, hidden_locator):
        visible_button = self.find(visible_locator)
        hidden_button = self.find(hidden_locator)
        ActionChains(self.driver).move_to_element(visible_button).click(hidden_button).perform()

