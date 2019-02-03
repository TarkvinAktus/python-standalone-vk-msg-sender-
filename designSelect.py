# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectLists.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ListsSelect(object):
    def setupUi(self, ListsSelect):
        ListsSelect.setObjectName("ListsSelect")
        ListsSelect.resize(300, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ListsSelect.sizePolicy().hasHeightForWidth())
        ListsSelect.setSizePolicy(sizePolicy)
        ListsSelect.setMinimumSize(QtCore.QSize(300, 400))
        ListsSelect.setMaximumSize(QtCore.QSize(300, 400))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        ListsSelect.setFont(font)
        ListsSelect.setWindowTitle("")
        ListsSelect.setWhatsThis("")
        ListsSelect.setAutoFillBackground(False)
        ListsSelect.setStyleSheet("QWidget\n"
"{\n"
"    background-color:white;\n"
"    border: 1px solid #d7ecf4;\n"
"}")
        #ListsSelect.setSizeGripEnabled(False)
        #ListsSelect.setModal(False)
        self.pushButton = QtWidgets.QPushButton(ListsSelect)
        self.pushButton.setGeometry(QtCore.QRect(0, 345, 300, 55))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 151, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 151, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 151, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 151, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 151, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 151, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 151, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(208, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 151, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(93, 151, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color:white;\n"
"    background-color:#5d9700;\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:#436d00;    \n"
"}\n"
"QPushButton:focus{outline: none;}")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(ListsSelect)
        self.listWidget.setGeometry(QtCore.QRect(39, 1, 221, 344))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("QListWidget::item { margin: 0.2em;}\n"
"QListWidget{\n"
"    background-color:white;\n"
"border:none;\n"
"}\n"
"QScrollBar:vertical {border: none;\n"
"background-color: white;}\n"
"QScrollBar::handle:vertical {\n"
"border:none;background-color:#acd8e8;}\n"
"QScrollBar:horizontal {border: none;\n"
"background-color: white;}\n"
"QScrollBar::handle:horizontall {\n"
"border:none;background-color:#acd8e8;}")
        self.listWidget.setLineWidth(0)
        self.listWidget.setObjectName("listWidget")
        self.closeButton = QtWidgets.QPushButton(ListsSelect)
        self.closeButton.setGeometry(QtCore.QRect(260, 1, 39, 40))
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
"background-color:white;\n"
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

        self.retranslateUi(ListsSelect)
        QtCore.QMetaObject.connectSlotsByName(ListsSelect)

    def retranslateUi(self, ListsSelect):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton.setText(_translate("ListsSelect", "Выбрать"))
        self.closeButton.setText(_translate("ListsSelect", "x"))

