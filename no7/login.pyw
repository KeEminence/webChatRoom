#!/usr/bin/env python

'''This program is for the login ui. After closing it, the ui turn into the chat room ui.'''

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_login
import client
import sqlite3

# This is ready for the mac os, if you are using mac os to code, this program works for coding successfully.
MAC = True
try:
    from PyQt4.QtGui import qt_mac_set_native_menubar
except ImportError:
    MAC = False

# The login ui class
class Login(QDialog,ui_login.Ui_loginx):
	def __init__(self,parent=None):
		super(Login,self).__init__(parent)

		# Connect to the sqlite to store the information of users and their password.
		self.conn=sqlite3.connect('/root/test.db')
		self.username=None
		self.passwd=None
		self.setupUi(self)
		if not MAC:
			self.loginButton.setFocusPolicy(Qt.NoFocus)
			self.registerButton.setFocusPolicy(Qt.NoFocus)
			self.updateUi()

	# When you edit a user name, the UI update itself.
	@pyqtSlot(QString)
	def on_userLineEdit_textEdited(self):
		self.updateUi()

	# When you edit a user password, the UI update itself too.
	@pyqtSlot(QString)
	def on_passWordLineEdit_textEdited(self):
		self.passWordLineEdit.setEchoMode(2)
		self.updateUi()

	# If you edit something on the editline, it enables the button to login or register.
	def updateUi(self):
		enable=not (self.userLineEdit.text().isEmpty() and self.passWordLineEdit.text().isEmpty())
		self.loginButton.setEnabled(enable)
		self.registerButton.setEnabled(enable)

	# When you click the login button, what heppens.
	@pyqtSlot()
	def on_loginButton_clicked(self):
		class PasswdError(Exception):pass
		class UserError(Exception):pass
		uflag=False
		# Store the input name and password to the instance variable.
		self.username=unicode(self.userLineEdit.text())
		self.passwd=unicode(self.passWordLineEdit.text())
		# Obtain the information from the sqlite
		cursor=self.conn.execute("select username,password from user")
		try:	
			# Verify if your input message is matching the condition from the sqlite, and raise the error behavior if it doesn't.	
			# Emit a signal to turn into the chat room UI.		
			for row in cursor:
				tempusername=row[0]
				temppasswd=row[1]
				if self.username==tempusername:
					if self.passwd==temppasswd:
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

	# Register the user to the sqlite, if it doesn't work, output the wrong message.
	@pyqtSlot()
	def on_registerButton_clicked(self):
		try:
			self.username=unicode(self.userLineEdit.text())
			self.passwd=unicode(self.passWordLineEdit.text())
			# Insert the new user to the sqlite
			self.conn.execute("insert into user (username,password)\
				values (?,?)",(self.username,self.passwd))
			QMessageBox.information(None,"User register","register new user successfully!")
			self.conn.commit()
		except Exception,e:
			QMessageBox.information(None,"User register","register new user failed! please check whether you has registered the user or forget the password!")

# close the login UI and open the chat room UI
def loginTo():
	a=client.clientv(form.username,form.passwd)
	form.close()
	a.show()
	a.exec_()

app = QApplication(sys.argv)
form = Login()
# When it get the signal, turn to the loginTo function
form.connect(form,SIGNAL("loginTo"),loginTo)
form.show()
app.exec_()
