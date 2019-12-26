from socket import *


class Client:
    def __init__(self):
        self.cSocket = socket()
        self.cSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, DEBUG)

    def handle(self):
        pass


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
