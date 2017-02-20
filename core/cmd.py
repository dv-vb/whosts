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
            cmd = "del" + " " + str(path) + str(filename)
        elif self.platform_type == 'Linux':
            cmd = "rm" + " " + str(path) + str(filename)
        elif self.platform_type == 'MacOS':
            cmd = "rm" + " " + str(path) + str(filename)
        else:
            cmd = "rm" + str(filename)

        os.system(cmd)


    def cp_file_to_path(self, filename, dstpath):
        cmd = ""
        if self.platform_type == 'Windows':
            cmd = "copy" + " " + str(filename) + " " + str(dstpath)
        elif self.platform_type == 'Linux':
            cmd = "sudo cp" + " " + str(filename) + " " + str(dstpath)
        elif self.platform_type == 'MacOS':
            cmd = "sudo cp" + " " + str(filename) + " " + str(dstpath)
        else:
            cmd = "cp" + " " + str(filename) + " " + str(dstpath)

        os.system(cmd)

    def back_file_to_path(self, filename, backupfile):
        cmd = ""
        if self.platform_type == 'Windows':
            cmd = "copy" + " "  + str(filename) + " " + str(backupfile)
        elif self.platform_type == 'Linux':
            cmd = "sudo cp" +  " "  + str(filename) + " " + str(backupfile)
        elif self.platform_type == 'MacOS':
            cmd = "sudo cp" + " "  + str(filename) + " " + str(backupfile)
        else:
            cmd = "cp" + " " + str(filename) + " " + str(backupfile)

        os.system(cmd)
    
