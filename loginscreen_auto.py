# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginscreen.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 110, 801, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.txteditUserName = QtWidgets.QLineEdit(self.centralwidget)
        self.txteditUserName.setGeometry(QtCore.QRect(350, 230, 181, 21))
        self.txteditUserName.setStyleSheet("QLineEdit {\n"
"    border-bottom: 1px solid #e5982c;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    background: transparent;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.txteditUserName.setObjectName("txteditUserName")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 170, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: rgb(90, 90, 90);\n"
"}")
        self.label.setObjectName("label")
        self.txteditPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txteditPassword.setGeometry(QtCore.QRect(350, 290, 181, 21))
        self.txteditPassword.setStyleSheet("QLineEdit {\n"
"    border-bottom: 1px solid #e5982c;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    background: transparent;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.txteditPassword.setObjectName("txteditPassword")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 230, 91, 31))
        self.label_2.setStyleSheet("QLabel {\n"
"    color: rgb(90, 90, 90);\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 290, 91, 31))
        self.label_3.setStyleSheet("QLabel {\n"
"    color: rgb(90, 90, 90);\n"
"}")
        self.label_3.setObjectName("label_3")
        self.pbLogin = QtWidgets.QPushButton(self.centralwidget)
        self.pbLogin.setGeometry(QtCore.QRect(340, 360, 121, 41))
        self.pbLogin.setStyleSheet("QPushButton {\n"
"    border: 1px solid #d35400;\n"
"    color: #d35400;\n"
"    border-radius: 20%\n"
"}\n"
"QPushButton:default {\n"
"    background-color:#e5982c;\n"
"}\n"
"QPushButton:pressed {\n"
"    position:relative;\n"
"    top:1px;\n"
"}\n"
"")
        self.pbLogin.setObjectName("pbLogin")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(660, 40, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.pbReturn = QtWidgets.QPushButton(self.centralwidget)
        self.pbReturn.setGeometry(QtCore.QRect(40, 30, 61, 51))
        self.pbReturn.setText("")
        self.pbReturn.setObjectName("pbReturn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter Login Information:"))
        self.label_2.setText(_translate("MainWindow", "User Name"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.pbLogin.setText(_translate("MainWindow", "Login"))

