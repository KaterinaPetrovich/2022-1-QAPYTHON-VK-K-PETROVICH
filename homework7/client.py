from _socket import timeout
import socket
import json


import settings


class ClientSocket:

    def __init__(self):
        self.host = settings.MOCK_HOST
        self.port = int(settings.MOCK_PORT)

    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(0.1)
        self.client.connect((self.host, self.port))

    def get_request(self, target_url):
        self.connect()
        request = f'GET {target_url} HTTP/1.1\r\n' \
                  f'Host:{self.host}\r\n\r\n'
        return self.make_request(request)

    def response(self):
        total_data = []

        while True:
            # читаем данные из сокета до тех пор пока они там есть
            data = self.client.recv(1024)
            if data:
                total_data.append(data.decode())
            else:
                break

        data = ''.join(total_data).splitlines()
        return data

    def post_request(self, target_url, params):
        self.connect()
        content_type = 'application/json'
        request = f'POST {target_url} HTTP/1.1\r\n' \
                  f'Host:{self.host}\r\n' \
                  f'Content-Type: {content_type}\r\n' \
                  f'Content-Length: {len(params)}\r\n' \
                  f'\r\n' \
                  f'{params}' \
                  f'\r\n\r\n'

        return self.make_request(request)

    def put_request(self, target_url, params):
        self.connect()
        content_type = 'Content-Type: application/json'
        content_length = f'Content-Length:{str(len(params))}'
        request = f'PUT {target_url} HTTP/1.1\r\n' \
                  f'Host: {self.host}\r\n' \
                  f'{content_type}\r\n' \
                  f'{content_length}\r\n\r\n' + json.dumps(params)

        return self.make_request(request)

    def delete_request(self, target_url, params):
        self.connect()
        content_type = 'Content-Type: application/json'
        content_length = f'Content-Length:{str(len(params))}'
        request = f'DELETE {target_url} HTTP/1.1\r\n' \
                  f'Host: {self.host}\r\n' \
                  f'{content_type}\r\n' \
                  f'{content_length}\r\n\r\n' \
                  + str(params)

    def make_request(self, request):
        self.client.send(request.encode())
        total_data = []
        try:
            while True:
                data = self.client.recv(4096)
                if data:
                    total_data.append(data.decode())
                else:
                    break
        except timeout:
            pass
        data = ''.join(total_data).splitlines()
        self.client.close()
        return data
