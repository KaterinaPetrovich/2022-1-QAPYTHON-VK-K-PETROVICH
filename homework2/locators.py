from selenium.webdriver.common.by import By


class LoginPageLocators:
    ENTER_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class,"responseHead-module-button")]')
    EMAIL_FIELD_LOCATOR = (By.XPATH, '//input[@name="email"]')
    PASSWORD_FIELD_LOCATOR = (By.XPATH, '//input[@name="password"]')
    ENTER_LOGIN_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "authForm-module-button")]')
    WRONG_LOGIN_NOTIFY = (By.XPATH, '//div[contains(@class, "notify-module-error")]')
    REGISTRATION_BUTTON = (By.XPATH, '// a[contains( @class ,"login_signup")]')



class MainPageLocators:
    SEGMENTS_BUTTON = (
    By.XPATH, '//a[@href="/segments" and contains(@class, "center-module-button")]')
    LOGO = (By.XPATH, '//a[@href = "//target.my.com"]')
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, '//div[contains(@class, "dashboard-module-createButton")]')
    NOTIFICATION = (By.XPATH, '//div[contains(@class, "notificationItem-module-title")]')


class CampaignPageLocators:
    IMPORT_FROM_FILE_BUTTON = (By.XPATH, '//div[contains(@class, "import-button")]/button')
    TITLE = (By.XPATH, '//span[@data-translated="Campaign objective"]')
    MY_TARGET_RADIOBUTTON = (By.XPATH, '//input[@id = "campaign_MyTarget"]')
    INPUT_FILE = (By.XPATH, '//input[@type = "file"]')
    INPUT_SUBMIT_BUTTON = (By.XPATH, '//div[contains(@class , "import__submit-button")]/button')
    CAMPAIGN_NAME_INPUT = (By.XPATH, '//div[contains(@class ,"campaign-name")]/*/input')
    CREATE_CAMPAIGN_BUTTON = (By.XPATH, '//div[contains(@class ,"save-button")]/button')
    CREATED_NOTIFY = (By.XPATH, '//div[contains(@class ,"notify-module-success")]')


class SegmentPageLocators:
    CREATE_SEGMENT_BUTTON = (By.XPATH, '//div[contains(@class, "create-button")]/button')
    CHECKBOX = (By.XPATH, '//input[contains(@class, "adding-segments") and @type = "checkbox"]')
    SUBMIT_BUTTON = (By.XPATH, '//div[contains(@class,"add-button")]/.')
    ADD_SEGMENTS_ITEM = (By.XPATH, '//div[@class = "adding-segments-item"]')
    SEGMENTS_NAME_INPUT = (By.XPATH, '//div[@class= "js-segment-name"]//input')
    FINAL_SUBMIT_BUTTON = (By.XPATH, '//button[@data-class-name="Submit"]')
    DELETE_BUTTON = (By.XPATH, '//li[@data-test="remove"]')
    SEARCH_INPUT = (By.XPATH, '//input[contains(@class,"search")]')
    NOTHING_NOTIFICATION = (By.XPATH, '//li[@data-test="nothing"]')
    SELECT_MODULE = (By.XPATH,'//div[contains(@class,"select-module-arrow")]')



