from selenium.webdriver.common.by import By

LOGOUT_BUTTON_LOCATOR = (By.XPATH, '//a[@href="/logout"]')
BALANCE_BUTTON_LOCATOR = (By.XPATH, '//a[@href="/billing"]')
STAT_BUTTON_LOCATOR = (By.XPATH, '//a[@href= "/statistics"]')

ENTER_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class,"responseHead-module-button")]')
EMAIL_FIELD_LOCATOR = (By.XPATH, '//input[@name="email"]')
PASSWORD_FIELD_LOCATOR = (By.XPATH, '//input[@name="password"]')

ENTER_LOGIN_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "authForm-module-button")]')
USERNAME_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "right-module-mail")]')
LOGO = (By.XPATH, '//a[@href = "//target.my.com"]')
NOTIFICATION = (By.XPATH, '//div[contains(@class, "notificationItem-module-title")]')

FIO_LOCATOR = (By.XPATH, '//div[@data-name ="fio"]/div/input')
SAVE_BUTTON_LOCATOR = (By.XPATH, '//div[@class="button__text"]')
SUCCESS_SAVE = (By.XPATH, '//div[contains(@class,"_notification_success-bg")]')
