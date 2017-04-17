#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import ui_login
import client

import sqlite3

MAC = True
try:
    from PyQt4.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False

class Login(QDialog,ui_login.Ui_loginx):
	def __init__(self,parent=None):
		super(Login,self).__init__(parent)
		#self.__text=unicode(text)
		self.conn=sqlite3.connect('/root/test.db')
		# print "init"
		#self.connect(self.loginButton,SIGNAL("loginTo"),self.loginTo)
		self.username=None
		self.passwd=None
		self.setupUi(self)
		if not MAC:
			self.loginButton.setFocusPolicy(Qt.NoFocus)
			self.registerButton.setFocusPolicy(Qt.NoFocus)
			self.updateUi()

	@pyqtSlot(QString)
	def on_userLineEdit_textEdited(self):
		self.updateUi()

	@pyqtSlot(QString)
	def on_passWordLineEdit_textEdited(self):
		self.updateUi()



	def updateUi(self):
		enable=not (self.userLineEdit.text().isEmpty() and self.passWordLineEdit.text().isEmpty())
		self.loginButton.setEnabled(enable)
		self.registerButton.setEnabled(enable)

	# def text(self):
	# 	return self.__text

	@pyqtSlot()
	def on_loginButton_clicked(self):
		class PasswdError(Exception):pass
		class UserError(Exception):pass
		uflag=False
		self.username=unicode(self.userLineEdit.text())
		self.passwd=unicode(self.passWordLineEdit.text())
		cursor=self.conn.execute("select username,password from user")
		try:			
			for row in cursor:
				tempusername=row[0]
				temppasswd=row[1]
				if self.username==tempusername:
					if self.passwd==temppasswd:
						#print "in"
						uflag=True
						self.emit(SIGNAL("loginTo"))
					else:
						raise PasswdError,("Please enter the correct password!")
			if not uflag:
				raise UserError,("There is no such a user.")
		except PasswdError,e:
			QMessageBox.warning(self,"Password Error",unicode(e))
			return
		except UserError,e:
			QMessageBox.warning(self,"User Error",unicode(e))
			return





	@pyqtSlot()
	def on_registerButton_clicked(self):
		# print "cliked"
		self.username=unicode(self.userLineEdit.text())
		self.passwd=unicode(self.passWordLineEdit.text())
		self.conn.execute("insert into user (username,password)\
			values (?,?)",(username,passwd))
		QMessageBox.information(None,"User register","register new user successfully!")
		self.conn.commit()


def loginTo():
	a=client.clientv(form.username,form.passwd)
	# print form.username
	form.close()
	a.show()
	a.exec_()

app = QApplication(sys.argv)
form = Login()
form.connect(form,SIGNAL("loginTo"),loginTo)
# print "done"
form.show()
app.exec_()
