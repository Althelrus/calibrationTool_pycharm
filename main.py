# By: Jonathan Ramirez
# Company: University of New Haven

# Import of basic System Functions
import sys
import os
import time
import logging

# GUI Imports
from PyQt4 import QtGui
from GUIHandler import UIHandler


# Other


class Balance(UIHandler):
    # ________ P R O C E D U R E -- B U I L D -- R E V S _____
    version = '0.1'
    git_build = '0 '
    # ________________________________________________________
    app = QtGui.QApplication(sys.argv)

    def __init__(self):
        super(Balance, self).__init__()
        self.start_calibration_btn.clicked.connect(self.start_test)
        self.recalibration_btn.clicked.connect(self.start_test)
        self.settings_btn.clicked.connect(self.show_setting)
        self.back_btn.clicked.connect(self.show_main_screen)

    def show_main_screen(self):
        self.mainFrame.show()
        self.logFrame.hide()
        self.loadingFrame.hide()
        self.settingFrame.hide()

    def start_test(self):
        self.mainFrame.hide()
        self.loadingFrame.show()
        self.calculation()

    def show_setting(self):
        self.mainFrame.hide()
        self.settingFrame.show()

    def show_log(self):
        self.mainFrame.hide()
        self.logFrame.show()
        self.loadingFrame.hide()
        self.settingFrame.hide()

    def calculation(self):
        self.update_progress_bar(0)
        for wait in range(0, 100, 1):
            time.sleep(0.01)
            self.update_progress_bar(wait)
        self.show_log()


if __name__ == '__main__':
    QtGui.QApplication.setStyle('cleanlooks ')
    ex_main = Balance()
    # print help(ex_main)
    # print '----------------'
    sys.exit(Balance.app.exec_())