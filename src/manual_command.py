# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\manual_command.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import gui_global
from CommandSetSmrBatteryCan import *
from PFC_control_done import *


class Ui_Form(object):
    def setupUi(self, Form):
        self.pfc = pfc_control()
        Form.setObjectName("Form")
        Form.resize(846, 332)
        Form.setWindowIcon(QtGui.QIcon(f"{gui_global.image_directory_location}logo_1.png"))
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 801, 291))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 30, 231, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 1, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(280, 30, 271, 101))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 1, 0, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 0, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 0, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 1, 1, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(280, 150, 271, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_11 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout.addWidget(self.pushButton_12)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 200, 231, 71))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_13 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_2.addWidget(self.pushButton_13)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(570, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_14.setGeometry(QtCore.QRect(590, 30, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setAutoDefault(True)
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(570, 130, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(570, 160, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(560, 210, 111, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setGeometry(QtCore.QRect(680, 211, 62, 31))
        self.doubleSpinBox.setProperty("value", 48.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.pushButton_29 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_29.setGeometry(QtCore.QRect(750, 210, 51, 31))
        self.pushButton_29.setObjectName("pushButton_29")

        self.pushButton_29.clicked.connect(self.smrVoltageSet)
        self.pushButton_14.clicked.connect(self.startATS)
        self.pushButton_13.clicked.connect(self.ACActive)
        self.pushButton.clicked.connect(self.LOAD1)
        self.pushButton_3.clicked.connect(self.LOAD2)
        self.pushButton_2.clicked.connect(self.LOAD3)
        self.pushButton_4.clicked.connect(self.LOAD4)
        self.pushButton_5.clicked.connect(self.LOAD5)
        self.pushButton_6.clicked.connect(self.LOADCommon)
        self.pushButton_7.clicked.connect(self.BATT1)
        self.pushButton_9.clicked.connect(self.BATT2)
        self.pushButton_8.clicked.connect(self.BATT3)
        self.pushButton_10.clicked.connect(self.BATTMAINS)
        # self.pushButton_11.clicked.connect(self.LOADMAINS)
        self.pushButton_12.clicked.connect(self.DcBus)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Manual Control"))
        self.groupBox.setTitle(_translate("Form", "INDIVIDUAL ATS CONTACTOR DRIVE"))
        self.pushButton_2.setText(_translate("Form", "LOAD 3 SET"))
        self.pushButton_4.setText(_translate("Form", "LOAD 4 SET"))
        self.pushButton_3.setText(_translate("Form", "LOAD 2 SET"))
        self.pushButton.setText(_translate("Form", "LOAD 1 SET"))
        self.pushButton_5.setText(_translate("Form", "LOAD 5 SET"))
        self.pushButton_6.setText(_translate("Form", "LOAD COMMON SET"))
        self.pushButton_8.setText(_translate("Form", "BATTERY 3 SET"))
        self.pushButton_7.setText(_translate("Form", "BATTERY 1 SET"))
        self.pushButton_9.setText(_translate("Form", "BATTERY 2 SET"))
        self.pushButton_10.setText(_translate("Form", "BATTERY COMM SET"))
        self.pushButton_11.setText(_translate("Form", "BATT LOAD SET"))
        self.pushButton_12.setText(_translate("Form", "DC LOAD SET"))
        self.label.setText(_translate("Form", "This Contactor is to be used to connect DC Load"))
        self.label_2.setText(_translate("Form", "to Battery Path, Normally this is OFF."))
        self.pushButton_13.setText(_translate("Form", "AC SET"))
        self.label_3.setText(_translate("Form", "NOTE: This SET basic Configuration."))
        self.pushButton_14.setText(_translate("Form", "START ATS"))
        self.label_4.setText(_translate("Form", "Please use individual button to set"))
        self.label_5.setText(_translate("Form", "Contactor as per requirement."))
        self.label_11.setText(_translate("Form", "Set Battery Voltage:"))
        self.pushButton_29.setText(_translate("Form", "SET"))
        self.count = 0
        self.smr = 0
        self.button_status(False)

    def startATS(self):
        if self.pushButton_14.pressed:
            self.count += 1

        if self.count == 1:
            self.button_status(True)
            self.pushButton_14.setText("CLEAR ATS")

        if self.count == 2:
            self.button_status(False)
            self.count = 0
            self.pushButton_14.setText("START ATS")
            self.pfc.pfc_set(0, 'all', 0)
            self.pushButton_6.setText("LOAD COMMON SET")
            # self.pfc.pfc_set(0, 'battery_mains', 0)
            self.pushButton_10.setText("BATTERY COMM SET")
            # self.pfc.pfc_set(0, 'bus', 0)
            self.pushButton_12.setText("DC LOAD SET")



    def button_status(self, state: bool):
        self.all_button = [self.pushButton, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5,
                           self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9,
                           self.pushButton_10,
                           self.pushButton_11, self.pushButton_12, self.pushButton_13, self.pushButton_29, self.doubleSpinBox]

        for i in self.all_button:
            i.setEnabled(state)



    def smrVoltageSet(self):
        SMR_BATTERY_SET_VOLTAGE(self.doubleSpinBox.value())

    def ACActive(self):
        self.status(self.pushButton_13, 'AC', ["r_phase", "y_phase", "b_phase"])

    def LOAD1(self):
        self.status(self.pushButton, 'LOAD 1', ['p_load'])
        if self.pushButton.text() == "LOAD 1 CLEAR" and self.pushButton_6.text() == "LOAD COMMON SET":
            self.status(self.pushButton_6, 'LOAD COMMON', ['load_mains'])
        self.BusCheck(self.pushButton_6, 'LOAD COMMON')


    def LOAD2(self):
        self.status(self.pushButton_3, 'LOAD 2', ['n_p_load_1'])
        if self.pushButton_3.text() == "LOAD 2 CLEAR" and self.pushButton_6.text() == "LOAD COMMON SET":
            self.status(self.pushButton_6, 'LOAD COMMON', ['load_mains'])
        self.BusCheck(self.pushButton_6, 'LOAD COMMON')

    def LOAD3(self):
        self.status(self.pushButton_2, 'LOAD 3', ['n_p_load_2'])
        if self.pushButton_2.text() == "LOAD 3 CLEAR" and self.pushButton_6.text() == "LOAD COMMON SET":
            self.status(self.pushButton_6, 'LOAD COMMON', ['load_mains'])
        self.BusCheck(self.pushButton_6, 'LOAD COMMON')

    def LOAD4(self):
        self.status(self.pushButton_4, 'LOAD 4', ['n_p_load_3'])
        if self.pushButton_4.text() == "LOAD 4 CLEAR" and self.pushButton_6.text() == "LOAD COMMON SET":
            self.status(self.pushButton_6, 'LOAD COMMON', ['load_mains'])
        self.BusCheck(self.pushButton_6, 'LOAD COMMON')

    def LOAD5(self):
        self.status(self.pushButton_5, 'LOAD 5', ['n_p_load_4'])
        if self.pushButton_5.text() == "LOAD 5 CLEAR" and self.pushButton_6.text() == "LOAD COMMON SET":
            self.status(self.pushButton_6, 'LOAD COMMON', ['load_mains'])
        self.BusCheck(self.pushButton_6, 'LOAD COMMON')

    def BATT1(self):
        self.status(self.pushButton_7, 'BATTERY 1', ['battery_1'])
        if self.pushButton_7.text() == "BATTERY 1 CLEAR" and self.pushButton_10.text() == "BATTERY COMM SET":
            self.status(self.pushButton_10, 'BATTERY COMM', ['battery_mains'])


    def BATT2(self):
        self.status(self.pushButton_9, 'BATTERY 2', ['battery_2'])
        if self.pushButton_9.text() == "BATTERY 2 CLEAR" and self.pushButton_10.text() == "BATTERY COMM SET":
            self.status(self.pushButton_10, 'BATTERY COMM', ['battery_mains'])

    def BATT3(self):
        self.status(self.pushButton_8, 'BATTERY 3', ['battery_3'])
        if self.pushButton_8.text() == "BATTERY 3 CLEAR" and self.pushButton_10.text() == "BATTERY COMM SET":
            self.status(self.pushButton_10, 'BATTERY COMM', ['battery_mains'])

    def BATTMAINS(self):
        self.status(self.pushButton_10, 'BATTERY COMM', ['battery_mains'])

    def LOADMAINS(self):
        self.status(self.pushButton_11, 'BATT LOAD', ['load_mains'])

    def DcBus(self):
        self.status(self.pushButton_12, "DC LOAD", ['bus'])

    def LOADCommon(self):
        self.status(self.pushButton_6, 'LOAD COMMON', ['load_mains'])


    def BusCheck(self, button, button_text):
        if button.text() == f"{button_text} CLEAR" and self.pushButton_12.text() == "DC LOAD SET":
            self.status(self.pushButton_12, "DC LOAD", ['bus'])

    def status(self, pushbutton: str, button_text: str, pfc_name: list):
        if pushbutton.text() == f'{button_text} SET':
            for itr in pfc_name:
                print(itr)
                self.pfc.pfc_set(0, itr, 1)
            pushbutton.setText(f"{button_text} CLEAR")
        elif pushbutton.text() == f'{button_text} CLEAR':
            for itr in pfc_name:
                print(itr)
                self.pfc.pfc_set(0, itr, 0)
            pushbutton.setText(f"{button_text} SET")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
