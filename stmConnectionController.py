#!usr/bin/python
import sys
import time
import random

class stmConnection():
    def __init__(self):
        self.sensorSignal = 0
        self.batteryLevel = 100
        self.stopRequestingBatteryData = 0
    def resumeCollectingBatteryData(self):
        self.stopRequestingBatteryData = 0
        
    def signalSensorToSTM(self,sensor):
        if sensor is not 4:
            self.stopRequestingBatteryData = 1
            self.sensorSignal = sensor
        elif self.stopRequestingBatteryData is 0:
            self.sensorSignal = sensor
        else:
            pass
        
    def readSensorData(self):
        if self.sensorSignal is 3:
            return random.randint(58,103)
        if self.sensorSignal is 2:
            return random.randint(300,900)
        if self.sensorSignal is 1:
            return random.randint(361,372)/10
        if self.sensorSignal is 4:
            self.batteryLevel = self.batteryLevel - 1
            return self.batteryLevel
