#!usr/bin/python
import sys

import PyQt5 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSvg import *

import mainscreen_auto
import createAccountScreen as createAccount
import loginScreen as login
import dataCollectionScreen as dataCollection
import serverConnectionController as server

class MainScreen(QMainWindow, mainscreen_auto.Ui_MainScreen):
##################################################################
    def createNewAccount(self):
        #takes user to new account screen
##        self.createAccount.showFullScreen()
        print("navigating to new account screen")
        self.createAccount.show()
        self.hide()
##################################################################  
    def hideCreateScreen(self):
##        self.showFullScreen()
        self.show()
        self.createAccount.hide()
##################################################################
    def login(self):
        #takes user to login screen
##        self.loginScreen.showFullScreen()
        print("navigating to login  screen")
        self.loginScreen.show()
        self.hide()
##################################################################
    def attemptLogin(self):
        config = server.connectionConfigurations()
        connection = server.serverConnection(config)
        connection.startConnection()
        print(str(self.loginScreen.txteditUserName.text()))
        if connection.checkLoginCredentials(self.loginScreen.txteditUserName.text(), \
                                         self.loginScreen.txteditPassword.text())\
                                         is True:
            self.dataCollectionScreen.userName = userName
            self.dataCollectionScreen.password = password
            self.showDataCollectionScreen()
        else:
            print(False)
        connection.closeConnection()
##################################################################
    def attemptCreateAccount(self):
        config = server.connectionConfigurations()
        connection = server.serverConnection(config)
        connection.startConnection()
        firstName = self.createAccount.txteditFirstName.text()
        lastName = (self.createAccount.txteditLastName.text())
        SSN = (self.createAccount.txteditSSN.text())
        userName = (self.createAccount.txteditUserName.text())
        password = (self.createAccount.txteditPassword.text())
        if connection.createNewUserAccount(firstName, lastName, SSN, userName, password) is True:
            self.dataCollectionScreen.userName = userName
            self.dataCollectionScreen.password = password
            self.showDataCollectionScreen()
        else:
            print(False)
        connection.closeConnection()
##################################################################
    def hideLoginScreen(self):
        print("hide login")
##        self.showFullScreen()
        self.show()
        self.loginScreen.hide()
##################################################################
    def showDataCollectionScreen(self):
##        self.dataCollectionScreen.showFullScreen()
        self.dataCollectionScreen.show()
        self.loginScreen.hide()
        self.loginScreen.txteditUserName.setText("")
        self.loginScreen.txteditPassword.setText("")
        self.createAccount.txteditFirstName.setText("")
        self.createAccount.txteditLastName.setText("")
        self.createAccount.txteditSSN.setText("")
        self.createAccount.txteditUserName.setText("")
        self.createAccount.txteditPassword.setText("")
        self.createAccount.hide()
##################################################################
    def onReturnPbPressFromDataCollectionScreen(self):
        if(self.userConfirmsLogout()):
            print("logout confirmed")
            self.hideDataCollectionScreen()
        else:
            return
##################################################################
    def userConfirmsLogout(self):
        print("showing logout Prompt")
        logoutPrompt = QMessageBox()
        logoutPrompt.setIcon(QMessageBox.Question)
        logoutPrompt.setText("Are you sure you would like to logout?")
        logoutPrompt.setStandardButtons(QMessageBox.Yes |\
            QMessageBox.No)
##        logoutPrompt.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint)
        logoutPrompt.show()
        if(logoutPrompt.exec_() == 65536):
            return 0
        else:
            return 1
##################################################################                                                             
    def hideDataCollectionScreen(self):
##        self.showFullScreen()
        self.show()
        self.dataCollectionScreen.clearData()
        self.dataCollectionScreen.hide()
##################################################################
    def __init__(self):
        print("Creating main screen")
        super(self.__class__, self).__init__()
        self.setupUi(self)
        
        # Create Other Screens
        self.createAccount = createAccount.CreateAccountScreen()
        self.loginScreen = login.LoginScreen()
        self.dataCollectionScreen = dataCollection.DataCollectionScreen()
        
        # Main Screen Functionalities:
        self.pbNewAccount.clicked.connect(lambda: self.createNewAccount())
        self.pbLogin.clicked.connect(lambda: self.login())

        # Returning From Other Screens
        self.createAccount.pbReturn.clicked.connect(lambda: self.hideCreateScreen())
        self.loginScreen.pbReturn.clicked.connect(lambda: self.hideLoginScreen())
        self.dataCollectionScreen.pbReturn\
            .clicked.connect(lambda: \
            self.onReturnPbPressFromDataCollectionScreen())

        #Navigation Between Other Screens
        self.loginScreen.pbLogin.clicked.connect(lambda: self.attemptLogin())
        self.createAccount.pbCreateAccount.clicked.connect(lambda: self.attemptCreateAccount())
##################################################################
def main():
    app = QApplication(sys.argv)
    form = MainScreen()
    form.show()
##    form.showFullScreen()
    sys.exit(app.exec_())
##################################################################
if __name__ == "__main__":
    main()
