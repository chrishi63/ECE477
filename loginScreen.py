#!usr/bin/python
import sys

import PyQt5
from PyQt5.QtWidgets import *

import loginscreen_auto as loginUi

class LoginScreen(QMainWindow, loginUi.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.txteditPassword.setEchoMode(QLineEdit.Password)

def main():
    app = QApplication(sys.argv)
    form = LoginScreen()
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
