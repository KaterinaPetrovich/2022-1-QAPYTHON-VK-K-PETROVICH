from tests.UI.pages.base_page import BasePage
from tests.UI.locators import MainPageLocators


class MainPage(BasePage):
    locators = MainPageLocators()
    url = "http://app:8080/welcome/"
    python_url = "https://www.python.org/"
    api_url = "https://en.wikipedia.org/wiki/API"
