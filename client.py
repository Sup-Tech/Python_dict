"""
tcp客户端
"""
from socket import *
import json


class Client:
    def __init__(self):
        """

        :param logic: 传入NoteLogic/DictLogic 类型[class]
        """
        server_address = ('127.0.0.1', 25014)
        self.cSocket = socket()
        self.cSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.cSocket.connect(server_address)


    def login(self):
        pass

    def send(self, msg):
        """
        param: msg --->[dict]
        """
        msg = json.dumps(msg)
        # print(msg)
        self.cSocket.send(msg.encode())

    def recive(self):
        data = self.cSocket.recv(1024*1024)
        data = json.loads(data)
        return data

    def close(self):
        self.cSocket.close()
