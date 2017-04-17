# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatroom.ui'
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

class Ui_chatRoom(object):
    def setupUi(self, chatRoom):
        chatRoom.setObjectName(_fromUtf8("chatRoom"))
        chatRoom.resize(327, 475)
        self.layoutWidget = QtGui.QWidget(chatRoom)
        self.layoutWidget.setGeometry(QtCore.QRect(-3, 0, 331, 471))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.browser = QtGui.QTextBrowser(self.layoutWidget)
        self.browser.setObjectName(_fromUtf8("browser"))
        self.verticalLayout.addWidget(self.browser)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.emitButton = QtGui.QPushButton(self.layoutWidget)
        self.emitButton.setObjectName(_fromUtf8("emitButton"))
        self.horizontalLayout.addWidget(self.emitButton)
        self.closeButton = QtGui.QPushButton(self.layoutWidget)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(chatRoom)
        QtCore.QMetaObject.connectSlotsByName(chatRoom)
        chatRoom.setTabOrder(self.lineEdit, self.emitButton)
        chatRoom.setTabOrder(self.emitButton, self.closeButton)
        chatRoom.setTabOrder(self.closeButton, self.browser)

    def retranslateUi(self, chatRoom):
        chatRoom.setWindowTitle(_translate("chatRoom", "chat room", None))
        self.emitButton.setText(_translate("chatRoom", "&Emit", None))
        self.closeButton.setText(_translate("chatRoom", "&Close", None))

