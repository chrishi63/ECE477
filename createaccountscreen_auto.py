# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createaccountscreen.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_createAccountScreen(object):
    def setupUi(self, createAccountScreen):
        createAccountScreen.setObjectName("createAccountScreen")
        createAccountScreen.resize(800, 480)
        createAccountScreen.setStyleSheet("background: #2e2e2e;\n"
"")
        self.centralwidget = QtWidgets.QWidget(createAccountScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 100, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(690, 40, 51, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    border: 1px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    color: rgb(128, 128, 128);\n"
"}\n"
"QProgressBar::chunk{\n"
"    background-color: rgb(211, 84, 0);\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 100, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: rgb(128, 128, 128);\n"
"}")
        self.label.setObjectName("label")
        self.txteditFirstName = QtWidgets.QLineEdit(self.centralwidget)
        self.txteditFirstName.setGeometry(QtCore.QRect(390, 150, 181, 21))
        self.txteditFirstName.setStyleSheet("QLineEdit {\n"
"    border-bottom: 1px solid #d35400;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    background: transparent;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.txteditFirstName.setText("")
        self.txteditFirstName.setFrame(True)
        self.txteditFirstName.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txteditFirstName.setObjectName("txteditFirstName")
        self.txteditLastName = QtWidgets.QLineEdit(self.centralwidget)
        self.txteditLastName.setGeometry(QtCore.QRect(390, 190, 181, 21))
        self.txteditLastName.setStyleSheet("QLineEdit {\n"
"    border-bottom: 1px solid #d35400;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    background: transparent;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.txteditLastName.setObjectName("txteditLastName")
        self.txteditSSN = QtWidgets.QLineEdit(self.centralwidget)
        self.txteditSSN.setGeometry(QtCore.QRect(390, 310, 181, 21))
        self.txteditSSN.setStyleSheet("QLineEdit {\n"
"    border-bottom: 1px solid #d35400;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    background: transparent;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.txteditSSN.setObjectName("txteditSSN")
        self.txteditUserName = QtWidgets.QLineEdit(self.centralwidget)
        self.txteditUserName.setGeometry(QtCore.QRect(390, 230, 181, 21))
        self.txteditUserName.setStyleSheet("QLineEdit {\n"
"    border-bottom: 1px solid #d35400;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    background: transparent;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.txteditUserName.setObjectName("txteditUserName")
        self.txteditPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txteditPassword.setGeometry(QtCore.QRect(390, 270, 181, 21))
        self.txteditPassword.setStyleSheet("QLineEdit {\n"
"    border-bottom: 1px solid #d35400;\n"
"    border-radius: 0px;\n"
"    padding: 0 8px;\n"
"    background: transparent;\n"
"    selection-background-color: darkgray;\n"
"}")
        self.txteditPassword.setObjectName("txteditPassword")
        self.pbCreateAccount = QtWidgets.QPushButton(self.centralwidget)
        self.pbCreateAccount.setGeometry(QtCore.QRect(340, 380, 121, 31))
        self.pbCreateAccount.setStyleSheet("QPushButton {\n"
"    border: 1px solid #d35400;\n"
"    color: #d35400;\n"
"    border-radius: 15%\n"
"}\n"
"QPushButton:disabled {\n"
"    color:     #A9A9A9;\n"
"    border:     1px solid #A9A9A9;\n"
"    border-radius: 15%\n"
"}\n"
"QPushButton:default {\n"
"    background-color:#e5982c;\n"
"}\n"
"QPushButton:pressed {\n"
"    position:relative;\n"
"    top:1px;\n"
"}\n"
"")
        self.pbCreateAccount.setObjectName("pbCreateAccount")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 150, 141, 21))
        self.label_2.setStyleSheet("QLabel {\n"
"    color: rgb(128, 128, 128);\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 190, 141, 21))
        self.label_3.setStyleSheet("QLabel {\n"
"    color: rgb(128, 128, 128);\n"
"}")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 310, 141, 21))
        self.label_4.setStyleSheet("QLabel {\n"
"    color: rgb(128, 128, 128);\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 230, 141, 21))
        self.label_5.setStyleSheet("QLabel {\n"
"    color: rgb(128, 128, 128);\n"
"}")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 270, 141, 21))
        self.label_6.setStyleSheet("QLabel {\n"
"    color: rgb(128, 128, 128);\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(250, 340, 301, 16))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("QLabel {\n"
"    color: rgb(128, 128, 128);\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 280, 281, 141))
        self.label_8.setObjectName("label_8")
        self.pbReturn = QtWidgets.QPushButton(self.centralwidget)
        self.pbReturn.setGeometry(QtCore.QRect(50, 20, 71, 51))
        self.pbReturn.setStyleSheet("background-image: url(:/backArrowNew.png) ;\n"
"background-repeat: none;\n"
"background-size: 100px;")
        self.pbReturn.setText("")
        self.pbReturn.setFlat(True)
        self.pbReturn.setObjectName("pbReturn")
        createAccountScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(createAccountScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        createAccountScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(createAccountScreen)
        self.statusbar.setObjectName("statusbar")
        createAccountScreen.setStatusBar(self.statusbar)

        self.retranslateUi(createAccountScreen)
        QtCore.QMetaObject.connectSlotsByName(createAccountScreen)

    def retranslateUi(self, createAccountScreen):
        _translate = QtCore.QCoreApplication.translate
        createAccountScreen.setWindowTitle(_translate("createAccountScreen", "MainWindow"))
        self.label.setText(_translate("createAccountScreen", "Enter New User Information"))
        self.pbCreateAccount.setText(_translate("createAccountScreen", "Create Account"))
        self.label_2.setText(_translate("createAccountScreen", "Patient First Name"))
        self.label_3.setText(_translate("createAccountScreen", "Patient Last Name"))
        self.label_4.setText(_translate("createAccountScreen", "Patient SSN"))
        self.label_5.setText(_translate("createAccountScreen", "User Name"))
        self.label_6.setText(_translate("createAccountScreen", "Password"))
        self.label_7.setText(_translate("createAccountScreen", "SSN will be used by hospital for any insurance related info and hospital record keeping"))
        self.label_8.setText(_translate("createAccountScreen", "<html><head/><body><p><img src=\"logo.png\" width=\"200\" height=\"100\" /></p></body></html>"))

