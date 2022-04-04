import locators


def login(test):
    test.driver.get("https://target.my.com/")
    test.click(locators.ENTER_BUTTON_LOCATOR)
    test.send_keys(locators.EMAIL_FIELD_LOCATOR, "katerina_petrovich@bk.ru")
    test.send_keys(locators.PASSWORD_FIELD_LOCATOR, "135qwe")
    test.click(locators.ENTER_LOGIN_BUTTON_LOCATOR)
