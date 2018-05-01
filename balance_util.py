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
        self.x2_L = 0
        self.x2_R = 0
        self.y1 = 0
        self.y2 = 0

        # H-moment
        self.h_moment = 0
        self.m_x = 0

        self.gravity = 32.2
        self.n_volume = 3.576
        self.t_volume = 0

        # center of mass
        self.cm_x1 = 13.75
        self.cm_x2 = 54.75
        self.cm_Xcg = 0
        self.cm_mt = 0
        self.cm_m1 = 0
        self.cm_m2 = 0

        # center of buouancy
        self.Xcb = 0
        self.f_b = 0

        # bouyany force
        self.b_engine_x = 0  # -100 to 100 maps to +- 2.5 inches
        self.density = 1.99  # slug/ft^3
        self.pi = 3.14159265359
        self.b_engine_radius = 3.9375

    def b_engine_cal(self):
        self.t_volume = self.n_volume + (self.pi*self.b_engine_radius^2*(self.b_engine_x*0.0275))
        self.f_b = self.density * self.gravity * self.t_volume

    # ------------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    # Calibration Sensors
    # ------------------------------------------------------------------------------------------------------------------
    def calibrate_sensor_left_min(self):
        self.x1_L = self.get_load_cell_left()
        self.y1 = 0

    def calibrate_sensor_left_max(self, weight):
        self.x2_L = self.get_load_cell_left()
        self.y2 = weight

    def set_left_slope(self):
        self.slope_L = self.find_slope(self.y2, self.y1, self.x2_L, self.x1_L)

    def calibrate_sensor_right_min(self):
        self.x1_R = self.get_load_cell_right()
        self.y1 = 0

    def calibrate_sensor_right_max(self, weight):
        self.x2_R = self.get_load_cell_right()
        self.y2 = weight

    def set_right_slope(self):
        self.slope_R = self.find_slope(self.y2, self.y1, self.x2_R, self.x1_R)

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
        self.cm_Xcg = (self.cm_m1 * self.cm_x1 + self.cm_m2 * self.cm_x2) / self.cm_mt

    def moment_balance(self):
        self.m_x = self.cm_Xcg*self.cm_mt - self.Xcb*self.f_b

    def calc_h_moment(self):
        pass

