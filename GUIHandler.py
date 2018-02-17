# By: Jonathan Ramirez
# Company: University of New Haven

# Import of basic System Functions
import sys
import os
import time
import logging

from PyQt4 import QtGui
from UI.main_gui import Ui_MainWindow
from UiFunctions import ExtraUiFunctions
from main import Balance


class MainOverride(QtGui.QMainWindow):
    def closeEvent(self, event):
        result = QtGui.QMessageBox.question(self,
                                            "Confirm Exit",
                                            "<b>Exit Balancing Test?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.Cancel)
        event.ignore()

        if result == QtGui.QMessageBox.Yes:
            event.accept()


class UIHandler(Ui_MainWindow, Balance, ExtraUiFunctions):
    app = QtGui.QApplication(sys.argv)

    def __init__(self):
        super(Balance, self).__init__()

        # ________ P R O C E D U R E -- B U I L D -- R E V S _____
        self.version = '0.1'
        self.git_build = '0 '
        # ________________________________________________________

        # Start Main Window
        self.mainWindow = MainOverride()
        self.setupUi(self.mainWindow)
        # self.MainWindow.setWindowIcon(QtGui.QIcon(os.getcwd() + '/graphics/win_icon1.png')) #To add window icon
        self.logFrame.hide()
        self.loadingFrame.hide()
        self.settingFrame.hide()
        self.update_progress_bar(0)
        self.mainWindow.show()

        # Link Buttons
        self.start_calibration_btn.clicked.connect(self.start_test)
        self.recalibration_btn.clicked.connect(self.start_test)
        self.settings_btn.clicked.connect(self.show_setting)
        self.back_btn.clicked.connect(self.show_main_screen)

        # Information Buttons
        self.actionAbout.triggered.connect(self.about)
        self.actionProcedure.triggered.connect(self.show_the_procedure)

    def show_the_procedure(self):
        pn_num = "balance_procedure"
        self.show_procedure(pn_num)

    def about(self):
        QtGui.QMessageBox.about(self.mainWindow, "About Balancing Test",
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
        self.loadingFrame.hide()
        self.settingFrame.hide()

    def start_test(self):
        self.mainFrame.hide()
        self.loadingFrame.show()
        self.show_loading()

    def show_setting(self):
        self.mainFrame.hide()
        self.settingFrame.show()

    def show_log(self):
        self.mainFrame.hide()
        self.logFrame.show()
        self.loadingFrame.hide()
        self.settingFrame.hide()

    def show_loading(self):
        self.update_progress_bar(0)
        self.print_to_log(self.do_calculation())
        for wait in range(0, 100, 1):
            time.sleep(0.01)
            self.update_progress_bar(wait)
        self.show_log()

    def print_to_log(self, balancing_info):
        pass


if __name__ == '__main__':
    QtGui.QApplication.setStyle('cleanlooks ')
    ex_main = UIHandler()
    # print help(ex_main)
    # print '----------------'
    sys.exit(UIHandler.app.exec_())