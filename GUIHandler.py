#By: Jonathan Ramirez
#Company: University of New Haven

from PyQt4 import QtGui
from UI.main_gui import Ui_MainWindow


class MainOverride(QtGui.QMainWindow):
    def closeEvent(self, event):
        result = QtGui.QMessageBox.question(self,
                                            "Confirm Exit",
                                            "<b>Exit Balancing Test?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.Cancel)
        event.ignore()

        if result == QtGui.QMessageBox.Yes:
            event.accept()


class UIHandler(Ui_MainWindow):

    def __init__(self):
        self.mainWindow = MainOverride()
        self.setupUi(self.mainWindow)
        # self.MainWindow.setWindowIcon(QtGui.QIcon(os.getcwd() + '/graphics/win_icon1.png')) #To add window icon
        self.logFrame.hide()
        self.loadingFrame.hide()
        self.settingFrame.hide()
        self.update_progress_bar(0)
        self.mainWindow.show()

    def about(self):
        QtGui.QMessageBox.about(self.MainWindow, "About Balancing Test",
                                "<b>University of New Haven <br><br>"
                                "File Name: Balancing Test <br>Revision: {}<br>"
                                "Build: {}<br><br><i><u>"
                                "Copyright (c) 2017 UNH, All rights reserved"
                                .format(self.version, self.git_build))

    def update_progress_bar(self, value):
        self.calibration_progbar.setValue(value)
