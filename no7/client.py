#!#!/usr/bin/env python

''' This is the program for chat room UI, and receiving the data from the server(a tcp client proagram) in another thread. '''

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_chatroom
import sqlite3
import socket,select,threading,sys,re,time,os;

# the chat room UI class
class clientv(QDialog,ui_chatroom.Ui_chatRoom):
	def __init__(self,username,passwd,parent=None):
		super(clientv,self).__init__(parent)

		# Once you are the verified user you can enter the room
		self.username0=username
		self.data=None

		self.filename=None
		self.name=None

		# Start the thread for receiving the data, if received the signal(parameter) from it, enter the functions to update the UI.
		self.thread=receiveData(self.username0)
		self.thread.text.connect(self.updateText)
		self.thread.inoroutSig.connect(self.updateInorOut)
		self.thread.fileSig.connect(self.saveFile)
		self.thread.start()
		
		# Contect the singal and slot from the qt desinger
		self.setupUi(self)

		self.initUI()

		self.updateUi()

		self.emitButton.setFocusPolicy(Qt.NoFocus)
		self.closeButton.setFocusPolicy(Qt.NoFocus)

	def initUI(self):
		self.browser.setStyleSheet('background-color:lightgrey')
		self.browser1.setStyleSheet('background-color:lightgrey')
		self.browser2.setStyleSheet('background-color:lightgrey')

	# When edit line, update the UI
	@pyqtSlot(QString)
	def on_lineEdit_textEdited(self):
		self.updateUi()

	# Enable the emit button
	def updateUi(self):
		# self.browser.setStyleSheet('background-image: url(arch.png)')
		enable=not self.lineEdit.text().isEmpty()
		self.emitButton.setEnabled(enable)

	# When you click the emit button, show the message on the browser, and emit the message to the server
	@pyqtSlot()
	def on_emitButton_clicked(self):
		if not self.lineEdit.text().isEmpty():
			sendTo=unicode(self.lineEdit.text())
			self.browser.append("<font color=navy><b>"+sendTo+"</b></font>")
			self.thread.sendMes(sendTo)
			self.lineEdit.clear()

	@pyqtSlot()
	def on_picButton_clicked(self):
		dir = (os.path.dirname(self.filename)
				if self.filename is not None else ".")
		formats = (["*.{0}".format(unicode(format).lower())
				for format in QImageReader.supportedImageFormats()])
		fname = unicode(QFileDialog.getOpenFileName(self,
				"Image Changer - Choose to be background image", dir,
				"Image files ({0})".format(" ".join(formats))))
		if fname:
			self.loadFile(fname)

	def loadFile(self,fname=None):
		if fname is None:
			return
		if fname:
			self.filename=None
			image=QImage(fname)
			if image.isNull():
				message="Failed to read %s"%fname
			else:
				self.image=QImage()
				self.image=image
				self.filename=fname
				self.showImage()
				# print self.filename

	def showImage(self):
		if self.image.isNull():
			return
		
		image=self.filename.rsplit('/')[-1]
		# self.browser.setStyleSheet('background-image: url(self.filename)')
		if image=='blue.jpg':
			self.browser.setStyleSheet('border-image: url(blue.jpg);border-style:solid')
		if image=='arch.png':
			self.browser.setStyleSheet('border-image: url(arch.png);border-style:solid')
		if image=='arch1.png':
			self.browser.setStyleSheet('border-image: url(arch1.png);border-style:solid')
		if image=='arch2.png':
			self.browser.setStyleSheet('border-image: url(arch2.png);border-style:solid')
		if image=='s.png':
			self.browser.setStyleSheet('border-image: url(s.png);border-style:solid')	
		if image=='s1.png':
			self.browser.setStyleSheet('border-image: url(s1.png);border-style:solid')
		if image=='s2.png':
			self.browser.setStyleSheet('border-image: url(s1.png);border-style:solid')
		if image=='s3.png':
			self.browser.setStyleSheet('border-image: url(s3.png);border-style:solid')
		if image=='s4.png':
			self.browser.setStyleSheet('border-image: url(s4.png);border-style:solid')
		if image=='s5.png':
			self.browser.setStyleSheet('border-image: url(s5.png);border-style:solid')
			

	@pyqtSlot()
	def on_fiButton_clicked(self):
		# Open the file UI
		dir = (os.path.dirname(self.filename)
				if self.filename is not None else ".")
		file_name = QFileDialog.getOpenFileName(self,"open file dialog (choose the file to sent)",dir,"Txt files(*.txt)")
		if not file_name.isEmpty():
			self.fileData(file_name)

	def fileData(self,filename=None):
		if filename is None:
			return
		if filename:
			fs=open(filename,"r+")
			na=filename.split('/')[-1]	# get the filename
			data=fs.read()
			na=unicode(na)
			data=unicode(data)
			# print data
			# Note the format of the data sent, it is very import when the client receive to resolve
			data=self.thread.fisk+' '+na+' '+data+' '+self.thread.fiek	# All datas are the str type so that the socket could send and receive successfully
			self.thread.sendMes(data)

	# Close the room UI
	@pyqtSlot()
	def on_closeButton_clicked(self):
		self.close()

	# Update the chat message
	def updateText(self,text):
		# print "i am in updateText"
		text=unicode(text)	
		name=text.split(':')[0]
		data=text.split(':')[1].rsplit(None,2)[0]
		ti=text.rsplit(None,1)[1]
		self.browser.append("<font color=red><b>"+name+"</font>"+':'+"<font color=purple><b>"+data+"</b></font>"+'   '+"<font size=1>"+ti+"</font>")

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
				self.browser2.append("<font color=blue><b>"+u+"</b></font>")

	def saveFile(self,text):
		# Important to init the var text
		text=unicode(text)
		# Check if it is the start of the file
		if text.startswith(self.thread.fisk):
			# Refer to the format of the data sent
			self.name=text.split(None,2)[1]
			data=text.split(None,2)[2]
			# The small file
			if text.endswith(self.thread.fiek):
				data=data.rsplit(None,1)[0]
				me=' you get a txt file on the local directory'	# Message to take a tip
				self.browser.append("<font color=blue><b>"+me+"</b></font>")
			with open(self.name,'w+') as f:
				f.write(data)
		# Check if it is the last of the file
		elif text.endswith(self.thread.fiek):
			data=text.rsplit(None,1)[0]
			with open(self.name,'a+') as f:
				f.write(data)
			me=' you get a txt file on the local directory'	# Message to take a tip
			self.browser.append("<font color=blue><b>"+me+"</b></font>")
		else:
			# the center of the file
			with open(self.name,'a+') as f:
					f.write(text)

		# print data

		

