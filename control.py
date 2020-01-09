from client import Client
import platform


class Control:
    def __init__(self, client):
        self.client = client
        self.logic = Logic(self.client)
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
            return self.dictLg.request(data)
        elif signal == 'request':
            return self.logic.request(data)
        elif signal == 'LOG':
            return self.logLg.request(data)
        elif signal == 'REG':
            return self.regLg.request(data)
        elif signal == 'QNT':
            return self.noteLg.request(data)
        elif signal == 'OPENF':
            return self.logLg.open_account_file(data)
        elif signal == 'ALTNT':
            return self.noteLg.request(data)
        elif signal == 'CNT':
            return self.noteLg.request(data)


class Logic:
    def __init__(self, client):
        self.client = client

    def request(self, data):
        self.client.send(data)
        msg = self.client.recive()
        return msg


class NoteLogic(Logic):
    def __init__(self, client):
        super(Logic, self).__init__()
        self.client = client


class DictLogic(Logic):
    def __init__(self, client):
        super(Logic, self).__init__()
        self.client = client


class LogLogic(Logic):
    def __init__(self, client):
        super(Logic, self).__init__()
        self.client = client
        self.account_path_Win = r'./jabna.txt'
        self.account_path_Darwin = r'/Users/Zuban/jabna.txt'

    def open_account_file(self, model):
        """ 根据操作系统 来决定文件路径"""
        s = platform.system()
        f = None
        if s == 'Windows':
            f = open(self.account_path_Win, model)
        elif s == 'Darwin':
            f = open(self.account_path_Darwin, model)
        return f


class RegLogic(Logic):
    def __init__(self, client):
        super(Logic, self).__init__()
        self.client = client
