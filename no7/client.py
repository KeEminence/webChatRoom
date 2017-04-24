#!/usr/bin/env python

''' This is the program for chat room UI, and receiving the data from the server(a tcp client proagram) in another thread. '''

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_chatroom
import sqlite3
import socket,select,threading,sys,re,time;

# the chat room UI class
class clientv(QDialog,ui_chatroom.Ui_chatRoom):
	def __init__(self,username,passwd,parent=None):
		super(clientv,self).__init__(parent)

		# Once you are the verified user you can enter the room
		self.username0=username
		self.data=None

		# Start the thread for receiving the data, if received the signal(parameter) from it, enter the functions to update the UI.
		self.thread=receiveData(self.username0)
		self.thread.text.connect(self.updateText)
		self.thread.inoroutSig.connect(self.updateInorOut)
		self.thread.start()
		
		# Contect the singal and slot from the qt desinger
		self.setupUi(self)

		self.updateUi()

		self.emitButton.setFocusPolicy(Qt.NoFocus)
		self.closeButton.setFocusPolicy(Qt.NoFocus)

	# When edit line, update the UI
	@pyqtSlot(QString)
	def on_lineEdit_textEdited(self):
		self.updateUi()

	# Enable the emit button
	def updateUi(self):
		enable=not self.lineEdit.text().isEmpty()
		self.emitButton.setEnabled(enable)

	# When you click the emit button, show the message on the browser, and emit the message to the server
	@pyqtSlot()
	def on_emitButton_clicked(self):
		sendTo=unicode(self.lineEdit.text())
		self.browser.append("<font color=red><b>"+sendTo+"</b></font>")
		self.thread.sendMes(sendTo)

	# Close the room UI
	@pyqtSlot()
	def on_closeButton_clicked(self):
		self.close()

	# Update the chat message
	def updateText(self,text):
		self.browser.append("<font color=blue><b>"+text+"</font>")

	# Update the news and online members UI(the in or out message), receive strings and show it or turn into list to get the user list
	def updateInorOut(self,text):
		me=text.split(";",3)[0]	#message
		ti=text.split(";",3)[2]# time
		self.browser1.append("<font color=blue><center>"+me+"</center></font>"+" "+"<font size=1><center>"+ti+"</center></font>")
		ul=text.split(";",3)[1]
		n=ul.split("'") #user list
		self.browser2.clear()
		self.browser2.append("<font size=3><b><i><center>"+'Online Members'+"</center></i></b></font>")
		# the user list like ['a','b','c']
		for i in range(len(n)):
			if i%2!=0:
				u=unicode(n[i])
				self.browser2.append("<font color=blue><b>"+u+"</font>")

# the main client program(thread) to receive and send messages
class receiveData(QThread):

	# Signal (parameter to the main thread) to be emited to tell the main thread functions
	text=pyqtSignal(str)
	inoroutSig=pyqtSignal(str)

	def __init__(self,usrname,parent=None):
		super(receiveData,self).__init__(parent)

		self.host='localhost'
		self.addr=(self.host,12321)

		self.clientsock=socket.socket()
		self.clientsock.connect(self.addr)

		self.username=usrname
		self.clientsock.send(self.username)

	# Send messages to the server, this function can be called by main thread 
	def sendMes(self,text):
		self.clientsock.send(text)

	# This thread runs when started
	def run(self):
		# Connect to the sqlite table key to verify the keyword, find out if users are in or out or do nothig(just chat).
		co=sqlite3.connect('/root/test.db')
		cursor=co.execute("select * from key")
		for key in cursor:
			onk=key[0] #into the room
			outk=key[1] #left the room
		while True:
			self.mes=self.clientsock.recv(1024)
			if self.mes:
				k=self.mes.rsplit(None,1)[1]
				if k==onk or k==outk:
					self.inoroutSig.emit(self.mes)
				else:
					self.text.emit(self.mes)

