from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_chatroom
# import clientcom
import socket,select,threading,sys;

# from time import time
# import socket,select,threading,sys;

# host=socket.gethostname()
# addr=(host,12323)

class clientv(QDialog,ui_chatroom.Ui_chatRoom):
	def __init__(self,username,passwd,parent=None):
		super(clientv,self).__init__(parent)

		self.host='localhost'
		self.addr=(self.host,12321)
		self.MAX=2048

		self.clientsock=socket.socket()
		self.clientsock.connect(self.addr)

		self.username=username
		self.clientsock.send(self.username)
		self.passwd=passwd
		# con(self.username)
		self.setupUi(self)
		self.updateUi()
		self.emitButton.setFocusPolicy(Qt.NoFocus)
		self.closeButton.setFocusPolicy(Qt.NoFocus)

		# self.s=socket.socket()
		# self.s.connect(addr)
		# self.s.send(self.username)

	@pyqtSlot(QString)
	def on_lineEdit_textEdited(self):
		self.updateUi()

	def updateUi(self):
		enable=not self.lineEdit.text().isEmpty()
		self.emitButton.setEnabled(enable)
		try:
			message=self.clientsock.recv(self.MAX)
			self.browser.append(message)
		except Exception:
			pass

	@pyqtSlot()
	def on_emitButton_clicked(self):
		sendTo=unicode(self.lineEdit.text())
		self.clientsock.send(sendTo)

	# def list(self):
	# 	me=[self.s]
	# 	while True:
	# 		r,w,e=select.select(me,[],[])
	# 		if self.s in r:
	# 			try:
	# 				print "me"
	# 			except socket.error:
	# 				print "socket is error"
	# 				exit()

	# def receivedata(self):
	# 	while True:
	# 		data,addr=self.s.recvfrom(1024)
	# 		print data
	# 	self.s.close()

	# def run(self):
	# 	t0=threading.Thread(target=self.receivedata,args=())
	# 	t0=start()
	# 	t1=threading.Thread(target=self.list,args=())
	# 	t1.start()



		


