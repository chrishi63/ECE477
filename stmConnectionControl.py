#!usr/bin/python
import sys
import smbus
import time
bus = smbus.SMBus(1)
deviceAddress = 0x0a
import stmConnectionController as stm

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
            try:
                bus.write_byte(deviceAddress, sensor)
            except:
                print("STM write Error")
                try:
                    bus.write_byte(deviceAddress,sensor)
                except:
                    print("STM write Error")
                    try:
                        bus.write_byte(deviceAddress,sensor)
                    except:
                        print("STM write Error")
                        bus.write_byte(deviceAddress,sensor)
                        return
        else:
            if self.stopRequestingBatteryData is 0:
                print("Requesting Battery Data")
                self.sensorSignal = sensor
                try:
                    bus.write_byte(deviceAddress, sensor)
                except:
                    print("STM write Error")
                    try:
                        bus.write_byte(deviceAddress,sensor)
                    except:
                        print("STM write Error")
                        bus.write_byte(deviceAddress,sensor)
                        return
            else:
                print("Cannot Request Battery Data")
        return
    
    def readSensorData(self):
        print("Reading sensor data from Sensor:")
        print(self.sensorSignal)
        if self.sensorSignal is 1:
            print("Reading 1")
            try:
                top = bus.read_byte(deviceAddress)
                bot = bus.read_byte(deviceAddress)
                return float(str(top) + '.' + str(bot))
            except:
                print("STM Read Error 1")
                try:
                    top = bus.read_byte(deviceAddress)
                    bot = bus.read_byte(deviceAddress)
                    return float(str(top) + '.' + str(bot))
                except:
                    print("STM Read Error 2")
                    return False
        elif self.sensorSignal is 2 or self.sensorSignal is 3:
            print("Reading 2 or 3")
            try:
                topNum = bin(bus.read_byte(deviceAddress))
                botNum = bin(bus.read_byte(deviceAddress))
                return (int(topNum.split('b')[1] + botNum.split('b')[1],2))
            except:
                print("STM Read Error 1")
                try:
                    topNum = bin(bus.read_byte(deviceAddress))
                    botNum = bin(bus.read_byte(deviceAddress))
                    return (int(topNum.split('b')[1] + botNum.split('b')[1],2))
                except:
                    print("STM Read Error 2")
                    return False
        elif self.sensorSignal is 4:
            print("Reading Battery Data")
            topNum = bin(bus.read_byte(deviceAddress))
            botNum = bin(bus.read_byte(deviceAddress))
            newNum = int('0b' + topNum.split('b')[1] + botNum.split('b')[1][0:3],2)
            floatNum = round(((.00976 * newNum) / 7) * 100)
            print(str(floatNum) + '%')
            return floatNum
        else:
            return False
