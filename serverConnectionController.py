#!usr/bin/python
import sys
import mysql.connector
import pymysql

class connectionConfigurations():
    def __init__(self, user='senior477', password='SET56?ra', host=\
                 'mysql.stackcp.com',database='senior-33352e44', port = 50857):
        self.config = {
            'user': user,
            'password' : password,
            'host' : host,
            'database' : database,
            'port' : port
        }    
################################################################################################
class serverConnection():
    ############################################################################################
    def __init__(self, configurations):
        self.configurations = configurations
        self.userName = ''
        self.password = ''
    
    ############################################################################################
    def startConnection(self):
        try:
            self.connection = mysql.connector.connect(**self.configurations.config)
        except mysql.connector.Error as err:
            serverConnectionFailedPrompt = QMessageBox()
            serverConnectionFailedPrompt.setIcon(QMessageBox.Question)
            serverConnectionFailedPrompt.setText("Connection to Server Failed")
            serverConnectionFailedPrompt.setStandardButtons(QMessageBox.Ok)
            serverConnectionFailedPrompt.show()
            serverConnectionFailedPrompt.exec_()
            print("Connection Failed")
            try:
                self.connection = pymysql.connect(**self.configurations.config)
            except:
                print("Connection 2 Failed")
        else:
            #self.connection.close()
            self.cur = self.connection.cursor()
    
    ############################################################################################
    def closeConnection(self):
        self.connection.close()
    
    ############################################################################################
    def clearCredentials(self):
        self.userName = ''
        self.password = ''
    
    ############################################################################################
    def checkLoginCredentials(self, usernameToCheck, passwordToCheck):
        loginString = 'SELECT user_id FROM users WHERE user_name = \'' + \
                      str(usernameToCheck) + '\' and password = \'' + \
                      str(passwordToCheck) + '\';' 
        query = (loginString) #change table name
        self.cur.execute(query)

        for val in self.cur:
            print(val[0])
            if val[0]:
                self.userName = usernameToCheck
                self.password = passwordToCheck
                return True
        return False
    
    ############################################################################################
    def createNewUserAccount(self, firstName, lastName, ssn, username, password):
        newAccountString = 'INSERT INTO users(first_name, last_name, ssn, \
                            user_name, password) VALUES' + '(\'' \
                            + firstName + '\', \'' + lastName + \
        '\', \'' + ssn + '\', \'' + username + '\', \'' + password + '\');'

        query = (newAccountString)
        self.cur.execute(query)
        self.connection.commit()
        self.user = username
        return True
    
    ############################################################################################
    def addSensorData(self, userName, password, bodyTemp, gsr, heartRate):
        #go to table for self.user
        dateQuery = ("SELECT CURDATE();")
        self.cur.execute(dateQuery)
        for value in self.cur:
            date = value[0]
            print(date)
        insertQuery = ('INSERT INTO datasets(heart,sweat,temp,time,user_id) \
                        VALUES (' + str(heartRate) + ',' + str(gsr) + ',' + str(bodyTemp) + ',' + \
                       '\'' + str(date) + '\',(SELECT user_id FROM users WHERE user_name = \''+\
                       str(userName) + '\' AND password = \'' + str(password) + '\'));')
        self.cur.execute(insertQuery)
        self.connection.commit()
        return True
    
