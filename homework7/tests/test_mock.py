import json
import settings

url = f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}'


class TestMock:

    def test_add_get_user(self, connection):
        resp = connection.post_request('/add_user', '{"name": "Stepan","surname": "ivanov"}')
        user_id_from_add = json.loads(resp[-1])["user_id"]
        resp = connection.get_request('/get_user/Stepan')
        user_id_from_get = json.loads(resp[-1])["user_id"]

        assert user_id_from_add == user_id_from_get

    def test_add_existent_user(self, connection):
        connection.post_request('/add_user', '{"name": "Vasya", "surname": "ivanov"}')
        resp = connection.post_request('/add_user', '{"name": "Vasya", "surname": "ivanov"}')
        assert resp[0].split()[1] == '400'

    def test_get_non_existent_user(self, connection):
        client = connection
        resp = client.get_request(f'/get_user/Masha')

        assert resp[0].split()[1] == '404'

    def test_delete_user(self, connection):
        connection.post_request('/add_user', '{"name": "nikolai", "surname": "ivanov"}')
        resp = connection.delete_request('/delete_user', '{"name": "nikolai"}')
        assert resp[0].split()[1] == '200'

    def test_put_request(self, connection):
        connection.post_request('/add_user', '{"name": "vitaly", "surname": "ivanov"}')
        connection.put_request('/change_surname',
                               '{"name": "vitaly", "new_surname": "stepanov"}')
        resp = connection.get_request('/get_user/vitaly')
        user_surname = json.loads(resp[-1])["surname"]
        assert user_surname == "stepanov"
