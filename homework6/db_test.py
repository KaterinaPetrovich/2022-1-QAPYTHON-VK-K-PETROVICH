import pytest

from mysql.models import TotalRequestsModel, UserErrorModel, MostCommonModel, ServerErrorModel, \
    TypesModel
from mysql.builder import MysqlBuilder
from parser_log import count_requests, count_types, count_longest_requests_with_error, \
    count_most_common_requests, count_users_with_server_error


class MyTest:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql = mysql_client
        self.builder = MysqlBuilder(self.mysql)


class TestMySql(MyTest):

    def test_total_requests(self):
        count = count_requests()
        self.builder.create_total_requests(count=count)
        assert self.mysql.session.query(TotalRequestsModel).all() == 1

    def test_most_common(self):
        urls = count_most_common_requests()
        for key in urls:
            self.builder.create_most_common(url=key, count=urls[key])
        assert self.mysql.session.query(MostCommonModel).all() == 10

    def test_types(self):
        types = count_types()
        for key in types:
            self.builder.create_types(type=key, count=types[key])
        assert self.mysql.session.query(TypesModel).all() == 10

    def test_user_error(self):
        requests = count_longest_requests_with_error()
        for req in requests:
            self.builder.create_user_error(url=req[0], status=req[1], size=req[2], IP=req[3])
        assert self.mysql.session.query(UserErrorModel) == 5

    def test_server_error(self):
        users = count_users_with_server_error()
        for key in users:
            self.builder.create_server_error(IP=key, count=users[key])
        assert self.mysql.session.query(ServerErrorModel) == 5
