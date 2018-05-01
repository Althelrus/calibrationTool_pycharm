# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QtCore.QSize(800, 480))
        MainWindow.setMaximumSize(QtCore.QSize(800, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logFrame = QtWidgets.QFrame(self.centralwidget)
        self.logFrame.setGeometry(QtCore.QRect(10, 10, 781, 421))
        self.logFrame.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));")
        self.logFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.logFrame.setLineWidth(2)
        self.logFrame.setObjectName("logFrame")
        self.weight_edit_log = QtWidgets.QListView(self.logFrame)
        self.weight_edit_log.setGeometry(QtCore.QRect(20, 61, 741, 281))
        self.weight_edit_log.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.weight_edit_log.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.weight_edit_log.setLineWidth(2)
        self.weight_edit_log.setObjectName("weight_edit_log")
        self.home_btn = QtWidgets.QPushButton(self.logFrame)
        self.home_btn.setGeometry(QtCore.QRect(640, 370, 121, 31))
        self.home_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.home_btn.setObjectName("home_btn")
        self.recalibration_btn = QtWidgets.QPushButton(self.logFrame)
        self.recalibration_btn.setGeometry(QtCore.QRect(20, 370, 121, 31))
        self.recalibration_btn.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.recalibration_btn.setObjectName("recalibration_btn")
        self.userlog_lbl = QtWidgets.QLabel(self.logFrame)
        self.userlog_lbl.setGeometry(QtCore.QRect(20, 10, 741, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.userlog_lbl.setFont(font)
        self.userlog_lbl.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.userlog_lbl.setFrameShape(QtWidgets.QFrame.Box)
        self.userlog_lbl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userlog_lbl.setLineWidth(2)
        self.userlog_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.userlog_lbl.setWordWrap(True)
        self.userlog_lbl.setObjectName("userlog_lbl")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setGeometry(QtCore.QRect(10, 10, 781, 421))
        self.mainFrame.setAutoFillBackground(False)
        self.mainFrame.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));")
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mainFrame.setLineWidth(2)
        self.mainFrame.setObjectName("mainFrame")
        self.start_calibration_btn = QtWidgets.QPushButton(self.mainFrame)
        self.start_calibration_btn.setGeometry(QtCore.QRect(270, 170, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.start_calibration_btn.setFont(font)
        self.start_calibration_btn.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.start_calibration_btn.setObjectName("start_calibration_btn")
        self.settings_btn = QtWidgets.QPushButton(self.mainFrame)
        self.settings_btn.setGeometry(QtCore.QRect(720, 1, 61, 61))
        self.settings_btn.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"background-image: url(:/images/gear.png);")
        self.settings_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/gear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_btn.setIcon(icon)
        self.settings_btn.setIconSize(QtCore.QSize(60, 60))
        self.settings_btn.setObjectName("settings_btn")
        self.loadingFrame = QtWidgets.QFrame(self.centralwidget)
        self.loadingFrame.setGeometry(QtCore.QRect(10, 10, 781, 421))
        self.loadingFrame.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));")
        self.loadingFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loadingFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.loadingFrame.setLineWidth(2)
        self.loadingFrame.setObjectName("loadingFrame")
        self.calibration_progbar = QtWidgets.QProgressBar(self.loadingFrame)
        self.calibration_progbar.setGeometry(QtCore.QRect(19, 200, 741, 40))
        self.calibration_progbar.setStyleSheet("")
        self.calibration_progbar.setProperty("value", 24)
        self.calibration_progbar.setTextVisible(False)
        self.calibration_progbar.setObjectName("calibration_progbar")
        self.settingFrame = QtWidgets.QFrame(self.centralwidget)
        self.settingFrame.setGeometry(QtCore.QRect(10, 10, 781, 421))
        self.settingFrame.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));")
        self.settingFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.settingFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.settingFrame.setLineWidth(2)
        self.settingFrame.setObjectName("settingFrame")
        self.admin_btn = QtWidgets.QPushButton(self.settingFrame)
        self.admin_btn.setGeometry(QtCore.QRect(700, 10, 61, 21))
        self.admin_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.admin_btn.setObjectName("admin_btn")
        self.get_data_btn = QtWidgets.QPushButton(self.settingFrame)
        self.get_data_btn.setGeometry(QtCore.QRect(310, 380, 161, 31))
        self.get_data_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.get_data_btn.setObjectName("get_data_btn")
        self.back_btn = QtWidgets.QPushButton(self.settingFrame)
        self.back_btn.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.back_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.back_btn.setObjectName("back_btn")
        self.v_adj_cbox = QtWidgets.QCheckBox(self.settingFrame)
        self.v_adj_cbox.setGeometry(QtCore.QRect(510, 187, 141, 17))
        self.v_adj_cbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.v_adj_cbox.setObjectName("v_adj_cbox")
        self.program_mode_lbl = QtWidgets.QLabel(self.settingFrame)
        self.program_mode_lbl.setGeometry(QtCore.QRect(510, 167, 141, 21))
        self.program_mode_lbl.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.program_mode_lbl.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.program_mode_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.program_mode_lbl.setObjectName("program_mode_lbl")
        self.foam_cbox = QtWidgets.QCheckBox(self.settingFrame)
        self.foam_cbox.setEnabled(False)
        self.foam_cbox.setGeometry(QtCore.QRect(510, 204, 141, 16))
        self.foam_cbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.foam_cbox.setObjectName("foam_cbox")
        self.save_cailbration = QtWidgets.QCheckBox(self.settingFrame)
        self.save_cailbration.setEnabled(False)
        self.save_cailbration.setGeometry(QtCore.QRect(510, 220, 141, 16))
        self.save_cailbration.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.save_cailbration.setObjectName("save_cailbration")
        self.sensor_set_btn = QtWidgets.QPushButton(self.settingFrame)
        self.sensor_set_btn.setGeometry(QtCore.QRect(50, 120, 211, 41))
        self.sensor_set_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sensor_set_btn.setObjectName("sensor_set_btn")
        self.screen_calibrate = QtWidgets.QPushButton(self.settingFrame)
        self.screen_calibrate.setGeometry(QtCore.QRect(50, 240, 211, 41))
        self.screen_calibrate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.screen_calibrate.setObjectName("screen_calibrate")
        self.variable_adj_btn = QtWidgets.QPushButton(self.settingFrame)
        self.variable_adj_btn.setGeometry(QtCore.QRect(50, 180, 211, 41))
        self.variable_adj_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.variable_adj_btn.setObjectName("variable_adj_btn")
        self.variable_adj_frame = QtWidgets.QFrame(self.centralwidget)
        self.variable_adj_frame.setGeometry(QtCore.QRect(10, 10, 781, 421))
        self.variable_adj_frame.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));")
        self.variable_adj_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.variable_adj_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.variable_adj_frame.setLineWidth(2)
        self.variable_adj_frame.setObjectName("variable_adj_frame")
        self.program_mode_lbl_3 = QtWidgets.QLabel(self.variable_adj_frame)
        self.program_mode_lbl_3.setGeometry(QtCore.QRect(210, 10, 361, 31))
        self.program_mode_lbl_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.program_mode_lbl_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.program_mode_lbl_3.setAlignment(QtCore.Qt.AlignCenter)
        self.program_mode_lbl_3.setObjectName("program_mode_lbl_3")
        self.submit_variables = QtWidgets.QPushButton(self.variable_adj_frame)
        self.submit_variables.setGeometry(QtCore.QRect(290, 300, 211, 41))
        self.submit_variables.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.submit_variables.setObjectName("submit_variables")
        self.bep_input_dsbox = QtWidgets.QDoubleSpinBox(self.variable_adj_frame)
        self.bep_input_dsbox.setGeometry(QtCore.QRect(290, 160, 71, 41))
        self.bep_input_dsbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bep_input_dsbox.setObjectName("bep_input_dsbox")
        self.label_10 = QtWidgets.QLabel(self.variable_adj_frame)
        self.label_10.setGeometry(QtCore.QRect(80, 170, 191, 21))
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_10.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_10.setObjectName("label_10")
        self.den_input_dsbox = QtWidgets.QDoubleSpinBox(self.variable_adj_frame)
        self.den_input_dsbox.setGeometry(QtCore.QRect(580, 160, 71, 41))
        self.den_input_dsbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.den_input_dsbox.setObjectName("den_input_dsbox")
        self.label_11 = QtWidgets.QLabel(self.variable_adj_frame)
        self.label_11.setGeometry(QtCore.QRect(460, 170, 101, 21))
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_11.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_11.setObjectName("label_11")
        self.calibration_ask_frame = QtWidgets.QFrame(self.centralwidget)
        self.calibration_ask_frame.setGeometry(QtCore.QRect(10, 10, 781, 421))
        self.calibration_ask_frame.setStyleSheet("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.7, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));")
        self.calibration_ask_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.calibration_ask_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.calibration_ask_frame.setLineWidth(2)
        self.calibration_ask_frame.setObjectName("calibration_ask_frame")
        self.lb1_input_sbox = QtWidgets.QSpinBox(self.calibration_ask_frame)
        self.lb1_input_sbox.setGeometry(QtCore.QRect(230, 180, 81, 31))
        self.lb1_input_sbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lb1_input_sbox.setObjectName("lb1_input_sbox")
        self.sensor1_set_btn = QtWidgets.QPushButton(self.calibration_ask_frame)
        self.sensor1_set_btn.setGeometry(QtCore.QRect(80, 180, 139, 31))
        self.sensor1_set_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sensor1_set_btn.setObjectName("sensor1_set_btn")
        self.sensor2_tare_btn = QtWidgets.QPushButton(self.calibration_ask_frame)
        self.sensor2_tare_btn.setGeometry(QtCore.QRect(490, 180, 139, 31))
        self.sensor2_tare_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sensor2_tare_btn.setObjectName("sensor2_tare_btn")
        self.sensor1_tare_btn = QtWidgets.QPushButton(self.calibration_ask_frame)
        self.sensor1_tare_btn.setGeometry(QtCore.QRect(80, 180, 139, 31))
        self.sensor1_tare_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sensor1_tare_btn.setObjectName("sensor1_tare_btn")
        self.sensor2_set_btn = QtWidgets.QPushButton(self.calibration_ask_frame)
        self.sensor2_set_btn.setGeometry(QtCore.QRect(490, 180, 139, 31))
        self.sensor2_set_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sensor2_set_btn.setObjectName("sensor2_set_btn")
        self.lb2_input_sbox = QtWidgets.QSpinBox(self.calibration_ask_frame)
        self.lb2_input_sbox.setGeometry(QtCore.QRect(640, 180, 81, 31))
        self.lb2_input_sbox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lb2_input_sbox.setObjectName("lb2_input_sbox")
        self.label_4 = QtWidgets.QLabel(self.calibration_ask_frame)
        self.label_4.setGeometry(QtCore.QRect(230, 150, 81, 21))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_4.setObjectName("label_4")
        self.submit_calibration = QtWidgets.QPushButton(self.calibration_ask_frame)
        self.submit_calibration.setGeometry(QtCore.QRect(290, 300, 211, 41))
        self.submit_calibration.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.submit_calibration.setObjectName("submit_calibration")
        self.label_5 = QtWidgets.QLabel(self.calibration_ask_frame)
        self.label_5.setGeometry(QtCore.QRect(80, 140, 101, 31))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.calibration_ask_frame)
        self.label_6.setGeometry(QtCore.QRect(490, 140, 101, 31))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.calibration_ask_frame)
        self.label_7.setGeometry(QtCore.QRect(640, 150, 81, 21))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_7.setObjectName("label_7")
        self.sensor2_set_btn.raise_()
        self.lb1_input_sbox.raise_()
        self.sensor1_set_btn.raise_()
        self.sensor2_tare_btn.raise_()
        self.sensor1_tare_btn.raise_()
        self.lb2_input_sbox.raise_()
        self.label_4.raise_()
        self.submit_calibration.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.loadingFrame.raise_()
        self.settingFrame.raise_()
        self.variable_adj_frame.raise_()
        self.logFrame.raise_()
        self.mainFrame.raise_()
        self.calibration_ask_frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionProcedure = QtWidgets.QAction(MainWindow)
        self.actionProcedure.setObjectName("actionProcedure")
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addAction(self.actionProcedure)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.back_btn.clicked.connect(self.settingFrame.hide)
        self.recalibration_btn.clicked.connect(self.loadingFrame.show)
        self.home_btn.clicked.connect(self.logFrame.hide)
        self.recalibration_btn.clicked.connect(self.logFrame.hide)
        self.back_btn.clicked.connect(self.mainFrame.show)
        self.home_btn.clicked.connect(self.mainFrame.show)
        self.start_calibration_btn.clicked.connect(self.mainFrame.hide)
        self.start_calibration_btn.clicked.connect(self.loadingFrame.show)
        self.settings_btn.clicked.connect(self.settingFrame.show)
        self.settings_btn.clicked.connect(self.mainFrame.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Balancing Test"))
        self.home_btn.setText(_translate("MainWindow", "Home"))
        self.recalibration_btn.setText(_translate("MainWindow", "Start"))
        self.userlog_lbl.setText(_translate("MainWindow", "Place weights in the corresponding areas given from the Log below."))
        self.start_calibration_btn.setText(_translate("MainWindow", "Start"))
        self.admin_btn.setText(_translate("MainWindow", "Admin"))
        self.get_data_btn.setText(_translate("MainWindow", "Download Calibration Results"))
        self.back_btn.setText(_translate("MainWindow", "Back"))
        self.v_adj_cbox.setText(_translate("MainWindow", "Variable Adjustment"))
        self.program_mode_lbl.setText(_translate("MainWindow", "Program Mode"))
        self.foam_cbox.setText(_translate("MainWindow", "Foam Compatiablity"))
        self.save_cailbration.setText(_translate("MainWindow", "Save Calibration"))
        self.sensor_set_btn.setText(_translate("MainWindow", "Load Cell Calibration"))
        self.screen_calibrate.setText(_translate("MainWindow", "Run Screen Calibrate"))
        self.variable_adj_btn.setText(_translate("MainWindow", "Input Variables Adjustment"))
        self.program_mode_lbl_3.setText(_translate("MainWindow", "Adjust Calculation Variables"))
        self.submit_variables.setText(_translate("MainWindow", "Submit"))
        self.label_10.setText(_translate("MainWindow", "Boyancy Engine Position (-100 to 100)"))
        self.label_11.setText(_translate("MainWindow", "Density (slug/ft^3)"))
        self.sensor1_set_btn.setText(_translate("MainWindow", "Set Left Weight"))
        self.sensor2_tare_btn.setText(_translate("MainWindow", "Tare Right"))
        self.sensor1_tare_btn.setText(_translate("MainWindow", "Tare Left"))
        self.sensor2_set_btn.setText(_translate("MainWindow", "Set Right Weight"))
        self.label_4.setText(_translate("MainWindow", "  Input Weight "))
        self.submit_calibration.setText(_translate("MainWindow", "Submit"))
        self.label_5.setText(_translate("MainWindow", "     Load Cell left"))
        self.label_6.setText(_translate("MainWindow", "    Load Cell Right"))
        self.label_7.setText(_translate("MainWindow", "  Input Weight "))
        self.menuAbout.setTitle(_translate("MainWindow", "More"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionProcedure.setText(_translate("MainWindow", "Procedure"))

# import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

