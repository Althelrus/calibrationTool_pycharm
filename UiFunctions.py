import os
from PyQt4.QtCore import QUrl
from PyQt4 import QtGui
from PyQt4.QtWebKit import *


class ExtraUiFunctions(object):
    def show_procedure(self, procedure_part_num):

        # PURPOSE:    Displays the Procedure in .htm format.
        #             We create a Qwidget containing a Qframe and
        #             display the file using QWebView.

        # The Widget
        test_procedure_window = QtGui.QDialog()
        test_procedure_window.setGeometry(100, 100, 850, 800)
        test_procedure_window.setWindowTitle('FMI Product Label Procedure')
        # Create a Frame inside the Widget
        proc_frame = QtGui.QFrame(test_procedure_window)
        proc_frame.setGeometry(10, 10, 840, 780)
        proc_frame.setFrameShape(QtGui.QFrame.StyledPanel | QtGui.QFrame.Sunken)
        # Create a QWebView inside the Frame.
        proc_viewer = QWebView(proc_frame)
        proc_viewer.setGeometry(5, 5, 830, 765)
        proc_viewer.settings().setAttribute(QWebSettings.PluginsEnabled, True)
        # Load the Procedure in .htm format into the proc_viewer.
        proc_viewer.load(QUrl('file:///' + os.getcwd() + '/htm_files/' + procedure_part_num))
        # print 'LOADING PROCEDURE', os.getcwd() + '/htm_files/'+procedure_part_num
        if not os.path.exists(os.getcwd() + '/htm_files/' + procedure_part_num ):
            self.pop_message('OK', 'Procedure: {} Not Found !!!!'.format(os.getcwd() + '/htm_files/' +procedure_part_num ))
            return
        # TODO Exception created, may use QDialog
        test_procedure_window.exec_()

    def pop_message(self, typeofbox='YN', error_msg='Nothing sent to pop_message', message_box_severity=1):
        # PURPOSE:           Display a Modal Pop-Up User Message Box.
        # typeofbox:         Message with 'OK or 'Y N' Buttons.
        # param error_msg:   Message to display to user.
        print 'POP_MESSAGE', typeofbox, error_msg, message_box_severity
        pop = QtGui.QDialog()
        typeofbox = typeofbox.upper()
        error_msg = '<br><b>' + str(error_msg)
        severity_list = [
            QtGui.QMessageBox.information,
            QtGui.QMessageBox.warning,
            QtGui.QMessageBox.critical
        ]
        if typeofbox == 'YN':
            reply = severity_list[message_box_severity](pop, 'User Message',
                                                        error_msg,
                                                        QtGui.QMessageBox.Yes,
                                                        QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.No:
                return 0
            else:
                return 1
        if typeofbox == 'OK':
            severity_list[message_box_severity](pop, 'User Message', error_msg)
            return