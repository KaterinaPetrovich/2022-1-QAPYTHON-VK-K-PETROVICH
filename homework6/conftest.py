import pytest
from mysql.client import MysqlClient


@pytest.fixture(scope='session')
def mysql_client():
    mysql_client = MysqlClient(user='root', port=3306, password='pass',
                               host='127.0.0.1', db_name='TEST_SQL')
    mysql_client.connect()
    yield mysql_client
    mysql_client.connection.close()


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        mysql_client = MysqlClient(user='root', port=3306, password='pass',
                                   host='127.0.0.1', db_name='TEST_SQL')
        mysql_client.create_db()
        mysql_client.connect()
        mysql_client.create_tables()
        mysql_client.connection.close()


def pytest_unconfigure(config):
    if not hasattr(config, 'workerinput'):
        mysql_client = MysqlClient(user='root', port=3306, password='pass',
                                   host='127.0.0.1', db_name='TEST_SQL')
        mysql_client.connect()
        mysql_client.delete_db()
        mysql_client.connection.close()
