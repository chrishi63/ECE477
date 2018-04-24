#!usr/bin/python
import sys
import time

import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
import datacollection_auto as dataUi
import serverConnectionController as server
import stmConnectionController as stm

class DataCollectionScreen(QMainWindow, dataUi.Ui_DataCollection):
    ############################################################################################
    def clearData(self):
        self.heartRate = 0
        self.gsr = 0
        self.bodyTemp = 0
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        
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
        if self.label_2.text() is not "":
            if self.userChoosesToOverrideHeartRateData():
                self.messageText.setText("Measuring Heart Rate")
                self.measureHeartRate()
        else:
            self.messageText.setText("Measuring Heart Rate")
            self.measureHeartRate()
            
    ############################################################################################
    def checkBodyTemperatureData(self):
        if self.label_4.text() is not "":
            if self.userChoosesToOverrideBodyTemperatureData():
                self.measureBodyTemperature()
        else:
            self.measureBodyTemperature()
            
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
        if self.stmAddressByte is 0:
            self.heartRate = self.heartRate + 1
            self.label_2.setText(str(self.heartRate))
        else:
            self.disablePushButtons()
            connection = stm.stmConnection()
            self.connection.signalSensorToSTM(self.heartRateSignal)
            QTimer.singleShot(10000,self.getHeartRateFromSTM)
            
    ############################################################################################
    def measureBodyTemperature(self):
        if self.stmAddressByte is 0:
            self.bodyTemp = self.bodyTemp + 1
            self.label_4.setText(str(self.bodyTemp))
        else:
            self.disablePushButtons()
            self.connection.signalSensorToSTM(self.bodyTempSignal)
            QTimer.singleShot(10000,self.getBodyTempFromSTM)
        
    ############################################################################################
    def measureGalvanicSkinResponse(self):
        if self.stmAddressByte is 0:
            self.gsr = self.gsr + 1
        else:
            self.disablePushButtons()
            self.connection.signalSensorToSTM(self.gsrSignal)
            QTimer.singleShot(10000,self.getGSRFromSTM)
        
    ############################################################################################
    def getBodyTempFromSTM(self):
        self.bodyTemp = self.connection.readSensorData()
        self.updateGUIAfterDataReceived()
    ############################################################################################
    def getHeartRateFromSTM(self):
        self.heartRate = self.connection.readSensorData()
        self.updateGUIAfterDataReceived()
    ############################################################################################
    def getGSRFromSTM(self):
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
        self.messageText.setText("")
        self.pbHeartRate.setEnabled(True)
        self.pbGSR.setEnabled(True)
        self.pbBodyTemp.setEnabled(True)
        if self.gsr > 0:
            self.label_3.setText(str(self.gsr))
        if self.bodyTemp > 0:
            print(self.bodyTemp)
            self.label_4.setText(str(self.bodyTemp))
        if self.heartRate > 0:
            self.label_2.setText(str(self.heartRate))
        self.updatePbEnable()
        self.connection.resumeCollectingBatteryData()
        
    ############################################################################################
    def updatePbEnable(self):
        if (self.heartRate * self.gsr * self.bodyTemp) > 0:
            self.pbSendData.setEnabled(True)
        else:
            self.pbSendData.setEnabled(False)
    def batteryDataAvailable(self):
        if self.connection.stopRequestingBatteryData is 1:
            return False
        else:
            self.connection.signalSensorToSTM(self.batterySignal)
            self.batteryLevel = self.connection.readSensorData()
            return self.batteryLevel
        
    ############################################################################################
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.heartRate = 0
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
