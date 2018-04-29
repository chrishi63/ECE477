#!usr/bin/python
import sys
import os
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
    wait_5()
    sendDataByteThroughI2C(deviceAddress, 1)
    top = readDataByteFromI2C(deviceAddress)
    bot = readDataByteFromI2C(deviceAddress)
    #print(top)
    #print(bot/100)
    #tempVal = float(top+(bot/100))
    
    #print(tempVal)
    #tempVal = str(round(tempVal,2))
    #print(type(tempVal))
    return str(top) + '.' + str(bot)
    #return tempVal
    

def getGSC(address):
    sendDataByteThroughI2C(deviceAddress, 2)
    wait_5()
    sendDataByteThroughI2C(deviceAddress, 2)
    topNum = bin(readDataByteFromI2C(deviceAddress))
    botNum = bin(readDataByteFromI2C(deviceAddress))
    return (int(topNum.split('b')[1] + botNum.split('b')[1],2))

def getPulse(address):
    sendDataByteThroughI2C(deviceAddress, 3)
    wait_10()
    sendDataByteThroughI2C(deviceAddress, 3)
    topNum = bin(readDataByteFromI2C(deviceAddress))
    botNum = bin(readDataByteFromI2C(deviceAddress))
    return (int(topNum.split('b')[1] + botNum.split('b')[1],2))

def getBatteryVoltage(address):
    sendDataByteThroughI2C(deviceAddress, 4)
    topNum = bin(readDataByteFromI2C(deviceAddress))
    botNum = bin(readDataByteFromI2C(deviceAddress))
    newNum = int('0b' + topNum.split('b')[1] + botNum.split('b')[1][0:3],2)
    #print(newNum)
    floatNum = round(((.00976 * newNum) / 7) * 100)
    return floatNum

def wait_10():
    timer_a = time.time()
    timer_b = time.time()
    #print(timer_a)
    #print(timer_b)
    while True:
        a = round((time.time() - timer_a),2)
        if (a == 11.0) or (a == 11.00):
            return ('11 seconds')
def wait_5():
    timer_a = time.time()
    timer_b = time.time()
    #print(timer_a)
    #print(timer_b)
    while True:
        a = round((time.time() - timer_a),2)
        #print(a)
        if (a == 6.0) or (a == 6.00) or (a == 6.01) or (a == 6.02):
            return ('6 seconds')
def wait_2():
    timer_a = time.time()
    timer_b = time.time()
    #print(timer_a)
    #print(timer_b)
    while True:
        a = round((time.time() - timer_a),2)
        #print(a)
        if (a == 2.0) or (a == 6.00) or (a == 2.01) or (a == 2.02):
            return ()

############################################################################################
if __name__ == "__main__":
    deviceAddress = 0x0a
    #try:
    #    print(getTemperature(deviceAddress))
    #except:
    #        wait_2()
    #        print("Error occured earlier")
    #        print(getTemperature(deviceAddress))
    print(str(getBatteryVoltage(deviceAddress)) + '%')
    #print(wait_2())
   # print(getTemperature(deviceAddress))
    #print(getGSC(deviceAddress))
    #print(getPulse(deviceAddress))
    #sendDataByteThroughI2c()
    #Wait 15 seconds
    #sendDataByteThroughI2C()
    #readDataByte()
    #readDataByte()
    #print(wait_5())

    
