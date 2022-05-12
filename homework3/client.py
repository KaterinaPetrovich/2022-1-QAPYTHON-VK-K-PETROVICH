from urllib.parse import urljoin
import json
import os
from helper import get_credentials

import requests


class ApiClient:
    def __init__(self):
        self.base_url = "https://target.my.com/"
        self.csrf_token = None
        self.session = requests.Session()

    def post_login(self):
        login, password = get_credentials()
        location = "https://auth-ac.my.com/auth"
        headers = {
            "Referer": "https://account.my.com/",
        }
        data = {
            "email": login,
            "password": password,
            "continue": "https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email",
            "failure": "https://account.my.com/login/",
            "nosavelogin": "0",
        }

        self.session.post(url=location, headers=headers, data=data)
        self.csrf_token = self.get_csrf_token()

    def get_csrf_token(self):
        location = "/csrf/"
        url = urljoin(self.base_url, location)
        headers = self.session.get(url).headers["Set-Cookie"].split(";")
        cookies = [c for c in headers if "csrftoken" in c]
        csrf_token = cookies[0].split("=")[-1]
        return csrf_token

    def post_create_segment(self, name):
        location = "/api/v2/remarketing/segments.json?fields=id,name"
        url = urljoin(self.base_url, location)
        headers = {"X-CSRFToken": f"{self.csrf_token}"}
        json_data = {
            "name": f"{name}",
            "pass_condition": 1,
            "relations": [
                {
                    "object_type": "remarketing_player",
                    "params": {"left": 365, "right": 0, "type": "positive"},
                }
            ],
        }
        response = self.session.post(url, headers=headers, json=json_data)
        return response.json()["id"]

    def post_delete_segment(self, segment_id):
        url = urljoin(self.base_url, "/api/v1/remarketing/mass_action/delete.json")
        headers = {"X-CSRFToken": self.csrf_token}
        json = [{"source_id": segment_id, "source_type": "segment"}]
        response = self.session.post(url, headers=headers, json=json)
        return response

    def get_check_segment(self, segment_id):
        url = urljoin(self.base_url, f"/api/v2/remarketing/segments/{segment_id}.json")
        response = self.session.get(url=url)
        return response

    def post_create_campaign(self, name, repo_root):
        url = urljoin(self.base_url, "/api/v2/campaigns.json")
        headers = {"X-CSRFToken": self.csrf_token}
        file_path = os.path.join(repo_root, "data.json")
        with open(file_path, "r") as read_file:
            data = json.load(read_file)
            data["name"] = name
        response = self.session.post(url=url, headers=headers, json=data)
        return response.json()["id"]

    def delete_campaign(self, campaign_id):
        url = urljoin(self.base_url, f"api/v2/campaigns/{campaign_id}.json")
        headers = {"X-CSRFToken": self.csrf_token}
        response = self.session.delete(url=url, headers=headers)
        return response

    def get_check_campaign(self, campaign_id):
        url = urljoin(self.base_url, f"api/v2/campaigns/{campaign_id}.json")
        headers = {"X-CSRFToken": self.csrf_token}
        response = self.session.get(url=url, headers=headers)
        return response
