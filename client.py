"""
tcp客户端
"""
from socket import *
import json


class Client:
    def __init__(self):
        server_address = ('127.0.0.1', 25014)
        self.cSocket = socket()
        self.cSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.cSocket.connect(server_address)

    def handle(self, data):
        pass

    def login(self):
        pass

    def send(self, msg):
        msg = json.dumps(msg)
        # print(msg)
        self.cSocket.send(msg.encode())

    def recive(self):
        data = self.cSocket.recv(1024)
        return data.decode()

    def close(self):
        self.cSocket.close()

class NoteLogic:
    def __init__(self):
        pass


class DictLogic:
    def __init__(self):
        pass
