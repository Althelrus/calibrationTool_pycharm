# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\jonramirez\Desktop\TempFiles\Pyproject\UI\main_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1007, 704)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.settings_btn = QtGui.QPushButton(self.centralwidget)
        self.settings_btn.setGeometry(QtCore.QRect(330, 10, 75, 71))
        self.settings_btn.setObjectName(_fromUtf8("settings_btn"))
        self.start_calibration_btn = QtGui.QPushButton(self.centralwidget)
        self.start_calibration_btn.setGeometry(QtCore.QRect(30, 100, 381, 171))
        self.start_calibration_btn.setObjectName(_fromUtf8("start_calibration_btn"))
        self.boyuancy_data_btn = QtGui.QPushButton(self.centralwidget)
        self.boyuancy_data_btn.setGeometry(QtCore.QRect(60, 60, 161, 81))
        self.boyuancy_data_btn.setObjectName(_fromUtf8("boyuancy_data_btn"))
        self.sensor2_btn = QtGui.QPushButton(self.centralwidget)
        self.sensor2_btn.setGeometry(QtCore.QRect(60, 150, 161, 81))
        self.sensor2_btn.setObjectName(_fromUtf8("sensor2_btn"))
        self.sensor1_btn = QtGui.QPushButton(self.centralwidget)
        self.sensor1_btn.setGeometry(QtCore.QRect(240, 60, 161, 81))
        self.sensor1_btn.setObjectName(_fromUtf8("sensor1_btn"))
        self.get_data_btn = QtGui.QPushButton(self.centralwidget)
        self.get_data_btn.setGeometry(QtCore.QRect(240, 150, 161, 81))
        self.get_data_btn.setObjectName(_fromUtf8("get_data_btn"))
        self.calibration_progbar = QtGui.QProgressBar(self.centralwidget)
        self.calibration_progbar.setGeometry(QtCore.QRect(40, 560, 401, 41))
        self.calibration_progbar.setProperty("value", 24)
        self.calibration_progbar.setTextVisible(False)
        self.calibration_progbar.setObjectName(_fromUtf8("calibration_progbar"))
        self.admin_btn = QtGui.QPushButton(self.centralwidget)
        self.admin_btn.setGeometry(QtCore.QRect(180, 240, 111, 31))
        self.admin_btn.setObjectName(_fromUtf8("admin_btn"))
        self.recalibration_btn = QtGui.QPushButton(self.centralwidget)
        self.recalibration_btn.setGeometry(QtCore.QRect(620, 530, 91, 21))
        self.recalibration_btn.setObjectName(_fromUtf8("recalibration_btn"))
        self.back_btn = QtGui.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(60, 20, 61, 21))
        self.back_btn.setObjectName(_fromUtf8("back_btn"))
        self.weight_edit_log = QtGui.QListView(self.centralwidget)
        self.weight_edit_log.setGeometry(QtCore.QRect(570, 320, 361, 192))
        self.weight_edit_log.setObjectName(_fromUtf8("weight_edit_log"))
        self.home_btn = QtGui.QPushButton(self.centralwidget)
        self.home_btn.setGeometry(QtCore.QRect(800, 530, 81, 21))
        self.home_btn.setObjectName(_fromUtf8("home_btn"))
        self.boyuancy_data_btn.raise_()
        self.sensor2_btn.raise_()
        self.sensor1_btn.raise_()
        self.get_data_btn.raise_()
        self.calibration_progbar.raise_()
        self.admin_btn.raise_()
        self.recalibration_btn.raise_()
        self.back_btn.raise_()
        self.start_calibration_btn.raise_()
        self.weight_edit_log.raise_()
        self.home_btn.raise_()
        self.settings_btn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1007, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.settings_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sensor2_btn.show)
        QtCore.QObject.connect(self.settings_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.boyuancy_data_btn.show)
        QtCore.QObject.connect(self.settings_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.admin_btn.show)
        QtCore.QObject.connect(self.settings_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sensor1_btn.show)
        QtCore.QObject.connect(self.settings_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.get_data_btn.show)
        QtCore.QObject.connect(self.settings_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start_calibration_btn.hide)
        QtCore.QObject.connect(self.settings_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.back_btn.show)
        QtCore.QObject.connect(self.back_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start_calibration_btn.show)
        QtCore.QObject.connect(self.back_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.boyuancy_data_btn.hide)
        QtCore.QObject.connect(self.back_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sensor2_btn.hide)
        QtCore.QObject.connect(self.back_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.settings_btn.show)
        QtCore.QObject.connect(self.back_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.admin_btn.hide)
        QtCore.QObject.connect(self.back_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.sensor1_btn.hide)
        QtCore.QObject.connect(self.back_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.get_data_btn.hide)
        QtCore.QObject.connect(self.settings_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.settings_btn.hide)
        QtCore.QObject.connect(self.back_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.back_btn.hide)
        QtCore.QObject.connect(self.start_calibration_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start_calibration_btn.hide)
        QtCore.QObject.connect(self.start_calibration_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.settings_btn.hide)
        QtCore.QObject.connect(self.start_calibration_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.calibration_progbar.show)
        QtCore.QObject.connect(self.recalibration_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.calibration_progbar.show)
        QtCore.QObject.connect(self.recalibration_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.weight_edit_log.hide)
        QtCore.QObject.connect(self.recalibration_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.home_btn.hide)
        QtCore.QObject.connect(self.home_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.home_btn.hide)
        QtCore.QObject.connect(self.home_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.weight_edit_log.hide)
        QtCore.QObject.connect(self.home_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.recalibration_btn.hide)
        QtCore.QObject.connect(self.home_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.start_calibration_btn.show)
        QtCore.QObject.connect(self.home_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.settings_btn.show)
        QtCore.QObject.connect(self.home_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.calibration_progbar.hide)
        QtCore.QObject.connect(self.settings_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.calibration_progbar.hide)
        QtCore.QObject.connect(self.settings_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.weight_edit_log.hide)
        QtCore.QObject.connect(self.settings_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.recalibration_btn.hide)
        QtCore.QObject.connect(self.settings_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.home_btn.hide)
        QtCore.QObject.connect(self.start_calibration_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.weight_edit_log.hide)
        QtCore.QObject.connect(self.start_calibration_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.recalibration_btn.hide)
        QtCore.QObject.connect(self.start_calibration_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.home_btn.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.settings_btn.setText(_translate("MainWindow", "Settings", None))
        self.start_calibration_btn.setText(_translate("MainWindow", "Start", None))
        self.boyuancy_data_btn.setText(_translate("MainWindow", "Edit Bouyacny Data", None))
        self.sensor2_btn.setText(_translate("MainWindow", "Calibrate Sensor 2", None))
        self.sensor1_btn.setText(_translate("MainWindow", "Calibrate Sensor 1", None))
        self.get_data_btn.setText(_translate("MainWindow", "Download Calibration", None))
        self.admin_btn.setText(_translate("MainWindow", "Admin", None))
        self.recalibration_btn.setText(_translate("MainWindow", "Start", None))
        self.back_btn.setText(_translate("MainWindow", "Back", None))
        self.home_btn.setText(_translate("MainWindow", "Home", None))

