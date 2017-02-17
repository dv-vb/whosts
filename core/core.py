# core.py create by dv-vb.
# support email: hxyjxxx@gmail.com
# Download the host file, and replace the local host file.
# Want to support all platform. MacOS, Linux, Window.
import urllib
import requests
from qt import *
import sys
import sip
from PyQt4.Qt import *
from PyQt4.uic import *

class Download(QObject):
    finishd = pyqtSignal()
    dataReady = pyqtSignal(int)
    def __init__(self, url):
        super(Download, self).__init__() 
        print(url)
        self.url = url
    @pyqtSlot()
    def start_download(self):
        self.filename = "./hosts.txt"
        urllib.request.urlretrieve(self.url, self.filename, self.report)
        self.finishd.emit()
    #blocknum, blocksize, totalsize
    @pyqtSlot(int)
    def report(self, blocknum, bs, tsize):
        percent = blocknum * bs * 1e2 / tsize
        print("Block number: ", blocknum," Block size: ", bs, "Total size:", tsize)
        self.dataReady.emit(percent)
        
    def reporthook(blocknum, blocksize, totalsize):
        # Report during remote transfers
        print("Block number: %d, Block size: %d, Total size: %d" %blocknum, blocksize, totalsize)

