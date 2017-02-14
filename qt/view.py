# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/view.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(578, 191)
        self.confirm_btn = QtGui.QPushButton(Dialog)
        self.confirm_btn.setGeometry(QtCore.QRect(100, 140, 86, 32))
        self.confirm_btn.setObjectName(_fromUtf8("confirm_btn"))
        self.filepath_edit = QtGui.QLineEdit(Dialog)
        self.filepath_edit.setGeometry(QtCore.QRect(190, 30, 320, 32))
        self.filepath_edit.setObjectName(_fromUtf8("filepath_edit"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QtCore.QRect(30, 110, 511, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.load_filepath = QtGui.QToolButton(Dialog)
        self.load_filepath.setGeometry(QtCore.QRect(510, 30, 50, 32))
        self.load_filepath.setObjectName(_fromUtf8("load_filepath"))
        self.filepath_lab = QtGui.QLabel(Dialog)
        self.filepath_lab.setGeometry(QtCore.QRect(10, 30, 170, 32))
        self.filepath_lab.setObjectName(_fromUtf8("filepath_lab"))
        self.url_lab = QtGui.QLabel(Dialog)
        self.url_lab.setGeometry(QtCore.QRect(10, 70, 170, 32))
        self.url_lab.setObjectName(_fromUtf8("url_lab"))
        self.url_edit = QtGui.QLineEdit(Dialog)
        self.url_edit.setGeometry(QtCore.QRect(190, 70, 370, 32))
        self.url_edit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.url_edit.setCursorPosition(0)
        self.url_edit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.url_edit.setDragEnabled(True)
        self.url_edit.setObjectName(_fromUtf8("url_edit"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "whosts", None))
        self.confirm_btn.setText(_translate("Dialog", "Confirm", None))
        self.filepath_edit.setText(_translate("Dialog", "%SystemRoot%\\System32\\drivers\\etc\\", None))
        self.load_filepath.setText(_translate("Dialog", "...", None))
        self.filepath_lab.setText(_translate("Dialog", "Backup hosts filepath", None))
        self.url_lab.setText(_translate("Dialog", "Update hosts url", None))
        self.url_edit.setText(_translate("Dialog", "https://raw.githubusercontent.com/racaljk/hosts/master/hosts", None))

