from client import ApiClient
import pytest
import random
import string
import os


@pytest.fixture(scope="session")
def api_client():
    api_client = ApiClient()
    return api_client


@pytest.fixture(scope="function")
def random_str(size=7):
    return "".join(random.choice(string.ascii_letters) for _ in range(size))


@pytest.fixture(scope="session")
def repo_root():
    return os.path.abspath(os.path.join(__file__, os.path.pardir))
