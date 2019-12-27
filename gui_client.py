"""
GUI界面对象
"""

from PyQt5.QtWidgets import QMainWindow, QWidget
from login_window import *
from python_dict import *
from register_page import *
import time


class PythonDict(QMainWindow):
    """
    主界面
    """
    def __init__(self, socket):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)
        self.socket = socket


class LoginWindow(QWidget):
    """
    登入界面
    """
    def __init__(self, socket):
        QWidget.__init__(self)
        self.login_page = Ui_login_page()
        self.login_page.setupUi(self)
        self.socket = socket

    def login(self):
        """
            登录界面的确认按钮 点击后 执行该方法
        :return:
        """
        print("excute login")
        msg = {'protocol': 'LOGIN',
               'name': self.login_page.username.text(),
               'pwd': self.login_page.password.text()}
        print('发送信息', msg)
        self.socket.send(msg)
        print('发送成功')
        data = self.socket.recive()
        print('接收信息')
        print(data)
        if data == 'loginok':
            print('---')
            time.sleep(2)
            self.show_status(data)
            self.login_page.cancel_login.clicked()
        else:
            print('sdf')
            self.show_status(data)



    def show_status(self, data):
        """
            根据data内容，在客户端显示相应的信息
        :param data: string
        :return: none
        """
        if data == 'loginok':
            self.login_page.label_3.setText('登录成功')
        elif data == 'usernamenotexist':
            self.login_page.label_3.setText('用户名不存在')
        elif data == 'lognok':
            self.login_page.label_3.setText('用户名或密码错误')
            print('sdf')





class RegisterWindow(QWidget):
    """
    注册界面
    """
    def __init__(self, socket):
        QWidget.__init__(self)
        self.register_page = Ui_Form()
        self.register_page.setupUi(self)
        self.socket = socket


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     main_page = PythonDict()
#     login_page = LoginWindow()
#     register_page = RegisterWindow()
#
#     main_page.show()
#     # 主界面菜单中的login-->打开登录界面
#     main_page.main_ui.actionlogin.triggered.connect(login_page.show)
#     # 登录界面中的注册按钮-->打开注册界面
#     login_page.login_page.registerButton.clicked.connect(register_page.show)
#
#     sys.exit(app.exec_())
