import os
import time
from client import ClientSocket
import pytest
import requests
from requests.exceptions import ConnectionError
from mock import flask_mock

import settings
from mock.flask_mock import clean_up

repo_root = os.path.abspath(os.path.join(__file__, os.pardir))


def wait_ready(host, port):
    started = False
    st = time.time()
    while time.time() - st <= 15:
        try:
            requests.get(f'http://{host}:{port}')
            started = True
            break
        except ConnectionError:
            pass
    if not started:
        raise RuntimeError(f'{host}:{port} did not started in 15s!')


@pytest.fixture(scope='session')
def connection():
    flask_mock.run_mock()
    wait_ready(settings.MOCK_HOST, settings.MOCK_PORT)
    client = ClientSocket()
    yield client
    requests.get(f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')

@pytest.fixture(scope='function', autouse=True)
def tear_down():
    yield
    clean_up()