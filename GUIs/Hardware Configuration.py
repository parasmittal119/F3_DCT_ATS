# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Hardware Configuration.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(878, 529)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 851, 481))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.DBPass_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.DBPass_checkbox.setEnabled(True)
        self.DBPass_checkbox.setGeometry(QtCore.QRect(10, 170, 93, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DBPass_checkbox.setFont(font)
        self.DBPass_checkbox.setObjectName("DBPass_checkbox")
        self.CanDevice_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.CanDevice_checkbox.setEnabled(True)
        self.CanDevice_checkbox.setGeometry(QtCore.QRect(10, 200, 86, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CanDevice_checkbox.setFont(font)
        self.CanDevice_checkbox.setObjectName("CanDevice_checkbox")
        self.CanID_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.CanID_checkbox.setEnabled(True)
        self.CanID_checkbox.setGeometry(QtCore.QRect(10, 230, 102, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CanID_checkbox.setFont(font)
        self.CanID_checkbox.setObjectName("CanID_checkbox")
        self.CanBit_check = QtWidgets.QCheckBox(self.groupBox)
        self.CanBit_check.setEnabled(True)
        self.CanBit_check.setGeometry(QtCore.QRect(10, 260, 93, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CanBit_check.setFont(font)
        self.CanBit_check.setObjectName("CanBit_check")
        self.RSLower_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.RSLower_checkbox.setEnabled(True)
        self.RSLower_checkbox.setGeometry(QtCore.QRect(10, 290, 123, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RSLower_checkbox.setFont(font)
        self.RSLower_checkbox.setObjectName("RSLower_checkbox")
        self.RSUpper_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.RSUpper_checkbox.setEnabled(True)
        self.RSUpper_checkbox.setGeometry(QtCore.QRect(10, 320, 122, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RSUpper_checkbox.setFont(font)
        self.RSUpper_checkbox.setObjectName("RSUpper_checkbox")
        self.RSLowerPort_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.RSLowerPort_checkbox.setEnabled(True)
        self.RSLowerPort_checkbox.setGeometry(QtCore.QRect(10, 350, 92, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RSLowerPort_checkbox.setFont(font)
        self.RSLowerPort_checkbox.setObjectName("RSLowerPort_checkbox")
        self.RSLowerBaud_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.RSLowerBaud_checkbox.setEnabled(True)
        self.RSLowerBaud_checkbox.setGeometry(QtCore.QRect(10, 380, 145, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RSLowerBaud_checkbox.setFont(font)
        self.RSLowerBaud_checkbox.setObjectName("RSLowerBaud_checkbox")
        self.RSUpperPort_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.RSUpperPort_checkbox.setEnabled(True)
        self.RSUpperPort_checkbox.setGeometry(QtCore.QRect(10, 410, 92, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RSUpperPort_checkbox.setFont(font)
        self.RSUpperPort_checkbox.setObjectName("RSUpperPort_checkbox")
        self.RSUpperBaud_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.RSUpperBaud_checkbox.setEnabled(True)
        self.RSUpperBaud_checkbox.setGeometry(QtCore.QRect(10, 440, 145, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.RSUpperBaud_checkbox.setFont(font)
        self.RSUpperBaud_checkbox.setObjectName("RSUpperBaud_checkbox")
        self.LoadComm_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.LoadComm_checkbox.setEnabled(True)
        self.LoadComm_checkbox.setGeometry(QtCore.QRect(420, 170, 119, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LoadComm_checkbox.setFont(font)
        self.LoadComm_checkbox.setObjectName("LoadComm_checkbox")
        self.DCLoadGPIB_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.DCLoadGPIB_checkbox.setEnabled(True)
        self.DCLoadGPIB_checkbox.setGeometry(QtCore.QRect(420, 200, 98, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DCLoadGPIB_checkbox.setFont(font)
        self.DCLoadGPIB_checkbox.setObjectName("DCLoadGPIB_checkbox")
        self.BatteryLoadGPIB_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.BatteryLoadGPIB_checkbox.setEnabled(True)
        self.BatteryLoadGPIB_checkbox.setGeometry(QtCore.QRect(420, 230, 123, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BatteryLoadGPIB_checkbox.setFont(font)
        self.BatteryLoadGPIB_checkbox.setObjectName("BatteryLoadGPIB_checkbox")
        self.DCLoadUSB_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.DCLoadUSB_checkbox.setEnabled(True)
        self.DCLoadUSB_checkbox.setGeometry(QtCore.QRect(420, 260, 94, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DCLoadUSB_checkbox.setFont(font)
        self.DCLoadUSB_checkbox.setObjectName("DCLoadUSB_checkbox")
        self.BatteryLoadUSB_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.BatteryLoadUSB_checkbox.setEnabled(True)
        self.BatteryLoadUSB_checkbox.setGeometry(QtCore.QRect(420, 290, 119, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BatteryLoadUSB_checkbox.setFont(font)
        self.BatteryLoadUSB_checkbox.setObjectName("BatteryLoadUSB_checkbox")
        self.PowerMeterUSB_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.PowerMeterUSB_checkbox.setEnabled(True)
        self.PowerMeterUSB_checkbox.setGeometry(QtCore.QRect(420, 320, 136, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.PowerMeterUSB_checkbox.setFont(font)
        self.PowerMeterUSB_checkbox.setObjectName("PowerMeterUSB_checkbox")
        self.CROComm_Checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.CROComm_Checkbox.setEnabled(True)
        self.CROComm_Checkbox.setGeometry(QtCore.QRect(420, 350, 131, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CROComm_Checkbox.setFont(font)
        self.CROComm_Checkbox.setObjectName("CROComm_Checkbox")
        self.CROBaud_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.CROBaud_checkbox.setEnabled(True)
        self.CROBaud_checkbox.setGeometry(QtCore.QRect(420, 380, 151, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.CROBaud_checkbox.setFont(font)
        self.CROBaud_checkbox.setObjectName("CROBaud_checkbox")
        self.BarCode_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.BarCode_checkbox.setEnabled(True)
        self.BarCode_checkbox.setGeometry(QtCore.QRect(420, 410, 115, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BarCode_checkbox.setFont(font)
        self.BarCode_checkbox.setObjectName("BarCode_checkbox")
        self.ATSLoad_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.ATSLoad_checkbox.setEnabled(True)
        self.ATSLoad_checkbox.setGeometry(QtCore.QRect(420, 140, 113, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ATSLoad_checkbox.setFont(font)
        self.ATSLoad_checkbox.setObjectName("ATSLoad_checkbox")
        self.ACSourceCommType_chechbox = QtWidgets.QCheckBox(self.groupBox)
        self.ACSourceCommType_chechbox.setEnabled(True)
        self.ACSourceCommType_chechbox.setGeometry(QtCore.QRect(420, 50, 161, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ACSourceCommType_chechbox.setFont(font)
        self.ACSourceCommType_chechbox.setObjectName("ACSourceCommType_chechbox")
        self.ACSourceeGPIB_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.ACSourceeGPIB_checkbox.setEnabled(True)
        self.ACSourceeGPIB_checkbox.setGeometry(QtCore.QRect(420, 80, 110, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ACSourceeGPIB_checkbox.setFont(font)
        self.ACSourceeGPIB_checkbox.setObjectName("ACSourceeGPIB_checkbox")
        self.ACSourceUSB_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.ACSourceUSB_checkbox.setEnabled(True)
        self.ACSourceUSB_checkbox.setGeometry(QtCore.QRect(420, 110, 122, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ACSourceUSB_checkbox.setFont(font)
        self.ACSourceUSB_checkbox.setObjectName("ACSourceUSB_checkbox")
        self.DBUser_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.DBUser_checkbox.setEnabled(True)
        self.DBUser_checkbox.setGeometry(QtCore.QRect(10, 140, 65, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DBUser_checkbox.setFont(font)
        self.DBUser_checkbox.setObjectName("DBUser_checkbox")
        self.TelnetPassword_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.TelnetPassword_checkbox.setEnabled(True)
        self.TelnetPassword_checkbox.setGeometry(QtCore.QRect(10, 110, 114, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TelnetPassword_checkbox.setFont(font)
        self.TelnetPassword_checkbox.setObjectName("TelnetPassword_checkbox")
        self.TelnetUser_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.TelnetUser_checkbox.setEnabled(True)
        self.TelnetUser_checkbox.setGeometry(QtCore.QRect(10, 80, 87, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TelnetUser_checkbox.setFont(font)
        self.TelnetUser_checkbox.setObjectName("TelnetUser_checkbox")
        self.IP_checkbox = QtWidgets.QCheckBox(self.groupBox)
        self.IP_checkbox.setEnabled(True)
        self.IP_checkbox.setGeometry(QtCore.QRect(10, 50, 81, 18))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.IP_checkbox.setFont(font)
        self.IP_checkbox.setObjectName("IP_checkbox")
        self.CanDevice_combo = QtWidgets.QComboBox(self.groupBox)
        self.CanDevice_combo.setGeometry(QtCore.QRect(170, 200, 201, 22))
        self.CanDevice_combo.setObjectName("CanDevice_combo")
        self.RSLower_combo = QtWidgets.QComboBox(self.groupBox)
        self.RSLower_combo.setGeometry(QtCore.QRect(170, 290, 201, 22))
        self.RSLower_combo.setObjectName("RSLower_combo")
        self.RSUpper_combo = QtWidgets.QComboBox(self.groupBox)
        self.RSUpper_combo.setGeometry(QtCore.QRect(170, 320, 201, 22))
        self.RSUpper_combo.setObjectName("RSUpper_combo")
        self.RSLowerPort_combo = QtWidgets.QComboBox(self.groupBox)
        self.RSLowerPort_combo.setGeometry(QtCore.QRect(170, 350, 201, 22))
        self.RSLowerPort_combo.setObjectName("RSLowerPort_combo")
        self.RSUpperPort_combo = QtWidgets.QComboBox(self.groupBox)
        self.RSUpperPort_combo.setGeometry(QtCore.QRect(170, 410, 201, 22))
        self.RSUpperPort_combo.setObjectName("RSUpperPort_combo")
        self.ATSLoad_combo = QtWidgets.QComboBox(self.groupBox)
        self.ATSLoad_combo.setGeometry(QtCore.QRect(600, 140, 201, 22))
        self.ATSLoad_combo.setObjectName("ATSLoad_combo")
        self.LoadComm_combo = QtWidgets.QComboBox(self.groupBox)
        self.LoadComm_combo.setGeometry(QtCore.QRect(600, 170, 201, 22))
        self.LoadComm_combo.setObjectName("LoadComm_combo")
        self.DCLoadUSB_combo = QtWidgets.QComboBox(self.groupBox)
        self.DCLoadUSB_combo.setGeometry(QtCore.QRect(600, 260, 201, 22))
        self.DCLoadUSB_combo.setObjectName("DCLoadUSB_combo")
        self.BatteryLoadUSB_combo = QtWidgets.QComboBox(self.groupBox)
        self.BatteryLoadUSB_combo.setGeometry(QtCore.QRect(600, 290, 201, 22))
        self.BatteryLoadUSB_combo.setObjectName("BatteryLoadUSB_combo")
        self.PowerMeterUSB_combo = QtWidgets.QComboBox(self.groupBox)
        self.PowerMeterUSB_combo.setGeometry(QtCore.QRect(600, 320, 201, 22))
        self.PowerMeterUSB_combo.setObjectName("PowerMeterUSB_combo")
        self.CROComm_combo = QtWidgets.QComboBox(self.groupBox)
        self.CROComm_combo.setGeometry(QtCore.QRect(600, 350, 201, 22))
        self.CROComm_combo.setObjectName("CROComm_combo")
        self.ACSourceCommType_combo = QtWidgets.QComboBox(self.groupBox)
        self.ACSourceCommType_combo.setGeometry(QtCore.QRect(600, 50, 201, 22))
        self.ACSourceCommType_combo.setObjectName("ACSourceCommType_combo")
        self.CanID_edit = QtWidgets.QLineEdit(self.groupBox)
        self.CanID_edit.setGeometry(QtCore.QRect(170, 230, 201, 21))
        self.CanID_edit.setObjectName("CanID_edit")
        self.CanBit_edit = QtWidgets.QLineEdit(self.groupBox)
        self.CanBit_edit.setGeometry(QtCore.QRect(170, 260, 201, 21))
        self.CanBit_edit.setObjectName("CanBit_edit")
        self.RSLowerBaud_edit = QtWidgets.QLineEdit(self.groupBox)
        self.RSLowerBaud_edit.setGeometry(QtCore.QRect(170, 380, 201, 21))
        self.RSLowerBaud_edit.setObjectName("RSLowerBaud_edit")
        self.RSUpperBaud_edit = QtWidgets.QLineEdit(self.groupBox)
        self.RSUpperBaud_edit.setGeometry(QtCore.QRect(170, 440, 201, 21))
        self.RSUpperBaud_edit.setObjectName("RSUpperBaud_edit")
        self.IP_edit = QtWidgets.QLineEdit(self.groupBox)
        self.IP_edit.setGeometry(QtCore.QRect(170, 50, 201, 21))
        self.IP_edit.setObjectName("IP_edit")
        self.DBPass_edit = QtWidgets.QLineEdit(self.groupBox)
        self.DBPass_edit.setGeometry(QtCore.QRect(170, 170, 201, 21))
        self.DBPass_edit.setObjectName("DBPass_edit")
        self.TelnetUser_edit = QtWidgets.QLineEdit(self.groupBox)
        self.TelnetUser_edit.setGeometry(QtCore.QRect(170, 80, 201, 21))
        self.TelnetUser_edit.setObjectName("TelnetUser_edit")
        self.DBUser_edit = QtWidgets.QLineEdit(self.groupBox)
        self.DBUser_edit.setGeometry(QtCore.QRect(170, 140, 201, 21))
        self.DBUser_edit.setObjectName("DBUser_edit")
        self.TelnetPass_edit = QtWidgets.QLineEdit(self.groupBox)
        self.TelnetPass_edit.setGeometry(QtCore.QRect(170, 110, 201, 21))
        self.TelnetPass_edit.setObjectName("TelnetPass_edit")
        self.CROBaud_edit = QtWidgets.QLineEdit(self.groupBox)
        self.CROBaud_edit.setGeometry(QtCore.QRect(600, 380, 201, 21))
        self.CROBaud_edit.setObjectName("CROBaud_edit")
        self.DCLoadGPIB_edit = QtWidgets.QLineEdit(self.groupBox)
        self.DCLoadGPIB_edit.setGeometry(QtCore.QRect(600, 200, 201, 21))
        self.DCLoadGPIB_edit.setObjectName("DCLoadGPIB_edit")
        self.ACSourceeGPIB_edit = QtWidgets.QLineEdit(self.groupBox)
        self.ACSourceeGPIB_edit.setGeometry(QtCore.QRect(600, 80, 201, 21))
        self.ACSourceeGPIB_edit.setObjectName("ACSourceeGPIB_edit")
        self.ACSourceUSB_edit = QtWidgets.QLineEdit(self.groupBox)
        self.ACSourceUSB_edit.setGeometry(QtCore.QRect(600, 110, 201, 21))
        self.ACSourceUSB_edit.setObjectName("ACSourceUSB_edit")
        self.BatteryLoadGPIB_edit = QtWidgets.QLineEdit(self.groupBox)
        self.BatteryLoadGPIB_edit.setGeometry(QtCore.QRect(600, 230, 201, 21))
        self.BatteryLoadGPIB_edit.setObjectName("BatteryLoadGPIB_edit")
        self.BarCode_edit = QtWidgets.QLineEdit(self.groupBox)
        self.BarCode_edit.setGeometry(QtCore.QRect(600, 410, 201, 21))
        self.BarCode_edit.setObjectName("BarCode_edit")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(710, 445, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 445, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(440, 445, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(430, 500, 411, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border:2px solid red")
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 500, 301, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border:2px solid green")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Hardware Configuration"))
        self.groupBox.setTitle(_translate("Form", "Hardware Configuration"))
        self.DBPass_checkbox.setText(_translate("Form", "DB Password"))
        self.CanDevice_checkbox.setText(_translate("Form", "CAN Device"))
        self.CanID_checkbox.setText(_translate("Form", "CAN Device ID"))
        self.CanBit_check.setText(_translate("Form", "CAN Bit Rate"))
        self.RSLower_checkbox.setText(_translate("Form", "RS485 Lower Port"))
        self.RSUpper_checkbox.setText(_translate("Form", "RS485 Upper Port"))
        self.RSLowerPort_checkbox.setText(_translate("Form", "RS485 Port1"))
        self.RSLowerBaud_checkbox.setText(_translate("Form", "RS485 Port1 Baudrate"))
        self.RSUpperPort_checkbox.setText(_translate("Form", "RS485 Port2"))
        self.RSUpperBaud_checkbox.setText(_translate("Form", "RS485 Port2 Baudrate"))
        self.LoadComm_checkbox.setText(_translate("Form", "Load Comm Type"))
        self.DCLoadGPIB_checkbox.setText(_translate("Form", "DC Load GPIB"))
        self.BatteryLoadGPIB_checkbox.setText(_translate("Form", "Battery Load GPIB"))
        self.DCLoadUSB_checkbox.setText(_translate("Form", "DC Load USB"))
        self.BatteryLoadUSB_checkbox.setText(_translate("Form", "Battery Load USB"))
        self.PowerMeterUSB_checkbox.setText(_translate("Form", "Power Meter USB ID"))
        self.CROComm_Checkbox.setText(_translate("Form", "CRO Comm Port"))
        self.CROBaud_checkbox.setText(_translate("Form", "CRO Comm Baudrate"))
        self.BarCode_checkbox.setText(_translate("Form", "Bar Code Length"))
        self.ATSLoad_checkbox.setText(_translate("Form", "ATS Load Count"))
        self.ACSourceCommType_chechbox.setText(_translate("Form", "AC Source Comm Type"))
        self.ACSourceeGPIB_checkbox.setText(_translate("Form", "AC Source GPIB"))
        self.ACSourceUSB_checkbox.setText(_translate("Form", "AC Source USB ID"))
        self.DBUser_checkbox.setText(_translate("Form", "DB user"))
        self.TelnetPassword_checkbox.setText(_translate("Form", "Telnet Password"))
        self.TelnetUser_checkbox.setText(_translate("Form", "Telnet User"))
        self.IP_checkbox.setText(_translate("Form", "IP Address"))
        self.pushButton_3.setText(_translate("Form", "Cancel"))
        self.pushButton_2.setText(_translate("Form", "OK "))
        self.pushButton.setText(_translate("Form", "Change "))
        self.label_4.setText(_translate("Form", "WARNING: These values will over ride setting file values."))
        self.label_2.setText(_translate("Form", "NOTE: Leave check blank in case of no value"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
