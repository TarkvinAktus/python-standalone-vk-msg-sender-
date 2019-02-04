# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Error(object):
    def setupUi(self, Error):
        Error.setObjectName("Error")
        Error.resize(200, 120)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Error.sizePolicy().hasHeightForWidth())
        Error.setSizePolicy(sizePolicy)
        Error.setMinimumSize(QtCore.QSize(200, 120))
        Error.setMaximumSize(QtCore.QSize(300, 120))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        Error.setFont(font)
        Error.setWindowTitle("")
        Error.setWhatsThis("")
        Error.setAutoFillBackground(False)
        Error.setStyleSheet("QWidget{\n"
"    background-color:#354052;\n"
"border:none;\n"
"}")
        #Error.setSizeGripEnabled(False)
        #Error.setModal(False)
        self.closeButton = QtWidgets.QPushButton(Error)
        self.closeButton.setGeometry(QtCore.QRect(0, 70, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.closeButton.setFont(font)
        self.closeButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.closeButton.setAutoFillBackground(False)
        self.closeButton.setStyleSheet("QPushButton {    \n"
"padding-bottom: 0.3em;\n"
"background-color:#3f4d63;\n"
"color:white;\n"
"border:none;    \n"
"}\n"
"QPushButton:hover {\n"
"padding-bottom: 0.3em;\n"
"background-color:#d2374a;\n"
"}\n"
"QPushButton:focus {\n"
"outline:none;\n"
"}")
        self.closeButton.setAutoDefault(False)
        self.closeButton.setDefault(False)
        self.closeButton.setObjectName("closeButton")
        self.label = QtWidgets.QLabel(Error)
        self.label.setGeometry(QtCore.QRect(0, 20, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"color:white;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Error)
        QtCore.QMetaObject.connectSlotsByName(Error)

    def retranslateUi(self, Error):
        _translate = QtCore.QCoreApplication.translate
        self.closeButton.setText(_translate("Error", "OK"))
        self.label.setText(_translate("Error", "Ошибка ввода"))

