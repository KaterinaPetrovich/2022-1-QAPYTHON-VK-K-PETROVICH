from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'submit')



class MainPageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//a[@href='/logout']")
    HOME = (By.XPATH, "//a[@href='/']")
    BADGE = (By.CLASS_NAME, 'uk-icon-bug')
    LINUX = (By.XPATH, "//a[contains(text(), 'Linux')]")
    NETWORK = (By.XPATH, "//a[contains(text(), 'Network')]")
    PYTHON = (By.XPATH, "//a[@href='https://www.python.org/']")

    PYTHON_HISTORY = (By.XPATH, "//a[contains(text(), 'Python history')]")
    ABOUT_FLASK = (By.XPATH, "//a[contains(text(), 'About Flask')]")

    DOWNLOAD_CENTOS = (By.XPATH, "//a[contains(text(), 'Download Centos7')]")
    EXAMPLES = (By.XPATH, "//a[contains(text(), 'Examples')]")
    DOWNLOAD = (By.XPATH, "//a[contains(@href, 'wireshark.org/#download')]")
    NEWS = (By.XPATH, "//a[contains(@href, 'www.wireshark.org/news/')]")

    FUTURE_OF_INTERNET = (By.XPATH, "//img[contains(@src,'loupe')]")
    WHAT_IS_API = (By.XPATH, "//img[contains(@src,'laptop')]")
    SMTP = (By.XPATH, "//img[contains(@src,'analytics')]")

    USERNAME_INFO = (By.XPATH, "//div[@id='login-name']//li[1]")
    NAME_SURNAME_INFO = (By.XPATH, "//div[@id='login-name']//li[2]")
    VK_ID_INFO = (By.XPATH, "//div[@id='login-name']//li[3]")


class RegistrationPageLocators:
    USER_NAME_FIELD = (By.ID, 'user_name')
    SURNAME_FIELD = (By.ID, 'user_surname')
    MIDDLENAME_FIELD = (By.ID, 'user_middle_name')
    USERNAME_FIELD = (By.ID, 'username')
    EMAIL_FIELD = (By.ID, 'email')
    REPEAT_PASSWORD_FIELD = (By.ID, 'confirm')
    PASSWORD_FIELD = (By.ID, 'password')
    CHECKBOX = (By.ID, 'term')
    REGISTER_BUTTON = (By.ID, 'submit')
    INVALID_EMAIL_ALERT = (By.XPATH, '//div[contains(text(), "Invalid email address")]')
    PASSWORDS_MUST_MATCH_ALERT = (By.XPATH, '//div[text()= "Passwords must match"]')
    USER_EXIST_ALERT = (By.XPATH, '//div[contains(text(), "User already exist")]')
    INTERNAL_SERVER_ERROR = (By.XPATH, '//div[contains(text(), "Internal Server Error")]')

