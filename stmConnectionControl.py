#!usr/bin/python
import sys
import smbus
import time
bus = smbus.SMBus(1)
deviceAddress = 0x10

class stmConnection():
    def sendDataByteToStm(dataByte):
        bus.write_byte(deviceAddress, dataByte)
        return
    
    def readDataByteFromStm():
        dataAvailable = 0
        while dataAvailable is 0:
            dataAvailable = bus.read_byte_data(deviceAddress, 1)
        return dataAvailable
