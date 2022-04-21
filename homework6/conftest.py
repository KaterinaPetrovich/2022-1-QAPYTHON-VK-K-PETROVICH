import pytest
from mysql.client import MysqlClient


@pytest.fixture(scope='session')
def mysql_client():
    mysql_client = MysqlClient()
    mysql_client.connect()
    yield mysql_client
    mysql_client.connection.close()

def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        mysql_client = MysqlClient()
        mysql_client.create_db()

        mysql_client.connect()
        mysql_client.create_table('total_requests')
        mysql_client.create_table('types')
        mysql_client.create_table('most_common')
        mysql_client.create_table('user_error')
        mysql_client.create_table('server_error')
        mysql_client.connection.close()