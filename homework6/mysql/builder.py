from mysql.models import TotalRequestsModel, TypesModel, MostCommonModel, UserErrorModel, \
    ServerErrorModel


class MysqlBuilder:

    def __init__(self, client):
        self.client = client

    def create_total_requests(self, count):
        total_requests = TotalRequestsModel(count=count)
        self.client.session.add(total_requests)
        self.client.session.commit()
        return total_requests

    def create_types(self, count, type_name):
        types = TypesModel(type_name=type_name, count=count)
        self.client.session.add(types)
        self.client.session.commit()
        return types

    def create_most_common(self, url, count):
        most_common = MostCommonModel(url=url, count=count)
        self.client.session.add(most_common)
        self.client.session.commit()
        return most_common

    def create_user_error(self, url, status, size, IP):
        user_error = UserErrorModel(url=url, status=status, size=size, IP=IP)
        self.client.session.add(user_error)
        self.client.session.commit()
        return user_error

    def create_server_error(self, IP, count):
        user_error = ServerErrorModel(IP=IP, count=count)
        self.client.session.add(user_error)
        self.client.session.commit()
        return user_error
