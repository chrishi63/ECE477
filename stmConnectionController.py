#!usr/bin/python
import sys
import smbus
import time
import random
bus = smbus.SMBus(1)
deviceAddress = 0x10

class stmConnection():
    def __init__(self):
        self.sensorSignal = 0
    def sendDataByteToStm(self,sensor):
        self.sensorSignal = sensor
    
    def readDataByteFromStm(self):
        sleep(10)
        if self.sensorSignal is 2:
            return random.randint(58,103)
        if self.sensorSignal is 3:
            return random.randint(300,900)
        if self.sensorSignal is 4:
            return random.randint(361,372)/10
