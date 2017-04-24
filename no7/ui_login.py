# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_loginx(object):
    def setupUi(self, loginx):
        loginx.setObjectName(_fromUtf8("loginx"))
        loginx.resize(354, 228)
        self.layoutWidget = QtGui.QWidget(loginx)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 32, 219, 156))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.userLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.userLineEdit.setObjectName(_fromUtf8("userLineEdit"))
        self.horizontalLayout.addWidget(self.userLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.passWordLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.passWordLineEdit.setObjectName(_fromUtf8("passWordLineEdit"))
        self.horizontalLayout_2.addWidget(self.passWordLineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.loginButton = QtGui.QPushButton(self.layoutWidget)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.horizontalLayout_3.addWidget(self.loginButton)
        self.registerButton = QtGui.QPushButton(self.layoutWidget)
        self.registerButton.setObjectName(_fromUtf8("registerButton"))
        self.horizontalLayout_3.addWidget(self.registerButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label.setBuddy(self.userLineEdit)
        self.label_2.setBuddy(self.passWordLineEdit)

        self.retranslateUi(loginx)
        QtCore.QMetaObject.connectSlotsByName(loginx)
        loginx.setTabOrder(self.userLineEdit, self.passWordLineEdit)
        loginx.setTabOrder(self.passWordLineEdit, self.loginButton)
        loginx.setTabOrder(self.loginButton, self.registerButton)

    def retranslateUi(self, loginx):
        loginx.setWindowTitle(_translate("loginx", "Welcome", None))
        self.label.setText(_translate("loginx", "&Username:", None))
        self.label_2.setText(_translate("loginx", "&Password:", None))
        self.loginButton.setText(_translate("loginx", "&Login", None))
        self.registerButton.setText(_translate("loginx", "&Register", None))

