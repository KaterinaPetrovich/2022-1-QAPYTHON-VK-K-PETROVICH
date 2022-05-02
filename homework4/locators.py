from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy


class MainPageLocators:
    KEYBOARD_BUTTON = (By.ID, "ru.mail.search.electroscope:id/keyboard")
    TEXT_FIELD = (By.ID, "ru.mail.search.electroscope:id/input_text")
    SEND_BUTTON = (By.ID, "ru.mail.search.electroscope:id/text_input_action")
    SUGGESTION = (By.XPATH, "//android.view.ViewGroup[5]/android.widget.TextView")
    POPULATION = (By.XPATH, "//android.widget.TextView[contains(@text, 'население россии')]")

    ELEMENT = "//android.widget.TextView[contains(@text, '{}')]"
    BURGER_MENU_BUTTON = (By.ID, "ru.mail.search.electroscope:id/assistant_menu_bottom")


class SettingsPageLocators:
    ABOUT_BUTTON = (By.XPATH, "//android.widget.TextView[contains(@text,'О приложении')]")
    SOURCE_OF_NEWS = (By.XPATH, "//android.widget.TextView[contains(@text,'Источник новостей')]")
    CLOSE_BUTTON = (MobileBy.CLASS_NAME, "android.widget.ImageButton")


class AboutPageLocators:
    CORRECT_VERSION = (By.XPATH, "//android.widget.TextView[contains(@text, 'Версия 1.57.0')]")
    TRADE_MARK = (By.XPATH, "//android.widget.TextView[contains(@text,'Все права защищены')]")


class SourcePageLocators:
    MAIL_RU = (By.XPATH, "//android.widget.TextView[contains(@text,'Новости Mail.ru')]")
    SELECTED =(MobileBy.ID, "ru.mail.search.electroscope:id/news_sources_item_selected")
    BACK_BUTTON = (MobileBy.CLASS_NAME, "android.widget.ImageButton")
