from client import ApiClient
import pytest
import random
import string


@pytest.fixture(scope='session')
def api_client():
    api_client = ApiClient()
    return api_client


@pytest.fixture(scope='function')
def random_str(size=7):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))
