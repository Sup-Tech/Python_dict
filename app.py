"""
这个文件用来集成GUI和客户端
"""
from gui_client import *
from PyQt5.QtWidgets import QApplication
import sys
from client import Client
from control import *

class ProcessApp:
    def __init__(self):
        """
        创建app界面对象
        """
        self.app = QApplication(sys.argv)
        self.client = Client()
        self.control = Control(self.client)
        self.login_page = LoginWindow(self.control)
        self.register_page = RegisterWindow(self.control)
        self.main_page = PythonDict(self.control, self.login_page, self.register_page)

    def start(self):
        """
        显示界面
        """
        # 显示主界面
        self.main_page.show()
        # 主界面note标签在没登录的时候被点击, 弹出登录窗口
        self.main_page.main_ui.tabWidget.tabBarClicked.connect(self.main_page.tabChange)
        # 主界面菜单中的login-->打开登录界面
        self.main_page.main_ui.actionlogin.triggered.connect(self.login_page.show)
        # 登录界面中的注册按钮-->打开注册界面
        self.login_page.login_page.registerButton.clicked.connect(self.register_page.show)
        # 注册界面中的注册按钮-->
        self.register_page.register_page.registerButton.clicked.connect(self.main_page.register)

        # 设置用户名的最长长度
        self.login_page.login_page.username.setMaxLength(12)
        self.register_page.register_page.username_register.setMaxLength(12)
        # 设置密码的最长长度
        self.login_page.login_page.password.setMaxLength(16)
        self.register_page.register_page.pwd2.setMaxLength(16)
        self.register_page.register_page.pwd1.setMaxLength(16)

        # 字典界面,结果列表中的对象被点击时-->执行方法list_re_clicked（显示相应单词的解释）
        self.main_page.main_ui.search_result_list.itemClicked.connect(self.main_page.list_re_clicked)
        # 字典界面，搜索按钮被点击时-->执行方法search
        self.main_page.main_ui.search.clicked.connect(self.main_page.search)

        # 笔记界面，设置笔记界面不可用
        self.main_page.main_ui.tab_note.setDisabled(True)
    def close(self):
        sys.exit(self.app.exec_())
