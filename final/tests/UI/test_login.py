import allure

from tests.API.helper import get_user
from tests.UI.base_test import BaseCase
import pytest
from tests.UI.pages.login_page import LoginPage


@allure.epic('UI тесты')
@allure.feature('Тесты на login')
class TestLogin(BaseCase):

    @pytest.mark.UI
    def test_valid_login(self):
        """
        Проверка входа на сайт с корректными данными
        Ожидаемый результат: 1.открылась главная страница
        2. у пользователя в БД поле active изменилось на 1
        """
        self.driver.get(self.login_page.url)
        self.login_page.login(self.def_user[3], self.def_user[4])
        assert self.main_page.find(self.main_page.locators.LOGOUT_BUTTON)
        assert self.mysql.check_by_username(self.def_user[3]).active == 1

    @pytest.mark.UI
    def test_short_username_login(self):
        """
        Проверка входа на сайт с username в 1 символ
        Ожидаемый результат: 1.появилось валидационное сообщение
        2. главная страница не открылась
        """
        self.driver.get(self.login_page.url)
        *data, username, passwd, email = self.def_user
        self.login_page.login(username[0], passwd)
        assert self.login_page.find(self.login_page.locators.LOGIN_BUTTON)
        assert "не короче" in self.login_page.find(self.login_page.locators.USERNAME_FIELD). \
            get_attribute('validationMessage') or "lengthen" in \
               self.login_page.find(self.login_page.locators.USERNAME_FIELD). \
                   get_attribute('validationMessage')

    @pytest.mark.UI
    def test_empty_password_login(self):
        """
        Проверка входа на сайт с пустым паролем
        Ожидаемый результат: 1.появилось валидационное сообщение
        2. главная страница не открылась
        """
        self.driver.get(self.login_page.url)
        *data, username, passwd, email = self.def_user
        self.login_page.login(username[0], "")
        assert self.login_page.find(self.login_page.locators.LOGIN_BUTTON)
        assert "Заполните" in self.login_page.find(self.login_page.locators.PASSWORD_FIELD). \
            get_attribute('validationMessage') or "fill" in self.login_page.find(
            self.login_page.locators.PASSWORD_FIELD). \
                   get_attribute('validationMessage')
        assert not self.mysql.check_by_username(self.def_user[3]).active == 1

    @pytest.mark.UI
    def test_empty_username_login(self):
        """
        Проверка входа на сайт с пустым username
        Ожидаемый результат: 1.появилось валидационное сообщение
        2. главная страница не открылась
        """
        self.driver.get(self.login_page.url)
        *data, username, passwd, email = self.def_user
        self.login_page.login("", passwd)
        assert self.login_page.find(self.login_page.locators.LOGIN_BUTTON)
        assert "Заполните" in self.login_page.find(self.login_page.locators.USERNAME_FIELD). \
            get_attribute('validationMessage') or "fill" in self.login_page.find(
            self.login_page.locators.USERNAME_FIELD). \
                   get_attribute('validationMessage')
        assert not self.mysql.check_by_username(self.def_user[3]).active == 1

    @pytest.mark.UI
    def test_wrong_password_login(self):
        """
        Проверка входа на сайт с неправильным паролем
        Ожидаемый результат: 1.остались на странице login
        2. у пользователя в БД поле active осталось 0
        """
        self.driver.get(self.login_page.url)
        self.login_page.login(self.def_user[3], self.def_user[4][:3])
        assert self.login_page.find(self.login_page.locators.LOGIN_BUTTON)
        assert not self.mysql.check_by_username(self.def_user[3]).active == 1

    @pytest.mark.UI
    def test_failing_short_password_login(self):
        """
        Проверка входа на сайт с паролем в 1 символ
        Ожидаемый результат: 1.появилось валидационное сообщение
        2. главная страница не открылась
        """
        new_password = "a"
        self.driver.get(self.login_page.url)
        self.builder.change_password(self.def_user[3], new_password)
        self.login_page.login(self.def_user[3], new_password)
        assert "не короче" in self.login_page.find(self.login_page.locators.PASSWORD_FIELD). \
            get_attribute('validationMessage') or "lengthen" in self.login_page.find(
            self.login_page.locators.PASSWORD_FIELD). \
                   get_attribute('validationMessage')
        assert not self.mysql.check_by_username(self.def_user[3]).active == 1


