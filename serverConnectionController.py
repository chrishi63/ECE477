#!usr/bin/python
import sys
import mysql.connector

class connectionConfigurations():
    def __init__(self, user='senior477', password='SET56?ra', host=\
                 'mysql.stackcp.com',database='senior-33352e44',port='50857'):
        self.config = {
            'user': user,
            'password' : password,
            'host' : host,
            'database' : database,
            'port' : port
        }

class serverConnection():
    def __init__(self, configurations):
        self.configurations = configurations
    def startConnection():
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
            self.connection.close()
        self.cur = self.connection.cursor()
                                        
    def closeConnection():
        self.connection.close()
    def checkLoginCredentials(usernameToCheck, passwordToCheck):
        query = ("SELECT * FROM users;") #change table name
        self.cur.execute(query)
        for {table elements} in cur:
            if username is usernameToCheck and password is passwordToCheck:
                self.user = username
                return True
        return False

    def createNewUserAccount(name, ssn, username, password):
        dateQuery = ("SELECT CURDATE();")
        self.cur.execute(dateQuery)
        date = self.cur[0][0]
        query = ("INSERT INTO users "
                 "(name, ssn, username, password)"
                 "VALUES ('" + name + "', " + ssn "');")
        self.cur.exectue(query)
        self.connection.commit()
        self.user = username
        return True

    def addBodyTemp(bodyTemp):
        #go to table for self.user
        dateQuery = ("SELECT CURDATE();")
        self.cur.execute(dateQuery)
        date = self.cur[0][0]
        quere = ("INSERT INTO tablename "
                 "(body temperature, date)"
                 "VALUES ('" + bodyTemp + "', " + date "');")
        self.cur.execute(query)
        self.connection.commit()

    def addGSR(gsr):
        pass
    def addHeartRate(heartRate):
        pass
    
