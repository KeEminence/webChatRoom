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
        chatRoom.resize(519, 497)
        self.line = QtGui.QFrame(chatRoom)
        self.line.setGeometry(QtCore.QRect(360, 10, 21, 501))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.layoutWidget = QtGui.QWidget(chatRoom)
        self.layoutWidget.setGeometry(QtCore.QRect(380, 10, 131, 481))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.browser1 = QtGui.QTextBrowser(self.layoutWidget)
        self.browser1.setMaximumSize(QtCore.QSize(131, 261))
        self.browser1.setObjectName(_fromUtf8("browser1"))
        self.verticalLayout_2.addWidget(self.browser1)
        self.line_2 = QtGui.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_2.addWidget(self.line_2)
        self.browser2 = QtGui.QTextBrowser(self.layoutWidget)
        self.browser2.setMaximumSize(QtCore.QSize(16777215, 201))
        self.browser2.setObjectName(_fromUtf8("browser2"))
        self.verticalLayout_2.addWidget(self.browser2)
        self.layoutWidget1 = QtGui.QWidget(chatRoom)
        self.layoutWidget1.setGeometry(QtCore.QRect(3, 14, 361, 481))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.browser = QtGui.QTextBrowser(self.layoutWidget1)
        self.browser.setObjectName(_fromUtf8("browser"))
        self.verticalLayout.addWidget(self.browser)
        self.lineEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.emitButton = QtGui.QPushButton(self.layoutWidget1)
        self.emitButton.setObjectName(_fromUtf8("emitButton"))
        self.horizontalLayout.addWidget(self.emitButton)
        self.picButton = QtGui.QPushButton(self.layoutWidget1)
        self.picButton.setObjectName(_fromUtf8("picButton"))
        self.horizontalLayout.addWidget(self.picButton)
        self.fiButton = QtGui.QPushButton(self.layoutWidget1)
        self.fiButton.setObjectName(_fromUtf8("fiButton"))
        self.horizontalLayout.addWidget(self.fiButton)
        self.closeButton = QtGui.QPushButton(self.layoutWidget1)
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
        self.browser1.setHtml(_translate("chatRoom", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#000000;\">NEWS</span></p></body></html>", None))
        self.browser2.setHtml(_translate("chatRoom", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.browser.setHtml(_translate("chatRoom", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#00007f;\">             Welcome to the chat room</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#00007f;\">                       Enjoy yourself</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; font-style:italic; color:#00007f;\">-------------------------------------------------</span></p></body></html>", None))
        self.emitButton.setText(_translate("chatRoom", "&Emit", None))
        self.picButton.setText(_translate("chatRoom", "&Image", None))
        self.fiButton.setText(_translate("chatRoom", "&File", None))
        self.closeButton.setText(_translate("chatRoom", "&Close", None))

