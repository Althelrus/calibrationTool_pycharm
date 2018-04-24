# By: Jonathan Ramirez
# Company: University of New Haven

# Import of basic System Functions
import sys
import os
import time
import logging
from loadCell_util.ABE_ADCPi import ADCPi
from loadCell_util.ABE_helpers import ABEHelpers

# Shared UI functions
from ui_handler import ExtraUiFunctions

class Balance(ExtraUiFunctions):
    def __init__(self):
        self.calibration_bit = False

        i2c_helper = ABEHelpers()
        bus = i2c_helper.get_smbus()
        self.adc = ADCPi(bus, 0x68, 0x69, 18)
        self.LS_pin = 5
        self.RS_pin = 8

        # Slope
        self.slope_L = 0
        self.slope_R = 0
        self.x1_L = 0
        self.x1_R = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0

        # H-moment
        self.h_moment = 0

        # center of mass
        self.cm_x1 = 2
        self.cm_x2 = 6
        self.cm_Xcm = 0
        self.cm_mt = 0
        self.cm_m1 = 0
        self.cm_m2 = 0

        # center of buouancy
        self.bCenter = 0
        self.mt = 0
        self.Xbm = 4

    def do_calculation(self):
        self.get_load_cell_left()
        self.get_load_cell_right()
        self.Xcm = self.find_center_of_mass()
        self.bCenter = self.find_center_of_buoyancy()
        self.h_moment = self.calc_h_moment()
        return self.to_string()

    def to_string(self):
        if self.h_moment > .5:
            return "Add " + self.find_calibration_weight() + " ounces to the forward"
        elif self.h_moment < .5:
            return "Add " + self.find_calibration_weight() + " ounces to the back"
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    # Calibration Sensors
    # ------------------------------------------------------------------------------------------------------------------
    def calibrate_sensor_left_min(self, weight):
        self.x1_L = self.get_load_cell_left()
        self.y1 = weight

    def calibrate_sensor_left_max(self, weight):
        self.x2 = self.get_load_cell_left()
        self.y2 = weight

    def set_left_slope(self):
        self.slope_L = self.find_slope(self.y2, self.y1, self.x2, self.x1_L)

    def calibrate_sensor_right_min(self, weight):
        self.x1_R = self.get_load_cell_right()
        self.y1 = weight

    def calibrate_sensor_right_max(self, weight):
        self.x2 = self.get_load_cell_right()
        self.y2 = weight

    def set_right_slope(self):
        self.slope_R = self.find_slope(self.y2, self.y1, self.x2, self.x1_R)

    def find_slope(self, y2, y1, x2, x1):
        return (y2 - y1)/(x2 - x1)
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    # Read Sensors
    # ------------------------------------------------------------------------------------------------------------------
    def get_load_cell_left(self):
        return self.adc.read_voltage(self.LS_pin)

    def get_load_cell_right(self):
        return self.adc.read_voltage(self.RS_pin)
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    # Get Sensor Weight (Only After Calibration
    # ------------------------------------------------------------------------------------------------------------------
    def get_left_weight(self):
        return self.slope_L*(self.get_load_cell_left()-self.x1_L)

    def get_right_weight(self):
        return self.slope_R*(self.get_load_cell_right()-self.x1_R)
    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    # CM/CB calculation
    # ------------------------------------------------------------------------------------------------------------------
    def find_center_of_buoyancy(self):
        pass

    def find_center_of_mass(self):
        self.cm_m1 = self.get_left_weight()
        self.cm_m2 = self.get_right_weight()
        self.cm_mt = self.cm_m1 + self.cm_m2
        self.cm_Xcm = (self.cm_m1 * self.mt + self.cm_m2 * self.mt) / self.mt

    def calc_h_moment(self):
        return abs(self.bCenter-self.Xcm)

