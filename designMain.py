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
        MainWindow.resize(914, 592)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color:#d7ecf4;\n"
"    border:none;outline: none;\n"
"}\n"
"QWidget::layout{\n"
"    margin:0px;    \n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(592, 540, 320, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.sendButton.setFont(font)
        self.sendButton.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    background-color:#5d9700;\n"
"    border:none;    \n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#436d00;    \n"
"}\n"
"QPushButton:focus{outline: none;}")
        self.sendButton.setAutoDefault(False)
        self.sendButton.setObjectName("sendButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(2, 390, 588, 200))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("QTextEdit{\n"
"    border:none;\n"
"    background-color:white;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(2, 40, 454, 348))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("QListWidget::item { margin: 0.2em;}\n"
"QListWidget{\n"
"    border:none;\n"
"    background-color:white;\n"
"}\n"
"QListWidget{\n"
"    border:none;\n"
"    background-color:white;\n"
"}\n"
"QScrollBar:vertical {border: none;\n"
"background-color: white;}\n"
"QScrollBar::handle:vertical {\n"
"border:none;background-color:#acd8e8;}\n"
"QScrollBar:horizontal {border: none;\n"
"background-color: white;}\n"
"QScrollBar::handle:horizontall {\n"
"border:none;background-color:#acd8e8;}")
        self.listWidget.setAutoScroll(True)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listWidget.setIconSize(QtCore.QSize(0, 0))
        self.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.listWidget.setBatchSize(100)
        self.listWidget.setObjectName("listWidget")
        self.sendListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.sendListWidget.setGeometry(QtCore.QRect(458, 40, 454, 348))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.sendListWidget.setFont(font)
        self.sendListWidget.setStyleSheet("QListWidget::item { margin: 0.2em;}\n"
"QListWidget{\n"
"    border:none;\n"
"    background-color:white;\n"
"}\n"
"QListWidget{\n"
"    border:none;\n"
"    background-color:white;\n"
"}\n"
"QScrollBar:vertical {border: none;\n"
"background-color: white;}\n"
"QScrollBar::handle:vertical {\n"
"border:none;background-color:#acd8e8;}\n"
"QScrollBar:horizontal {border: none;\n"
"background-color: white;}")
        self.sendListWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.sendListWidget.setObjectName("sendListWidget")
        self.findButton = QtWidgets.QPushButton(self.centralwidget)
        self.findButton.setGeometry(QtCore.QRect(592, 490, 320, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.findButton.setFont(font)
        self.findButton.setStyleSheet("QPushButton{\n"
"    background-color:white;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#f2f6fc;\n"
"}")
        self.findButton.setObjectName("findButton")
        self.selectAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectAllButton.setGeometry(QtCore.QRect(592, 440, 320, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.selectAllButton.setFont(font)
        self.selectAllButton.setStyleSheet("QPushButton{\n"
"    background-color:white;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#f2f6fc;\n"
"}")
        self.selectAllButton.setObjectName("selectAllButton")
        self.addListButton = QtWidgets.QPushButton(self.centralwidget)
        self.addListButton.setGeometry(QtCore.QRect(872, 348, 40, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addListButton.sizePolicy().hasHeightForWidth())
        self.addListButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.addListButton.setFont(font)
        self.addListButton.setStyleSheet("QPushButton{\n"
"    background-color:white;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#f2f6fc;\n"
"}")
        self.addListButton.setObjectName("addListButton")
        self.loadListsButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadListsButton.setGeometry(QtCore.QRect(592, 390, 320, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.loadListsButton.setFont(font)
        self.loadListsButton.setStyleSheet("QPushButton{\n"
"    background-color:white;\n"
"border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#f2f6fc;\n"
"}")
        self.loadListsButton.setObjectName("loadListsButton")
        self.rollButton = QtWidgets.QPushButton(self.centralwidget)
        self.rollButton.setGeometry(QtCore.QRect(832, 0, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.rollButton.setFont(font)
        self.rollButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rollButton.setAutoFillBackground(False)
        self.rollButton.setStyleSheet("QPushButton {    \n"
"padding-bottom: 0.4em;\n"
"background-color:#d7ecf4;\n"
"border:none;    \n"
"}\n"
"QPushButton:hover {\n"
"padding-bottom: 0.4em;\n"
"background-color:#b7e3f4;\n"
"}\n"
"QPushButton:focus {\n"
"outline:none;\n"
"}")
        self.rollButton.setAutoDefault(False)
        self.rollButton.setDefault(False)
        self.rollButton.setObjectName("rollButton")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(872, 0, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.closeButton.setFont(font)
        self.closeButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.closeButton.setAutoFillBackground(False)
        self.closeButton.setStyleSheet("QPushButton {    \n"
"padding-bottom: 0.4em;\n"
"background-color:#d7ecf4;\n"
"border:none;    \n"
"}\n"
"QPushButton:hover {\n"
"padding-bottom: 0.4em;\n"
"background-color:#d2374a;\n"
"color:white;\n"
"}\n"
"QPushButton:focus {\n"
"outline:none;\n"
"}")
        self.closeButton.setAutoDefault(False)
        self.closeButton.setDefault(False)
        self.closeButton.setObjectName("closeButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Message sender"))
        self.sendButton.setText(_translate("MainWindow", "Рассылка"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Введите текст сообщения"))
        self.findButton.setText(_translate("MainWindow", "Поиск"))
        self.selectAllButton.setText(_translate("MainWindow", "Выбрать всё"))
        self.addListButton.setToolTip(_translate("MainWindow", "Сохранить список"))
        self.addListButton.setText(_translate("MainWindow", "+"))
        self.loadListsButton.setText(_translate("MainWindow", "Загрузить список"))
        self.rollButton.setText(_translate("MainWindow", "-"))
        self.closeButton.setText(_translate("MainWindow", "x"))