@allure.epic('UI тесты')
@allure.feature('Тесты на регистрацию')
class TestRegistration(BaseCase):

    @pytest.mark.UI
    def test_valid_registration(self, user):
        """
        Проверка регистрации с корректными данными
        Ожидаемый результат: 1. открылась главная страница,
        2. в БД появилась запись с новым пользователем
        """
        self.driver.get(self.registration_page.url)
        self.registration_page.register(*user)
        assert self.main_page.find(self.main_page.locators.BADGE)
        assert self.mysql.check_by_username(user[3])

    @pytest.mark.UI
    def test_registration_with_short_username(self, user):
        """
        Проверка регистрации с username в 1 символ
        Ожидаемый результат: пользователь не появляется в БД
        """
        name, surname, middle_name, username, *data = user

        self.driver.get(self.registration_page.url)
        self.registration_page.register(name, surname, middle_name, username[0], *data)
        assert "не короче" in self.registration_page.find(
            self.registration_page.locators.USERNAME_FIELD).get_attribute('validationMessage') \
               or "lengthen" in self.registration_page.find(
            self.registration_page.locators.USERNAME_FIELD).get_attribute('validationMessage')

        assert not self.mysql.check_by_username(username[0])

    @pytest.mark.UI
    def test_registration_with_short_email(self, user):
        """
        Проверка регистрации с email в 1 символ
        Ожидаемый результат: пользователь не появляется в БД
        """
        *data, email = user

        self.driver.get(self.registration_page.url)
        self.registration_page.register(*data, email[0])
        assert "не короче" in self.registration_page.find(
            self.registration_page.locators.EMAIL_FIELD).get_attribute(
            'validationMessage') or "lengthen" in self.registration_page.find(
            self.registration_page.locators.EMAIL_FIELD).get_attribute('validationMessage')
        assert not self.mysql.check_by_username(user[3])

    @pytest.mark.UI
    def test_failing_registration_without_email(self, user):
        """
        Проверка регистрации с email в 0 символов
        Ожидаемый результат: 1. пользователь не появляется в БД
        2. появляется сообщение то том, что нужно ввести email

        """
        *data, email = user

        self.driver.get(self.registration_page.url)
        self.registration_page.register(*data, "")
        assert not self.mysql.check_by_username(user[3])
        assert "Заполните" in self.registration_page.find(
            self.registration_page.locators.EMAIL_FIELD).get_attribute(
            'validationMessage') or "fill" in self.registration_page.find(
            self.registration_page.locators.EMAIL_FIELD).get_attribute('validationMessage')

    @pytest.mark.UI
    def test_registration_without_password(self, user):
        """
        Проверка регистрации с паролем в 0 символов
        Ожидаемый результат: 1. пользователь не появляется в БД
        2. появляется сообщение то том, что нужно ввести пароль
        """
        *data, passwd, email = user

        self.driver.get(self.registration_page.url)
        self.registration_page.register(*data, "", email)
        assert "Заполните" in self.registration_page.find(
            self.registration_page.locators.PASSWORD_FIELD).get_attribute(
            'validationMessage') or "fill" in self.registration_page.find(
            self.registration_page.locators.PASSWORD_FIELD).get_attribute('validationMessage')
        assert not self.mysql.check_by_username(user[3])

    @pytest.mark.UI
    def test_failing_registration_with_short_password(self, user):
        """
        Проверка регистрации с паролем в 1 символов
        Ожидаемый результат: 1. пользователь не появляется в БД
        2. появляется сообщение то том, что нужно ввести более длинный пароль
        """
        *data, passwd, email = user
        short_password = "a"
        self.driver.get(self.registration_page.url)
        self.registration_page.register(*data, short_password, email)
        assert "не короче" in self.registration_page.find(
            self.registration_page.locators.PASSWORD_FIELD).get_attribute('validationMessage') or \
               "lengthen" in self.registration_page.find(
            self.registration_page.locators.PASSWORD_FIELD).get_attribute('validationMessage')
        assert not self.mysql.check_by_username(user[3])

    @pytest.mark.UI
    def test_registration_with_invalid_email(self, user):
        """
        Проверка регистрации с некорректным email
        Ожидаемый результат: 1. пользователь не появляется в БД
        2. появляется сообщение то том, что нужно ввести корректный email
        """
        *data, passwd, email = user
        self.driver.get(self.registration_page.url)
        self.registration_page.register(*data, passwd, passwd)
        assert self.registration_page.find(self.registration_page.locators.INVALID_EMAIL_ALERT)
        assert not self.mysql.check_by_username(user[3])

    @pytest.mark.UI
    def test_registration_with_not_matching_passwords(self, user):
        """
        Проверка регистрации с не совпадающими паролями
        Ожидаемый результат: 1. пользователь не появляется в БД
        2. появляется сообщение то том, что нужно пароли не совпадают
        """
        self.driver.get(self.registration_page.url)
        self.registration_page.register(*user, not_match=True)
        assert self.registration_page.find(
            self.registration_page.locators.PASSWORDS_MUST_MATCH_ALERT)
        assert not self.mysql.check_by_username(user[3])

    @pytest.mark.UI
    def test_failing_registration_with_existing_email(self, user):
        """
        Проверка регистрации с cуществующим email
        Ожидаемый результат: 1. пользователь не появляется в БД
        2. появляется сообщение то том, что email уже существует
        """
        existing_email = user[-1]
        self.driver.get(self.registration_page.url)
        self.builder.add_user(*user)
        *new_user, email = get_user()
        self.registration_page.register(*new_user, existing_email)
        assert not self.registration_page.find(
            self.registration_page.locators.INTERNAL_SERVER_ERROR)
        assert not self.mysql.check_by_username(new_user[3])

    @pytest.mark.UI
    def test_registration_with_existing_username(self, user):
        """
        Проверка регистрации с cуществующим username
        Ожидаемый результат: 1. пользователь не появляется в БД
        2. появляется сообщение то том, что username уже существует
        """
        existing_username = user[3]
        self.driver.get(self.registration_page.url)
        self.builder.add_user(*user)
        *new_user, username, password, email = get_user()
        self.registration_page.register(*new_user, existing_username, password, email)
        assert self.registration_page.find(self.registration_page.locators.USER_EXIST_ALERT)
        assert not self.mysql.check_by_username(username)

    @pytest.mark.UI
    def test_failing_registration_with_not_matching_passwords_and_invalid_email(self, user):
        """
        Проверка регистрации одновременно с  несовпадающими паролями и некорректным email
        Ожидаемый результат: 1. пользователь не появляется в БД
        2. появляется корректное сообщение об ошибке
        """
        self.driver.get(self.registration_page.url)
        *data, passwd, email = user
        self.registration_page.register(*data, passwd, passwd, not_match=True)
        assert self.registration_page.find(
            self.registration_page.locators.PASSWORDS_MUST_MATCH_ALERT)
        assert self.registration_page.find(self.registration_page.locators.INVALID_EMAIL_ALERT)
        assert not self.mysql.check_by_username(user[3])


