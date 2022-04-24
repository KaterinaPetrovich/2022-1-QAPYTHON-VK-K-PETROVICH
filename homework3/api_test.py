from base import ApiBase
import pytest


class TestApi(ApiBase):
    @pytest.mark.API
    def test_segment_creation(self, random_str):
        name = random_str
        id = self.api_client.post_create_segment(name)
        assert self.api_client.get_check_segment(id).json()["name"] == name
        assert self.api_client.get_check_segment(id).status_code == 200

    @pytest.mark.API
    def test_segment_deletion(self, random_str):
        name = random_str
        id = self.api_client.post_create_segment(name)
        self.api_client.post_delete_segment(id)
        assert self.api_client.get_check_segment(id).status_code == 404

    @pytest.mark.API
    def test_campaign_creation(self, random_str, repo_root):
        name = random_str
        id = self.api_client.post_create_campaign(name, repo_root)
        assert self.api_client.get_check_campaign(id).json()["name"] == name
        assert self.api_client.get_check_campaign(id).status_code == 200
        self.api_client.delete_campaign(id)
