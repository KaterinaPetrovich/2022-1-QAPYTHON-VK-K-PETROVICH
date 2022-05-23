from mysql.models import TestUsersModel
from tests.API.helper import get_user


class MysqlBuilder:

    def __init__(self, client):
        self.client = client

    def add_user(self, name, surname, middle_name, username,
                 password, email, access=None, active=None, start_active_time=None):
        test_users = TestUsersModel(name=name,
                                    surname=surname,
                                    middle_name=middle_name,
                                    username=username,
                                    password=password,
                                    email=email,
                                    access=access,
                                    active=active,
                                    start_active_time=start_active_time)
        self.client.session.add(test_users)
        self.client.session.commit()
        return test_users

    def add_default_user(self):
        user = get_user()
        self.add_user(*user)
        return user

    def change_password(self, username, new_passwd):
        user_id = self.client.check_by_username(username).id
        self.client.session.query(TestUsersModel).get(user_id).password = new_passwd
        self.client.session.commit()
