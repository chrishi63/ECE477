#!usr/bin/python
import sys
import smbus
import time
bus = smbus.SMBus(1)
deviceAddress = 0x0a

class stmConnection():
    def __init__(self):
        self.sensorSignal = 0
        self.stopRequestingBatteryData = 0
    def signalSensorToSTM(self,sensor):
        if sensor is not 4:
            print("Requesting data from sensor #")
            print(sensor)
            self.stopRequestingBatteryData = 1
            self.sensorSignal = sensor
            bus.write_byte(deviceAddress, sensor)
        else:
            if self.stopRequestingBatteryData is 0:
                self.sensorSignal = sensor
                bus.write_byte(deviceAddress, sensor)
        return
    
    def readSensorData(self):
        if self.sensorSignal is 1:
            print(self.sensorSignal)
            print("Collecting temperature data")
            top = bus.read_byte(deviceAddress)
            bot = bus.read_byte(deviceAddress)
            return float(str(top) + '.' + str(bot))
        elif self.sensorSignal is 2 or 3:
            print("Collecting data from sensor:")
            print(self.sensorSignal)
            topNum = bin(bus.read_byte(deviceAddress))
            botNum = bin(bus.read_byte(deviceAddress))
            return (int(topNum.split('b')[1] + botNum.split('b')[1],2))
        else:
            batteryLevel = bus.read_byte(deviceAddress)
            return int(batteryLevel)
