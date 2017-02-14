from qt import *
from qt.view import * 
from qt.main_view import *
import sys
import sip
import qt.main_view
from PyQt4.Qt import *
from PyQt4.uic import *

class mainapp(QtGui.QMainWindow, Ui_whosts):
	def __init__(self):
	    super(self.__class__, self).__init__()
	    self.setupUi(self)
		

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = mainapp()
    view.show()
    app.exec_()
    #sys.exit(app.exec_())
    #f.setupUi()
    #app.setMainWidget(f)
    #app.exec_loop()
