#!usr/bin/python
import sys

import PyQt5
from PyQt5.QtWidgets import *

import createaccountscreen_auto as createAccountUi

class CreateAccountScreen(QMainWindow, createAccountUi.Ui_createAccountScreen):
    def createAccount(self):
        #send information to server
        #go to data collection screen
        pass
    def returnToMainScreen(self):
        #return to main screen
        pass
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        print("Creating createAccountScreen")
        self.txteditPassword.setEchoMode(QLineEdit.Password)


def main():
    app = QApplication(sys.argv)
    form = CreateAccountScreen()
    form.show()
    print("Showing screen")
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
