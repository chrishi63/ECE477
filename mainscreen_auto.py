# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainscreen.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainScreen(object):
    def setupUi(self, MainScreen):
        MainScreen.setObjectName("MainScreen")
        MainScreen.resize(800, 480)
        self.centralWidget = QtWidgets.QWidget(MainScreen)
        self.centralWidget.setObjectName("centralWidget")
        self.pbNewAccount = QtWidgets.QPushButton(self.centralWidget)
        self.pbNewAccount.setGeometry(QtCore.QRect(320, 190, 191, 41))
        self.pbNewAccount.setStyleSheet("QPushButton {\n"
"   background-color: #d35400;\n"
"    border: 1px solid #d35400;\n"
"    margin-right: 15px;\n"
"   border-radius: 20%;\n"
"    color: #ffffff\n"
"}\n"
"QPushButton:default {\n"
"    background-color:#e5982c;\n"
"}\n"
"QPushButton:pressed {\n"
"    position:relative;\n"
"    top:1px;\n"
"}\n"
"")
        self.pbNewAccount.setFlat(False)
        self.pbNewAccount.setObjectName("pbNewAccount")
        self.pbLogin = QtWidgets.QPushButton(self.centralWidget)
        self.pbLogin.setGeometry(QtCore.QRect(320, 260, 171, 41))
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
        self.pbLogin.setFlat(True)
        self.pbLogin.setObjectName("pbLogin")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 231, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    padding: 2px;\n"
"    border-image: url(:/logo1.svg) 0 0 0 0 stretch stretch;\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.batteryIndicator = QtWidgets.QProgressBar(self.centralWidget)
        self.batteryIndicator.setGeometry(QtCore.QRect(670, 40, 101, 21))
        self.batteryIndicator.setProperty("value", 24)
        self.batteryIndicator.setObjectName("batteryIndicator")
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(0, 100, 801, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainScreen.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainScreen)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuBar.setObjectName("menuBar")
        MainScreen.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainScreen)
        self.mainToolBar.setObjectName("mainToolBar")
        MainScreen.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainScreen)
        self.statusBar.setObjectName("statusBar")
        MainScreen.setStatusBar(self.statusBar)

        self.retranslateUi(MainScreen)
        QtCore.QMetaObject.connectSlotsByName(MainScreen)

    def retranslateUi(self, MainScreen):
        _translate = QtCore.QCoreApplication.translate
        MainScreen.setWindowTitle(_translate("MainScreen", "MainScreen"))
        self.pbNewAccount.setText(_translate("MainScreen", "Setup New Account"))
        self.pbLogin.setText(_translate("MainScreen", "Login"))