# the main client program(thread) to receive and send messages
class receiveData(QThread):

	# Signal (parameter to the main thread) to be emited to tell the main thread functions
	text=pyqtSignal(str)
	inoroutSig=pyqtSignal(str)
	fileSig=pyqtSignal(str)

	def __init__(self,usrname,parent=None):
		super(receiveData,self).__init__(parent)

		# Define the var
		self.host='localhost'
		self.addr=(self.host,12321)

		self.clientsock=socket.socket()
		self.clientsock.connect(self.addr)

		self.username=usrname
		self.clientsock.send(self.username)

		self.co=None
		self.onk=None
		self.outk=None
		self.fik=None

	# Send messages to the server, this function can be called by main thread 
	def sendMes(self,text):
		self.clientsock.send(text)

	# This thread runs when started
	def run(self):
		# Connect to the sqlite table key to verify the keyword, find out if users are in or out or do nothig(just chat).
		self.co=sqlite3.connect('/root/test.db')
		cursor=self.co.execute("select * from key")
		for key in cursor:
			self.onk=key[0] #into the room
			self.outk=key[1] #left the room
			self.fisk=key[2]	#file start key
			self.fiek=key[3]	#file end key
		while True:
			self.mes=self.clientsock.recv(10000)
			if self.mes:
				ks=self.mes.split(None,1)[0]
				ke=self.mes.rsplit(None,1)[1]
				# print self.mes # Very important flag
				if ke==self.onk or ke==self.outk:
					self.inoroutSig.emit(self.mes)
				# If you get a file
				elif ks==self.fisk:
					# If you get a small file
					if ke==self.fiek:
						self.fileSig.emit(self.mes)
					else:
						self.fileSig.emit(self.mes)
						while 1:
							self.mes=self.clientsock.recv(10000)
							if self.mes:
								self.fileSig.emit(self.mes)
								ke=self.mes.rsplit(None,1)[1]
								# Check if it is the last of the file
								if ke==self.fiek:
									break
						
				else:
					# The chat message
					self.text.emit(self.mes)

