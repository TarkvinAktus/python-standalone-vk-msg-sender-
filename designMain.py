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
        MainWindow.resize(1080, 610)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(1500, 1000))
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color:#ebeef5;\n"
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
        self.sendButton.setGeometry(QtCore.QRect(0, 300, 320, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.sendButton.setFont(font)
        self.sendButton.setStyleSheet("QPushButton{\n"
"    background-color: #354052;\n"
"    color:white;\n"
"    border:none;\n"
"    border-left: 10px solid #354052\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#3f4d63;\n"
"    border-left: 10px solid #1dba9b\n"
"}")
        self.sendButton.setAutoDefault(False)
        self.sendButton.setObjectName("sendButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(340, 440, 720, 150))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("QTextEdit{\n"
"    border:none;\n"
"    background-color:white;\n"
"    padding: 0.5em;\n"
"}")
        self.textEdit.setObjectName("textEdit")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(340, 60, 350, 360))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("QListWidget::item { margin: 0.2em;}\n"
"QListWidget{\n"
"    border:none;\n"
"    background-color:white;\n"
"    padding: 0.5em;\n"
"}\n"
"QListWidget{\n"
"    border:none;\n"
"    background-color:white;\n"
"}\n"
"QScrollBar:vertical {border: none;\n"
"background-color: white;}\n"
"QScrollBar::handle:vertical {\n"
"border:none;background-color:#d1d2d7;}\n"
"QScrollBar:horizontal {border: none;\n"
"background-color: white;}\n"
"QScrollBar::handle:horizontall {\n"
"border:none;background-color:#d1d2d7;}")
        self.listWidget.setAutoScroll(True)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.listWidget.setIconSize(QtCore.QSize(0, 0))
        self.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.listWidget.setBatchSize(100)
        self.listWidget.setObjectName("listWidget")
        self.sendListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.sendListWidget.setGeometry(QtCore.QRect(710, 60, 350, 360))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.sendListWidget.setFont(font)
        self.sendListWidget.setStyleSheet("QListWidget::item { margin: 0.2em;}\n"
"QListWidget{\n"
"    border:none;\n"
"    background-color:white;\n"
"padding: 0.5em;\n"
"}\n"
"QListWidget{\n"
"    border:none;\n"
"    background-color:white;\n"
"}\n"
"QScrollBar:vertical {border: none;\n"
"background-color: white;}\n"
"QScrollBar::handle:vertical {\n"
"border:none;background-color:#d1d2d7;}\n"
"QScrollBar:horizontal {border: none;\n"
"background-color: white;}\n"
"QScrollBar::handle:horizontall {\n"
"border:none;background-color:#d1d2d7;}")
        self.sendListWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.sendListWidget.setObjectName("sendListWidget")
        self.findButton = QtWidgets.QPushButton(self.centralwidget)
        self.findButton.setGeometry(QtCore.QRect(0, 200, 320, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.findButton.setFont(font)
        self.findButton.setStyleSheet("QPushButton{\n"
"    background-color: #354052;\n"
"    color:white;\n"
"    border:none;\n"
"    border-left: 10px solid #354052\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#3f4d63;\n"
"    border-left: 10px solid #1dba9b\n"
"}")
        self.findButton.setObjectName("findButton")
        self.selectAllButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectAllButton.setGeometry(QtCore.QRect(0, 150, 320, 50))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.selectAllButton.setFont(font)
        self.selectAllButton.setStyleSheet("QPushButton{\n"
"    background-color: #354052;\n"
"    color:white;\n"
"    border:none;\n"
"    border-left: 10px solid #354052\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#3f4d63;\n"
"    border-left: 10px solid #1dba9b\n"
"}")
        self.selectAllButton.setObjectName("selectAllButton")
        self.addListButton = QtWidgets.QPushButton(self.centralwidget)
        self.addListButton.setGeometry(QtCore.QRect(0, 250, 320, 50))
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
"    background-color: #354052;\n"
"    color:white;\n"
"    border:none;\n"
"    border-left: 10px solid #354052\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#3f4d63;\n"
"    border-left: 10px solid #1dba9b\n"
"}")
        self.addListButton.setObjectName("addListButton")
        self.loadListsButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadListsButton.setGeometry(QtCore.QRect(0, 100, 320, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        self.loadListsButton.setFont(font)
        self.loadListsButton.setStyleSheet("QPushButton{\n"
"    background-color: #354052;\n"
"    color:white;\n"
"    border:none;\n"
"    border-left: 10px solid #354052\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#3f4d63;\n"
"    border-left: 10px solid #1dba9b\n"
"}")
        self.loadListsButton.setObjectName("loadListsButton")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(1040, 0, 40, 40))
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
"background-color: #1dba9b;\n"
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
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 320, 610))
        self.frame.setStyleSheet("QWidget{\n"
"    background-color: #354052;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(139, 20, 47, 70))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/70px.png"))
        self.label.setObjectName("label")
        self.sendButton.raise_()
        self.label.raise_()
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(320, 0, 760, 40))
        self.frame_2.setStyleSheet("QWidget{\n"
"    background-color: #1dba9b;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.rollButton = QtWidgets.QPushButton(self.frame_2)
        self.rollButton.setGeometry(QtCore.QRect(680, 0, 40, 40))
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
"background-color: #1dba9b;\n"
"border:none;    \n"
"}\n"
"QPushButton:hover {\n"
"padding-bottom: 0.4em;\n"
"background-color:#16967d;\n"
"}\n"
"QPushButton:focus {\n"
"outline:none;\n"
"}")
        self.rollButton.setAutoDefault(False)
        self.rollButton.setDefault(False)
        self.rollButton.setObjectName("rollButton")
        self.frame_2.raise_()
        self.frame.raise_()
        self.sendButton.raise_()
        self.textEdit.raise_()
        self.listWidget.raise_()
        self.sendListWidget.raise_()
        self.findButton.raise_()
        self.selectAllButton.raise_()
        self.addListButton.raise_()
        self.loadListsButton.raise_()
        self.closeButton.raise_()
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
        self.addListButton.setText(_translate("MainWindow", "Сохранить список"))
        self.loadListsButton.setText(_translate("MainWindow", "Загрузить список"))
        self.closeButton.setText(_translate("MainWindow", "x"))
        self.rollButton.setText(_translate("MainWindow", "-"))

import rs_rc
