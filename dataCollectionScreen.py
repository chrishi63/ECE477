#!usr/bin/python
import sys
import time

rPin = 29
bPin = 33
gPin = 13

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(rPin, GPIO.OUT)
GPIO.setup(bPin, GPIO.OUT)
GPIO.setup(gPin, GPIO.OUT)

import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
import datacollection_auto as dataUi
import serverConnectionController as server
import stmConnectionControl as stm


class DataCollectionScreen(QMainWindow, dataUi.Ui_DataCollection):
    ############################################################################################
    def clearData(self):
        self.heartRate = -1
        self.gsr = 0
        self.bodyTemp = 0
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.updatePbEnable()
        
    ############################################################################################
    def onSendDataPbPress(self):
        if (self.sendingDataToServerFails()):
            # make a popup window that send data sending failed
            clearDataPrompt = QMessageBox()
            clearDataPrompt.setIcon(QMessageBox.Question)
            clearDataPrompt.setText("Sending Data To Server Failed")
            #clearDataPrompt.setInformativeText(informativeText)        
            clearDataPrompt.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            clearDataPrompt.show()
            print("failed sending data to server")
            return False
        sendSuccessPrompt = QMessageBox()
        sendSuccessPrompt.setIcon(QMessageBox.Question)
        sendSuccessPrompt.setText("Data Sent To Server Successfully")
        sendSuccessPrompt.setStandardButtons(QMessageBox.Ok)
        sendSuccessPrompt.show()
        sendSuccessPrompt.exec_()
        self.clearData()
        return True
    
    ############################################################################################
    def sendingDataToServerFails(self):
        #send data to server and return 0 if successful, 1 if unsuccessful
        config = server.connectionConfigurations()
        connection = server.serverConnection(config)
        connection.startConnection()
        if (connection.addSensorData(self.userName, self.password, \
                                     self.bodyTemp, self.gsr, self.heartRate)):
            return 0
        return 1
    
    ############################################################################################
    def createDataPrompt(self, text, informativeText):
        clearDataPrompt = QMessageBox()
        clearDataPrompt.setIcon(QMessageBox.Question)
        clearDataPrompt.setText(text)
        clearDataPrompt.setInformativeText(informativeText)        
        clearDataPrompt.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        clearDataPrompt.show()

        return clearDataPrompt.exec_() != 65536
    ############################################################################################
    def promptUserToOverrideData(self, sensor):
        if sensor is 1:
            informativeText = "There is existing heart rate data that \
has not been sent to the server. Taking a new measurement will override this data. \
Would you like to proceed?"
        elif sensor is 3:
            informativeText = "There is existing gsr data that has  not been sent to the \
server. Taking a new measurement will override this data. \
Would you like to proceed?"
        else:
            informativeText = "There is existing body temperature data that has not been \
sent to the server. Taking a new measurement will override this data. \
Would you like to proceed?"
        return self.createDataPrompt("Existing data has not been sent", informativeText)
    ############################################################################################
    def userChoosesToOverrideHeartRateData(self):
        return self.promptUserToOverrideData(1)
    
    ############################################################################################
    def userChoosesToOverrideGSRData(self):
        return self.promptUserToOverrideData(2)
    
    ########################################################################################
    def userChoosesToOverrideBodyTemperatureData(self):
        return self.promptUserToOverrideData(3)
    
    ############################################################################################
    def checkStoredHeartRateData(self):
        print("Checking Heart Rate")
        if self.label_2.text() is not "":
            print("Heart rate already exisits")
            if self.userChoosesToOverrideHeartRateData():
                self.messageText.setText("Measuring Heart Rate")
                self.measureHeartRate()
        else:
            print("Measuring Heart Rate")
            self.messageText.setText("Measuring Heart Rate")
            self.measureHeartRate()
            
    ############################################################################################
    def checkBodyTemperatureData(self):
        if self.label_4.text() is not "":
            if self.userChoosesToOverrideBodyTemperatureData():
                self.messageText.setText("Measuring Body Temp")
                self.measureBodyTemperature()
        else:
            self.measureBodyTemperature()
            self.messageText.setText("Measuring Body Temp")
            
    ############################################################################################
    def checkGalvanicSkinResponseData(self):
        if self.label_3.text() is not "":
            if self.userChoosesToOverrideGSRData():
                self.messageText.setText("Measuring GSR")
                self.measureGalvanicSkinResponse()
        else:
            self.measureGalvanicSkinResponse()
            self.messageText.setText("Measuring GSR")
            
            
    ############################################################################################
    def measureHeartRate(self):
        self.messageText.setText("Measuring Heart Rate")
        if self.stmAddressByte is 0:
            self.heartRate = self.heartRate + 1
            self.label_2.setText(str(self.heartRate))
        else:
            print("Disabling pushbuttons and measuring heart rate")
            self.disablePushButtons()
            #GPIO.output(rPin, GPIO.LOW)
            #GPIO.output(bPin, GPIO.LOW)
            #GPIO.output(gPin, GPIO.HIGH)
            connection = stm.stmConnection()
            try:
                self.connection.signalSensorToSTM(self.heartRateSignal)
                QTimer.singleShot(10000,self.getHeartRateFromSTM)
            except:
                self.updateGUIAfterDataReceived()
            
    ############################################################################################
    def measureBodyTemperature(self):
        if self.stmAddressByte is 0:
            self.bodyTemp = self.bodyTemp + 1
            self.label_4.setText(str(self.bodyTemp))
        else:
            self.disablePushButtons()
            #GPIO.output(rPin, GPIO.LOW)
            #GPIO.output(bPin, GPIO.HIGH)
            #GPIO.output(gPin, GPIO.LOW)
            #self.connection.getTemperature()
            try:
                self.connection.signalSensorToSTM(self.bodyTempSignal)
                QTimer.singleShot(5000,self.getBodyTempFromSTM)
            except:
                self.updateGUIAfterDataReceived()
        
    ############################################################################################
    def measureGalvanicSkinResponse(self):
        if self.stmAddressByte is 0:
            self.gsr = self.gsr + 1
        else:
            self.disablePushButtons()
            #GPIO.output(rPin, GPIO.HIGH)
            #GPIO.output(bPin, GPIO.HIGH)
            #GPIO.output(gPin, GPIO.LOW)
            try:
                self.connection.signalSensorToSTM(self.gsrSignal)
                QTimer.singleShot(5000,self.getGSRFromSTM)
            except:
                self.updateGUIAfterDataReceived()
            #QTimer.singleShot(10000,self.getGSRFromSTM)
        
    ############################################################################################
    def getBodyTempFromSTM(self):
        self.connection.signalSensorToSTM(self.bodyTempSignal)
        self.bodyTemp = self.connection.readSensorData()
        self.updateGUIAfterDataReceived()
    ############################################################################################
    def getHeartRateFromSTM(self):
        self.connection.signalSensorToSTM(self.heartRateSignal)
        self.heartRate = self.connection.readSensorData()
        self.updateGUIAfterDataReceived()
        
    ############################################################################################
    def getGSRFromSTM(self):
        self.connection.signalSensorToSTM(self.gsrSignal)
        self.gsr = self.connection.readSensorData()
        self.updateGUIAfterDataReceived()
        
    ############################################################################################
    def disablePushButtons(self):
        
        self.pbSendData.setEnabled(False)
        self.pbHeartRate.setEnabled(False)
        self.pbGSR.setEnabled(False)
        self.pbBodyTemp.setEnabled(False)
        
    ############################################################################################
    def updateGUIAfterDataReceived(self):
        #GPIO.output(rPin, GPIO.LOW)
        #GPIO.output(bPin, GPIO.LOW)
        #GPIO.output(gPin, GPIO.LOW)
        self.messageText.setText("")
        self.pbHeartRate.setEnabled(True)
        self.pbGSR.setEnabled(True)
        self.pbBodyTemp.setEnabled(True)
        if self.gsr > 0:
            self.label_3.setText(str(self.gsr))
        if self.bodyTemp > 0:
            print(self.bodyTemp)
            self.label_4.setText(str(self.bodyTemp))
        if self.heartRate > -1:
            self.label_2.setText(str(self.heartRate))
        self.updatePbEnable()
        self.connection.stopCollectingBatteryData = 0
        
    ############################################################################################
    def updatePbEnable(self):
        if (self.heartRate * self.gsr * self.bodyTemp) > 0:
            self.pbSendData.setEnabled(True)
        else:
            self.pbSendData.setEnabled(False)
            
    ############################################################################################      
    def batteryDataAvailable(self):
        if self.connection.stopRequestingBatteryData is 1:
            print("Data collection screen - cannot request battery data")
            return False
        else:
            print("Data collection screen requesting battery data")
            self.connection.signalSensorToSTM(self.batterySignal)
            print(self.connection.sensorSignal)
            print("Data COllection Screen reading battery Data")
            self.batteryLevel = self.connection.readSensorData()
            return self.batteryLevel
        
    ############################################################################################
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.heartRate = -1
        self.gsr = 0
        self.bodyTemp = 0
        self.batterySignal = 4
        self.heartRateSignal = 3
        self.gsrSignal = 2
        self.bodyTempSignal = 1
        self.stmAddressByte = 1
        self.userName = ''
        self.password = ''
        self.connection = stm.stmConnection()
        self.pbSendData.setEnabled(False)
        
        self.pbHeartRate.clicked.connect(lambda: self.checkStoredHeartRateData())
        self.pbGSR.clicked.connect(lambda: self.checkGalvanicSkinResponseData())
        self.pbBodyTemp.clicked.connect(lambda: self.checkBodyTemperatureData())
        self.pbSendData.clicked.connect(lambda: self.onSendDataPbPress())
        
################################################################################################
def main():
    app = QApplication(sys.argv)
    form = DataCollectionScreen()
    form.show()
    sys.exit(app.exec_())
    
################################################################################################
if __name__ == "__main__":
    main()
