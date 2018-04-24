#!/usr/bin/python3
# By: Jonathan Ramirez
# Company: University of New Haven

import sys
import os
import time
from loadCell_util.ABE_ADCPi import ADCPi
from loadCell_util.ABE_helpers import ABEHelpers


class ADC_TEST:
    def __init__(self):
        # Left              Pins
        #self.sensorL_p = 0  #5
        #self.sensorL_n = 0  #4
        # Right
        #self.sensorR_p = 0  #8
        #self.sensorR_n = 0  #7

        #init of adc
        i2c_helper = ABEHelpers()
        bus = i2c_helper.get_smbus()
        self.adc = ADCPi(bus, 0x68, 0x69, 18)

    def get_info(self):
        self.print_data()

    def print_data(self):
        # read from adc channels and print to screen
        print(" ")
        #print ("SensorLP: %03f" % self.adc.read_voltage(5))
        print("SensorLP: %02f" % self.adc.read_voltage(5))
        
        # wait 0.5 seconds before reading the pins again
        time.sleep(0.5)
        
        print("SensorRP: %03f" % self.adc.read_voltage(8))
        #print ("SensorRN: %02f" % self.adc.read_voltage(7))
        print(" ")
        
        # wait 0.5 seconds before reading the pins again
        time.sleep(0.5)
        
        
if __name__ == '__main__':
    temp = ADC_TEST()
    
    for x in range(0, 100):
        temp.get_info()

