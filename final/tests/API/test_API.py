import allure
import pytest
import faker

from tests.API.helper import get_user
from tests.UI.base_test import ApiBase


@allure.epic('API тесты')
class TestApi(ApiBase):

    @pytest.fixture()
    def user(self):
        user = get_user()
        self.builder.add_user(*user)
        self.api_client.get_cookie(user)
        return user

    @pytest.mark.API
    @allure.feature('Тест на получение статуса')
    def test_status(self):
        """
        проверка получения статуса приложения
        Ожидаемый результат: статус-код ответа 200
        """
        assert self.api_client.get_status().status_code == 200

    @pytest.mark.API
    @allure.feature('Тест на добавление пользователя')
    def test_add_user(self, user):
        username = user[3]
        self.api_client.post_add_user(*user)
        assert self.mysql.check_by_username(username)

    @pytest.mark.API
    @allure.feature('Тест на смену пароля')
    def test_change_password(self, user):
        username = user[3]
        new_password = "pass"
        self.api_client.put_change_password(username=username,
                                            new_password=new_password)
        assert self.mysql.check_by_username(username).password == new_password

    @pytest.mark.API
    @allure.feature('Тест на добавление пользователя')
    def test_add_existing_user(self, user):
        assert self.api_client.post_add_user(*user).json()[
                   "detail"] == "User already exists"



    @pytest.mark.API
    @allure.feature('Тест на удаление пользователя')
    def test_failing_delete_user(self, user):
        username = user[3]
        self.api_client.delete_user(username)
        assert not self.mysql.check_by_username(username)

    @pytest.mark.API
    @allure.feature('Тест на блокировку пользователя')
    def test_block_user(self, user):
        username = user[3]
        self.api_client.block_user(username)
        assert self.mysql.check_by_username(username).access == 0

    @pytest.mark.API
    @allure.feature('Тест на разблокировку пользователя')
    def unblock_user(self):
        username = "udfgngne14"
        self.builder.add_user(name="a", surname="b", username=username, password="pass1",
                              email="shkld@.nk.cbbbcdc", access=0)
        self.api_client.unblock_user(username)
        assert self.mysql.check_by_username(username).access == 1
