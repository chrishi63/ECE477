#!usr/bin/python
import sys
#For i2c: (GPIO8 (pin 3) -> SDA GPI09 (pin 5) -> SCL)
import smbus
import time
bus = smbus.SMBus(1) #(1) because using I2C1 port
##deviceAddress = 0x (check address using sudo i2cdetect -y 1)


import PyQt5
from PyQt5.QtWidgets import *

import datacollection_auto as dataUi
import serverConnectionController as server

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
        if (self.heartRate * self.gsr * self.bodyTemp) is 0:
            emptyMeasurementsPrompt = QMessageBox()
            ##emptyMeasurementsPrompt.setIcon(QMessageBox.Question)
            emptyMeasurementsPrompt.setText("Empty Data Entries")
            emptyMeasurementsPrompt.setInformativeText("Please take all measurements \
before attempting to send data to server")        
            emptyMeasurementsPrompt.show()
            print("empty")
            return False
        if (self.sendingDataToServerFails()):
            # make a popup window that send data sending failed
            clearDataPrompt = QMessageBox()
            #clearDataPrompt.setIcon(QMessageBox.Question)
            clearDataPrompt.setText("Sending Data To Server Failed")
            #clearDataPrompt.setInformativeText(informativeText)        
            #clearDataPrompt.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            clearDataPrompt.show()
            print("failed sending data to server")
            return False
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
    def sendDataByteThroughI2C(self, address, dataByte):
        bus.write_byte(address, dataByte)
        return
    
    ############################################################################################    
    def sendDataByteToStm(self, dataByte):
##        bus.write_byte(self.stmAddressByte, 10)
        self.sendDataByteThroughI2C(self.stmAddressByte, dataByte)
        return
    
    ############################################################################################
    def readDataByteFromI2C(self, address):
        dataAvailable = 0
        while dataAvailable is 0:
            dataAvailable = bus.read_byte_data(address, 1)
        return dataAvailable
    
    ############################################################################################
    def readDataByteFromStm(self):
        return self.readDataByteFromI2C(self.stmAddressByte)
    
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
        elif sensor is 2:
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
        return self.promptsUserToOverrideData(2)
    
    ########################################################################################
    def userChoosesToOverrideBodyTemperatureData(self):
        return self.promptUserToOverrideData(3)
    
    ############################################################################################
    def checkStoredHeartRateData(self):
        if self.label_2.text() is not "":
            if self.userChoosesToOverrideHeartRateData():
                self.measureHeartRate()
            else:
                pass
        else:
            self.measureHeartRate()
            
    ############################################################################################
    def checkBodyTemperatureData(self):
        if self.label_4.text() is not "":
            if self.userChoosesToOverrideGSRData():
                self.measureBodyTemperare()
        else:
            self.measureBodyTemperature()
            
    ############################################################################################
    def checkGalvanicSkinResponseData(self):
        if self.label_3.text() is not "":
            if self.userChoosesToOverrideBodyTemperatureData():
                self.measureGalvanicSkinResponse()
        else:
            self.measureGalvanicSkinResponse()
            
    ############################################################################################
    def measureHeartRate(self):
        if self.stmAddressByte is 0:
            self.heartRate = self.heartRate + 1
        else:
            measuringPrompt = QMessageBox()
            measuringPrompt.setText("Measuring Heart Rate")
            measuringPrompt.show()
            self.sendDataByteToStm(self.heartRateSignal)
##            time.sleep(5)
            #may need to add a delay to raspberry pi here to prevent connection time out
            self.heartRate = self.readDataByteFromStm()
        #disable other pushbuttons
        #send data byte signaling heart rate to stm:
##        self.sendDataByteToStm(self.heartRateSignal)
        #read data from stm
##        self.heartRate = readDataByteFromStm(self)
        #display data on screen
##        self.label_2.setText(str(self.heartRate))
            measuringPrompt.hide()
        self.label_2.setText(str(self.heartRate))
        #reenable other pushbuttons
        
    ############################################################################################
    def measureBodyTemperature(self):
        if self.stmAddressByte is 0:
            self.bodyTemp = self.bodyTemp + 1
        else:
            measuringPrompt = QMessageBox()
            measuringPrompt.setText("Measuring Body Temperature")
            measuringPrompt.show()
            self.sendDataByteToStm(self.bodyTempSignal)
##            time.sleep(5)
            self.bodyTemp = self.readDataByteFromStm()
            measuringPrompt.hide()
        #send body temperature signal to stm
        #wait for data from stm
        self.label_4.setText(str(self.bodyTemp))
        
    ############################################################################################
    def measureGalvanicSkinResponse(self):
        if self.stmAddressByte is 0:
            self.gsr = self.gsr + 1
        else:
            measuringPrompt = QMessageBox()
            measuringPrompt.setText("Measuring Galvanic Skin Response")
            measuringPrompt.show()
            self.sendDataByteToStm(self.gsrSignal)
##            time.sleep(5)
            self.gsr = self.readDataByteFromStm()
            measuringPrompt.hide()
        #send gsr signal to stm
        #wait for data from stm    
        self.label_3.setText(str(self.gsr))
        
    ############################################################################################
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.heartRate = 0
        self.gsr = 0
        self.bodyTemp = 0
        self.stmAddressByte = 0x0 #<- change this
        self.heartRateSignal = 2
        self.gsrSignal = 3
        self.bodyTempSignal = 4
        self.userName = ''
        self.password = ''
        
        #button functionality:
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
