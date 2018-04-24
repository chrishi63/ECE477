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
        MainWindow.setStyleSheet("background: #2e2e2e;\n"
"")
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
"    border-bottom: 1px solid #d35400;\n"
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
"    color: rgb(128, 128, 128);\n"
"}")
        self.label.setObjectName("label")
        self.txteditPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txteditPassword.setGeometry(QtCore.QRect(350, 290, 181, 21))
        self.txteditPassword.setStyleSheet("QLineEdit {\n"
"    border-bottom: 1px solid #d35400;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    background: transparent;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.txteditPassword.setObjectName("txteditPassword")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 230, 91, 31))
        self.label_2.setStyleSheet("QLabel {\n"
"    color: rgb(128, 128, 128);\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(240, 290, 91, 31))
        self.label_3.setStyleSheet("QLabel {\n"
"    color: rgb(128, 128, 128);\n"
"}")
        self.label_3.setObjectName("label_3")
        self.pbLogin = QtWidgets.QPushButton(self.centralwidget)
        self.pbLogin.setGeometry(QtCore.QRect(340, 360, 121, 41))
        self.pbLogin.setStyleSheet("QPushButton {\n"
"    border: 1px solid #d35400;\n"
"    color: #d35400;\n"
"    border-radius: 20%\n"
"}\n"
"QPushButton:disabled {\n"
"    color:     #A9A9A9;\n"
"    border:     1px solid #A9A9A9;\n"
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
        self.pbReturn = QtWidgets.QPushButton(self.centralwidget)
        self.pbReturn.setGeometry(QtCore.QRect(70, 30, 41, 51))
        self.pbReturn.setStyleSheet("background-image: url(:/backArrowNew.png) ;\n"
"background-repeat: none;\n"
"background-size: 100px;")
        self.pbReturn.setText("")
        self.pbReturn.setFlat(True)
        self.pbReturn.setObjectName("pbReturn")
        self.batteryIndicator = QtWidgets.QProgressBar(self.centralwidget)
        self.batteryIndicator.setGeometry(QtCore.QRect(690, 50, 51, 21))
        self.batteryIndicator.setStyleSheet("QProgressBar{\n"
"    border: 1px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color: rgb(128, 128, 128);\n"
"}\n"
"QProgressBar::chunk{\n"
"    background-color: rgb(211, 84, 0);\n"
"}")
        self.batteryIndicator.setProperty("value", 24)
        self.batteryIndicator.setObjectName("batteryIndicator")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 330, 281, 121))
        self.label_5.setObjectName("label_5")
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
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/logo.png\" width=\"200\" height=\"100\" /></p></body></html>"))

