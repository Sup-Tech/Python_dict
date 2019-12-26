from PyQt5 import QtWidgets
from login_window import *
from client import *


class Example(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_login_page()
        self.ui.setupUi(self)
        self.client = Client()
    def login(self):
        """
            登录界面的确认按钮
        :return:
        """
        msg = {}
        msg['protocol'] = 'LOGIN'
        msg['name'] = self.ui.username.text()
        msg['pwd'] = self.ui.password.text()
        print(msg)
        self.client.send(msg)
        data = self.client.recive()
        print(data)
        if data == 'loginok':
            self.ui.cancel_login.clicked()
        else:
            self.showStatus(data)

    def showStatus(self, data):
        """
            根据data内容，在客户端显示相应的信息
        :param data: string
        :return: none
        """
        if data == '':
            pass
