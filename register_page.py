# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_page.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(470, 330)
        Form.setMinimumSize(QtCore.QSize(470, 330))
        Form.setBaseSize(QtCore.QSize(470, 330))
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pwd1 = QtWidgets.QLineEdit(Form)
        self.pwd1.setMinimumSize(QtCore.QSize(0, 30))
        self.pwd1.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setKerning(False)
        self.pwd1.setFont(font)
        self.pwd1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pwd1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd1.setReadOnly(False)
        self.pwd1.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.pwd1.setObjectName("pwd1")
        self.gridLayout.addWidget(self.pwd1, 2, 3, 1, 5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 5, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 6, 6, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 7, 1, 1)
        self.pwd2 = QtWidgets.QLineEdit(Form)
        self.pwd2.setMinimumSize(QtCore.QSize(0, 30))
        self.pwd2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd2.setObjectName("pwd2")
        self.gridLayout.addWidget(self.pwd2, 4, 3, 1, 5)
        self.registerButton = QtWidgets.QPushButton(Form)
        self.registerButton.setObjectName("registerButton")
        self.gridLayout.addWidget(self.registerButton, 6, 4, 1, 1)
        self.username_register = QtWidgets.QLineEdit(Form)
        self.username_register.setMinimumSize(QtCore.QSize(0, 30))
        self.username_register.setObjectName("username_register")
        self.gridLayout.addWidget(self.username_register, 0, 3, 1, 5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 3, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 5, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 0, 0, 7, 1)
        spacerItem6 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 0, 10, 7, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 2, 1, 1)

        self.retranslateUi(Form)
        self.cancelButton.clicked.connect(Form.close)
        self.registerButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "注册"))
        Form.setAccessibleName(_translate("Form", "register_page"))
        self.pwd1.setPlaceholderText(_translate("Form", "请输入密码"))
        self.label.setText(_translate("Form", "用户名"))
        self.cancelButton.setText(_translate("Form", "取消"))
        self.pwd2.setPlaceholderText(_translate("Form", "请再次输入密码"))
        self.registerButton.setText(_translate("Form", "注册"))
        self.username_register.setAccessibleName(_translate("Form", "username_register"))
        self.username_register.setPlaceholderText(_translate("Form", "请输入用户名"))
        self.label_3.setText(_translate("Form", "密码"))
        self.label_2.setText(_translate("Form", "密码"))
