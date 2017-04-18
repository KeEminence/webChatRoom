import re
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_findandreplacedlg

MAC="qt_mac_set_native_menubar" in dir()

class FindAndReplaceDlg(QDialog,ui_findandreplacedlg.Ui_FindAndReplaceDlg):
	def __init__(self,text,parent=None):
		super(FindAndReplaceDlg,self),__init__(parent)
		self.__text=unicode(text)
		self.__index=0
		self.setupUi(self)
		if not MAC:
			self.findButton.setFocusPolicy(Qt.NoFoucs)
			self.replaceButton.setFocusPolicy(Qt.NoFoucs)
			self.closeButton.setFocusPolicy(Qt.NoFoucs)
		self.updateUi()
