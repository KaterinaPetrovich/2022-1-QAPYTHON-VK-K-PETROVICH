from urllib.parse import urljoin

import requests


class ApiClient:
    def __init__(self):
        self.base_url = "https://target.my.com/"
        self.csrf_token = None
        self.session = requests.Session()

    def post_login(self):
        login = "katerina_petrovich@bk.ru"
        password = "135qwe"
        location = "https://auth-ac.my.com/auth"
        headers = {
            "Referer": "https://account.my.com/",
        }
        data = {
                "email": login,
                "password": password,
                "continue": "https://target.my.com/auth/mycom?state=target_login%3D1%26ignore_opener%3D1#email",
                "failure": "https://account.my.com/login/",
                "nosavelogin": "0"
                }

        self.session.post(url=location, headers=headers, data=data)
        self.csrf_token = self.get_csrf_token()

    def get_csrf_token(self):
        location = '/csrf/'
        url=urljoin(self.base_url, location)
        headers = self.session.get(url).headers['Set-Cookie'].split(';')
        cookies = [c for c in headers if 'csrftoken' in c]
        csrf_token = cookies[0].split('=')[-1]
        return csrf_token

    def post_create_segment(self, name):
        location = "/api/v2/remarketing/segments.json?fields=id,name"
        url = urljoin(self.base_url, location)
        headers = {"X-CSRFToken": f'{self.csrf_token}'}
        json = {
            "name": f"{name}",
            "pass_condition": 1,
            "relations": [{"object_type": "remarketing_player",
                           "params": {"left": 365, "right": 0, "type": "positive"}}]}
        response = self.session.post(url, headers=headers, json=json)
        return response.json()["id"]


    def post_delete_segment(self, segment_id):
        url = urljoin(self.base_url, "/api/v1/remarketing/mass_action/delete.json")
        headers = {"X-CSRFToken": self.csrf_token}
        json = [{"source_id": segment_id, "source_type": 'segment'}]
        response = self.session.post(url, headers=headers, json=json)
        return response

    def get_check_segment(self, segment_id):
        url = urljoin(self.base_url, f"/api/v2/remarketing/segments/{segment_id}.json")
        response = self.session.get(url=url)
        return response

    # def post_create_campaign(self, name, image_id, url_id, objective='reach', package_id=960):
    #     location = "/api/v2/campaigns.json"
    #     url = urljoin(self.base_url, location)
    #     headers = {"X-CSRFToken": self.csrf_token}
    #     json = {
    #         #"banners": [{"content": {"image_240x400": {"id": image_id}},
    #                      "urls": {"primary": {"id": url_id}}}],
    #         "name": name,
    #         #"objective": objective, "package_id": package_id}
    #     response = self.session.post(url=url, headers=headers, json=json)
    #     return response







