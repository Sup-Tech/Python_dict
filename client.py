from socket import *
import json

class Client:
    def __init__(self):
        self.server_address = ('192.168.10.156', 25014)
        self.cSocket = socket()
        self.cSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.cSocket.connect(self.server_address)
    def handle(self, data):
        pass

    def login(self):
        pass

    def send(self, msg):
        msg = json.dumps(msg)
        # print(msg)
        self.cSocket.send(msg.encode())

    def recive(self):
        data = self.cSocket.recv(1024*1024)
        return data.decode()


class NoteLogic:
    def __init__(self):
        pass



class DictLogic:
    def __init__(self):
        pass


# <register>
# input>>name,passwd,passwd_
# button [sign up]
#     is passwd == passwd_?
#     -->ok
# msg=json.dump({'name:name;pwd:pwd'})
# send(msg)
#     recv()--re
#     handle(re)
#     showStatus(msg)
#     -->no
#     showStatus(msg)
# >>>ok
# <login>
# input>>name,pwd
# button [sign in]
#     send(name,pwd)
#     recv() -->re
#     re-->ok