@allure.epic('UI тесты')
@allure.feature('Тесты главной страницы')
class TestMainPage(BaseCase):

    @pytest.fixture(scope='function', autouse=True)
    def login(self, setup):
        self.driver.get(self.login_page.url)
        self.login_page.login(self.def_user[3], self.def_user[4])

    @pytest.mark.UI
    def test_logout(self):
        """
        Проверка кнопки log out на главной странице.
        Ожидаемый результат:
         1. открылась страница с логином
         2. у пользователя в БД поле active стало равно 0
        """
        self.main_page.click(self.main_page.locators.LOGOUT_BUTTON)
        assert self.login_page.find(self.login_page.locators.LOGIN_BUTTON)
        assert self.mysql.check_by_username(self.def_user[3]).active == 0

    @pytest.mark.UI
    def test_username_visibility(self):
        """
        Проверка отображения username текущего пользователя
        """
        assert f'Logged as {self.def_user[3]}' == self.main_page.find(
            self.main_page.locators.USERNAME_INFO).text

    @pytest.mark.UI
    def test_name_surname_visibility(self):
        """
        Проверка отображения  name, surname текущего пользователя
        """
        assert f'User: {self.def_user[0]} {self.def_user[1]} {self.def_user[2]}' == \
               self.main_page.find(self.main_page.locators.NAME_SURNAME_INFO).text

    @pytest.mark.UI
    def test_vk_id_visibility(self):
        """
        Проверка видимости vk id на главной странице
        """
        vk_id = self.get_vk_id(self.def_user[3])
        assert f'VK ID: {vk_id}' == self.main_page.find(self.main_page.locators.VK_ID_INFO).text


    @pytest.mark.UI
    def test_home_button(self):
        """
        Проверка кнопки Home на главной странице
        Ожидаемый результат: остались на главной странице
        """
        self.main_page.click(self.main_page.locators.HOME)
        assert self.driver.current_url == self.main_page.url

    @pytest.mark.UI
    def test_logo(self):
        """
        Проверка нажатия на логотип на главной странице
        Ожидаемый результат: остались на главной странице
        """
        self.main_page.click(self.main_page.locators.BADGE)
        assert self.driver.current_url == self.main_page.url

    @pytest.mark.UI
    def test_failing_python_button(self):
        """
        Проверка кнопки Python на главной странице
        Ожидаемый результат: в новой вкладке открылась страница о Python
        """
        self.main_page.click(self.main_page.locators.PYTHON)
        assert self.driver.current_url == self.main_page.python_url

    @pytest.mark.UI
    def test_failing_linux_button(self):
        """
        Проверка кнопки Linux на главной странице
        Ожидаемый результат: в новой вкладке открылась страница о Linux
        """
        self.main_page.click(self.main_page.locators.LINUX)
        assert len(self.driver.window_handles) == 2

    @pytest.mark.UI
    def test_failing_network_button(self):
        """
        Проверка кнопки Network на главной странице
        Ожидаемый результат: в новой вкладке открылась страница о Network
        """
        self.main_page.click(self.main_page.locators.NETWORK)
        assert len(self.driver.window_handles) == 2

    @pytest.mark.UI
    def test_API_button(self):
        """
        Проверка кнопки WHAT_IS_API на главной странице
        Ожидаемый результат: в новой вкладке открылась страница об API
        """
        self.main_page.click(self.main_page.locators.WHAT_IS_API)
        self.driver.switch_to_window(self.driver.window_handles[1])
        assert self.driver.current_url == self.main_page.api_url
        assert len(self.driver.window_handles) == 2

    @pytest.mark.UI
    def test_future_of_internet_button(self):
        """
        Проверка кнопки FUTURE_OF_INTERNET на главной странице
        Ожидаемый результат: в новой вкладке открылась страница с заголовком future of the internet
        """
        self.main_page.click(self.main_page.locators.FUTURE_OF_INTERNET)
        self.driver.switch_to_window(self.driver.window_handles[1])
        assert 'future', 'Internet' in self.driver.title
        assert len(self.driver.window_handles) == 2

    @pytest.mark.UI
    def test_SMTP_button(self):
        """
        Проверка кнопки SMTP на главной странице
        Ожидаемый результат: в новой вкладке открылась страница о SMTP
        """
        self.main_page.click(self.main_page.locators.SMTP)
        self.driver.switch_to_window(self.driver.window_handles[1])
        assert 'SMTP' in self.driver.title
        assert len(self.driver.window_handles) == 2

    @pytest.mark.UI
    def test_about_flask(self):
        """
        Проверка кнопки about_flask под кнопкой python на главной странице
        Ожидаемый результат: в новой вкладке открылась страница с заголовком flask
        """
        self.main_page.click_on_hidden_element(self.main_page.locators.PYTHON,
                                               self.main_page.locators.ABOUT_FLASK)
        self.driver.switch_to_window(self.driver.window_handles[1])
        assert 'Flask' in self.driver.title
        assert len(self.driver.window_handles) == 2

    @pytest.mark.UI
    def test_failing_python_history(self):
        """
        Проверка кнопки python_history под кнопкой python на главной странице
        Ожидаемый результат: в новой вкладке открылась страница  с заголовком Python history
        """
        self.main_page.click_on_hidden_element(self.main_page.locators.PYTHON,
                                               self.main_page.locators.PYTHON_HISTORY)
        assert len(self.driver.window_handles) == 2
        self.driver.switch_to_window(self.driver.window_handles[1])
        assert 'Python', 'history' in self.driver.title

    @pytest.mark.UI
    def test_failing_download_centos(self):
        """
        Проверка кнопки download_centos под кнопкой linux на главной странице
        Ожидаемый результат: в новой вкладке открылась страница download centos 7
        """
        self.main_page.click_on_hidden_element(self.main_page.locators.LINUX,
                                               self.main_page.locators.DOWNLOAD_CENTOS)
        self.driver.switch_to_window(self.driver.window_handles[1])
        assert len(self.driver.window_handles) == 2
        assert 'Centos' in self.driver.title

    @pytest.mark.UI
    def test_network_wireshark_news(self):
        """
        Проверка кнопки news под кнопкой network на главной странице
        Ожидаемый результат: в новой вкладке открылась страница news
        """
        self.main_page.click_on_hidden_element(self.main_page.locators.NETWORK,
                                               self.main_page.locators.NEWS)
        self.driver.switch_to_window(self.driver.window_handles[1])
        assert len(self.driver.window_handles) == 2
        assert 'news' in self.driver.current_url

    @pytest.mark.UI
    def test_network_examples(self):
        """
        Проверка кнопки examples под кнопкой network на главной странице
        Ожидаемый результат: в новой вкладке открылась страница c заголовком Tcpdump Examples
        """
        self.main_page.click_on_hidden_element(self.main_page.locators.NETWORK,
                                               self.main_page.locators.EXAMPLES)
        self.driver.switch_to_window(self.driver.window_handles[1])
        assert len(self.driver.window_handles) == 2
        assert 'Tcpdump Examples' in self.driver.title

    @pytest.mark.UI
    def test_network_wireshark_download(self):
        """
        Проверка кнопки download под кнопкой network на главной странице
        Ожидаемый результат: в новой вкладке открылась страница c заголовком Wireshark
        """
        self.main_page.click_on_hidden_element(self.main_page.locators.NETWORK,
                                               self.main_page.locators.DOWNLOAD)
        self.driver.switch_to_window(self.driver.window_handles[1])
        assert len(self.driver.window_handles) == 2
        assert 'Wireshark', 'Deep' in self.driver.title
