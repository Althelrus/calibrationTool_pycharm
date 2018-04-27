import sys
from PyQt5.QtWidgets import QApplication
from ui_handler import UIHandler

if __name__ == '__main__':
    # QApplication.setStyle('cleanlooks ')
    ex_main = UIHandler()
    # print help(ex_main)
    # print '----------------'
    sys.exit(UIHandler.app.exec_())