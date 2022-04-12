from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self, driver):
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
        elem = self.wait(timeout).until(
            EC.visibility_of_element_located(locator))
        elem.clear()
        elem.send_keys(text)

    def swipe_element_lo_left(self, locator):
        web_element = self.find(locator, 10)
        left_x = web_element.location['x']
        right_x = left_x + web_element.rect['width']
        upper_y = web_element.location['y']
        lower_y = upper_y + web_element.rect['height']
        middle_y = (upper_y + lower_y) / 2
        action = TouchAction(self.driver)
        action.press(x=right_x, y=middle_y).wait(ms=300).move_to(x=left_x,
                                                                 y=middle_y).release().perform()

    def swipe_up(self, swipetime=200):
        action = TouchAction(self.driver)
        dimension = self.driver.get_window_size()
        x = int(dimension['width'] / 2)
        start_y = int(dimension['height'] * 0.8)
        end_y = int(dimension['height'] * 0.2)
        action. \
            press(x=x, y=start_y). \
            wait(ms=swipetime). \
            move_to(x=x, y=end_y). \
            release(). \
            perform()
