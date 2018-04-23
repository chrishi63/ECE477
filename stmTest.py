#!usr/bin/python
import sys
#For i2c: (GPIO8 (pin 3) -> SDA GPI09 (pin 5) -> SCL)
import smbus
import time
bus = smbus.SMBus(1) #(1) because using I2C1 port

############################################################################################    
def sendDataByteThroughI2C(address, dataByte):
    bus.write_byte(address, dataByte)
    return
############################################################################################
def readDataByteFromI2C(address):
    #dataAvailable = 0
    #while dataAvailable is 0:
    #    dataAvailable = bus.read_byte_data(address, 1)
    #return dataAvailable
    return bus.read_byte(address)

def getTemperature(address):
    sendDataByteThroughI2C(deviceAddress, 1)
    top = readDataByteFromI2C(deviceAddress)
    bot = readDataByteFromI2C(deviceAddress)
    return str(top) + '.' + str(bot)
    

def getGSC(address):
    sendDataByteThroughI2C(deviceAddress, 2)
    topNum = bin(readDataByteFromI2C(deviceAddress))
    botNum = bin(readDataByteFromI2C(deviceAddress))
    return (int(topNum.split('b')[1] + botNum.split('b')[1],2))

def getPulse(address):
    sendDataByteThroughI2C(deviceAddress, 3)
    topNum = bin(readDataByteFromI2C(deviceAddress))
    botNum = bin(readDataByteFromI2C(deviceAddress))
    return (int(topNum.split('b')[1] + botNum.split('b')[1],2))
        

############################################################################################
if __name__ == "__main__":
    deviceAddress = 0x0a 
    print(getTemperature(deviceAddress))
    #print(getGSC(deviceAddress))
    #print(getPulse(deviceAddress))
