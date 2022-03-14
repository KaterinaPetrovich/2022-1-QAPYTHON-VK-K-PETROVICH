from selenium.webdriver.common.by import By

ENTER_BUTTON_LOCATOR = \
    (By.XPATH, '//div[contains(@class,"responseHead-module-button")]')
EMAIL_FIELD_LOCATOR = (By.XPATH, '//input[@name="email"]')
PASSWORD_FIELD_LOCATOR = (By.XPATH, '//input[@name="password"]')
enter_login_button_locator = \
    (By.XPATH, '//div[contains(@class, "authForm-module-button")]')
instruction_locator = (
    By.XPATH, '//div[contains(@class, "instruction-module-title")]')
username_button_locator = \
    (By.XPATH, '//div[contains(@class, "right-module-mail")]'
               '')
logout_button_locator = (By.XPATH, '//a[@href="/logout"]')

FIO_LOCATOR = (By.XPATH, '//div[@data-name ="fio"]/div/input')
SAVE_BUTTON_LOCATOR = (By.XPATH, '//div[@class="button__text"]')
SUCCESS_SAVE = (By.XPATH,
                '//div[@class ="_notification _notification_success-bg js-group-form-success-bg"]')

DEPOSIT_FORM_LOCATOR = (
    By.XPATH, '//div[@class = "deposit__payment-form__header"]')
BALANCE_BUTTON_LOCATOR = (
    By.XPATH,
    '//a[@href="/billing" and contains(@class, "center-module-button")]')
STAT_BUTTON_LOCATOR = (
    By.XPATH, '//a[contains(@class, "center-module-stat")]')
STAT_PAGE_LOCATOR = (By.XPATH, '//a[@href ="/statistics/summary"]')
