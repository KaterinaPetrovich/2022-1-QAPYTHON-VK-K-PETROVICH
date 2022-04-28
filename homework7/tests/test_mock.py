import requests
import pytest
import settings

from mock import flask_mock

url = f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}'


class TestMock:
    def test_add_get_user(self, connection):
        resp = connection.post_request('/add_user', {'name': 'Stepan'})
        user_id_from_add = resp

        resp = connection.get_request('/get_user/Ilya')
        user_id_from_get = resp

        assert user_id_from_add == user_id_from_get

    def test_add_existent_user(self, connection):
        connection.post_request('/add_user', {"name": "Vasya", "surname": "ivanov"})
        resp = connection.post_request('/add_user', {"name": "Vasya", "surname": "ivanov"})
        assert resp[0].split()[1] == '400'

    def test_get_non_existent_user(self, connection):
        client = connection
        resp = client.get_request(f'/get_user/Masha')

        assert resp[0].split()[1] == '404'

    def test_delete_user(self, connection):
        connection.post_request('/add_user', {"name": "nikolai", "surname": "ivanov"})
        resp = connection.delete_request('/delete_user', {"name": 'nikolai'})
        assert resp[0].split()[1] == '200'

    def test_put_request(self, connection):
        connection.post_request('/add_user', {"name": "vitaly", "surname": "ivanov"})
        resp = connection.put_request('/change_surname', {"name": "vitaly", "new_surname": "stepanov"})
        assert resp[0].split()[1] == '200'
