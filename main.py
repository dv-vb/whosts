# main.py create by dv-vb.
# support email: hxyjxxx@gmail.com
from qt import *
from qt.view import * 
from qt.main_view import *
import sys
import sip
import qt.main_view
from core.core import *
from core.cmd import *
import time
from PyQt4.Qt import *
from PyQt4.uic import *


class Uploader(QThread): 
    def __init__(self,parent=None): 
        super(Uploader, self).__init__(parent) 
        self.working = True
        self.tmpfile = "./hosts"
        self.num=0 
    def __del__(self): 
        self.working = False 
        self.wait()
    def seturl_and_path(self, url, path):
        self.url = url
        self.path = path
    def run(self): 
        # will download the file, update the local file.
        self.download = Download(self.url, self.tmpfile)
        self.download.finishd.connect(self.update_host)
        self.download.dataReady.connect(self.output_result)
        self.num = 0
        self.download.start_download()
        if self.working==True: 
            for delay in range(1, 101):
                #self.emit(SIGNAL('output(int)'), self.num) 
                self.msleep(50)
    def backup_host(self):
        cmd = Cmd()
        host_file = self.path + "hosts"
        backup_file = self.path + "hosts.bak"
        cmd.back_file_to_path(host_file, backup_file)
    
    def update_host(self):
        self.backup_host()
        self.num = 75
        self.emit(SIGNAL('output(int)'), self.num)  
        cmd = Cmd()
        cmd.cp_file_to_path(self.tmpfile, self.path)
        self.num = 100
        self.emit(SIGNAL('output(int)'), self.num)  
        
    def output_result(self, value):
        self.num = value/2
        self.emit(SIGNAL('output(int)'), self.num) 

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
        self.thread.seturl_and_path(self.url_edit.text(), self.filepath_edit.text())
        self.thread.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = mainapp()
    view.show()
    app.exec_()
