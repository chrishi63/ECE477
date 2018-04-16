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
    return bus.read_byte_data(address, 1)
############################################################################################
if __name__ == "__main__":
    deviceAddress = 0x10 
    sendDataByteThroughI2C(deviceAddress, 1)
    print("first data byte sent")
    #sendDataByteThroughI2C(deviceAddress, 2)

    print(readDataByteFromI2C(deviceAddress))
    
    
