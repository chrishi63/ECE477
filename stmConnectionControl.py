#!usr/bin/python
import sys
import smbus
import time
bus = smbus.SMBus(1)
deviceAddress = 0x10

class stmConnection():
    def __init__(self):
        self.sensorSignal = 0
        self.stopRequestingBatteryData = 0
    def signalSensorToSTM(self,sensor):
        if sensor is not 4:
            self.stopRequestingBatteryData = 1
            self.sensorSignal = sensor
            bus.write_byte(deviceAddress, sensor)
        else:
            if self.stopRequestingBatteryData is 0:
                self.sensorSignal = sensor
                bus.write_byte(deviceAddress, sensor)
        return
    
    def readSensorData():
        if self.sensorSignal is 1:
            top = readDataByteFromI2C(deviceAddress)
            bot = readDataByteFromI2C(deviceAddress)
            return str(top) + '.' + str(bot)
        elif self.sensorSignal is 2 or 3:
            topNum = bin(readDataByteFromI2C(deviceAddress))
            botNum = bin(readDataByteFromI2C(deviceAddress))
            return (int(topNum.split('b')[1] + botNum.split('b')[1],2))
        else:
            batteryLevel = readDataByteFromI2C(deviceAddress)
            return int(batteryLevel)
