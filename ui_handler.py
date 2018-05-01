# By: Jonathan Ramirez
# Company: University of New Haven
#
# Import of basic System Functions
import sys
import os
import time
import logging
import subprocess
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
from UI.main_gui import Ui_MainWindow
from ui_util import ExtraUiFunctions
from balance_util import Balance


class MainOverride(QMainWindow):
    def closeEvent(self, event):
        result = QMessageBox.question(self,
                                            "Confirm Exit",
                                            "<b>Exit Balancing Test?",
                                            QMessageBox.Yes | QMessageBox.Cancel)
        event.ignore()

        if result == QMessageBox.Yes:
            event.accept()


class UIHandler(Ui_MainWindow, Balance, ExtraUiFunctions):
    app = QApplication(sys.argv)

    def __init__(self):
        super(Balance, self).__init__()

        # ________ P R O C E D U R E -- B U I L D -- R E V S _____
        self.version = '3.0'
        self.git_build = '5'
        # ________________________________________________________

        # Check Bits
        self.calibration_bit_left = True
        self.calibration_bit_right = True
        self.variable_bit = True
        self.last_frame = ""

        # Start Main Window
        self.mainWindow = MainOverride()
        self.setupUi(self.mainWindow)
        # self.MainWindow.setWindowIcon(QtGui.QIcon(os.getcwd() + '/graphics/win_icon1.png')) #To add window icon
        self.logFrame.hide()
        self.loadingFrame.hide()
        self.settingFrame.hide()
        self.calibration_ask_frame.hide()
        self.variable_adj_frame.hide()
        self.update_progress_bar(0)
        self.mainWindow.show()

        # todo commented objects from the gui for the sensor calibration
        # Link Calibration Frame
        self.sensor1_set_btn.clicked.connect(self.set_cali_weight)
        self.sensor2_set_btn.clicked.connect(self.set_cali_weight)
        self.sensor1_tare_btn.clicked.connect(self.set_tare)
        self.sensor2_tare_btn.clicked.connect(self.set_tare)
        self.submit_calibration.clicked.connect(self.sub_last)

        # Link Variables Frame
        self.submit_variables.clicked.connect(self.save_variables)

        # Link Buttons
        self.start_calibration_btn.clicked.connect(self.start_test)
        self.recalibration_btn.clicked.connect(self.start_test)
        self.settings_btn.clicked.connect(self.show_setting)
        self.back_btn.clicked.connect(self.show_main_screen)  # Check sender to return person to correct screen

        # link Settings Buttons
        self.get_data_btn.clicked.connect(self.activate_localhost_download)
        self.variable_adj_btn.clicked.connect(self.show_variable_ask)
        self.sensor_set_btn.clicked.connect(self.show_calibration_ask)
        self.screen_calibrate.clicked.connect(self.screen_calibrate_script)
        self.admin_btn.clicked.connect(self.admin_state)

        # Information Buttons
        self.actionAbout.triggered.connect(self.about)
        self.actionProcedure.triggered.connect(self.show_the_procedure)

        # Check Box Stats
        self.variable_ask_state = True
        self.save_calibration_state = True
        self.foam_state = False

        # TODO Coming Soon
        self.admin_btn.hide()
        self.get_data_btn.hide()

    def sub_last(self):
        print(self.last_frame)
        # self.save_cailbration()
        if self.last_frame == "main":
            self.start_test()
        elif self.last_frame == "settings":
            self.show_setting()
        else:
            print("Can not find last")

    def set_cali_weight(self):
        # print(self.last_frame)
        if self.lb1_input_sbox.text() != "0" or self.lb2_input_sbox.text() != "0":
            if self.mainWindow.sender().text() == "Set Left Weight":
                self.calibrate_sensor_left_max(int(self.lb1_input_sbox.text()))
                self.calibration_bit_left = False
                #self.set_left_slope()
                self.sensor1_set_btn.hide()
                self.lb1_input_sbox.hide()
            elif self.mainWindow.sender().text() == "Set Right Weight":
                self.calibrate_sensor_right_max(int(self.lb2_input_sbox.text()))
                self.calibration_bit_right = False
                #self.set_right_slope()
                self.sensor2_set_btn.hide()
                self.lb2_input_sbox.hide()
        else:
            self.pop_message("OK", "Need to change Weight")
            print("Not Set")

    def set_tare(self):
        if self.mainWindow.sender().text() == "Tare Left":
            self.calibrate_sensor_left_min()
            self.sensor1_tare_btn.hide()
        elif self.mainWindow.sender().text() == "Tare Right":
            self.calibrate_sensor_right_min()
            self.sensor2_tare_btn.hide()
        else:
            print("Not Set")

    def set_salinity_state(self):
        self.v_adj_cbox.setEnabled(self.variable_ask_state)
        self.foam_cbox.setEnabled(self.foam_state)
        self.save_cailbration.setEnabled(self.save_calibration_state)

    def check_box_state_update(self):
        self.variable_ask_state = self.v_adj_cbox.setEnabled.isChecked()
        self.foam_state = self.foam_cbox.isChecked()
        self.save_calibration_state = self.save_cailbration.isChecked()

    @staticmethod
    def screen_calibrate_script():
        subprocess.call(['./screen_calibration.sh'])

    def show_the_procedure(self):
        pn_num = "balance_procedure"
        self.show_procedure(pn_num)

    def about(self):
        QMessageBox.about(self.mainWindow, "About Balancing Test",
                                "<b>University of New Haven <br><br>"
                                "File Name: Balancing Test <br>Revision: {}<br>"
                                "Build: {}<br><br><i><u>"
                                "Copyright (c) 2017 UNH, All rights reserved"
                                .format(self.version, self.git_build))

    def update_progress_bar(self, value):
        self.calibration_progbar.setValue(value)

    def show_main_screen(self):
        self.last_frame = "main"
        self.mainFrame.show()
        self.logFrame.hide()
        self.calibration_ask_frame.hide()
        self.variable_adj_frame.hide()
        self.loadingFrame.hide()
        self.settingFrame.hide()

    def start_test(self):
        self.last_frame = "main"
        self.mainFrame.hide()
        if self.calibration_bit_left or self.calibration_bit_right:
            # Pop Message add next Version
            self.show_calibration_ask()
        elif self.variable_bit:
            # Pop Message add next Version
            self.show_variable_ask()
        else:
            self.show_loading()

    def show_calibration_ask(self):
        self.mainFrame.hide()
        self.calibration_ask_frame.show()
        self.variable_adj_frame.hide()
        self.settingFrame.hide()
        self.logFrame.hide()
        self.loadingFrame.hide()

    def show_setting(self):
        self.last_frame = "settings"
        self.mainFrame.hide()
        self.calibration_ask_frame.hide()
        self.variable_adj_frame.hide()
        self.settingFrame.show()
        self.logFrame.hide()
        self.loadingFrame.hide()

    def show_variable_ask(self):
        self.mainFrame.hide()
        self.calibration_ask_frame.hide()
        self.variable_adj_frame.show()
        self.settingFrame.hide()
        self.logFrame.hide()
        self.loadingFrame.hide()

    def save_variables(self):
        print("saving")
        self.b_engine_x = self.bep_input_dsbox.text()
        self.density = self.den_input_dsbox.text()
        self.variable_bit = False
        self.sub_last()

    def show_log(self):
        self.last_frame = "log"
        self.mainFrame.hide()
        self.logFrame.show()
        self.calibration_ask_frame.hide()
        self.variable_adj_frame.hide()
        self.loadingFrame.hide()
        self.settingFrame.hide()

    def show_loading(self):
        self.variable_adj_frame.hide()
        self.calibration_ask_frame.hide()
        self.last_frame = "loading"
        self.loadingFrame.show()
        self.update_progress_bar(0)
        for wait in range(0, 200, 1):
            time.sleep(0.01)
            self.update_progress_bar(wait)
        self.show_log()

    # todo allow quitting
    def admin_state(self):
        pass

    # todo make local host to download calibration settings
    def activate_localhost_download(self):
        pass

    # todo finish setters and getter for saving calibration settings
    def save_settings(self):
        pass

    def read_settings(self):
        pass


