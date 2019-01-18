# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtdesigner.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(930, 441)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color:#d7ecf4\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(600, 160, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.sendButton.setFont(font)
        self.sendButton.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    background-color:#5d9700;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#436d00;    \n"
"}\n"
"QPushButton:focus{outline: none;}")
        self.sendButton.setAutoDefault(False)
        self.sendButton.setObjectName("sendButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 580, 190))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("QTextEdit{\n"
"    border:none;\n"
"    background-color:white;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 210, 450, 190))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("QListWidget{\n"
"    border:none;\n"
"    background-color:white;\n"
"}")
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(470, 210, 450, 190))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet("QListWidget{\n"
"    border:none;\n"
"    background-color:white;\n"
"}")
        self.listWidget_2.setObjectName("listWidget_2")
        self.findButton = QtWidgets.QPushButton(self.centralwidget)
        self.findButton.setGeometry(QtCore.QRect(600, 110, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.findButton.setFont(font)
        self.findButton.setStyleSheet("QPushButton{\n"
"    background-color:#cbd5d8;\n"
"}")
        self.findButton.setObjectName("findButton")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(600, 60, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.cancelButton.setFont(font)
        self.cancelButton.setStyleSheet("QPushButton{\n"
"    background-color:#cbd5d8;\n"
"}")
        self.cancelButton.setObjectName("cancelButton")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(600, 10, 320, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.closeButton.setFont(font)
        self.closeButton.setStyleSheet("QPushButton {    \n"
"background-color:#d2374a;\n"
"color:white\n"
"}\n"
"QPushButton:hover {\n"
"background-color:#b22e3e;\n"
"}")
        self.closeButton.setObjectName("closeButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 930, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Message sender"))
        self.sendButton.setText(_translate("MainWindow", "Рассылка"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Введите текст сообщения"))
        self.findButton.setText(_translate("MainWindow", "Поиск"))
        self.cancelButton.setText(_translate("MainWindow", "Отмена рассылки"))
        self.closeButton.setText(_translate("MainWindow", "Закрыть"))
