#!usr/bin/python
import sys
import mysql.connector

class connectionConfigurations():
    def __init__(self, user='achhetri', password='aka619ASH', host=\
                 'mydb.ics.purdue.edu',database='achhetri'):
        self.config = {
            'user': user,
            'password' : password,
            'host' : host,
            'database' : database,
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
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Unable to access server with given username/password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
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
    def addSensorData(bodyTemp, gsr, heartRate):
        #go to table for self.user
        dateQuery = ("SELECT CURDATE();")
        self.cur.execute(dateQuery)
        date = self.cur[0][0]
        insertQuery = ('INSERT INTO datasets(heart,sweat,temp,time,user_id) \
                        VALUES (' + heartRate + ',' + gsr + ',' + bodyTemp + ',' + \
                       '\'' + date + '\',(SELECT user_id FROM users WHERE user_name = \''+\
                       self.userName + '\' AND password = \'' + self.password + '\'));')
        self.cur.execute(query)
        self.connection.commit()
        return True
    
