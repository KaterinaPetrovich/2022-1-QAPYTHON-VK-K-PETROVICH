from urllib.parse import urljoin

import pytest
import requests

from mysql.builder import MysqlBuilder
from tests.API.helper import get_user


class ApiClient:

    def __init__(self):
        self.base_url = "http://app:8080/"
        #self.base_url = "http://127.0.0.1:8080/"
        self.session = requests.Session()

    def post_add_user(self, name, surname, middle_name, username, password, email):
        location = "/api/user"
        url = urljoin(self.base_url, location)
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f'session={self.cookie}'

        }
        data = {
            "name": name,
            "surname": surname,
            "middle_name": middle_name,
            "username": username,
            "password": password,
            "email": email
        }
        return self.session.post(url=url, headers=headers, json=data)

    def delete_user(self, username):
        location = f"/api/user/{username}"
        url = urljoin(self.base_url, location)
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f'session={self.cookie}'
        }
        return self.session.delete(url=url, headers=headers)

    def block_user(self, username):
        location = f"/api/user/{username}/block"
        url = urljoin(self.base_url, location)
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f'session={self.cookie}'
        }
        return self.session.post(url=url, headers=headers)

    def unblock_user(self, username):
        location = f"/api/user/{username}/accept"
        url = urljoin(self.base_url, location)
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f'session={self.cookie}'
        }
        return self.session.post(url=url, headers=headers)

    def get_status(self):
        location = "/status"
        url = urljoin(self.base_url, location)
        headers = {
            'Content-Type': 'application/json'
        }

        return self.session.get(url=url, headers=headers)

    def put_change_password(self, username, new_password):
        location = f"/api/user/{username}/change-password"
        url = urljoin(self.base_url, location)
        headers = {
            'Content-Type': 'application/json',
            'Cookie': f'session={self.cookie}'
        }
        data = {
            "password": new_password
        }
        return self.session.put(url=url, headers=headers, json=data)

    def get_cookie(self, user):
        location = "/login"
        url = urljoin(self.base_url, location)

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            "username": user[3],
            "password": user[4],
            "submit": "Login"
        }
        #print(user)
        res = self.session.post(url=url, headers=headers, data=data, allow_redirects=False)

        self.cookie = res.headers["Set-Cookie"].split(";")[0].split("=")[-1]
