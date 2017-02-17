# cmd.py create by dv-vb.
# support email: hxyjxxx@gmail.com
# copy file, delete file, backup file cmd
# Want to support all platform. MacOS, Linux, Window.


from qt import *
from PyQt4.Qt import *
from PyQt4.uic import *
import platform
import os
import sys

class Cmd(QObject):
    def __init__(self):
        super(Cmd, self).__init__() 
        self.platform_type = platform.system()
        
    def del_file(self, filename, path=None):
        cmd = ""
        if self.platform_type == 'Windows':
            cmd = "del" + " " + path + filename
        elif self.platform_type == 'Linux':
            cmd = "rm" + " " + path + filename
        elif self.platform_type == 'MacOS':
            cmd = "rm" + " " + path + filename
        else:
            cmd = "rm" + filename

        os.system(cmd)


    def cp_file_to_path(self, filename, dstpath):
        cmd = ""
        if self.platform_type == 'Windows':
            cmd = "copy" + " " + filename + " " + dstpath
        elif self.platform_type == 'Linux':
            cmd = "cp" + " " + filename + " " + dstpath
        elif self.platform_type == 'MacOS':
            cmd = "cp" + " " + filename + " " + dstpath
        else:
            cmd = "cp" + " " + filename + " " + dstpath

        os.system(cmd)

    def back_file_to_path(self, filename, backupfile, path=None, backuppath=None):
        cmd = ""
        if self.platform_type == 'Windows':
            cmd = "copy" + " " + path + filename + " " + backuppath + backupfile
        elif self.platform_type == 'Linux':
            cmd = "cp" + " " + path + filename + " " + backuppath + backupfile
        elif self.platform_type == 'MacOS':
            cmd = "cp" + " " + path + filename + " " + backuppath + backupfile
        else:
            cmd = "cp" + " " + path + filename + " " + backuppath + backupfile

        os.system(cmd)
    
