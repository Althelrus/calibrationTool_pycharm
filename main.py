
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_handler import UIHandler

if __name__ == '__main__':
    QtGui.QApplication.setStyle('cleanlooks ')
    ex_main = UIHandler()
    # print help(ex_main)
    # print '----------------'
    sys.exit(UIHandler.app.exec_())