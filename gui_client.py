"""
GUI界面对象
"""

from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5 import QtCore, QtWidgets, QtGui
from login_window import *
from python_dict import *
from register_page import *
import time


"""
signal: 前4位代表信号头不能改,用来调相应功能的类
DICT QUE
NOTE
LOGN
REGS
"""

class PythonDict(QMainWindow):
    """
    主界面
    """
    def __init__(self, control):
        """
        param: control -->[class]

        主界面元素参数信息：
        笔记页区
        self.note_edit = 笔记-笔记编辑区[QTextEdit对象]
        self.checkBoxNote = 笔记-编辑复选框[QCheckBox对象]
        self.note_profile = 笔记-显示笔记详细信息（如：创建时间）[QLabel对象]
        self.notes_list = 笔记-所有个人笔记列表显示区[QListWidget对象]
        字典页区
        self.search = 搜索按钮[QPushButton对象]
        self.search_bar = 搜索栏[QLineEdit对象]
        self.search_result_list = 搜索的结果列表[QListWidget对象]
        self.result_browser = 搜索的单个结果详细显示[QTextBrowser对象]
        """
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.initUI()
        self.main_ui.setupUi(self)
        # 传入control对象
        self.control = control
        # 字典查询结果
        self.dict_re_data = {}

    def initUI(self):
        """
            设置UI界面
        """
        # 设置窗口 Icon
        self.setWindowIcon(QtGui.QIcon('./img/Quantum light logo bold.png'))

    def search(self):
        """ 搜索按钮 点击 后执行此方法 """

        data = {'protocol': 'QUEDICT', 'word': self.main_ui.search_bar.text()}
        print(data)
        # 向control传信号 return---> data
        msg = self.control.signal_in('QUEDICT', data)
        print('last:', msg)
        if msg['protocol'] == 'QUEOK':
            self.show_query_result(msg)
        else:
            self.show_failed()

    def show_query_result(self, data):
        """
            根据参数data进行协议判定 最终在界面显示数据
            data: [dict]
        """
        # 删除字典中的协议
        del data['protocol']
        self.dict_re_data = data
    # 把单词查询结果 在界面列表显示出来
        # 清屏 --> search_result_list
        self.main_ui.search_result_list.clear()
        for value in data.values():
            # search_result_list添加条目
            self.main_ui.search_result_list.addItem(value['word'])
            # 判定 search_bar 中的搜索词 是否一样
            if value['word'] == self.main_ui.search_bar.text():
                # 清屏--> result_browser
                self.main_ui.result_browser.clear()
                self.dict_result_display_logic(value)

    def list_re_clicked(self):
        """
        当字典界面的 <search_result_list 搜索的结果列表> 中的条目被点击时 执行此函数
        :return: none
        """
        # 获取点击条目的单词 target_obj -->[string]
        target_obj = self.main_ui.search_result_list.currentItem().text()
        print(target_obj)
        # 清空字典界面中 <self.result_browser 搜索的单个结果详细显示>
        self.main_ui.result_browser.clear()
        print('screen clear')
        for key, value in self.dict_re_data.items():
            if value['word'] == target_obj:
                print(value)
                self.dict_result_display_logic(value)


    def show_failed(self):
        """
            当查询失败时 在界面提示
        """
        self.main_ui.result_browser.append('无查询结果')

    def dict_result_display_logic(self, item):
        """
            <self.result_browser 搜索的单个结果详细显示>显示逻辑
        :param item: 单词 -->{'id': '', 'word': '', 'mean': '', 'eg': ''}
        :return: none
        """
        for key, value in item.items():
            if value == '':
                continue
            if key == 'id' or key == 'word':
                continue
            elif key == 'mean':
                result = '中文释义: ' + value
                self.main_ui.result_browser.append(result)
            elif key == 'eg':
                result = '例子: ' + value
                self.main_ui.result_browser.append(result)
            elif key == 'eg_mean':
                result = '解释: ' + value
                self.main_ui.result_browser.append(result)

    # --------------------------------------------------------- 往下 Note 部分代码

    # def list_pop_menu(self):
    #     self.popMenu = QtWidgets.QMenu(self.main_ui.search_result_list)
    #     self.item_del = QtWidgets.QAction(QtGui.QIcon('./img/del.jpg'), '删除', self)
    #     self.popMenu.addAction(self.item_del)
    #     # popMenu出现在窗口的位置
    #     self.popMenu.exec_(QtGui.QCursor.pos())
    #     if self.item_del.isEnabled():
    #         self.del_item()
    #
    # def del_item(self):
    #     print('yes')

        # self.search_result_list.setContextMenuPolicy(3)
        # self.search_result_list.customContextMenuRequested[QtCore.QPoint].connect(MainWindow.list_pop_menu)

class LoginWindow(QWidget):
    """
        登入界面
    元素:
    self.username = 用户名 [QLineEdit]
    self.password = 密码  [QLineEdit]
    self.login = 登录按钮   [QPushButton]
    self.cancel_login = 取消登录按钮  [QPushButton]
    self.remember_me_check = 记住用户 [QCheckBox]
    self.login_status_bar = 登录提示信息  [QLabel]
    """
    def __init__(self, control):
        QWidget.__init__(self)
        self.login_page = Ui_login_page()
        self.login_page.setupUi(self)
        self.control = control

    def login(self):
        """
            登录界面的确认按钮 点击后 执行该方法
        :return:
        """
        msg = {'protocol': 'LOG',
       'name': self.login_page.username.text(),
       'pwd': self.login_page.password.text()}
        # 向control传信号 return---> data
        result = self.control.signal_in('LOGOK', msg)
        # 对data['protocol']判断
        if result['protocol'] == 'LOGOK':
            self.show_status('LOGOK')
        elif result['protocol'] == 'LOGUNE':
            # 无此用户名
            self.show_status('LOGUNE')
        elif result['protocol'] == 'LOGWP':
            # 密码错误
            self.show_status('LOGWP')


    def show_status(self, data):
        """
            根据data内容，在客户端显示相应的信息
        :param data: string
        :return: none
        """
        if data == 'LOGOK':
            self.login_page.login_status_bar.setText('登录成功')
        elif data == 'LOGUNE':
            self.login_page.login_status_bar.setText('用户名不存在')
        elif data == 'LOGWP':
            self.login_page.login_status_bar.setText('用户名或密码错误')



class RegisterWindow(QWidget):
    """
    注册界面
    """
    def __init__(self, control):
        QWidget.__init__(self)
        self.register_page = Ui_Form()
        self.register_page.setupUi(self)
        self.control = control
