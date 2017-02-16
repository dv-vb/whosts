from qt import *
from qt.view import * 
from qt.main_view import *
import sys
import sip
import qt.main_view
import time
from PyQt4.Qt import *
from PyQt4.uic import *

class Uploader(QThread): 
    def __init__(self,parent=None): 
        super(Uploader, self).__init__(parent) 
        self.working = True 
        self.num=0 
    def __del__(self): 
        self.working = False 
        self.wait()
    def run(self): 
        # will download the file, update the local file.
        if self.working==True: 
            for self.num in range(1, 101):
                self.emit(SIGNAL('output(int)'), self.num) 
                self.msleep(50)

class mainapp(QtGui.QMainWindow, Ui_whosts):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.thread = Uploader()
        self.setupUi(self)
        self.set_events(self)

    def clear_pro_bar(self, status):
        if status == True:
            self.confirm_btn.setEnabled(True)
            self.progressBar.reset()
            self.progressBar.hide()

    def set_pro_bar(self, value):
        self.progressBar.setValue(value)
        if value == 100:
            d = QMessageBox()
            d.setWindowTitle('Result')
            d.setText("update host file successd.")
            d.exec_()
            print("Finish.")
            self.confirm_btn.setEnabled(True)
            self.progressBar.reset()
            self.progressBar.hide()

    def set_events(self, Ui_whosts):
        self.connect(self.confirm_btn,SIGNAL('clicked()'), self.confirm_clicked) 
        self.connect(self.thread, SIGNAL('output(int)'), self.set_pro_bar)

    def confirm_clicked(self):
        self.confirm_btn.setEnabled(False) 
        self.progressBar.show()
        self.thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = mainapp()
    view.show()
    app.exec_()
