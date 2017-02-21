# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/main_view.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import time
from PyQt4 import QtCore, QtGui
import platform
import os
import sys
from qt.helper import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_whosts(object):
    def setupUi(self, whosts):
        whosts.setObjectName(_fromUtf8("whosts"))
        whosts.resize(600, 240)
        self.centralwidget = QtGui.QWidget(whosts)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QtCore.QRect(50, 110, 500, 25))
        self.progressBar.setProperty("value", 0)
        self.progressBar.hide()
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.filepath_lab = QtGui.QLabel(self.centralwidget)
        self.filepath_lab.setGeometry(QtCore.QRect(30, 10, 170, 32))
        self.filepath_lab.setObjectName(_fromUtf8("filepath_lab"))
        self.url_edit = QtGui.QLineEdit(self.centralwidget)
        self.url_edit.setGeometry(QtCore.QRect(190, 60, 370, 32))
        self.url_edit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.url_edit.setCursorPosition(0)
        self.url_edit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.url_edit.setDragEnabled(True)
        self.url_edit.setObjectName(_fromUtf8("url_edit"))
        self.filepath_edit = QtGui.QLineEdit(self.centralwidget)
        self.filepath_edit.setGeometry(QtCore.QRect(190, 10, 370, 32))
        self.filepath_edit.setObjectName(_fromUtf8("filepath_edit"))
        self.url_lab = QtGui.QLabel(self.centralwidget)
        self.url_lab.setGeometry(QtCore.QRect(30, 60, 170, 32))
        self.url_lab.setObjectName(_fromUtf8("url_lab"))
        self.confirm_btn = QtGui.QPushButton(self.centralwidget)
        self.confirm_btn.setGeometry(QtCore.QRect(220, 150, 160, 32))
        self.confirm_btn.setObjectName(_fromUtf8("confirm_btn"))
        whosts.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(whosts)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 598, 28))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuStart = QtGui.QMenu(self.menubar)
        self.menuStart.setObjectName(_fromUtf8("menuStart"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        whosts.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(whosts)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        whosts.setStatusBar(self.statusbar)
        self.actionSetting = QtGui.QAction(whosts)
        self.actionSetting.setObjectName(_fromUtf8("actionSetting"))
        self.actionSetting.setShortcut("Ctrl+S")
        self.actionExit = QtGui.QAction(whosts)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.setShortcut("Ctrl+Q")
        self.actionExit.triggered.connect(self.quit_app)
        self.menuStart.addAction(self.actionSetting)
        self.menuStart.addAction(self.actionExit)
        self.about_self = QtGui.QAction(whosts)
        self.about_self.setObjectName(_fromUtf8("actionAbout"))
        self.about_self.triggered.connect(self.helper_event)
        self.menuHelp.addAction(self.about_self)
        self.menubar.addAction(self.menuStart.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(whosts)
        #self.setEvent(whosts)

    def retranslateUi(self, whosts):
        self.platform_type = platform.system()
        whosts.setWindowTitle(_translate("whosts", "whosts", None))
        self.filepath_lab.setText(_translate("whosts", "Backup hosts filepath", None))
        self.url_edit.setText(_translate("whosts", "https://raw.githubusercontent.com/racaljk/hosts/master/hosts", None))
        self.url_lab.setText(_translate("whosts", "Update hosts url", None))
        self.confirm_btn.setText(_translate("whosts", "Confirm", None))
        self.menuStart.setTitle(_translate("whosts", "Start", None))
        self.menuHelp.setTitle(_translate("whosts", "Help", None))
        self.actionSetting.setText(_translate("whosts", "Setting", None))
        self.actionExit.setText(_translate("whosts", "Exit", None))
        self.about_self.setText(_translate("whosts", "About whosts", None))
        if self.platform_type == 'Windows':
            self.filepath_edit.setText(_translate("whosts", "%SystemRoot%\\System32\\drivers\\etc\\", None))
        if self.platform_type == 'Linux':
            self.filepath_edit.setText(_translate("whosts", "/etc/", None))
        if self.platform_type == 'MacOS':
            self.filepath_edit.setText(_translate("whosts", "/private/etc/", None))


    def quit_app(self):
        print("leave!bye-bye!")
        sys.exit()
    
    def helper_event(self):
        print("helper event.")
        self.helper = QtGui.QWidget()
        ui = Ui_helper()
        ui.setupUi(self.helper)
        self.helper.show()
    
    #def setEvent(self, whosts):
        #QtCore.QObject.connect(self.confirm_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.progressBar.reset)
        #QtCore.QMetaObject.connectSlotsByName(whosts)
        #self.confirm_btn.clicked.connect(self.confirm_clicked)







