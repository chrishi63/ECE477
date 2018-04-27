#!usr/bin/python
import sys

import PyQt5
from PyQt5.QtWidgets import *

import createaccountscreen_auto as createAccountUi
import keyboard as keyboard

class CreateAccountScreen(QMainWindow, createAccountUi.Ui_createAccountScreen):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.txteditPassword.setEchoMode(QLineEdit.Password)
        self.pbCreateAccount.setEnabled(False)
        self.txteditFirstName.textChanged.connect(self.updatePbEnable)
        self.txteditLastName.textChanged.connect(self.updatePbEnable)
        self.txteditSSN.textChanged.connect(self.updatePbEnable)
        self.txteditUserName.textChanged.connect(self.updatePbEnable)
        self.txteditPassword.textChanged.connect(self.updatePbEnable)
        
        self.txteditFirstName.clicked.connect(self.getFirstName)
        self.txteditLastName.clicked.connect(self.getLastName)
        self.txteditSSN.clicked.connect(self.getSSN)
        self.txteditUserName.clicked.connect(self.getUserName)
        self.txteditPassword.clicked.connect(self.getPassword)
    def updatePbEnable(self):
        if len(self.txteditFirstName.text())*len(self.txteditLastName.text()) \
          *len(self.txteditSSN.text())*len(self.txteditUserName.text())\
          *len(self.txteditPassword.text()) > 0:
            self.pbCreateAccount.setEnabled(True)
        else:
            self.pbCreateAccount.setEnabled(False)
    def getFirstName(self):
        newKeyboard = keyboard.Keyboard()
        newKeyboard.parent = self.txteditFirstName
        newKeyboard.show()
    def getLastName(self):
        newKeyboard = keyboard.Keyboard()
        newKeyboard.parent = self.txteditLastName
        newKeyboard.show()
    def getSSN(self):
        newKeyboard = keyboard.Keyboard()
        newKeyboard.parent = self.txteditSSN
        newKeyboard.show()
    def getUserName(self):
        newKeyboard = keyboard.Keyboard()
        newKeyboard.parent = self.txteditUserName
        newKeyboard.show()
    def getPassword(self):
        newKeyboard = keyboard.Keyboard()
        newKeyboard.parent = self.txteditPassword
        newKeyboard.show()
    
    
def main():
    app = QApplication(sys.argv)
    form = CreateAccountScreen()
    form.show()
    print("Showing screen")
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
