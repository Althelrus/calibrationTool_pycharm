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
        self.git_build = '0 '
        # ________________________________________________________

        # Check Bits
        self.calibration_bit = True
        self.salinity_bit = True

        # Start Main Window
        self.mainWindow = MainOverride()
        self.setupUi(self.mainWindow)
        # self.MainWindow.setWindowIcon(QtGui.QIcon(os.getcwd() + '/graphics/win_icon1.png')) #To add window icon
        self.logFrame.hide()
        self.loadingFrame.hide()
        self.settingFrame.hide()
        self.calibration_ask_frame.hide()
        self.salinity_ask_frame.hide()
        self.update_progress_bar(0)
        self.mainWindow.show()

        # Link Calibration Frame
        # self.sensor1_btn_2.clicked.connect()
        # self.sensor2_btn_2.clicked.connect()
        # self.sensor1_set_btn_2.clicked.connect()
        # self.sensor2_set_btn_2.clicked.connect()
        # self.lb1_input_sbox_2.text()
        # self.lb2_input_sbox_2.text()
        self.submit_calibration.clicked.connect(self.sub_cali)

        # Link Salinity Frame
        self.submit_salinity.clicked.connect(self.sub_sal)

        # Link Buttons
        self.start_calibration_btn.clicked.connect(self.start_test)
        self.recalibration_btn.clicked.connect(self.start_test)
        self.settings_btn.clicked.connect(self.show_setting)
        self.back_btn.clicked.connect(self.show_main_screen)  # Check sender to return person to correct screen

        # link Settings Buttons
        # self.set_calibration_weight_btn.clicked.connect(self.set_weight) # Calibration
        # self.set_calibration
        self.get_data_btn.clicked.connect(self.activate_localhost_download)
        self.sensor1_btn.clicked.connect(self.set_sensor)
        self.sensor2_btn.clicked.connect(self.set_sensor)
        self.screen_calibrate.clicked.connect(self.screen_calibrate_script)
        self.admin_btn.clicked.connect(self.admin_state)

        # Information Buttons
        self.actionAbout.triggered.connect(self.about)
        self.actionProcedure.triggered.connect(self.show_the_procedure)

        # Check Box Stats
        self.ask_for_salinity_state = True
        self.save_calibration_state = False
        self.foam_state = False

        # radio box states
        self.deep = True
        self.deep_constant = 34.9
        self.fresh = False
        self.fresh_constant = 0
        self.coastal = False
        self.coastal_constant = 31
        self.other = False
        self.current_salinity_level = 0
        self.set_salinity_state()

    def calibration_mode(self):
        pass

    def sub_cali(self):
        self.calibration_mode()
        self.calibration_bit = False
        time.sleep(1)
        self.calibration_ask_frame.hide()
        self.start_test()

    def sub_sal(self):
        self.check_box_state_update()
        self.salinity_bit = False
        time.sleep(1)
        self.salinity_ask_frame.hide()
        self.start_test()

    def set_salinity_state(self):
        self.salinity_cbox.setEnabled(self.ask_for_salinity_state)
        self.foam_cbox.setEnabled(self.foam_state)
        self.save_cailbration.setEnabled(self.foam_state)

        self.salinity_mode_1.setEnabled(self.deep)
        self.salinity_mode_2.setEnabled(self.fresh)
        self.salinity_mode_3.setEnabled(self.coastal)
        self.salinity_mode_4.setEnabled(self.other)

        self.salinity_mode_8.setEnabled(self.deep)
        self.salinity_mode_6.setEnabled(self.fresh)
        self.salinity_mode_5.setEnabled(self.coastal)
        self.salinity_mode_7.setEnabled(self.other)

    def check_box_state_update(self):
        self.ask_for_salinity_state = self.salinity_cbox.isChecked()
        self.foam_state = self.foam_cbox.isChecked()
        self.save_calibration_state = self.save_cailbration.isChecked()

        self.deep = self.salinity_mode_1.isChecked()
        self.fresh = self.salinity_mode_2.isChecked()
        self.coastal = self.salinity_mode_3.isChecked()
        self.other = self.salinity_mode_4.isChecked()

        self.deep = self.salinity_mode_8.isChecked()
        self.fresh = self.salinity_mode_6.isChecked()
        self.coastal = self.salinity_mode_5.isChecked()
        self.other = self.salinity_mode_7.isChecked()

        if self.deep:
            self.current_salinity_level = self.deep_constant
        if self.fresh:
            self.current_salinity_level = self.fresh_constant
        if self.coastal:
            self.current_salinity_level = self.coastal_constant
        if self.other:
            self.current_salinity_level = self.salinity_input_dsbox.text()

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
        self.mainFrame.show()
        self.logFrame.hide()
        self.calibration_ask_frame.hide()
        self.salinity_ask_frame.hide()
        self.loadingFrame.hide()
        self.settingFrame.hide()

    def start_test(self):
        self.mainFrame.hide()
        if self.calibration_bit:
            # Pop Message add next Version
            self.show_calibration_ask()
        elif self.salinity_bit:
            # Pop Message add next Version
            self.show_salinity_ask()
        else:
            self.show_loading()

    def show_calibration_ask(self):
        self.mainFrame.hide()
        self.calibration_ask_frame.show()
        self.salinity_ask_frame.hide()
        self.settingFrame.hide()
        self.logFrame.hide()
        self.loadingFrame.hide()

    def show_setting(self):
        self.mainFrame.hide()
        self.calibration_ask_frame.hide()
        self.salinity_ask_frame.hide()
        self.settingFrame.show()
        self.logFrame.hide()
        self.loadingFrame.hide()

    def show_salinity_ask(self):
        self.mainFrame.hide()
        self.calibration_ask_frame.hide()
        self.salinity_ask_frame.show()
        self.settingFrame.hide()
        self.logFrame.hide()
        self.loadingFrame.hide()

    def show_log(self):
        self.mainFrame.hide()
        self.logFrame.show()
        self.calibration_ask_frame.hide()
        self.salinity_ask_frame.hide()
        self.loadingFrame.hide()
        self.settingFrame.hide()
        # self.print_to_log()

    def show_loading(self):
        self.loadingFrame.show()
        self.update_progress_bar(0)
        for wait in range(0, 100, 1):
            time.sleep(0.01)
            self.update_progress_bar(wait)
        self.show_log()

    def print_to_log(self):
        pass

    def admin_state(self):
        pass

    def set_weight(self):
        pass

    def activate_localhost_download(self):
        pass

    def set_sensor(self):
        pass


