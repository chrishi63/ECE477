#!usr/bin/python
import sys

import PyQt5
from PyQt5.QtWidgets import *

import loginscreen_auto as loginUi
import keyboard as keyboard

class LoginScreen(QMainWindow, loginUi.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.txteditPassword.setEchoMode(QLineEdit.Password)
        self.pbLogin.setEnabled(False)
        self.txteditUserName.clicked.connect(self.getUserNameInput)
        self.txteditUserName.textChanged.connect(self.updatePbEnable)
        self.txteditPassword.textChanged.connect(self.updatePbEnable)
        self.txteditPassword.clicked.connect(self.getPassword)
    def updatePbEnable(self):
        if len(self.txteditUserName.text()) * len(self.txteditPassword.text()) > 0:
            self.pbLogin.setEnabled(True)
        else:
            self.pbLogin.setEnabled(False)
    def getUserNameInput(self):
        newKeyboard = keyboard.Keyboard()
        newKeyboard.parent = self.txteditUserName
        newKeyboard.show()
        #newKeyboard.exec_()
    def getPassword(self):
        newKeyboard = keyboard.Keyboard()
        newKeyboard.parent = self.txteditPassword
        newKeyboard.show()
    def setUserNameInput(self, userName):
        self.txteditUserName.setText(userName)
        
def main():
    app = QApplication(sys.argv)
    form = LoginScreen()
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
