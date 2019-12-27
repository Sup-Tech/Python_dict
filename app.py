"""
这个文件用来集成GUI和客户端
"""
from gui_client import *
from PyQt5.QtWidgets import QApplication
import sys
from client import Client


class ProcessApp:
    def __init__(self):
        """
        创建app界面对象
        """
        self.app = QApplication(sys.argv)
        self.client = Client()
        self.main_page = PythonDict(self.client)
        self.login_page = LoginWindow(self.client)
        self.register_page = RegisterWindow(self.client)

    def start(self):
        """
        显示界面
        """
        # 显示主界面
        self.main_page.show()
        # 主界面菜单中的login-->打开登录界面
        self.main_page.main_ui.actionlogin.triggered.connect(self.login_page.show)
        # 登录界面中的注册按钮-->打开注册界面
        self.login_page.login_page.registerButton.clicked.connect(self.register_page.show)

    def close(self):
        sys.exit(self.app.exec_())
