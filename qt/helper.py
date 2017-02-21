# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt/helper.ui'
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

class Ui_helper(object):
    def __init__(self):
        super(Ui_helper, self).__init__()
    def setupUi(self, helper):
        helper.setObjectName(_fromUtf8("helper"))
        helper.resize(400, 230)
        self.textEdit = QtGui.QTextEdit(helper)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 360, 210))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(helper)
        QtCore.QMetaObject.connectSlotsByName(helper)

    def retranslateUi(self, helper):
        helper.setWindowTitle(_translate("helper", "Helper", None))
        self.textEdit.setHtml(_translate("helper", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'YaHei Consolas Hybrid\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Why change hosts file can visit the Google website?</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">When you in bus station and you want to go the XXX place,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">maybe you will ask somebody or find the station board to get the help.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The Great Firewall and DNS server is play a rote who is help you to get wrong answer.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Change the hosts file seem like you have a traffic map,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">you don\'t need to ask athers to get help.And you will need the real-time traffic map that will help you visit the right ip address website directly.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">dv-vb. email: hxyjxxx@gmail.com</p></body></html>", None))

