from socket import *
import json

sock = socket()
sock.bind(('192.168.10.156', 25014))
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.listen(3)
connfd, addr = sock.accept()
while True:
    data = connfd.recv(1024*1024)
    print(data.decode())
    # data_2 = json.loads(data)
    # print(data_2)
    if data:
        print(data)
        connfd.send(b'loginok')
        print('21')
