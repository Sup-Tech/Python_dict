from socket import *
import json

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 25014))
s.listen(3)
connfd, addr = s.accept()
print(connfd, addr)
print('已连接')

while True:

    data = connfd.recv(128)
    print(data.decode())
    # data_2 = json.loads(data)
    # print(data_2)
    if data:
        print(data)
        connfd.send(b'lognok')
        print('21')
