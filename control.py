from client import Client
import platform


class Control:
    def __init__(self, client):
        self.client = client
        self.noteLg = NoteLogic(self.client)
        self.dictLg = DictLogic(self.client)
        self.logLg = LogLogic(self.client)
        self.regLg = RegLogic(self.client)

    def signal_in(self, signal, data):
        """
            由gui_client调用，并传参
        param: signal -->[string]
        param: data -->[dict]
        """
        if signal == 'QUEDICT':
            return self.dictLg.query(data)
        elif signal == 'LOG':
            return self.logLg.login(data)
        elif signal == 'REG':
            return self.regLg.register(data)
        elif signal == 'QNT':
            return self.noteLg.queryNote(data)
        elif signal == 'OPENF':
            return self.logLg.open_account_file(data)

            
class Logic:
    def __init__(self):
        pass

    def handle(self):
        pass


class NoteLogic:
    def __init__(self, client):
        self.client = client

    def handle(self, data):
        print('逻辑成功')
        print(data)

    def queryNote(self, data):
        self.client.send(data)
        msg = self.client.recive()
        return msg


class DictLogic:
    def __init__(self, client):
        self.client = client

    def query(self, data):
        self.client.send(data)
        print('self.client.send(data) 执行')
        msg = self.client.recive()
        print('msg = self.client.recive() 执行')
        print(msg)
        return msg


class LogLogic:
    def __init__(self, client):
        self.client = client
        self.account_path_Win = r'C:/jabna.txt'
        self.account_path_Darwin = r'/Users/Zuban/jabna.txt'
    def login(self, data):
        self.client.send(data)
        print('发送成功')
        msg = self.client.recive()
        print('接收成功', msg)
        return msg

    def open_account_file(self, model):
        """ 根据操作系统 来决定文件路径"""
        s = platform.system()
        f = None
        if s == 'Windows':
            f = open(self.account_path_Win, model)
        elif s == 'Darwin':
            f = open(self.account_path_Darwin, model)
        return f

class RegLogic:
    def __init__(self, client):
        self.client = client

    def register(self, data):
        self.client.send(data)
        print('发送成功')
        msg = self.client.recive()
        return msg
