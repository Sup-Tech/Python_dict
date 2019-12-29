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

    data = connfd.recv(1024)
    data = json.loads(data)
    # data_2 = json.loads(data)
    # print(data_2)
    if data['protocol'] == 'QUEDICT':
        print(data)
        msg = {'protocol': 'QUEOK',
               're1': {'id': '11', 'word': 'input', 'mean': '输入', 'eg': 'a = input(\'Please enter username: \')',
                       'eg_mean': "引号中的内容提示用户输入 最后用户输入的结果将赋值给a"},
               're2':{'id': '11', 'word': 'output', 'mean': '输出', 'eg': 'a = input(\'Please enter username: \')',
                       'eg_mean': "垃圾收款星期几居室的方法呢但就在小歘在新年惨剧啊忽视的附件是宪法的撒大火发生的纠纷获取 是否哈哈第三方进行呢ad艾弗森速度 是你发的顺丰适得府君书加案件的说法\n圾收款星期几居室的方法呢但就在小歘在新年惨剧啊忽视的附件是宪法的撒大火发生的纠纷获取 是否哈哈第三方进行呢ad艾弗森速度 是你发的顺丰适得府君书加案"}
               }
        msg = json.dumps(msg)
        connfd.send(msg.encode())
    elif data['protocol'] == 'LOG':
        print(data)
        msg = {'protocol': 'LOGUNE'}
        msg = json.dumps(msg)
        connfd.send(msg.encode())
