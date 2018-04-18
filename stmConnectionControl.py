#!usr/bin/python
import sys
import smbus
import time
bus = smbus.SMBus(1)
deviceAddress = 0x10

class stmConnection():
    def __init__(self):
        self.sensorSignal = 0
    def signalSensorToSTM(sensor):
        self.sensorSignal = sensor
        bus.write_byte(deviceAddress, sensor)
        return
    def readSensorData():
        time.sleep(15)
        if self.sensorSignal is 1:
            top = readDataByteFromI2C(deviceAddress)
            bot = readDataByteFromI2C(deviceAddress)
            return str(top) + '.' + str(bot)
        else:
            topNum = bin(readDataByteFromI2C(deviceAddress))
            botNum = bin(readDataByteFromI2C(deviceAddress))
            return (int(topNum.split('b')[1] + botNum.split('b')[1],2))
