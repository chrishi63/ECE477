# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keyboard.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 380)
        MainWindow.setStyleSheet("background: #2e2e2e;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.aKey = QtWidgets.QPushButton(self.centralwidget)
        self.aKey.setGeometry(QtCore.QRect(70, 210, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.aKey.setFont(font)
        self.aKey.setStyleSheet("QPushButton {\n"
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
        self.aKey.setObjectName("aKey")
        self.lKey = QtWidgets.QPushButton(self.centralwidget)
        self.lKey.setGeometry(QtCore.QRect(630, 210, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lKey.setFont(font)
        self.lKey.setStyleSheet("QPushButton {\n"
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
        self.lKey.setObjectName("lKey")
        self.wKey = QtWidgets.QPushButton(self.centralwidget)
        self.wKey.setGeometry(QtCore.QRect(120, 140, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wKey.setFont(font)
        self.wKey.setStyleSheet("QPushButton {\n"
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
        self.wKey.setObjectName("wKey")
        self.Key5 = QtWidgets.QPushButton(self.centralwidget)
        self.Key5.setGeometry(QtCore.QRect(290, 70, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Key5.setFont(font)
        self.Key5.setStyleSheet("QPushButton {\n"
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
        self.Key5.setObjectName("Key5")
        self.Key6 = QtWidgets.QPushButton(self.centralwidget)
        self.Key6.setGeometry(QtCore.QRect(360, 70, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Key6.setFont(font)
        self.Key6.setStyleSheet("QPushButton {\n"
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
        self.Key6.setObjectName("Key6")
        self.Key7 = QtWidgets.QPushButton(self.centralwidget)
        self.Key7.setGeometry(QtCore.QRect(430, 70, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Key7.setFont(font)
        self.Key7.setStyleSheet("QPushButton {\n"
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
        self.Key7.setObjectName("Key7")
        self.Key8 = QtWidgets.QPushButton(self.centralwidget)
        self.Key8.setGeometry(QtCore.QRect(500, 70, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Key8.setFont(font)
        self.Key8.setStyleSheet("QPushButton {\n"
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
        self.Key8.setObjectName("Key8")
        self.Key9 = QtWidgets.QPushButton(self.centralwidget)
        self.Key9.setGeometry(QtCore.QRect(570, 70, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Key9.setFont(font)
        self.Key9.setStyleSheet("QPushButton {\n"
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
        self.Key9.setObjectName("Key9")
        self.backspace = QtWidgets.QPushButton(self.centralwidget)
        self.backspace.setGeometry(QtCore.QRect(700, 70, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.backspace.setFont(font)
        self.backspace.setStyleSheet("QPushButton {\n"
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
        self.backspace.setObjectName("backspace")
        self.bKey = QtWidgets.QPushButton(self.centralwidget)
        self.bKey.setGeometry(QtCore.QRect(390, 280, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bKey.setFont(font)
        self.bKey.setStyleSheet("QPushButton {\n"
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
        self.bKey.setObjectName("bKey")
        self.cKey = QtWidgets.QPushButton(self.centralwidget)
        self.cKey.setGeometry(QtCore.QRect(250, 280, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cKey.setFont(font)
        self.cKey.setStyleSheet("QPushButton {\n"
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
        self.cKey.setObjectName("cKey")
        self.dKey = QtWidgets.QPushButton(self.centralwidget)
        self.dKey.setGeometry(QtCore.QRect(210, 210, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dKey.setFont(font)
        self.dKey.setStyleSheet("QPushButton {\n"
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
        self.dKey.setObjectName("dKey")
        self.eKey = QtWidgets.QPushButton(self.centralwidget)
        self.eKey.setGeometry(QtCore.QRect(190, 140, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.eKey.setFont(font)
        self.eKey.setStyleSheet("QPushButton {\n"
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
        self.eKey.setObjectName("eKey")
        self.fKey = QtWidgets.QPushButton(self.centralwidget)
        self.fKey.setGeometry(QtCore.QRect(280, 210, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fKey.setFont(font)
        self.fKey.setStyleSheet("QPushButton {\n"
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
        self.fKey.setObjectName("fKey")
        self.gKey = QtWidgets.QPushButton(self.centralwidget)
        self.gKey.setGeometry(QtCore.QRect(350, 210, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gKey.setFont(font)
        self.gKey.setStyleSheet("QPushButton {\n"
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
        self.gKey.setObjectName("gKey")
        self.hKey = QtWidgets.QPushButton(self.centralwidget)
        self.hKey.setGeometry(QtCore.QRect(420, 210, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.hKey.setFont(font)
        self.hKey.setStyleSheet("QPushButton {\n"
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
        self.hKey.setObjectName("hKey")
        self.iKey = QtWidgets.QPushButton(self.centralwidget)
        self.iKey.setGeometry(QtCore.QRect(540, 140, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.iKey.setFont(font)
        self.iKey.setStyleSheet("QPushButton {\n"
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
        self.iKey.setObjectName("iKey")
        self.jKey = QtWidgets.QPushButton(self.centralwidget)
        self.jKey.setGeometry(QtCore.QRect(490, 210, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.jKey.setFont(font)
        self.jKey.setStyleSheet("QPushButton {\n"
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
        self.jKey.setObjectName("jKey")
        self.kKey = QtWidgets.QPushButton(self.centralwidget)
        self.kKey.setGeometry(QtCore.QRect(560, 210, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.kKey.setFont(font)
        self.kKey.setStyleSheet("QPushButton {\n"
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
        self.kKey.setObjectName("kKey")
        self.mKey = QtWidgets.QPushButton(self.centralwidget)
        self.mKey.setGeometry(QtCore.QRect(530, 280, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.mKey.setFont(font)
        self.mKey.setStyleSheet("QPushButton {\n"
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
        self.mKey.setObjectName("mKey")
        self.nKey = QtWidgets.QPushButton(self.centralwidget)
        self.nKey.setGeometry(QtCore.QRect(460, 280, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nKey.setFont(font)
        self.nKey.setStyleSheet("QPushButton {\n"
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
        self.nKey.setObjectName("nKey")
        self.oKey = QtWidgets.QPushButton(self.centralwidget)
        self.oKey.setGeometry(QtCore.QRect(610, 140, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.oKey.setFont(font)
        self.oKey.setStyleSheet("QPushButton {\n"
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
        self.oKey.setObjectName("oKey")
        self.pKey = QtWidgets.QPushButton(self.centralwidget)
        self.pKey.setGeometry(QtCore.QRect(680, 140, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pKey.setFont(font)
        self.pKey.setStyleSheet("QPushButton {\n"
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
        self.pKey.setObjectName("pKey")
        self.qKey = QtWidgets.QPushButton(self.centralwidget)
        self.qKey.setGeometry(QtCore.QRect(50, 140, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.qKey.setFont(font)
        self.qKey.setStyleSheet("QPushButton {\n"
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
        self.qKey.setObjectName("qKey")
        self.rKey = QtWidgets.QPushButton(self.centralwidget)
        self.rKey.setGeometry(QtCore.QRect(260, 140, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rKey.setFont(font)
        self.rKey.setStyleSheet("QPushButton {\n"
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
        self.rKey.setObjectName("rKey")
        self.sKey = QtWidgets.QPushButton(self.centralwidget)
        self.sKey.setGeometry(QtCore.QRect(140, 210, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sKey.setFont(font)
        self.sKey.setStyleSheet("QPushButton {\n"
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
        self.sKey.setObjectName("sKey")
        self.tKey = QtWidgets.QPushButton(self.centralwidget)
        self.tKey.setGeometry(QtCore.QRect(330, 140, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tKey.setFont(font)
        self.tKey.setStyleSheet("QPushButton {\n"
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
        self.tKey.setObjectName("tKey")
        self.uKey = QtWidgets.QPushButton(self.centralwidget)
        self.uKey.setGeometry(QtCore.QRect(470, 140, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.uKey.setFont(font)
        self.uKey.setStyleSheet("QPushButton {\n"
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
        self.uKey.setObjectName("uKey")
        self.vKey = QtWidgets.QPushButton(self.centralwidget)
        self.vKey.setGeometry(QtCore.QRect(320, 280, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.vKey.setFont(font)
        self.vKey.setStyleSheet("QPushButton {\n"
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
        self.vKey.setObjectName("vKey")
        self.xKey = QtWidgets.QPushButton(self.centralwidget)
        self.xKey.setGeometry(QtCore.QRect(180, 280, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.xKey.setFont(font)
        self.xKey.setStyleSheet("QPushButton {\n"
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
        self.xKey.setObjectName("xKey")
        self.yKey = QtWidgets.QPushButton(self.centralwidget)
        self.yKey.setGeometry(QtCore.QRect(400, 140, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.yKey.setFont(font)
        self.yKey.setStyleSheet("QPushButton {\n"
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
        self.yKey.setObjectName("yKey")
        self.zKey = QtWidgets.QPushButton(self.centralwidget)
        self.zKey.setGeometry(QtCore.QRect(110, 280, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.zKey.setFont(font)
        self.zKey.setStyleSheet("QPushButton {\n"
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
        self.zKey.setObjectName("zKey")
        self._0Key = QtWidgets.QPushButton(self.centralwidget)
        self._0Key.setGeometry(QtCore.QRect(640, 70, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self._0Key.setFont(font)
        self._0Key.setStyleSheet("QPushButton {\n"
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
        self._0Key.setObjectName("_0Key")
        self.Key1 = QtWidgets.QPushButton(self.centralwidget)
        self.Key1.setGeometry(QtCore.QRect(10, 70, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Key1.setFont(font)
        self.Key1.setStyleSheet("QPushButton {\n"
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
        self.Key1.setObjectName("Key1")
        self.Key2 = QtWidgets.QPushButton(self.centralwidget)
        self.Key2.setGeometry(QtCore.QRect(80, 70, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Key2.setFont(font)
        self.Key2.setStyleSheet("QPushButton {\n"
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
        self.Key2.setObjectName("Key2")
        self.Key3 = QtWidgets.QPushButton(self.centralwidget)
        self.Key3.setGeometry(QtCore.QRect(150, 70, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Key3.setFont(font)
        self.Key3.setStyleSheet("QPushButton {\n"
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
        self.Key3.setObjectName("Key3")
        self.Key4 = QtWidgets.QPushButton(self.centralwidget)
        self.Key4.setGeometry(QtCore.QRect(220, 70, 55, 55))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Key4.setFont(font)
        self.Key4.setStyleSheet("QPushButton {\n"
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
        self.Key4.setObjectName("Key4")
        self.enter = QtWidgets.QPushButton(self.centralwidget)
        self.enter.setGeometry(QtCore.QRect(600, 280, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.enter.setFont(font)
        self.enter.setStyleSheet("QPushButton {\n"
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
        self.enter.setObjectName("enter")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 20, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("QLineEdit\n"
"{\n"
"    background-color: rgb(211, 84, 0);\n"
"    color: rgb(46, 46, 46);\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(211, 84, 0)")
        self.label.setObjectName("label")
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
        self.aKey.setText(_translate("MainWindow", "A"))
        self.lKey.setText(_translate("MainWindow", "L"))
        self.wKey.setText(_translate("MainWindow", "W"))
        self.Key5.setText(_translate("MainWindow", "5"))
        self.Key6.setText(_translate("MainWindow", "6"))
        self.Key7.setText(_translate("MainWindow", "7"))
        self.Key8.setText(_translate("MainWindow", "8"))
        self.Key9.setText(_translate("MainWindow", "9"))
        self.backspace.setText(_translate("MainWindow", "BACKSPACE"))
        self.bKey.setText(_translate("MainWindow", "B"))
        self.cKey.setText(_translate("MainWindow", "C"))
        self.dKey.setText(_translate("MainWindow", "D"))
        self.eKey.setText(_translate("MainWindow", "E"))
        self.fKey.setText(_translate("MainWindow", "F"))
        self.gKey.setText(_translate("MainWindow", "G"))
        self.hKey.setText(_translate("MainWindow", "H"))
        self.iKey.setText(_translate("MainWindow", "I"))
        self.jKey.setText(_translate("MainWindow", "J"))
        self.kKey.setText(_translate("MainWindow", "K"))
        self.mKey.setText(_translate("MainWindow", "M"))
        self.nKey.setText(_translate("MainWindow", "N"))
        self.oKey.setText(_translate("MainWindow", "O"))
        self.pKey.setText(_translate("MainWindow", "P"))
        self.qKey.setText(_translate("MainWindow", "Q"))
        self.rKey.setText(_translate("MainWindow", "R"))
        self.sKey.setText(_translate("MainWindow", "S"))
        self.tKey.setText(_translate("MainWindow", "T"))
        self.uKey.setText(_translate("MainWindow", "U"))
        self.vKey.setText(_translate("MainWindow", "V"))
        self.xKey.setText(_translate("MainWindow", "X"))
        self.yKey.setText(_translate("MainWindow", "Y"))
        self.zKey.setText(_translate("MainWindow", "Z"))
        self._0Key.setText(_translate("MainWindow", "0"))
        self.Key1.setText(_translate("MainWindow", "1"))
        self.Key2.setText(_translate("MainWindow", "2"))
        self.Key3.setText(_translate("MainWindow", "3"))
        self.Key4.setText(_translate("MainWindow", "4"))
        self.enter.setText(_translate("MainWindow", "ENTER"))
        self.label.setText(_translate("MainWindow", "Enter User Name:"))

