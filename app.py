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
        # 登录界面的登录按钮-->执行main_page的login方法
        self.login_page.login_page.login.clicked.connect(self.main_page.login)
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

        # 笔记界面，启动程序时，根据是否登录，设置笔记界面是否可用
        if self.main_page.isLogin == False:
            self.main_page.main_ui.tab_note.setDisabled(True)
        elif self.main_page.isLogin == True:
            self.main_page.main_ui.tab_note.setDisabled(False)
        # 笔记界面， 启动程序时， 将笔记界面的标题编辑, 笔记编辑区 禁用
        self.main_page.main_ui.note_title.setDisabled(True)
        self.main_page.main_ui.note_edit.setDisabled(True)
        # 笔记界面，编辑checkbox状态变化时 -->
        self.main_page.main_ui.checkBoxNote.stateChanged.connect(self.main_page.noteCheckBoxChange)
        # 笔记界面，新建按钮 -->
        self.main_page.main_ui.new_button.clicked.connect(self.main_page.newNote)
        # 笔记界面，note_list 中条目被点击时
        self.main_page.main_ui.notes_list.itemClicked.connect(self.main_page.notes_list_item_clicked)


        # 自动登录
        self.main_page.autologin()

    def close(self):
        sys.exit(self.app.exec_())
