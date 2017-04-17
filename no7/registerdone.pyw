from PyQt4.QtCore import *
from PyQt4.QtGui import *

class registerDone(QDialog):
	def __init__(self,parent=None):
		super(registerDone,self).__init__(parent)

		news=QLabel("register new user successfully!")
		okButton=QPushButton("&Ok")
		layout=QVBoxLayout()
		layout.addWidget(news)
		layout.addWidget(okButton)
		self.setLayout(layout)

		self.connect(okButton,SIGNAL("accepted()"),self,SLOT("accept()"))
		self.setWindowTitle("User register")
		print "in the register "

	def accept():
		return

if __name__ == '__main__':
	import sys
	app=QApplication(sys.argv)
	form=registerDone()
	form.show()
	app.exec_()


