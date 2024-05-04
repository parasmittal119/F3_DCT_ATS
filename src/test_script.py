# -*- coding: utf-8 -*-
import datetime
import os.path
import time
from excel_automation import CSVHandler
from PyQt5 import QtCore, QtGui, QtWidgets
from screeninfo import get_monitors
import CommandSetDcLoadUsb
import CommandSetSmrBatteryCan
import PFC_control_done
import gui_global
import test_order_done
from ModbusServer import MODBUS_CHECK
from config_done import SettingRead
from report_gui import *
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
import CanModule

global w, h, m, factor

"""MULTIPLYING FACTOR"""
try:
    factor = abs(eval(SettingRead('MULTIPLY')['factor']))
    # if factor <= 0 or factor >= 2:
    #     factor = 1
except TypeError:
    with open(f'{gui_global.files_directory_location}setting.txt', 'a') as file:
        file.write("\n[MULTIPLY]\nfactor=0.8\n")
    factor = round(abs(eval(SettingRead('MULTIPLY')['factor'])))
    if factor <= 0 or factor >= 2:
        factor = 1
print(factor)
w = get_monitors()[0].width
h = get_monitors()[0].height

from config_done import *
import M1000Telnet
import M2000
from prompts import Prompt

try:
    if os.path.exists(os.path.join(gui_global.files_directory_location), 'setting.txt'):
        if SettingRead("SETTING")['ate load comm type'] == "RS232C":
            from CommandDCLoad import *
        if SettingRead("SETTING")['ate load comm type'] == "USB" or \
                SettingRead("SETTING")['ate load comm type'] == "GPIB":
            from CommandDCLoad import *

        ATE_LOAD_COUNT = int(SettingRead("SETTING")['ate load count'])
except:
    pass


def get_date_time(date=0, time=0):
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month)
    day = str(now.day)
    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = "0" + day
    date_only = day + "-" + month + "-" + year
    hour = str(now.hour)
    if len(hour) == 1:
        hour = "0" + hour
    minute = str(now.minute)
    if len(minute) == 1:
        minute = "0" + minute
    second = str(now.second)
    if len(second) == 1:
        second = "0" + second
    time_only = hour + ":" + minute + ":" + second
    if time == 1 and date == 1:
        return date_only + " " + time_only
    elif date == 1:
        return date_only
    elif time == 1:
        return time_only


class WindowSignalHandler(QObject):
    openWindow = pyqtSignal()


class Ui_Test(object):
    global w, h

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1402, 778)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setWindowIcon(QtGui.QIcon(f"{gui_global.image_directory_location}logo_1.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.heading_box = QtWidgets.QGroupBox(self.centralwidget)
        # self.heading_box.setGeometry(
        #     QtCore.QRect(int(w * 0.28505), int(h * 0.052083), int(w * 0.3806), int(h * 0.0651)))
        # self.heading_box.setTitle("")
        # self.heading_box.setObjectName("heading_box")
        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setGeometry(QtCore.QRect(width(410), int(h * 0.039), int(w * 0.3806), int(h * 0.0651)))
        font = QtGui.QFont()
        font.setPointSize(width(22))
        font.setBold(True)
        font.setWeight(width(75))
        self.heading.setStyleSheet("QLabel{\n\nborder-top: 5px solid black;\nborder-bottom: 5px solid black;\n\n}")
        self.heading.setFont(font)
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.test_detail_box = QtWidgets.QGroupBox(self.centralwidget)
        self.test_detail_box.setEnabled(True)
        self.test_detail_box.setGeometry(QtCore.QRect(width(30), height(150), width(330), height(461)))
        self.font8_BF_UF_50 = QtGui.QFont()
        self.font8_BF_UF_50.setPointSize(width(8))
        self.font8_BF_UF_50.setBold(False)
        self.font8_BF_UF_50.setUnderline(False)
        self.font8_BF_UF_50.setWeight(width(50))
        self.test_detail_box.setStyleSheet(
            "QGroupBox{background-color:rgba(42,58,86,255);color:rgba(255,255,255,255); border-top-right-radius:50px; border-bottom-left-radius:50px; padding-top:10px}")
        self.test_detail_box.setFont(self.font8_BF_UF_50)
        self.test_detail_box.setObjectName("test_detail_box")
        self.test_id = QtWidgets.QLabel(self.test_detail_box)
        self.test_id.setGeometry(QtCore.QRect(width(20), height(60), width(71), height(16)))
        self.font11_BF_UF_50 = QtGui.QFont()
        self.font11_BF_UF_50.setPointSize(width(11))
        self.font11_BF_UF_50.setBold(False)
        self.font11_BF_UF_50.setUnderline(False)
        self.font11_BF_UF_50.setWeight(width(50))
        self.test_id.setStyleSheet("color:rgba(255,255,255,255)")
        self.test_id.setFont(self.font11_BF_UF_50)
        self.test_id.setObjectName("test_id")
        self.system_part_no = QtWidgets.QLabel(self.test_detail_box)
        self.system_part_no.setGeometry(QtCore.QRect(width(20), height(90), width(141), height(16)))
        self.system_part_no.setStyleSheet("color:rgba(255,255,255,255)")
        self.system_part_no.setFont(self.font11_BF_UF_50)
        self.system_part_no.setObjectName("system_part_no")
        self.dut_serial_number = QtWidgets.QLabel(self.test_detail_box)
        self.dut_serial_number.setGeometry(QtCore.QRect(width(20), height(120), width(101), height(16)))
        self.dut_serial_number.setStyleSheet("color:rgba(255,255,255,255)")
        self.dut_serial_number.setFont(self.font11_BF_UF_50)
        self.dut_serial_number.setObjectName("dut_serial_number")
        self.test_id_edit = QtWidgets.QLineEdit(self.test_detail_box)
        self.test_id_edit.setGeometry(QtCore.QRect(width(150), height(60), width(151), height(20)))
        self.test_id_edit.setStyleSheet(
            "QLineEdit\n{\nbackground-color:rgba(0,0,0,0);\nborder:none;\nborder-bottom:2px solid rgba(42,226,230,255);\ncolor:rgba(255,255,255,255);\npadding-bottom:7px;\n}")
        self.test_id_edit.setObjectName("test_id_edit")
        self.test_id_edit.setReadOnly(True)
        self.test_id_edit.setPlaceholderText("Test ID will be shown here")
        self.test_id_edit.setStyleSheet(
            "QLineEdit\n{\nbackground-color:rgba(0,0,0,0);\nborder:none;\nborder-bottom:2px solid rgba(42,226,230,255);\ncolor:rgba(255,255,255,255);\npadding-bottom:7px;\n}")
        self.test_id_edit.setFont(self.font8_BF_UF_50)

        self.system_part_no_edit = QtWidgets.QLineEdit(self.test_detail_box)
        self.system_part_no_edit.setGeometry(QtCore.QRect(width(150), height(90), width(151), height(20)))
        self.system_part_no_edit.setObjectName("system_part_no_edit")
        self.system_part_no_edit.setStyleSheet(
            "QLineEdit\n{\nbackground-color:rgba(0,0,0,0);\nborder:none;\nborder-bottom:2px solid rgba(42,226,230,255);\ncolor:rgba(255,255,255,255);\npadding-bottom:7px;\n}")
        self.system_part_no_edit.setPlaceholderText("System Part Code")
        self.system_part_no_edit.setFont(self.font8_BF_UF_50)
        self.dut_serial_number_edit = QtWidgets.QLineEdit(self.test_detail_box)
        self.dut_serial_number_edit.setGeometry(QtCore.QRect(width(150), height(120), width(151), height(20)))
        self.dut_serial_number_edit.setObjectName("dut_serial_number_edit")
        self.dut_serial_number_edit.setStyleSheet(
            "QLineEdit\n{\nbackground-color:rgba(0,0,0,0);\nborder:none;\nborder-bottom:2px solid rgba(42,226,230,255);\ncolor:rgba(255,255,255,255);\npadding-bottom:7px;\n}")
        self.dut_serial_number_edit.setPlaceholderText("System Serial Number")
        self.dut_serial_number_edit.setFont(self.font8_BF_UF_50)
        self.customer_name = QtWidgets.QLabel(self.test_detail_box)
        self.customer_name.setGeometry(QtCore.QRect(width(20), height(150), width(131), height(16)))
        self.customer_name.setStyleSheet("color:rgba(255,255,255,255)")
        self.customer_name.setFont(self.font11_BF_UF_50)
        self.customer_name.setObjectName("customer_name")
        self.associate_name = QtWidgets.QLabel(self.test_detail_box)
        self.associate_name.setGeometry(QtCore.QRect(width(20), height(180), width(131), height(16)))
        self.associate_name.setStyleSheet("color:rgba(255,255,255,255)")
        self.associate_name.setFont(self.font11_BF_UF_50)
        self.associate_name.setObjectName("associate_name")
        self.associate_name_edit = QtWidgets.QLineEdit(self.test_detail_box)
        self.associate_name_edit.setGeometry(QtCore.QRect(width(150), height(180), width(151), height(20)))
        self.associate_name_edit.setObjectName("associate_name_edit")
        self.associate_name_edit.setStyleSheet(
            "QLineEdit\n{\nbackground-color:rgba(0,0,0,0);\nborder:none;\nborder-bottom:2px solid rgba(42,226,230,255);\ncolor:rgba(255,255,255,255);\npadding-bottom:7px;\n}")
        self.associate_name_edit.setPlaceholderText("Enter Associate Name")
        self.associate_name_edit.setFont(self.font8_BF_UF_50)
        self.customer_name_edit = QtWidgets.QLineEdit(self.test_detail_box)
        self.customer_name_edit.setGeometry(QtCore.QRect(width(150), height(150), width(151), height(20)))
        self.customer_name_edit.setObjectName("customer_name_edit")
        self.customer_name_edit.setReadOnly(True)

        self.customer_name_edit.setStyleSheet(
            "QLineEdit\n{\nbackground-color:rgba(0,0,0,0);\nborder:none;\nborder-bottom:2px solid rgba(42,226,230,255);\ncolor:rgba(255,255,255,255);\npadding-bottom:7px;\n}")
        self.customer_name_edit.setPlaceholderText("Cust. Name will be shown here")

        self.customer_name_edit.setFont(self.font8_BF_UF_50)

        self.start_time_edit = QtWidgets.QLineEdit(self.test_detail_box)
        self.start_time_edit.setGeometry(QtCore.QRect(width(150), height(220), width(151), height(20)))
        self.start_time_edit.setObjectName("start_time_edit")
        self.start_time_edit.setReadOnly(True)

        self.start_time_edit.setStyleSheet(
            "QLineEdit\n{\nbackground-color:rgba(0,0,0,0);\nborder:none;\nborder-bottom:2px solid rgba(42,226,230,255);\ncolor:rgba(255,255,255,255);\npadding-bottom:7px;\n}")
        self.start_time_edit.setPlaceholderText("Start time of test")
        self.start_time_edit.setFont(self.font8_BF_UF_50)

        self.end_time_edit = QtWidgets.QLineEdit(self.test_detail_box)
        self.end_time_edit.setGeometry(QtCore.QRect(width(150), height(250), width(151), height(20)))
        self.end_time_edit.setObjectName("end_time_edit")
        self.end_time_edit.setReadOnly(True)

        self.end_time_edit.setStyleSheet(
            "QLineEdit\n{\nbackground-color:rgba(0,0,0,0);\nborder:none;\nborder-bottom:2px solid rgba(42,226,230,255);\ncolor:rgba(255,255,255,255);\npadding-bottom:7px;\n}")
        self.end_time_edit.setPlaceholderText("End time of test")
        self.end_time_edit.setFont(self.font8_BF_UF_50)

        self.end_time = QtWidgets.QLabel(self.test_detail_box)
        self.end_time.setGeometry(QtCore.QRect(width(20), height(250), width(141), height(16)))
        self.end_time.setStyleSheet("color:rgba(255,255,255,255)")
        self.end_time.setFont(self.font11_BF_UF_50)
        self.end_time.setObjectName("end_time")
        self.start_time = QtWidgets.QLabel(self.test_detail_box)
        self.start_time.setGeometry(QtCore.QRect(width(20), height(220), width(161), height(16)))
        self.start_time.setFont(self.font11_BF_UF_50)
        self.start_time.setObjectName("start_time")
        self.start_time.setStyleSheet("color:rgba(255,255,255,255)")
        self.barcode_check = QtWidgets.QCheckBox(self.test_detail_box)
        self.barcode_check.setGeometry(QtCore.QRect(width(20), height(30), width(91), height(17)))
        self.barcode_check.setObjectName("barcode_check")
        self.barcode_check.setFont(self.font11_BF_UF_50)
        self.barcode_check.setStyleSheet("color:rgba(255,255,255,255)")

        self.custom_check = QtWidgets.QCheckBox(self.test_detail_box)
        self.custom_check.setGeometry(QtCore.QRect(width(20), height(300), width(141), height(21)))
        self.custom_check.setFont(self.font11_BF_UF_50)
        self.custom_check.setStyleSheet("color:rgba(255,255,255,255)")
        self.custom_check.setObjectName("custom_check")
        self.manual_checkbox = QtWidgets.QCheckBox(self.test_detail_box)
        self.manual_checkbox.setGeometry(QtCore.QRect(width(165), height(300), width(151), height(21)))
        # self.manual_checkbox.setStyleSheet("QCheckBox::indicator { width: 50px; height: 50px;}")
        self.manual_checkbox.setFont(self.font11_BF_UF_50)
        self.manual_checkbox.setStyleSheet("color:rgba(255,255,255,255)")
        self.manual_checkbox.setObjectName("manual_checkbox")
        self.start = QtWidgets.QPushButton(self.test_detail_box)
        self.start.setGeometry(QtCore.QRect(width(0), height(335), width(330), height(41)))
        font = QtGui.QFont()
        font.setPointSize(width(15))
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(width(75))
        self.start.setStyleSheet(
            "QPushButton{\nbackground-color:rgba(42,226,230,255);\nfont: 75 25pt 'MS Shell Dlg 2';\nborder-bottom-left-radius:0px;\n}\nQPushButton::hover{\nfont: 75 35pt 'MS Shell Dlg 2';\nbackground-color:rgba(42,226,230,255);\n}\nQPushButton::pressed{\nfont: 75 35pt 'MS Shell Dlg 2';\nbackground-color:rgba(42,226,230,255);\npadding-top:10px;\n}")
        self.start.setFont(font)
        # self.start.setToolTip("Starts the test")
        self.start.setObjectName("start")
        self.start.clicked.connect(self.start_function)
        self.stop = QtWidgets.QPushButton(self.test_detail_box)
        self.stop.setGeometry(QtCore.QRect(width(0), height(390), width(330), height(41)))
        font = QtGui.QFont()
        font.setPointSize(width(15))
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(width(75))
        self.stop.setFont(font)
        self.stop.setObjectName("stop")
        self.stop.setStyleSheet(
            "QPushButton{\nbackground-color:rgba(42,226,230,255);\nfont: 75 25pt 'MS Shell Dlg 2';\nborder-bottom-left-radius:5fpx;\n}\nQPushButton::hover{\nfont: 75 35pt 'MS Shell Dlg 2';\nbackground-color:rgba(42,226,230,255);\n}\nQPushButton::pressed{\nfont: 75 35pt 'MS Shell Dlg 2';\nbackground-color:rgba(42,226,230,255);\npadding-top:10px;\n}")
        self.stop.clicked.connect(self.stop_function)

        """
        FONT FOR TEST ITEM GROUP BOX
        """

        self.font11_UF = QtGui.QFont()
        self.font11_UF.setPointSize(width(11))
        self.font11_UF.setUnderline(False)

        self.test_item_box = QtWidgets.QGroupBox(self.centralwidget)
        self.test_item_box.setGeometry(QtCore.QRect(width(410), height(105), width(521), height(566)))
        self.test_item_box.setFont(self.font11_BF_UF_50)
        self.test_item_box.setStyleSheet(
            "QGroupBox{border:5px solid black; border-top-left-radius:80px; border-bottom-right-radius:80px; border-top-right-radius:8px; border-bottom-left-radius:8px;}")
        self.test_item_box.setObjectName("test_item_box")
        self.test_item_label = QtWidgets.QLabel(self.test_item_box)
        self.test_item_label.setGeometry(QtCore.QRect(width(70), height(50), width(101), height(16)))
        self.test_item_label.setFont(self.font11_UF)
        self.test_item_label.setObjectName("test_item_label")
        self.status_label = QtWidgets.QLabel(self.test_item_box)
        self.status_label.setGeometry(QtCore.QRect(width(430), height(50), width(61), height(21)))
        self.status_label.setFont(self.font11_UF)
        self.status_label.setObjectName("status_label")
        self.serial_label = QtWidgets.QLabel(self.test_item_box)
        self.serial_label.setGeometry(QtCore.QRect(width(10), height(50), width(41), height(16)))
        self.serial_label.setFont(self.font11_UF)
        self.serial_label.setObjectName("serial_label")
        self.serial1 = QtWidgets.QLabel(self.test_item_box)
        self.serial1.setGeometry(QtCore.QRect(width(20), height(80), width(21), height(31)))
        self.serial1.setFont(self.font11_UF)
        self.serial1.setObjectName("serial1")
        self.controller_health_label = QtWidgets.QLabel(self.test_item_box)
        self.controller_health_label.setGeometry(QtCore.QRect(width(70), height(85), width(121), height(21)))
        self.controller_health_label.setFont(self.font11_UF)
        self.controller_health_label.setObjectName("controller_health_label")
        self.controller_health_status = QtWidgets.QLabel(self.test_item_box)
        self.controller_health_status.setGeometry(QtCore.QRect(width(430), height(80), width(61), height(31)))
        self.controller_health_status.setFont(self.font11_UF)
        self.controller_health_status.setObjectName("controller_health_status")
        self.serial2 = QtWidgets.QLabel(self.test_item_box)
        self.serial2.setGeometry(QtCore.QRect(width(20), height(110), width(21), height(31)))
        self.serial2.setObjectName("serial2")
        self.serial2.setFont(self.font11_UF)
        self.serial3 = QtWidgets.QLabel(self.test_item_box)
        self.serial3.setGeometry(QtCore.QRect(width(20), height(140), width(21), height(31)))
        self.serial3.setObjectName("serial3")
        self.serial3.setFont(self.font11_UF)
        self.serial4 = QtWidgets.QLabel(self.test_item_box)
        self.serial4.setGeometry(QtCore.QRect(width(20), height(170), width(21), height(31)))
        self.serial4.setObjectName("serial4")
        self.serial4.setFont(self.font11_UF)
        self.serial5 = QtWidgets.QLabel(self.test_item_box)
        self.serial5.setGeometry(QtCore.QRect(width(20), height(200), width(21), height(31)))
        self.serial5.setObjectName("serial5")
        self.serial5.setFont(self.font11_UF)
        self.serial6 = QtWidgets.QLabel(self.test_item_box)
        self.serial6.setGeometry(QtCore.QRect(width(20), height(230), width(21), height(31)))
        self.serial6.setObjectName("serial6")
        self.serial6.setFont(self.font11_UF)
        self.serial7 = QtWidgets.QLabel(self.test_item_box)
        self.serial7.setGeometry(QtCore.QRect(width(20), height(260), width(21), height(31)))
        self.serial7.setObjectName("serial7")
        self.serial7.setFont(self.font11_UF)
        self.serial8 = QtWidgets.QLabel(self.test_item_box)
        self.serial8.setGeometry(QtCore.QRect(width(20), height(290), width(21), height(31)))
        self.serial8.setObjectName("serial8")
        self.serial8.setFont(self.font11_UF)
        self.serial9 = QtWidgets.QLabel(self.test_item_box)
        self.serial9.setGeometry(QtCore.QRect(width(20), height(320), width(21), height(31)))
        self.serial9.setObjectName("serial9")
        self.serial9.setFont(self.font11_UF)
        self.serial10 = QtWidgets.QLabel(self.test_item_box)
        self.serial10.setGeometry(QtCore.QRect(width(20), height(350), width(21), height(31)))
        self.serial10.setObjectName("serial10")
        self.serial10.setFont(self.font11_UF)
        self.serial11 = QtWidgets.QLabel(self.test_item_box)
        self.serial11.setGeometry(QtCore.QRect(width(20), height(380), width(21), height(31)))
        self.serial11.setObjectName("serial11")
        self.serial11.setFont(self.font11_UF)
        self.unit_comm_label = QtWidgets.QLabel(self.test_item_box)
        self.unit_comm_label.setGeometry(QtCore.QRect(width(70), height(110), width(141), height(31)))
        self.unit_comm_label.setFont(self.font11_UF)
        self.unit_comm_label.setObjectName("unit_comm_label")
        self.temp_label = QtWidgets.QLabel(self.test_item_box)
        self.temp_label.setGeometry(QtCore.QRect(width(70), height(140), width(191), height(31)))
        self.temp_label.setFont(self.font11_UF)
        self.temp_label.setObjectName("temp_label")
        self.output_pfc_label = QtWidgets.QLabel(self.test_item_box)
        self.output_pfc_label.setGeometry(QtCore.QRect(width(70), height(170), width(121), height(31)))
        self.output_pfc_label.setFont(self.font11_UF)
        self.output_pfc_label.setObjectName("output_pfc_label")
        self.input_pfc_label = QtWidgets.QLabel(self.test_item_box)
        self.input_pfc_label.setGeometry(QtCore.QRect(width(70), height(200), width(121), height(31)))
        self.input_pfc_label.setFont(self.font11_UF)
        self.input_pfc_label.setObjectName("input_pfc_label")
        self.dc_voltage_check_label = QtWidgets.QLabel(self.test_item_box)
        self.dc_voltage_check_label.setGeometry(QtCore.QRect(width(70), height(230), width(171), height(31)))
        self.dc_voltage_check_label.setFont(self.font11_UF)
        self.dc_voltage_check_label.setObjectName("dc_voltage_check_label")
        self.dc_voltage_calib_label = QtWidgets.QLabel(self.test_item_box)
        self.dc_voltage_calib_label.setGeometry(QtCore.QRect(width(70), height(260), width(241), height(31)))
        self.dc_voltage_calib_label.setFont(self.font11_UF)
        self.dc_voltage_calib_label.setObjectName("dc_voltage_calib_label")
        self.dc_current_check_discharge_label = QtWidgets.QLabel(self.test_item_box)
        self.dc_current_check_discharge_label.setGeometry(QtCore.QRect(width(70), height(290), height(251), height(31)))
        self.dc_current_check_discharge_label.setFont(self.font11_UF)
        self.dc_current_check_discharge_label.setObjectName("dc_current_check_discharge_label")
        self.smr_register_label = QtWidgets.QLabel(self.test_item_box)
        self.smr_register_label.setGeometry(QtCore.QRect(width(70), height(320), width(121), height(31)))
        self.smr_register_label.setFont(self.font11_UF)
        self.smr_register_label.setObjectName("smr_register_label")
        self.dc_current_check_charge_label = QtWidgets.QLabel(self.test_item_box)
        self.dc_current_check_charge_label.setGeometry(QtCore.QRect(width(70), height(350), width(241), height(31)))
        self.dc_current_check_charge_label.setFont(self.font11_UF)
        self.dc_current_check_charge_label.setObjectName("dc_current_check_charge_label")
        self.dc_current_calib_label = QtWidgets.QLabel(self.test_item_box)
        self.dc_current_calib_label.setGeometry(QtCore.QRect((width(70)), height(380), width(241), height(31)))
        self.dc_current_calib_label.setFont(self.font11_UF)
        self.dc_current_calib_label.setObjectName("dc_current_calib_label")
        self.lvd_label = QtWidgets.QLabel(self.test_item_box)
        self.lvd_label.setGeometry(QtCore.QRect(width(70), height(410), width(111), height(31)))
        self.lvd_label.setFont(self.font11_UF)
        self.lvd_label.setObjectName("lvd_label")
        self.ac_phase_label = QtWidgets.QLabel(self.test_item_box)
        self.ac_phase_label.setGeometry(QtCore.QRect(width(70), height(440), width(131), height(31)))
        self.ac_phase_label.setFont(self.font11_UF)
        self.ac_phase_label.setObjectName("ac_phase_label")
        self.current_sharing_label = QtWidgets.QLabel(self.test_item_box)
        self.current_sharing_label.setGeometry(QtCore.QRect(width(70), height(470), width(181), height(31)))
        self.current_sharing_label.setFont(self.font11_UF)
        self.current_sharing_label.setObjectName("current_sharing_label")
        self.rs485_label = QtWidgets.QLabel(self.test_item_box)
        self.rs485_label.setGeometry(QtCore.QRect(width(70), height(500), width(71), height(31)))
        self.rs485_label.setFont(self.font11_UF)
        self.rs485_label.setObjectName("rs485_label")
        self.default_label = QtWidgets.QLabel(self.test_item_box)
        self.default_label.setGeometry(QtCore.QRect(width(70), height(530), width(61), height(31)))
        self.default_label.setFont(self.font11_UF)
        self.default_label.setObjectName("default_label")
        self.serial12 = QtWidgets.QLabel(self.test_item_box)
        self.serial12.setGeometry(QtCore.QRect(width(20), height(410), width(21), height(31)))
        self.serial12.setObjectName("serial12")
        self.serial12.setFont(self.font11_UF)
        self.serial13 = QtWidgets.QLabel(self.test_item_box)
        self.serial13.setGeometry(QtCore.QRect(width(20), height(440), width(21), height(31)))
        self.serial13.setObjectName("serial13")
        self.serial13.setFont(self.font11_UF)
        self.serial14 = QtWidgets.QLabel(self.test_item_box)
        self.serial14.setGeometry(QtCore.QRect(width(20), height(470), width(21), height(31)))
        self.serial14.setObjectName("serial14")
        self.serial14.setFont(self.font11_UF)
        self.serial15 = QtWidgets.QLabel(self.test_item_box)
        self.serial15.setGeometry(QtCore.QRect(width(20), height(500), width(21), height(31)))
        self.serial15.setObjectName("serial15")
        self.serial15.setFont(self.font11_UF)
        self.serial16 = QtWidgets.QLabel(self.test_item_box)
        self.serial16.setGeometry(QtCore.QRect(width(20), height(530), width(21), height(31)))
        self.serial16.setObjectName("serial16")
        self.serial16.setFont(self.font11_UF)
        self.unit_comm_status = QtWidgets.QLabel(self.test_item_box)
        self.unit_comm_status.setGeometry(QtCore.QRect(width(430), height(110), width(61), height(31)))
        self.unit_comm_status.setFont(self.font11_UF)
        self.unit_comm_status.setObjectName("unit_comm_status")
        self.temp_status = QtWidgets.QLabel(self.test_item_box)
        self.temp_status.setGeometry(QtCore.QRect(width(430), height(140), width(61), height(31)))
        self.temp_status.setFont(self.font11_UF)
        self.temp_status.setObjectName("temp_status")
        self.output_pfc_status = QtWidgets.QLabel(self.test_item_box)
        self.output_pfc_status.setGeometry(QtCore.QRect(width(430), height(170), width(61), height(31)))
        self.output_pfc_status.setFont(self.font11_UF)
        self.output_pfc_status.setObjectName("output_pfc_status")
        self.input_pfc_status = QtWidgets.QLabel(self.test_item_box)
        self.input_pfc_status.setGeometry(QtCore.QRect(width(430), height(200), width(61), height(31)))
        self.input_pfc_status.setFont(self.font11_UF)
        self.input_pfc_status.setObjectName("input_pfc_status")
        self.dc_voltage_check_status = QtWidgets.QLabel(self.test_item_box)
        self.dc_voltage_check_status.setGeometry(QtCore.QRect(width(430), height(230), width(61), height(31)))
        self.dc_voltage_check_status.setFont(self.font11_UF)
        self.dc_voltage_check_status.setObjectName("dc_voltage_check_status")
        self.dc_voltage_calib_status = QtWidgets.QLabel(self.test_item_box)
        self.dc_voltage_calib_status.setGeometry(QtCore.QRect(width(430), height(260), width(61), height(31)))
        self.dc_voltage_calib_status.setFont(self.font11_UF)
        self.dc_voltage_calib_status.setObjectName("dc_voltage_calib_status")
        self.dc_current_check_discharge_status = QtWidgets.QLabel(self.test_item_box)
        self.dc_current_check_discharge_status.setGeometry(QtCore.QRect(width(430), height(290), width(61), height(31)))
        self.dc_current_check_discharge_status.setFont(self.font11_UF)
        self.dc_current_check_discharge_status.setObjectName("dc_current_check_discharge_status")
        self.smr_register_status = QtWidgets.QLabel(self.test_item_box)
        self.smr_register_status.setGeometry(QtCore.QRect(width(430), height(320), width(61), height(31)))
        self.smr_register_status.setFont(self.font11_UF)
        self.smr_register_status.setObjectName("smr_register_status")
        self.dc_current_check_charge_status = QtWidgets.QLabel(self.test_item_box)
        self.dc_current_check_charge_status.setGeometry(QtCore.QRect(width(430), height(350), width(61), height(31)))
        self.dc_current_check_charge_status.setFont(self.font11_UF)
        self.dc_current_check_charge_status.setObjectName("dc_current_check_charge_status")
        self.dc_current_calib_status = QtWidgets.QLabel(self.test_item_box)
        self.dc_current_calib_status.setGeometry(QtCore.QRect(width(430), height(380), width(61), height(31)))
        self.dc_current_calib_status.setFont(self.font11_UF)
        self.dc_current_calib_status.setObjectName("dc_current_calib_status")
        self.lvd_status = QtWidgets.QLabel(self.test_item_box)
        self.lvd_status.setGeometry(QtCore.QRect(width(430), height(410), width(61), height(31)))
        self.lvd_status.setFont(self.font11_UF)
        self.lvd_status.setObjectName("lvd_status")
        self.ac_phase_status = QtWidgets.QLabel(self.test_item_box)
        self.ac_phase_status.setGeometry(QtCore.QRect(width(430), height(440), width(61), height(31)))
        self.ac_phase_status.setFont(self.font11_UF)
        self.ac_phase_status.setObjectName("ac_phase_status")
        self.current_sharing_status = QtWidgets.QLabel(self.test_item_box)
        self.current_sharing_status.setGeometry(QtCore.QRect(width(430), height(470), width(61), height(31)))
        self.current_sharing_status.setFont(self.font11_UF)
        self.current_sharing_status.setObjectName("current_sharing_status")
        self.default_status = QtWidgets.QLabel(self.test_item_box)
        self.default_status.setGeometry(QtCore.QRect(width(430), height(530), width(61), height(31)))
        self.default_status.setFont(self.font11_UF)
        self.default_status.setObjectName("default_status")
        self.rs485_status = QtWidgets.QLabel(self.test_item_box)
        self.rs485_status.setGeometry(QtCore.QRect(width(430), height(500), width(61), height(31)))
        self.rs485_status.setFont(self.font11_UF)
        self.rs485_status.setObjectName("rs485_status")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(width(980), height(80), width(341), height(481)))
        self.frame.setObjectName("frame_window")
        self.frame.setStyleSheet(
            "QFrame {\nborder-top-right-radius: 50px;\nbackground-color:rgba(240,240,240,255);\nborder-bottom-right-radius: 50px;\n}\n")

        self.log_window = QtWidgets.QTextBrowser(self.frame)
        self.log_window.setGeometry(QtCore.QRect(width(0), height(0), width(341), height(481)))
        self.log_window.setObjectName("log_window")
        self.log_window.setStyleSheet(
            "QTextBrowser{\nborder:2px solid black;\nborder-top-left-radius:20px;\nborder-top-right-radius:20px;\nborder-bottom-left-radius:20px;\nborder-bottom-right-radius:20px;\n}")
        self.test_log = QtWidgets.QLabel(self.centralwidget)
        self.test_log.setGeometry(QtCore.QRect(width(985), height(42), width(101), height(41)))
        self.test_log.setFont(self.font11_BF_UF_50)
        self.test_log.setOpenExternalLinks(True)
        self.test_log.setObjectName("test_log")

        self.report = QtWidgets.QLabel(self.centralwidget)
        self.report.setGeometry(QtCore.QRect(width(1120), height(40), width(130), height(41)))
        self.report.setFont(self.font11_BF_UF_50)
        self.report.setStyleSheet("QLabel{color:Blue;}")
        self.report.mousePressEvent = self.report_function
        self.report.setObjectName("test_log")

        self.log_clear = QtWidgets.QPushButton(self.centralwidget)
        self.log_clear.setGeometry(QtCore.QRect(width(1240), height(50), width(75), height(23)))
        self.log_clear.setFont(self.font11_BF_UF_50)
        self.log_clear.setStyleSheet(
            "QPushButton{\nbackground-color:rgba(42,226,230,255);\nborder-bottom-left-radius:0px;border:2px solid black;\n"
            "border-top-left-radius:15px;border-bottom-right-radius:15px;}QPushButton::pressed{padding-top:5px;}")

        self.log_clear.setObjectName("log_clear")
        # self.final_status_box = QtWidgets.QGroupBox(self.centralwidget)
        # self.final_status_box.setGeometry(QtCore.QRect(width(980), height(580), width(341), height(71)))
        # self.final_status_box.setTitle("")
        # self.final_status_box.setObjectName("final_status_box")
        self.final_status = QtWidgets.QLabel(self.centralwidget)
        self.final_status.setGeometry(QtCore.QRect(width(980), height(580), width(341), height(71)))
        font = QtGui.QFont()
        font.setPointSize(width(28))
        font.setBold(True)
        font.setWeight(width(75))
        self.final_status.setFont(font)
        self.final_status.setStyleSheet("QLabel{border:5px solid black; border-radius:40px;}")
        self.final_status.setScaledContents(True)
        self.final_status.setAlignment(QtCore.Qt.AlignCenter)
        self.final_status.setObjectName("final_status")
        self.ate_logo = QtWidgets.QLabel(self.centralwidget)
        self.ate_logo.setGeometry(QtCore.QRect(width(70), height(50), width(251), height(71)))
        self.ate_logo.setText("")
        self.ate_logo.setPixmap(QtGui.QPixmap(f"{gui_global.image_directory_location}exicome logo.png"))
        self.ate_logo.setScaledContents(True)
        # self.ate_logo.setStyleSheet("QLabel{border:2px solid black; border-bottom-right-radius:50px; border-top-left-radius:50px}")
        self.ate_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.ate_logo.setObjectName("ate_logo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        try:
            test_mode = SettingRead('TEST MODE')['test_mode']
            if test_mode == "test":
                self.system_part_no_edit.setText("HE517512")
                self.dut_serial_number_edit.setText("123456789012345")
                self.associate_name_edit.setText("Paras")
        except Exception:
            pass

        CanModule.CAN.CAN_WRITE_SOLO(CanModule.CAN, 0, 0x208, [0x60B,0,0, 43, 00, 32, 00, 00, 20, 00, 00])


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        global ate_name
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", ""))
        self.heading.setText(_translate("MainWindow", "Power Plant Production ATS"))
        self.test_detail_box.setTitle(_translate("MainWindow", ""))
        self.test_id.setText(_translate("MainWindow", "Test ID"))
        self.system_part_no.setText(_translate("MainWindow", "System Part No."))
        self.dut_serial_number.setText(_translate("MainWindow", "DUT Serial No."))
        self.customer_name.setText(_translate("MainWindow", "Customer Name"))
        self.associate_name.setText(_translate("MainWindow", "Associate Name"))
        self.end_time.setText(_translate("MainWindow", "End Time"))
        self.start_time.setText(_translate("MainWindow", "Start Time"))
        self.barcode_check.setText(_translate("MainWindow", "Bar Code"))
        self.custom_check.setText(_translate("MainWindow", "Custom Settings"))
        self.manual_checkbox.setText(_translate("MainWindow", "Manual Resources"))
        self.start.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.start.setText(_translate("MainWindow", "START"))
        self.stop.setText(_translate("MainWindow", "STOP"))
        self.test_item_box.setTitle(_translate("MainWindow", "Test Program"))
        self.test_item_label.setText(_translate("MainWindow", "Test Item"))
        self.status_label.setText(_translate("MainWindow", "Status"))
        self.serial_label.setText(_translate("MainWindow", "S No."))
        self.serial1.setText(_translate("MainWindow", "1"))
        self.controller_health_label.setText(_translate("MainWindow", "Controller Health"))
        self.controller_health_status.setText(_translate("MainWindow", "Pending"))
        self.serial2.setText(_translate("MainWindow", "2"))
        self.serial3.setText(_translate("MainWindow", "3"))
        self.serial4.setText(_translate("MainWindow", "4"))
        self.serial5.setText(_translate("MainWindow", "5"))
        self.serial6.setText(_translate("MainWindow", "6"))
        self.serial7.setText(_translate("MainWindow", "7"))
        self.serial8.setText(_translate("MainWindow", "8"))
        self.serial9.setText(_translate("MainWindow", "9"))
        self.serial10.setText(_translate("MainWindow", "10"))
        self.serial11.setText(_translate("MainWindow", "11"))
        self.unit_comm_label.setText(_translate("MainWindow", "Unit Communication"))
        self.temp_label.setText(_translate("MainWindow", "Temperature Measurement"))
        self.output_pfc_label.setText(_translate("MainWindow", "Output PFC"))
        self.input_pfc_label.setText(_translate("MainWindow", "Input PFC"))
        self.dc_voltage_check_label.setText(_translate("MainWindow", "DC Voltage Measurement"))
        self.dc_voltage_calib_label.setText(_translate("MainWindow", "DC Voltage Calibration/Verification"))
        self.dc_current_check_discharge_label.setText(_translate("MainWindow", "DC Current Measurement (Discharge)"))
        self.smr_register_label.setText(_translate("MainWindow", "SMR Registration"))
        self.dc_current_check_charge_label.setText(_translate("MainWindow", "DC Current Measurement (Charge)"))
        self.dc_current_calib_label.setText(_translate("MainWindow", "DC Current Calibration/Verification"))
        self.lvd_label.setText(_translate("MainWindow", "LVD Contactor"))
        self.ac_phase_label.setText(_translate("MainWindow", "AC Phase Allocation"))
        self.current_sharing_label.setText(_translate("MainWindow", "Current Sharing / Bus Drop"))
        self.rs485_label.setText(_translate("MainWindow", "RS485"))
        self.default_label.setText(_translate("MainWindow", "Default"))
        self.serial12.setText(_translate("MainWindow", "12"))
        self.serial13.setText(_translate("MainWindow", "13"))
        self.serial14.setText(_translate("MainWindow", "14"))
        self.serial15.setText(_translate("MainWindow", "15"))
        self.serial16.setText(_translate("MainWindow", "16"))
        self.unit_comm_status.setText(_translate("MainWindow", "Pending"))
        self.temp_status.setText(_translate("MainWindow", "Pending"))
        self.output_pfc_status.setText(_translate("MainWindow", "Pending"))
        self.input_pfc_status.setText(_translate("MainWindow", "Pending"))
        self.dc_voltage_check_status.setText(_translate("MainWindow", "Pending"))
        self.dc_voltage_calib_status.setText(_translate("MainWindow", "Pending"))
        self.dc_current_check_discharge_status.setText(_translate("MainWindow", "Pending"))
        self.smr_register_status.setText(_translate("MainWindow", "Pending"))
        self.dc_current_check_charge_status.setText(_translate("MainWindow", "Pending"))
        self.dc_current_calib_status.setText(_translate("MainWindow", "Pending"))
        self.lvd_status.setText(_translate("MainWindow", "Pending"))
        self.ac_phase_status.setText(_translate("MainWindow", "Pending"))
        self.current_sharing_status.setText(_translate("MainWindow", "Pending"))
        self.default_status.setText(_translate("MainWindow", "Pending"))
        self.rs485_status.setText(_translate("MainWindow", "Pending"))
        self.test_log.setText(
            _translate("MainWindow", f"<a href='file:{gui_global.directory_location}logs'>Log Folder</a>"))
        self.report.setText(_translate("MainWindow", "Reports"))
        self.log_clear.setText(_translate("MainWindow", "Log Clear"))
        self.final_status.setText(_translate("MainWindow", ""))
        self.start.setToolTip(_translate("MainWindow", "Starts the test"))
        self.prompt = Prompt()
        self.M2000 = M2000.M2000CommandSet()
        self.pfc = PFC_control_done.pfc_control()
        self.contact = PFC_control_done.pfc_control()

        self.dcload = CommandSetDcLoadUsb
        self.smrcan = CommandSetSmrBatteryCan

        # self.dcload.DC_LOAD.OPEN_DC_LOAD(self.dcload.DC_LOAD)
        # self.dcload.DC_LOAD_SET_CURRENT_CC(5)

    def dut_serial_check(self):
        global customer_name
        self.associate_name_edit.setText(self.associate_name_edit.text().upper())
        self.system_part_no_edit.setText(self.system_part_no_edit.text().upper())
        self.dut_serial_number_edit.setText(self.dut_serial_number_edit.text().upper())
        self.associate_name = self.associate_name_edit.text()
        self.part_number = self.system_part_no_edit.text()
        self.serial_number = self.dut_serial_number_edit.text()
        name_check = False
        part_check = False
        serial_check = False
        if self.associate_name == "":
            self.prompt.Message("Error!", "Kindly enter NAME to proceed!")
        else:
            name_check = True
            if self.part_number == "":
                self.prompt.Message("Error!", "Kindly enter HE-Part Code")
            else:
                if len(self.part_number) == 8:
                    with open(f"{gui_global.files_directory_location}customer_detail.csv", 'r') as file:
                        lines = file.readlines()
                    not_found = True
                    self.config_version_list = []
                    for i in lines:
                        if self.part_number == i.split(",")[0]:
                            not_found = False
                            self.customer_name = i.split(",")[2]
                            self.config_version_list.append(float(i.split(",")[1]))
                            self.mcm_type = i.split(",")[3].split("\n")[0]
                            if self.mcm_type == "M1000":
                                self.mcm_type = 1
                            elif self.mcm_type == "M2000":
                                self.mcm_type = 2
                            print(f"Type of MCM is: {self.mcm_type}")
                    if not_found:
                        self.prompt.Message("Warning!", "HE Part Code not found in Database!")
                    else:
                        self.customer_name_edit.setText(str(self.customer_name))
                        part_check = True
                        if self.serial_number == "":
                            self.prompt.Message("Error!", "Kindly enter/ scan system serial number")
                        else:
                            if len(self.serial_number) == 15:
                                serial_check = True
                            else:
                                self.prompt.Message("Warning!", "Kindly enter correct length of Serial Number")
                else:
                    self.prompt.Message("Warning!", "Kindly enter correct length of Part Code")

        if name_check and serial_check and part_check:
            self.test_id_edit.setText(SettingRead("TEST ID")['count'])
            self.configversion = max(self.config_version_list)
            count = int(float(self.test_id_edit.text())) + 1
            config.read(f"{gui_global.files_directory_location}setting.txt")
            SectionCall = config['TEST ID']
            for option in SectionCall:
                SectionCall[option] = str(count)

            with open(f"{gui_global.files_directory_location}setting.txt", 'w') as configfile:
                config.write(configfile)

            self.start_time_edit.setText(str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
            return True
        else:
            return False

    def stop_function(self):
        self.end_time_edit.setText(str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

    def initials(self):
        self.final_status.setText("")
        self.final_status.setStyleSheet("QLabel{border:5px solid black; border-radius:40px;}")
        self.controller_health_status.setText("Pending")
        self.controller_health_status.setStyleSheet("")
        self.unit_comm_status.setText("Pending")
        self.unit_comm_status.setStyleSheet("")
        self.temp_status.setText("Pending")
        self.temp_status.setStyleSheet("")
        self.output_pfc_status.setText("Pending")
        self.output_pfc_status.setStyleSheet("")
        self.input_pfc_status.setText("Pending")
        self.input_pfc_status.setStyleSheet("")
        self.dc_voltage_check_status.setText("Pending")
        self.dc_voltage_calib_status.setText("Pending")
        self.dc_voltage_check_status.setStyleSheet("")
        self.dc_voltage_calib_status.setStyleSheet("")
        self.dc_current_check_discharge_status.setText("Pending")
        self.dc_current_check_discharge_status.setStyleSheet("")
        self.smr_register_status.setText("Pending")
        self.smr_register_status.setStyleSheet("")
        self.dc_current_check_charge_status.setText("Pending")
        self.dc_current_check_charge_status.setStyleSheet("")
        self.dc_current_calib_status.setText("Pending")
        self.dc_current_calib_status.setStyleSheet("")
        self.lvd_status.setText("Pending")
        self.lvd_status.setStyleSheet("")
        self.ac_phase_status.setText("Pending")
        self.ac_phase_status.setStyleSheet("")
        self.current_sharing_status.setText("Pending")
        self.current_sharing_status.setStyleSheet("")
        self.rs485_status.setText("Pending")
        self.rs485_status.setStyleSheet("")
        self.default_status.setText("Pending")
        self.default_status.setStyleSheet("")
        self.log_window.clear()

    def test_detail_clear(self):
        self.test_id_edit.clear()
        self.system_part_no_edit.clear()
        self.dut_serial_number_edit.clear()
        self.customer_name_edit.clear()
        self.associate_name_edit.clear()

    def start_function(self):

        """
        This function starts and handles the test script with final result status, Log and Report Creation

        final_output: list ==> shows test cases result, initially BLANK
        test_detail_flag: bool ==> Result of details in Test Details Box are correctly filled
        testing_flag: bool ==> signifies the status of IS TESTING ACTIVE, initially TRUE
        """
        self.test_order = test_order_done.Ui_Form.get_values(test_order_done.Ui_Form)
        self.start.setDisabled(True)
        global final_output
        testing_flag = True

        CanModule.CAN.CAN_WRITE_SOLO(CanModule.CAN, 0, 0x208, [0x60B, 0, 0, 43, 00, 32, 00, 00, 18, 00, 00])

        test_detail_flag = self.dut_serial_check()

        if test_detail_flag:
            '''Set the initials to default before starting the testing'''

            self.initials()
            # self.physical_check(BYPASS=True)
            self.prompt.Message(prompt="Switch OFF Load MCBs/ Battery MCBs/ Remove Fuses/ SMR MCBs")

            self.print_console(f'DUT PART NUMBER: {self.part_number}')
            self.print_console(f'DUT SERIAL NUMBER: {self.serial_number}')
            self.print_console(f'CUSTOMER NAME: {self.customer_name_edit.text()}')
            if self.part_number == "HE517553" or self.part_number == "HE517610":
                self.print_console(f"SOFTWARE VERSION: {self.configversion}")
            else:
                self.print_console(f"CONFIGURATION FILE VERSION: {self.configversion}")
            self.print_console(f"TEST START DATE TIME: {get_date_time(date=1, time=1)}")
            self.print_console(f"ASSOCIATE NAME: {self.associate_name_edit.text()}")

            print(f"Test detail flag: {test_detail_flag}")  # Shows Boolean expression of test_detail_flag

            '''Starting testing'''
            self.excel_handler = CSVHandler(os.path.join(gui_global.directory_location + "/records/", "active_" + str(SettingRead("STATION")['id']) + ".csv"))
            value = self.excel_handler.get_last_row_first_column_value() or "0"
            value = value if value != "SR NO" else "0"
            # Incrementing the value by 1
            last_cell = int(value) + 1

            # Generating bulk upload data
            bulk_upload = [str(last_cell)] + ["FAIL"] * (len(self.excel_handler.get_headers()) - 1)

            self.excel_handler.append_row(bulk_upload)


            while testing_flag:
                final_output = []
                for i in range(1, len(self.test_order) + 1):

                    function_status = self.run_test(i)  # Running test sequences

                    print(
                        f"Test Number {i} : {function_status}")  # Display the status of the last function block tested

                    '''Keeping/ Storing the status of last function block tested'''

                    if function_status:
                        final_output.append(function_status)

                    else:
                        user_response = self.prompt.User_prompt("Do you want to skip\nthis test and continue?")
                        if user_response:
                            testing_flag = True
                            final_output.append(function_status)
                        else:
                            final_output.append(function_status)
                            testing_flag = False
                            break  # terminating test loop if USER wishes not to continue the test

                    '''Terminating test loop when all tests are performed'''
                    if i == 16:
                        testing_flag = False
                        print(final_output)
                        break

            console_output_flag = True
            for results in final_output:
                if results == False:
                    console_output_flag = False

            if all(final_output):
                self.final_status.setText("PASS")
                # self.final_status.setStyleSheet("QLabel{border:5px solid black; border-radius:40px;}")
                self.final_status.setFont(QtGui.QFont("Calibri", 60))
                self.final_status.setStyleSheet("QLabel{border:5px solid black; border-radius:40px;color:DARKGREEN;}")
                self.excel_handler.update_cell("RESULT", "PASS")
            else:
                self.final_status.setText("FAIL")
                # self.final_status.setStyleSheet("QLabel{border:5px solid black; border-radius:40px;}")
                self.final_status.setFont(QtGui.QFont("Calibri", 60))
                self.final_status.setStyleSheet("QLabel{border:5px solid black; border-radius:40px;color:RED;}")
                self.excel_handler.update_cell("RESULT", "FAIL")
            self.shadowFunction(self.final_status, (0, 0, 0, 255), 35, (10, 10))

            self.end_time_edit.setText(str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

            self.log()
        else:
            self.prompt.Message("Error!", "Kindly complete Test Details")

        self.start.setDisabled(False)

        CanModule.CAN.CAN_WRITE_SOLO(CanModule.CAN, 0, 0x208, [0x60B, 0, 0, 43, 00, 32, 00, 00, 20, 00, 00])

    def shadowFunction(self, element, colors_alpha=(0, 0, 0, 0), blurRadius=0, offset=(0, 0)):
        effect = QGraphicsDropShadowEffect()
        effect.setBlurRadius(blurRadius)
        effect.setColor(QColor(colors_alpha[0], colors_alpha[1], colors_alpha[2], colors_alpha[3]))
        effect.setOffset(offset[0], offset[1])
        element.setGraphicsEffect(effect)

    def run_test(self, test_number):
        if test_number == int(self.test_order[0]):
            # controller_health_check_variable = self.prompt.User_prompt("Do you want to pass this test and continue?")
            controller_health_check_variable = self.physical_check(BYPASS=False)
            self.setStatus(self.controller_health_status)
            self.excel_handler.update_cell("PHYSICAL TEST", "FAIL")
            if controller_health_check_variable:
                self.setStatus(self.controller_health_status, 1)
                self.excel_handler.update_cell("PHYSICAL TEST", "PASS")
            return controller_health_check_variable
        elif test_number == int(self.test_order[1]):
            unit_comm_variable = self.prompt.User_prompt("Do you want to pass this test and continue?")
            # unit_comm_variable = self.CARD_COMMUNICATION()
            self.setStatus(self.unit_comm_status)
            self.excel_handler.update_cell("COMMUNICATION TEST", "FAIL")
            if unit_comm_variable:
                self.setStatus(self.unit_comm_status, 1)
                self.excel_handler.update_cell("COMMUNICATION TEST", "PASS")
            return unit_comm_variable
        elif test_number == int(self.test_order[2]):
            temp_variable = self.prompt.User_prompt("Do you want to pass this test and continue?")
            # temp_variable = self.TEMPERATURE_MEASUREMENT()
            self.setStatus(self.temp_status)
            self.excel_handler.update_cell("TEMPERATURE TEST", "FAIL")
            if temp_variable:
                self.setStatus(self.temp_status, 1)
                self.excel_handler.update_cell("TEMPERATURE TEST", "PASS")
            return temp_variable
        elif test_number == int(self.test_order[3]):
            out_pfc_variable = self.prompt.User_prompt("Do you want to pass this test and continue?")
            # out_pfc_variable = self.OP_PFC_CHECK()
            self.excel_handler.update_cell("OUTPUT/INPUT PFC", "FAIL")
            self.setStatus(self.output_pfc_status)
            if out_pfc_variable:
                self.setStatus(self.output_pfc_status, 1)
                self.excel_handler.update_cell("OUTPUT/INPUT PFC", "PASS")
            return out_pfc_variable
        elif test_number == int(self.test_order[4]):
            input_pfc_variable = self.prompt.User_prompt("Do you want to pass this test and continue?")
            # input_pfc_variable = self.IP_PFC_CHECK()
            self.setStatus(self.input_pfc_status)
            self.excel_handler.update_cell("OUTPUT/INPUT PFC", "FAIL")
            if input_pfc_variable:
                self.setStatus(self.input_pfc_status, 1)
                self.excel_handler.update_cell("OUTPUT/INPUT PFC", "PASS")
            return input_pfc_variable
        elif test_number == int(self.test_order[5]):
            dc_voltage_check = self.prompt.User_prompt("Do you want to pass this test and continue?")
            # dc_voltage_check = self.DC_VOLTAGE_MEASUREMENT()
            self.setStatus(self.dc_voltage_check_status)
            self.excel_handler.update_cell("DC VOLTAGE TEST", "FAIL")
            if dc_voltage_check:
                self.setStatus(self.dc_voltage_check_status, 1)
                self.excel_handler.update_cell("DC VOLTAGE TEST", "PASS")
            return dc_voltage_check
        elif test_number == int(self.test_order[6]):
            dc_voltage_calib_variable = self.prompt.User_prompt("Do you want to pass this test and continue?")
            # dc_voltage_calib_variable = self.CALIBRATE_DC_VOLTAGE()
            self.excel_handler.update_cell("DC VOLTAGE CALIBRATION", "FAIL")
            self.setStatus(self.dc_voltage_calib_status)
            if dc_voltage_calib_variable:
                self.setStatus(self.dc_voltage_calib_status, 1)
                self.excel_handler.update_cell("DC VOLTAGE CALIBRATION", "PASS")
            return dc_voltage_calib_variable
        elif test_number == int(self.test_order[7]):
            dc_current_discharge_variable = self.prompt.User_prompt("Do you want to pass this test and continue?")
            # dc_current_discharge_variable = self.DC_CURRENT_MEASUREMENT_BATT_DISCHARGE()
            self.setStatus(self.dc_current_check_discharge_status)
            self.excel_handler.update_cell("DC CURRENT TEST", "FAIL")
            if dc_current_discharge_variable:
                self.setStatus(self.dc_current_check_discharge_status, 1)
                self.excel_handler.update_cell("DC CURRENT TEST", "PASS")
            return dc_current_discharge_variable
        elif test_number == int(self.test_order[8]):
            smr_registration_variable = self.prompt.User_prompt("Do you want to pass this test and continue?")
            # smr_registration_variable = self.SMR_REGISTRATION()
            self.setStatus(self.smr_register_status)
            self.excel_handler.update_cell("SMR REGISTRATION TEST", "FAIL")
            if smr_registration_variable:
                self.setStatus(self.smr_register_status, 1)
                self.excel_handler.update_cell("SMR REGISTRATION TEST", "PASS")
            return smr_registration_variable
        elif test_number == int(self.test_order[9]):
            dc_current_charge_variable = self.prompt.User_prompt("Do you want to pass this test and continue?")
            # dc_current_charge_variable = self.DC_CURRENT_MEASUREMENT_BATT_CHARGE()
            self.setStatus(self.dc_current_check_charge_status)
            self.excel_handler.update_cell("DC CURRENT CALIBRATION", "FAIL")
            if dc_current_charge_variable:
                self.setStatus(self.dc_current_check_charge_status, 1)
                self.excel_handler.update_cell("DC CURRENT CALIBRATION", "PASS")
            return dc_current_charge_variable
        elif test_number == int(self.test_order[10]):
            dc_current_calib_variable = self.prompt.User_prompt("Do you want to pass this test and continue?")
            # dc_current_calib_variable = self.CALIBRATE_DC_CURRENT()
            self.setStatus(self.dc_current_calib_status)
            self.excel_handler.update_cell("DC CURRENT CALIBRATION", "FAIL")
            if dc_current_calib_variable:
                self.setStatus(self.dc_current_calib_status, 1)
                self.excel_handler.update_cell("DC CURRENT CALIBRATION", "PASS")
            return dc_current_calib_variable
        elif test_number == int(self.test_order[11]):
            lvd_variable = self.prompt.User_prompt("Do you want to pass this test and continue?")
            # lvd_variable = self.LVD_CONTACTOR_CHECK()
            self.setStatus(self.lvd_status)
            self.excel_handler.update_cell("LVD TEST", "FAIL")
            if lvd_variable:
                self.setStatus(self.lvd_status, 1)
                self.excel_handler.update_cell("LVD TEST", "PASS")
            return lvd_variable
        elif test_number == int(self.test_order[12]):
            ac_phase_variable = self.prompt.User_prompt("Do you want to pass this test and continue?")
            # ac_phase_variable = self.PHASE_ALLOCATION()
            self.setStatus(self.ac_phase_status)
            self.excel_handler.update_cell("AC PHASE ALLOCATION TEST", "FAIL")
            if ac_phase_variable:
                self.setStatus(self.ac_phase_status, 1)
                self.excel_handler.update_cell("AC PHASE ALLOCATION TEST", "PASS")
            return ac_phase_variable
        elif test_number == int(self.test_order[13]):
            current_sharing_variable = self.prompt.User_prompt("Do you want to pass this test and continue?")
            # current_sharing_variable = self.CURRENT_SHARING()
            self.setStatus(self.current_sharing_status)
            self.excel_handler.update_cell("DC CURRENT SHARING/ BUS DROP TEST", "FAIL")
            if current_sharing_variable:
                self.setStatus(self.current_sharing_status, 1)
                self.excel_handler.update_cell("DC CURRENT SHARING/ BUS DROP TEST", "PASS")
            return current_sharing_variable
        elif test_number == int(self.test_order[14]):
            rs485_variable = self.prompt.User_prompt("Do you want to pass this test and continue?")
            # rs485_variable = self.RS_485_CHECK()
            self.setStatus(self.rs485_status)
            self.excel_handler.update_cell("RS-485 TEST", "FAIL")
            if rs485_variable:
                self.setStatus(self.rs485_status, 1)
                self.excel_handler.update_cell("RS-485 TEST", "PASS")
            return rs485_variable
        elif test_number == int(self.test_order[15]):
            default_variable = self.prompt.User_prompt("Do you want to pass this test and continue?")
            # self.default_status = self.DEFAULT_SETTING()
            self.setStatus(self.default_status)
            self.excel_handler.update_cell("DEFAULT SETTING", "FAIL")
            if default_variable:
                self.setStatus(self.default_status, 1)
                self.excel_handler.update_cell("DEFAULT SETTING", "PASS")
            return default_variable
        else:
            return False

    def setStatus(self, element, status=0):
        element.setText("FAIL")
        element.setStyleSheet("color:RED")
        if status:
            element.setText("PASS")
            element.setStyleSheet("color:GREEN")

    def print_console(self, text="", color="BLUE"):
        if color == "RED":
            self.log_window.setTextColor(QtCore.Qt.red)
        elif color == "BLUE":
            self.log_window.setTextColor(QtCore.Qt.blue)
        elif color == "GREEN":
            self.log_window.setTextColor(QtCore.Qt.darkGreen)
        self.log_window.append(str(text))
        QtWidgets.qApp.processEvents()
        time.sleep(0.0001)

    def physical_check(self, BYPASS=False):
        if BYPASS:
            return True
        else:

            RESULT = []
            self.print_console("PHYSICAL CHECK TEST STARTED...")

            physical_state = self.prompt.User_prompt("Is all bus-bar/ screws tight?")
            if physical_state:
                RESULT_TEMP = True
            else:
                RESULT_TEMP = False
            RESULT.append(RESULT_TEMP)

            physical_state = self.prompt.User_prompt("Is AC/Battery/LOAD/PFC/RS-485(if any) connection tightly done?")
            if physical_state:
                RESULT_TEMP = True
            else:
                RESULT_TEMP = False
            RESULT.append(RESULT_TEMP)

            physical_state = self.prompt.User_prompt("Is connection to optional AC MCB is correct?")
            if physical_state:
                RESULT_TEMP = True
            else:
                RESULT_TEMP = False
            RESULT.append(RESULT_TEMP)

            self.print_console("PHYSICAL CHECK TEST FINISHED....")
            self.CLEAR_JIG()
            # self.CHECK_DEVICES()
            # self.INITIALIZE_JIG()
            return CALCULATE_RESULT(RESULT)

    def report_function(self, event):
        report = QtWidgets.QDialog()
        report.ui = Ui_report()
        report.ui.setupUi(report)
        report.exec_()
        report.show()

    def GETTIME(self):
        time_var = datetime.datetime.now()
        time_var = str(time_var.date()) + "_" + str(time_var.time().hour) + "_" + str(
            time_var.time().minute) + "_" + str(time_var.time().second)
        return time_var

    def log(self):
        import sys
        root, extension = os.path.splitext(os.path.basename(sys.argv[0]))
        """Log Creation"""
        # if os.path.exists(f'{os.path.dirname(os.getcwd())}\\logs'):
        #     pass
        # else:
        #     os.system("mkdir logs")
        filename = f"{gui_global.directory_location}logs\\log_" + str(
            self.dut_serial_number_edit.text()).upper() + "_" + str(
            self.associate_name_edit.text()).upper() + "_" + str(self.GETTIME()) + '.txt'
        myfile = open(filename, 'w')
        myfile.write("DUT SERIAL NUMBER: " + self.dut_serial_number_edit.text().upper())
        myfile.write('\n\n')
        myfile.write(f"DUT PART NUMBER : {self.system_part_no_edit.text().upper()}")
        myfile.write('\n\n')
        myfile.write("Testing Engg. Name: " + self.associate_name_edit.text().upper())
        myfile.write('\n\n')
        myfile.write("ATE Version: " + root)
        myfile.write('\n\n')
        myfile.write(self.log_window.toPlainText())
        myfile.write('\n')
        myfile.write(f"Test Ended : {self.get_current_datetime()}")
        myfile.close()

    def get_current_datetime(self):
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
        return formatted_datetime


    def controller_health_method(self):
        global SITE_ID
        self.print_console("CONTROLLER HEALTH CHECK TEST STARTED...")
        if self.mcm_type == 1:
            M1000Telnet.telnet_set_command(OIDRead('SYSTEM COMMANDS')['ate test'], "TEST_M1000_ATE")
            SITE_ID = M1000Telnet.telnet_get_command(OIDRead("SYSTEM CONFIG")['site id'])
        elif self.mcm_type == 2:
            SITE_ID = self.MCM_READ_COMMAND().telnet_get_command(OIDRead("SYSTEM CONFIG")['site id'])
        RESULT = []
        if SITE_ID is not None:
            self.print_console("Controller Healthy")
            RESULT_TEMP = True
            self.RTC_SET()
        else:
            self.print_console("Controller OFF")
            RESULT_TEMP = False
        if self.mcm_type == 1:
            M1000Telnet.telnet_get_command(OIDRead('SYSTEM COMMANDS')['ate test'], "TEST_M1000_ATE")

        test_id = self.test_id_edit.text()

        if test_id != "0":
            self.record_result.append(test_id)
        else:
            self.record_result.append(test_id)

        RESULT.append(RESULT_TEMP)

        self.print_console("CONTROLLER_HEALTH_CHECK TEST FINISHED.")

        return CALCULATE_RESULT(RESULT)



    def RTC_SET(self):
        self.print_console("RTC SET STARTED...")
        date_time = self.MCM_READ_COMMAND('SYSTEM COMMANDS', 'rtc date time')
        # date_time = M1000Telnet.telnet_get_command(OIDRead("SYSTEM COMMANDS")['rtc date time'])
        print("SYSTEM Time and Date: " + str(date_time))
        now = get_date_time(date=1, time=1)
        self.MCM_WRITE_COMMAND('SYSTEM COMMANDS', 'rtc date time', now)
        # M1000Telnet.telnet_set_command(OIDRead('SYSTEM COMMANDS')['rtc date time'], now)
        self.print_console("RTC SET COMPLETED...")

    def INITIALIZE_JIG(self):
        self.print_console("INITIALIZING JIG TEST STARTED...")
        # self.M2000.SET_PFC(pfc=1, status=1, alarm_index=1)
        # self.M2000.SET_PFC(pfc=1, status=1, alarm_index=1)
        self.pfc.pfc_set(0, 'battery_mains', 1)
        self.pfc.pfc_set(0, "battery_1", 1)
        time.sleep(5)
        self.print_console("INITIALIZING JIG TEST FINISHED....")

    def ConfigureATS(self):
        global battery_capacity, bcl_factor
        self.print_console("FACTORY RESTORE")
        self.print_console("WAITING FOR 20 SECONDS")
        if self.mcm_type == 1:
            M1000Telnet.telnet_set_command(OIDRead('SYSTEM COMMANDS')['ate test'], "TEST_M1000_ATE")
            M1000Telnet.telnet_set_command(OIDRead('SYSTEM COMMANDS')['factory restore'], 1)
            time.sleep(5)
            M1000Telnet.telnet_set_command(OIDRead('SYSTEM COMMANDS')['system reset'], 1)
            time.sleep(15)
            self.print_console("RESET DONE")
            self.print_console("CONFIGURING ATS...")
            config = configparser.ConfigParser()
            cfgfile = open(f"{gui_global.files_directory_location}config.ini", 'w')
            config.add_section("DUT CONFIGURATION")
            if self.custom_check.isChecked():
                if DefaultRead("DEFAULT SETTING STATE")['max smr count'] == "YES":
                    max_smr_count = int(DefaultRead('DEFAULT SETTING')["max smr count"])
                    M1000Telnet.telnet_set_command(OIDRead('SYSTEM CONFIG')['smr count'], max_smr_count)

            phase_type = int(M1000Telnet.telnet_get_command(OIDRead("SYSTEM CONFIG")['ac phases type']))
            if phase_type == 0:
                phase_type = 'SINGLE PHASE'
            elif phase_type == 1:
                phase_type = 'THREE PHASE'
            config.set("DUT CONFIGURATION", 'ac phases type', phase_type)

            battery_fuses_count = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['no. of battery fuses']))
            config.set('DUT CONFIGURATION', 'no. of battery fuses', battery_fuses_count)

            battery_lvd_count = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['no. of battery lvd']))
            config.set('DUT CONFIGURATION', 'no. of battery lvd', battery_lvd_count)

            load_lvd_count = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['no. of load lvd']))
            config.set('DUT CONFIGURATION', 'no. of load lvd', load_lvd_count)

            load_current_count = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['no. of load current']))
            config.set('DUT CONFIGURATION', 'no. of load current', load_current_count)

            load_current_sensor_state = int(
                M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['load current sensor']))
            if load_current_sensor_state == 0:
                load_current_sensor_state = 'DISABLE'
            elif load_current_sensor_state == 1:
                load_current_sensor_state = 'ENABLE'
            # PRINT_CONSOLE(self,load_current_sensor_state)
            config.set('DUT CONFIGURATION', 'load current sensor', load_current_sensor_state)

            dcif_card_state = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['dcif card']))
            if dcif_card_state == 0:
                dcif_card_state = 'DISABLE'
            elif dcif_card_state == 1:
                dcif_card_state = 'PRESENT'
            config.set('DUT CONFIGURATION', 'dcif card', dcif_card_state)

            dcif_type = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['dcif card type']))
            config.set('DUT CONFIGURATION', 'dcif card type number', dcif_type)
            if dcif_type == 0:
                dcif_type = 'HALL EFFECT'
                for count in range(1, load_current_count + 1):
                    load_hall_effect_value = int(M1000Telnet.telnet_get_command(
                        OIDRead('SYSTEM CONFIG')['load' + str(count) + ' hall effect value']))
                    config.set('DUT CONFIGURATION', 'channel ' + str(count) + ' hall effect value',
                               load_hall_effect_value)
                for count in range(load_current_count + 1, load_current_count + battery_lvd_count + 1):
                    batt_hall_effect_value = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')[
                                                                                    'batt' + str(
                                                                                        count - load_current_count) + ' hall effect value']))
                    config.set('DUT CONFIGURATION', 'channel ' + str(count) + ' hall effect value',
                               batt_hall_effect_value)

            elif dcif_type == 1:
                dcif_type = 'SHUNT'
                for count in range(1, load_current_count + 1):
                    load_hall_effect_value = int(
                        M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['load' + str(count) + ' shunt value']))
                    config.set('DUT CONFIGURATION', 'channel ' + str(count) + ' shunt value', load_hall_effect_value)
                    load_hall_effect_value = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')[
                                                                                    'load' + str(
                                                                                        count) + ' shunt mv value']))
                    config.set('DUT CONFIGURATION', 'channel ' + str(count) + ' shunt mv value', load_hall_effect_value)
                for count in range(load_current_count + 1, load_current_count + battery_lvd_count + 1):
                    batt_hall_effect_value = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')[
                                                                                    'batt' + str(
                                                                                        count - load_current_count) + ' shunt value']))
                    config.set('DUT CONFIGURATION', 'channel ' + str(count) + ' shunt value', batt_hall_effect_value)
                    batt_hall_effect_value = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')[
                                                                                    'batt' + str(
                                                                                        count - load_current_count) + ' shunt mv value']))
                    config.set('DUT CONFIGURATION', 'channel ' + str(count) + ' shunt mv value', batt_hall_effect_value)

            elif dcif_type == 2 or dcif_type == 3:  # added dcif type 3 to logic ,17/06/2019
                dcif_type = 'SHUNT SMALL'
                for count in range(1, load_current_count + 1):
                    load_hall_effect_value = int(
                        M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['load' + str(count) + ' shunt value']))
                    config.set('DUT CONFIGURATION', 'channel ' + str(count) + ' shunt value', load_hall_effect_value)
                    load_hall_effect_value = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')[
                                                                                    'load' + str(
                                                                                        count) + ' shunt mv value']))
                    config.set('DUT CONFIGURATION', 'channel ' + str(count) + ' shunt mv value', load_hall_effect_value)
                for count in range(load_current_count + 1, load_current_count + battery_lvd_count + 1):
                    batt_hall_effect_value = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')[
                                                                                    'batt' + str(
                                                                                        count - load_current_count) + ' shunt value']))
                    config.set('DUT CONFIGURATION', 'channel ' + str(count) + ' shunt value', batt_hall_effect_value)
                    batt_hall_effect_value = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')[
                                                                                    'batt' + str(
                                                                                        count - load_current_count) + ' shunt mv value']))
                    config.set('DUT CONFIGURATION', 'channel ' + str(count) + ' shunt mv value', batt_hall_effect_value)

            config.set('DUT CONFIGURATION', 'dcif card type', dcif_type)

            hvlv_card_state = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['hvlv card']))
            if hvlv_card_state == 0:
                hvlv_card_state = 'DISABLE'
            elif hvlv_card_state == 1:
                hvlv_card_state = 'PRESENT'
            config.set('DUT CONFIGURATION', 'hvlv card', hvlv_card_state)

            dcif_ip_card_state = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['dcif ip card']))
            if dcif_ip_card_state == 0:
                dcif_ip_card_state = 'DISABLE'
            elif dcif_ip_card_state == 1:
                dcif_ip_card_state = 'PRESENT'
            config.set('DUT CONFIGURATION', 'dcif ip card', dcif_ip_card_state)

            dcif_op_card_state = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['dcif op card']))
            if dcif_op_card_state == 0:
                dcif_op_card_state = 'DISABLE'
            elif dcif_op_card_state == 1:
                dcif_op_card_state = 'PRESENT'
            config.set('DUT CONFIGURATION', 'dcif op card', dcif_op_card_state)

            batt_temperature_state = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['temperature1']))
            if batt_temperature_state == 0:
                batt_temperature_state = 'DISABLE'
            elif batt_temperature_state == 1:
                batt_temperature_state = 'PRESENT'
            config.set('DUT CONFIGURATION', 'temperature1', batt_temperature_state)

            room_temperature1_state = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['temperature2']))
            if room_temperature1_state == 0:
                room_temperature1_state = 'DISABLE'
            elif room_temperature1_state == 1:
                room_temperature1_state = 'PRESENT'
            config.set('DUT CONFIGURATION', 'temperature2', room_temperature1_state)

            room_temperature2_state = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['temperature3']))
            if room_temperature2_state == 0:
                room_temperature2_state = 'DISABLE'
            elif room_temperature2_state == 1:
                room_temperature2_state = 'PRESENT'
            config.set('DUT CONFIGURATION', 'temperature3', room_temperature2_state)

            pfc_io_card_state = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['pfc io card']))
            if pfc_io_card_state == 0:
                pfc_io_card_state = 'DISABLE'
            elif pfc_io_card_state == 1:
                pfc_io_card_state = 'PRESENT'
            config.set('DUT CONFIGURATION', 'pfc io card', pfc_io_card_state)

            smr_count = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['smr count']))
            config.set('DUT CONFIGURATION', 'smr count', smr_count)

            smr_type = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['smr type']))
            if smr_type == 0:
                smr_type = '100A'
            elif smr_type == 1:
                smr_type = '3KW'
            elif smr_type == 2:
                smr_type = '25A'
            config.set('DUT CONFIGURATION', 'smr type', smr_type)

            battery_type = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['battery type']))
            if battery_type == 0:
                battery_type = 'VRLA'
            elif battery_type == 1:
                battery_type = 'VRLA+LION'
            elif battery_type == 2:
                battery_type = 'LION'
            config.set('DUT CONFIGURATION', 'battery type', battery_type)

            if battery_type == 'VRLA':
                battery_capacity = int(
                    M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['vrla battery capacity']))
                bcl_factor = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['vrla bcl factor']))
            if battery_type == 'LION' or battery_type == 'VRLA+LION':
                battery_capacity = int(
                    M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['lion battery capacity']))
                bcl_factor = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['lion bcl factor']))
                module_count = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['lion module count']))
                config.set('DUT CONFIGURATION', 'lion module count', module_count)
            config.set('DUT CONFIGURATION', 'battery capacity', battery_capacity)
            config.set('DUT CONFIGURATION', 'bcl factor', bcl_factor)

            ac_ip_voltage_source = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['ac ip voltage source']))
            if ac_ip_voltage_source == 1:
                ac_ip_voltage_source = 'ACIF '
            elif ac_ip_voltage_source == 2:
                ac_ip_voltage_source = 'HVLV PN'
            elif ac_ip_voltage_source == 3:
                ac_ip_voltage_source = 'HVLV PP'
            elif ac_ip_voltage_source == 4:
                ac_ip_voltage_source = 'SMR 1P'
            elif ac_ip_voltage_source == 5:
                ac_ip_voltage_source = 'SMR 3P'
            config.set('DUT CONFIGURATION', 'ac ip voltage source', ac_ip_voltage_source)

            ac_ip_current_source = int(M1000Telnet.telnet_get_command(OIDRead('SYSTEM CONFIG')['ac ip current source']))
            if ac_ip_current_source == 0:
                ac_ip_current_source = 'NO SENSING '
            elif ac_ip_current_source == 1:
                ac_ip_current_source = 'ACIF '
            elif ac_ip_current_source == 2:
                ac_ip_current_source = 'HVLV PN'
            elif ac_ip_current_source == 3:
                ac_ip_current_source = 'HVLV PP'
            elif ac_ip_current_source == 4:
                ac_ip_current_source = 'SMR 1P'
            elif ac_ip_current_source == 5:
                ac_ip_current_source = 'SMR 3P'
            config.set('DUT CONFIGURATION', 'ac ip current source', ac_ip_current_source)

            lower_port_baudrate = int(M1000Telnet.telnet_get_command(OIDRead('RS 485')['lower port baudrate']))
            config.set('DUT CONFIGURATION', 'lower port baudrate', lower_port_baudrate)

            upper_port_baudrate = int(M1000Telnet.telnet_get_command(OIDRead('RS 485')['upper port baudrate']))
            config.set('DUT CONFIGURATION', 'upper port baudrate', upper_port_baudrate)

            modbus_comm_port = int(M1000Telnet.telnet_get_command(OIDRead('RS 485')['modbus comm']))
            config.set('DUT CONFIGURATION', 'modbus comm', modbus_comm_port)

            lithium_ion_comm_port = int(M1000Telnet.telnet_get_command(OIDRead('RS 485')['lithium ion comm']))
            config.set('DUT CONFIGURATION', 'lithium ion comm', lithium_ion_comm_port)

            acem_comm_port = int(M1000Telnet.telnet_get_command(OIDRead('RS 485')['acem comm']))
            config.set('DUT CONFIGURATION', 'acem comm', acem_comm_port)

            dg_amf_comm_port = int(M1000Telnet.telnet_get_command(OIDRead('RS 485')['dg amf comm']))
            config.set('DUT CONFIGURATION', 'dg amf comm', dg_amf_comm_port)

            solar_hvlv_comm_port = int(M1000Telnet.telnet_get_command(OIDRead('RS 485')['solar hvlv comm']))
            config.set('DUT CONFIGURATION', 'solar hvlv comm', solar_hvlv_comm_port)

            ext_dcem_comm_port = int(M1000Telnet.telnet_get_command(OIDRead('RS 485')['ext dcem comm']))
            config.set('DUT CONFIGURATION', 'ext dcem comm', ext_dcem_comm_port)

            bnms_comm_port = int(M1000Telnet.telnet_get_command(OIDRead('RS 485')['bnms comm']))
            config.set('DUT CONFIGURATION', 'bnms comm', bnms_comm_port)

            config.write(cfgfile)
            cfgfile.close()
            self.print_console("ATS CONFIGURED...")
            return True

        elif self.mcm_type == 2:
            self.M2000.MCM_SET_COMMAND(M2000OIDRead("SYSTEM COMMANDS")['system reset'], 1)
            time.sleep(5)
            self.M2000.MCM_SET_COMMAND(M2000OIDRead('SYSTEM COMMANDS')['system reset'], 1)
            time.sleep(15)
            self.print_console("RESET DONE")
            self.print_console("CONFIGURING ATS....")
            config = configparser.ConfigParser()
            cfgfile = open(f"{gui_global.files_directory_location}config.ini", 'w')
            config.add_section("DUT CONFIGURATION")
            if self.custom_check.isChecked():
                if DefaultRead('DEFAULT SETTING STATE')['max smr count'] == "YES":
                    max_smr_count = int(DefaultRead("DEFAULT SETTING")['max smr count'])
                    self.M2000.MCM_SET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['smr count'], max_smr_count)

            phase_type = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['ac phases type']))
            if phase_type == 0:
                phase_type = 'SINGLE PHASE'
            elif phase_type == 1:
                phase_type = 'THREE PHASE'
            # PRINT_CONSOLE(self,phase_type)
            config.set('DUT CONFIGURATION', 'ac phases type', phase_type)

            battery_fuses_count = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['no. of battery fuses']))
            config.set('DUT CONFIGURATION', 'no. of battery fuses', battery_fuses_count)

            battery_lvd_count = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['no. of battery lvd']))
            config.set('DUT CONFIGURATION', 'no. of battery lvd', battery_lvd_count)

            load_lvd_count = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['no. of load lvd']))
            config.set('DUT CONFIGURATION', 'no. of load lvd', load_lvd_count)

            load_current_count = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['no. of load current']))
            config.set('DUT CONFIGURATION', 'no. of load current', load_current_count)

            load_current_sensor_state = int(
                self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['load current sensor']))
            if load_current_sensor_state == 0:
                load_current_sensor_state = 'DISABLE'
            elif load_current_sensor_state == 1:
                load_current_sensor_state = 'ENABLE'
            # PRINT_CONSOLE(self,load_current_sensor_state)
            config.set('DUT CONFIGURATION', 'load current sensor', load_current_sensor_state)

            dcif_card_state = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['dcif card']))
            if dcif_card_state == 0:
                dcif_card_state = 'DISABLE'
            elif dcif_card_state == 1:
                dcif_card_state = 'PRESENT'
            config.set('DUT CONFIGURATION', 'dcif card', dcif_card_state)

            dcif_type = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['dcif card type']))
            config.set('DUT CONFIGURATION', 'dcif card type number', dcif_type)
            if dcif_type == 0:
                dcif_type = 'HALL EFFECT'
                for count in range(1, load_current_count + 1):
                    load_hall_effect_value = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')[
                                                                                'load' + str(
                                                                                    count) + ' hall effect value']))
                    config.set('DUT CONFIGURATION', 'channel ' + str(count) + ' hall effect value',
                               load_hall_effect_value)
                for count in range(load_current_count + 1, load_current_count + battery_lvd_count + 1):
                    batt_hall_effect_value = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')[
                                                                                'batt' + str(
                                                                                    count - load_current_count) + ' hall effect value']))
                    config.set('DUT CONFIGURATION', 'channel ' + str(count) + ' hall effect value',
                               batt_hall_effect_value)

            elif dcif_type == 1:
                dcif_type = 'SHUNT'
                for count in range(1, load_current_count + 1):
                    load_hall_effect_value = int(
                        self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['load' + str(count) + ' shunt value']))
                    config.set('DUT CONFIGURATION', 'channel ' + str(count) + ' shunt value', load_hall_effect_value)
                    load_hall_effect_value = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')[
                                                                                'load' + str(
                                                                                    count) + ' shunt mv value']))
                    config.set('DUT CONFIGURATION', 'channel ' + str(count) + ' shunt mv value', load_hall_effect_value)
                for count in range(load_current_count + 1, load_current_count + battery_lvd_count + 1):
                    batt_hall_effect_value = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')[
                                                                                'batt' + str(
                                                                                    count - load_current_count) + ' shunt value']))
                    config.set('DUT CONFIGURATION', 'channel' + str(count) + ' shunt value', batt_hall_effect_value)
                    batt_hall_effect_value = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')[
                                                                                'batt' + str(
                                                                                    count - load_current_count) + ' shunt mv value']))
                    config.set('DUT CONFIGURATION', 'channel' + str(count) + ' shunt mv value', batt_hall_effect_value)

            elif dcif_type == 2 or dcif_type == 3:  # added dcif type 3 to logic ,17/06/2019
                dcif_type = 'SHUNT SMALL'
                for count in range(1, load_current_count + 1):
                    load_hall_effect_value = int(
                        self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['load' + str(count) + ' shunt value']))
                    config.set('DUT CONFIGURATION', 'channel' + str(count) + ' shunt value', load_hall_effect_value)
                    load_hall_effect_value = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')[
                                                                                'load' + str(
                                                                                    count) + ' shunt mv value']))
                    config.set('DUT CONFIGURATION', 'channel' + str(count) + ' shunt mv value', load_hall_effect_value)
                for count in range(load_current_count + 1, load_current_count + battery_lvd_count + 1):
                    batt_hall_effect_value = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')[
                                                                                'batt' + str(
                                                                                    count - load_current_count) + ' shunt value']))
                    config.set('DUT CONFIGURATION', 'channel' + str(count) + ' shunt value', batt_hall_effect_value)
                    batt_hall_effect_value = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')[
                                                                                'batt' + str(
                                                                                    count - load_current_count) + ' shunt mv value']))
                    config.set('DUT CONFIGURATION', 'channel' + str(count) + ' shunt mv value', batt_hall_effect_value)

            config.set('DUT CONFIGURATION', 'dcif card type', dcif_type)

            hvlv_card_state = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['hvlv card']))
            if hvlv_card_state == 0:
                hvlv_card_state = 'DISABLE'
            elif hvlv_card_state == 1:
                hvlv_card_state = 'PRESENT'
            config.set('DUT CONFIGURATION', 'hvlv card', hvlv_card_state)

            dcif_ip_card_state = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['dcif ip card']))
            if dcif_ip_card_state == 0:
                dcif_ip_card_state = 'DISABLE'
            elif dcif_ip_card_state == 1:
                dcif_ip_card_state = 'PRESENT'
            config.set('DUT CONFIGURATION', 'dcif ip card', dcif_ip_card_state)

            dcif_op_card_state = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['dcif op card']))
            if dcif_op_card_state == 0:
                dcif_op_card_state = 'DISABLE'
            elif dcif_op_card_state == 1:
                dcif_op_card_state = 'PRESENT'
            config.set('DUT CONFIGURATION', 'dcif op card', dcif_op_card_state)

            batt_temperature_state = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['temperature1']))
            if batt_temperature_state == 1:
                batt_temperature_state = 'DISABLE'
            elif batt_temperature_state == 0:
                batt_temperature_state = 'PRESENT'
            config.set('DUT CONFIGURATION', 'temperature1', batt_temperature_state)

            room_temperature1_state = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['temperature2']))
            if room_temperature1_state == 0:
                room_temperature1_state = 'DISABLE'
            elif room_temperature1_state == 1:
                room_temperature1_state = 'PRESENT'
            config.set('DUT CONFIGURATION', 'temperature2', room_temperature1_state)

            room_temperature2_state = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['temperature3']))
            if room_temperature2_state == 0:
                room_temperature2_state = 'DISABLE'
            elif room_temperature2_state == 1:
                room_temperature2_state = 'PRESENT'
            config.set('DUT CONFIGURATION', 'temperature3', room_temperature2_state)

            pfc_io_card_state = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['pfc io card']))
            if pfc_io_card_state == 0:
                pfc_io_card_state = 'DISABLE'
            elif pfc_io_card_state == 1:
                pfc_io_card_state = 'PRESENT'
            config.set('DUT CONFIGURATION', 'pfc io card', pfc_io_card_state)

            smr_count = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['smr count']))
            config.set('DUT CONFIGURATION', 'smr count', smr_count)

            smr_type = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['smr type']))
            if smr_type == 0:
                smr_type = '100A'
            elif smr_type == 1:
                smr_type = '3KW'
            elif smr_type == 2:
                smr_type = '25A'
            elif smr_type == 3:
                smr_type = '25A'
            config.set('DUT CONFIGURATION', 'smr type', smr_type)

            battery_type = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['battery type']))
            if battery_type == 0:
                battery_type = 'VRLA'
            elif battery_type == 1:
                battery_type = 'VRLA+LION'
            elif battery_type == 2:
                battery_type = 'LION'
            config.set('DUT CONFIGURATION', 'battery type', battery_type)

            if battery_type == 'VRLA':
                battery_capacity = int(
                    self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['vrla battery capacity']))
                bcl_factor = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['vrla bcl factor']))
            if battery_type == 'LION' or battery_type == 'VRLA+LION':
                battery_capacity = int(
                    self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['lion battery capacity']))
                bcl_factor = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['lion bcl factor']))
                module_count = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['lion module count']))
                config.set('DUT CONFIGURATION', 'lion module count', module_count)
            config.set('DUT CONFIGURATION', 'battery capacity', battery_capacity)
            config.set('DUT CONFIGURATION', 'bcl factor', bcl_factor)

            ac_ip_voltage_source = int(
                self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['ac ip voltage source']))
            if ac_ip_voltage_source == 1:
                ac_ip_voltage_source = 'ACIF '
            elif ac_ip_voltage_source == 2:
                ac_ip_voltage_source = 'HVLV PN'
            elif ac_ip_voltage_source == 3:
                ac_ip_voltage_source = 'HVLV PP'
            elif ac_ip_voltage_source == 4:
                ac_ip_voltage_source = 'SMR 1P'
            elif ac_ip_voltage_source == 5:
                ac_ip_voltage_source = 'SMR 3P'
            config.set('DUT CONFIGURATION', 'ac ip voltage source', ac_ip_voltage_source)

            ac_ip_current_source = int(
                self.M2000.MCM_GET_COMMAND(M2000OIDRead('SYSTEM CONFIG')['ac ip current source']))
            if ac_ip_current_source == 0:
                ac_ip_current_source = 'NO SENSING '
            elif ac_ip_current_source == 1:
                ac_ip_current_source = 'ACIF '
            elif ac_ip_current_source == 2:
                ac_ip_current_source = 'HVLV PN'
            elif ac_ip_current_source == 3:
                ac_ip_current_source = 'HVLV PP'
            elif ac_ip_current_source == 4:
                ac_ip_current_source = 'SMR 1P'
            elif ac_ip_current_source == 5:
                ac_ip_current_source = 'SMR 3P'
            config.set('DUT CONFIGURATION', 'ac ip current source', ac_ip_current_source)

            lower_port_baudrate = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('RS 485')['lower port baudrate']))
            if lower_port_baudrate == 0:
                lower_port_baudrate = 9600
            elif lower_port_baudrate == 1:
                lower_port_baudrate = 19200
            elif lower_port_baudrate == 2:
                lower_port_baudrate = 115200
            config.set('DUT CONFIGURATION', 'lower port baudrate', lower_port_baudrate)

            upper_port_baudrate = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('RS 485')['upper port baudrate']))

            if upper_port_baudrate == 0:
                upper_port_baudrate = 9600
            elif upper_port_baudrate == 1:
                upper_port_baudrate = 19200
            elif upper_port_baudrate == 2:
                upper_port_baudrate = 115200
            config.set('DUT CONFIGURATION', 'upper port baudrate', upper_port_baudrate)
            modbus_comm_port = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('RS 485')['modbus comm']))
            config.set('DUT CONFIGURATION', 'modbus comm', modbus_comm_port)

            lithium_ion_comm_port = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('RS 485')['lithium ion comm']))
            config.set('DUT CONFIGURATION', 'lithium ion comm', lithium_ion_comm_port)

            acem_comm_port = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('RS 485')['acem comm']))
            config.set('DUT CONFIGURATION', 'acem comm', acem_comm_port)

            dg_amf_comm_port = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('RS 485')['dg amf comm']))
            config.set('DUT CONFIGURATION', 'dg amf comm', dg_amf_comm_port)

            solar_hvlv_comm_port = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('RS 485')['solar hvlv comm']))
            config.set('DUT CONFIGURATION', 'solar hvlv comm', solar_hvlv_comm_port)

            ext_dcem_comm_port = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('RS 485')['ext dcem comm']))
            config.set('DUT CONFIGURATION', 'ext dcem comm', ext_dcem_comm_port)

            bnms_comm_port = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('RS 485')['bnms comm']))
            config.set('DUT CONFIGURATION', 'bnms comm', bnms_comm_port)

            config.write(cfgfile)
            cfgfile.close()
            PRINT_CONSOLE(self, "ATS CONFIGURED...")
            return True

    def CARD_COMMUNICATION(self):
        self.print_console("CARD COMMUNICATION TEST STARTED....")
        RESULT = []
        hvlv_card_state = ConfigRead("DUT CONFIGURATION")['hvlv card']
        dcif_card_state = ConfigRead("DUT CONFIGURATION")['dcif card']
        pfcio_card_state = ConfigRead("DUT CONFIGURATION")['pfc op card']
        ac_phase_type = ConfigRead("DUT CONFIGURATION")['ac phases type']

        if self.mcm_type == 1:
            self.MCM_WRITE_COMMAND('SYSTEM COMMANDS', 'ate test', 'TEST_M1000_ATE')
            alarm_comm_fail = int(M1000Telnet.telnet_get_command(OIDRead('ALARM')['can comm fail']))
            if alarm_comm_fail == 0:
                RESULT_TEMP = True
                self.print_console("CAN COMM OK")
                self.excel_handler.update_cell("UNIT COMMUNICATION", "PASS")
            else:
                RESULT_TEMP = False
                self.print_console("CAN COMM FAIL", "RED")
                self.excel_handler.update_cell("UNIT COMMUNICATION", "FAIL")
            RESULT.append(RESULT_TEMP)

            if hvlv_card_state == "PRESENT":
                if ac_phase_type == "SINGLE PHASE":
                    print("SINGLE PHASE VOLTAGE")  # add
                    ACSET(self.pfc, 1, 1)
                elif ac_phase_type == "THREE PHASE":
                    print("THREE PHASE VOLTAGE")  # add
                    ACSET(self.pfc, 3, 1)

                ## AC Contactor PFC need to be added

                time.sleep(10)
                self.print_console("HVLV CARD IS PRESENT ")
                alarm_comm_fail = int(M1000Telnet.telnet_get_command(OIDRead("ALARM")['hvlv comm fail']))
                if alarm_comm_fail == 0:
                    RESULT_TEMP = True
                    self.print_console("HVLV COMM OK")
                else:
                    RESULT_TEMP = False
                    self.print_console("HVLV COMM FAIL", "RED")
                ACSET(self.pfc, 3, 0)

            else:
                self.print_console("HVLV CARD IS NOT PRESENT", 'RED')
                RESULT_TEMP = True
            RESULT.append(RESULT_TEMP)

            if dcif_card_state == "PRESENT":
                alarm_comm_fail = int(M1000Telnet.telnet_get_command(OIDRead('ALARM')['dcif comm fail']))
                if alarm_comm_fail == 0:
                    RESULT_TEMP = True
                    self.print_console("DCIF COMM OK")
                else:
                    RESULT_TEMP = False
                    self.print_console("DCIF COMM FAIL", "RED")
            else:
                RESULT_TEMP = True
            RESULT.append(RESULT_TEMP)

            if pfcio_card_state == "PRESENT":
                alarm_comm_fail = int(M1000Telnet.telnet_get_command(OIDRead('ALARM')['pfc1 comm fail']))
                if alarm_comm_fail == 0:
                    RESULT_TEMP = True
                    self.print_console("CAN PFC IO COMM OK")
                else:
                    RESULT_TEMP = False
                    self.print_console("CAN PFC IO COMM FAIL", "RED")
            else:
                RESULT_TEMP = True
            RESULT.append(RESULT_TEMP)

            self.print_console("CARD COMMUNICATION TEST FINISHED....")
            return CALCULATE_RESULT(RESULT)

            # return True
        elif self.mcm_type == 2:
            alarm_comm_fail = int(self.MCM_READ_COMMAND("ALARM", "can comm fail"))
            if alarm_comm_fail == 0:
                self.print_console("CAN COMM OK")
                self.excel_handler.update_cell("UNIT COMMUNICATION", "PASS")
                RESULT_TEMP = True
            else:
                RESULT_TEMP = False
                self.print_console('CAN COMM FAIL')
                self.excel_handler.update_cell("UNIT COMMUNICATION", "FAIL")
            RESULT.append(RESULT_TEMP)

            if hvlv_card_state == "PRESENT":
                if ac_phase_type == "SINGLE PHASE":
                    print("Single phase voltage")
                    ACSET(self.pfc, 1, 1)
                else:
                    ACSET(self.pfc, 3, 1)
                time.sleep(8)
                self.print_console("HVLV CARD IS PRESENT")
                alarm_comm_fail = int(self.MCM_READ_COMMAND("alarm", "hvlv comm fail"))
                if alarm_comm_fail == 0:
                    RESULT_TEMP = True
                    self.print_console("HVLV COMM OK")
                else:
                    RESULT_TEMP = False
                    self.print_console("HVLV COMM FAIL", "RED")
                ACSET(self.pfc, 3, 0)
            else:
                self.print_console("HVLV CARD IS NOT PRESENT", "RED")
                RESULT_TEMP = True
            RESULT.append(RESULT_TEMP)

            if dcif_card_state == "PRESENT":
                alarm_comm_fail = int(self.MCM_READ_COMMAND("ALARM", 'dcif comm fail'))
                if alarm_comm_fail == 0:
                    RESULT_TEMP = True
                    self.print_console("DCIF COMM OK")
                else:
                    RESULT_TEMP = False
                    self.print_console("DCIF COMM FAIL", "RED")
            else:
                RESULT_TEMP = True
            RESULT.append(RESULT_TEMP)

            if pfcio_card_state == "PRESENT":
                alarm_comm_fail = int(self.MCM_READ_COMMAND('ALARM', 'pfc1 comm fail'))
                if alarm_comm_fail == 0:
                    RESULT_TEMP = True
                    self.print_console("CAN PFC IO COMM OK")
                else:
                    RESULT_TEMP = False
                    self.print_console("CAN PFC IO COMM FAIL", "RED")
            else:
                RESULT_TEMP = True
            RESULT.append(RESULT_TEMP)

            self.print_console("CARD COMMUNICATION TEST FINISHED....")
            return CALCULATE_RESULT(RESULT)


    def TEMPERATURE_MEASUREMENT(self):
        global temperature_text
        RESULT = []
        self.print_console("TEMPERATURE MEASUREMENT TEST STARTED....")
        if self.mcm_type == 1:
            M1000Telnet.telnet_set_command(OIDRead('SYSTEM COMMANDS')['ate test'], "TEST_M1000_ATE")
            for temp in range(1, 4):
                if temp == 1:
                    temperature_text = "BATTERY TEMPERATURE"
                elif temp == 2:
                    temperature_text = "ROOM TEMPERATURE 1"
                elif temp == 3:
                    temperature_text = "ROOM TEMPERATURE 2"
                temperature_state = ConfigRead("DUT CONFIGURATION")['temperature' + str(temp)]
                if temperature_state == "DISABLE":
                    self.print_console(f"{temperature_text} sensor not applicable")
                    RESULT_TEMP = True
                    RESULT.append(RESULT_TEMP)
                else:
                    temperature = float(
                        M1000Telnet.telnet_get_command(OIDRead('READ TEMPERATURE')['temperature' + str(temp)]))
                    if temperature < 9 or temperature > 40:
                        self.print_console(f"{temperature_text} cable not installed/ faulty", "RED")
                        RESULT_TEMP = False
                        RESULT.append(RESULT_TEMP)
                        self.print_console(f"{temperature_text} : {temperature}")
                    else:
                        temperature_list = []
                        for i in range(1, 5):
                            temperature = M1000Telnet.telnet_get_command(
                                OIDRead('READ TEMPERATURE')['temperature' + str(temp)])
                            temperature_list.append(temperature)
                        # self.print_console(f"{temperature_list}")
                        temperature_minimum = float(min(temperature_list))
                        temperature_maximum = float(max(temperature_list))
                        if abs(temperature_maximum - temperature_minimum) < 2:
                            RESULT_TEMP = True
                            self.print_console(f"{temperature_text} CABLE OK")
                        else:
                            RESULT_TEMP = False
                            self.print_console(f"{temperature_text} CABLE FAULTY", "RED")
                        RESULT.append(RESULT_TEMP)
            self.print_console("TEMPERATURE MEASUREMENT TEST FINISHED...")
            return CALCULATE_RESULT(RESULT)

        elif self.mcm_type == 2:
            for temp in range(1, 4):
                if temp == 1:
                    temperature_text = "BATTERY TEMPERATURE"
                elif temp == 2:
                    temperature_text = "ROOM TEMPERATURE 1"
                elif temp == 3:
                    temperature_text = "ROOM TEMPERATURE 2"
                temperature_state = ConfigRead("DUT CONFIGURATION")['temperature' + str(temp)]
                if temperature_state == "DISABLE":
                    self.print_console(f"{temperature_text} sensor not applicable")
                    RESULT_TEMP = True
                    RESULT.append(RESULT_TEMP)
                else:
                    temperature = float(
                        self.M2000.MCM_GET_COMMAND(M2000OIDRead('READ TEMPERATURE')['temperature' + str(temp)]))
                    if temperature < 9 or temperature > 40:
                        self.print_console(f"{temperature_text} cable not installed/ faulty", "RED")
                        RESULT_TEMP = False
                        RESULT.append(RESULT_TEMP)
                        self.print_console(f"{temperature_text} : {temperature}")
                    else:
                        temperature_list = []
                        for i in range(1, 5):
                            temperature = self.M2000.MCM_GET_COMMAND(
                                M2000OIDRead('READ TEMPERATURE')['temperature' + str(temp)])
                            temperature_list.append(temperature)
                        # self.print_console(f"{temperature_list}")
                        temperature_minimum = float(min(temperature_list))
                        temperature_maximum = float(max(temperature_list))
                        if abs(temperature_maximum - temperature_minimum) < 2:
                            RESULT_TEMP = True
                            self.print_console(f"{temperature_text} CABLE OK")
                        else:
                            RESULT_TEMP = False
                            self.print_console(f"{temperature_text} CABLE FAULTY", "RED")
                        RESULT.append(RESULT_TEMP)
            self.print_console("TEMPERATURE MEASUREMENT TEST FINISHED...")
            return CALCULATE_RESULT(RESULT)

    def OP_PFC_CHECK(self):

        """
        TEST BLOCK OF OUTPUT PFC

        DEFINES AND TEST OUTPUT PFC(S) OR LVD(S) OF THE RACK SYSTEM

        :return: STATUS OF THE FUNCTION BLOCK IN BOOLEAN FORM (TRUE OR FALSE)
        """

        RESULT = []
        RESULT_1 = []
        RESULT_2 = []
        self.print_console("OP_PFC_CHECK TEST STARTED...")
        pfcio_card_state = ConfigRead("DUT CONFIGURATION")['pfc io card']
        dcif_op_card_state = ConfigRead("DUT CONFIGURATION")['dcif op card']
        dcif_type_number = int(ConfigRead('DUT CONFIGURATION')['dcif card type number'])
        if dcif_type_number == 1 or dcif_type_number == 2:
            if self.mcm_type == 1:
                M1000Telnet.telnet_set_command(OIDRead('SYSTEM COMMANDS')['ate test'], "TEST_M1000_ATE")

            for op_pfc in range(1, 3):
                set_dut_pfc = pow(2, op_pfc + 4)
                if self.mcm_type == 1:
                    M1000Telnet.telnet_set_command(OIDRead('DCIF 2 OP PFC')['pfc'], set_dut_pfc)
                elif self.mcm_type == 2:
                    self.M2000.MCM_SET_COMMAND(M2000OIDRead('DCIF 2 OP PFC')['pfc'], set_dut_pfc)
                if dcif_op_card_state == "PRESENT":
                    set_dcif_pfc = pow(2, op_pfc - 1)
                    if self.mcm_type == 1:
                        M1000Telnet.telnet_set_command(OIDRead('DCIF 8 OP PFC')['pfc'], set_dcif_pfc)
                    elif self.mcm_type == 2:
                        self.M2000.MCM_SET_COMMAND(M2000OIDRead('DCIF 8 OP PFC')['pfc'], set_dcif_pfc)
                time.sleep(2)
                print(f"Checking for pfc {op_pfc}")
                for op_pfc_check in range(1, 3):
                    jig_pfc = (2 * op_pfc_check) - 1

                    if op_pfc == op_pfc_check:
                        print("same PFC")
                        if self.pfc.read_pfc(card_id=self.contact.CARD2, pfc_number=jig_pfc) == 0:
                            RESULT_TEMP = True
                            self.print_console(f"LVD PFC {op_pfc_check} NC is OK")
                        else:
                            RESULT_TEMP = False
                            self.print_console(f"LVD OP PFC {op_pfc} NC SLOT IS FAULTY", 'RED')
                        RESULT_1.append(RESULT_TEMP)
                        if self.pfc.read_pfc(self.contact.CARD2, pfc_number=jig_pfc + 1) == 1:
                            RESULT_TEMP = True
                            self.print_console(f"LVD PFC {op_pfc_check} NC IS OK")
                        else:
                            RESULT_TEMP = False
                            self.print_console(f"LVD OP PFC {op_pfc} NC SLOT IS FAULTY", 'RED')
                        RESULT_1.append(RESULT_TEMP)
                    else:
                        print("Different PFC")
                        if self.pfc.read_pfc(self.contact.CARD2, jig_pfc) == 1:
                            RESULT_TEMP = True
                        else:
                            RESULT_TEMP = False
                            self.print_console(f"LVD OP PFC {op_pfc_check} NC SLOT IS SHORT WITH OP PFC {op_pfc}",
                                               "RED")
                        RESULT_1.append(RESULT_TEMP)
                        if self.pfc.read_pfc(self.contact.CARD2, jig_pfc + 1) == 0:
                            RESULT_TEMP = True
                        else:
                            RESULT_TEMP = False
                            self.print_console(f"LVD OP PFC {op_pfc_check} NC SLOT IS SHORT WITH OP PFC {op_pfc}",
                                               "RED")
                        RESULT_1.append(RESULT_TEMP)
                if self.mcm_type == 1:
                    M1000Telnet.telnet_set_command(OIDRead('DCIF 2 OP PFC')['pfc'], 0)
                    M1000Telnet.telnet_set_command(OIDRead('DCIF 8 OP PFC')['pfc'], 0)
                elif self.mcm_type == 2:
                    self.M2000.MCM_SET_COMMAND(M2000OIDRead('DCIF 2 OP PFC')['pfc'], 0)
                    self.M2000.MCM_SET_COMMAND(M2000OIDRead('DCIF 8 OP PFC')['pfc'], 0)

            RESULT.append(CALCULATE_RESULT(RESULT_1))

            if dcif_op_card_state == "PRESENT":
                for op_pfc in range(1, 9):
                    if op_pfc < 3:
                        set_dut_pfc = pow(2, op_pfc + 4)
                        if self.mcm_type == 1:
                            M1000Telnet.telnet_set_command(OIDRead('DCIF 2 OP PFC')['pfc'], set_dut_pfc)
                        elif self.mcm_type == 2:
                            self.M2000.MCM_SET_COMMAND(M2000OIDRead('DCIF 2 OP PFC')['pfc'], set_dut_pfc)
                    set_dcif_pfc = pow(2, op_pfc - 1)
                    if self.mcm_type == 1:
                        M1000Telnet.telnet_set_command(OIDRead('DCIF 8 OP PFC')['pfc'], set_dcif_pfc)
                    elif self.mcm_type == 2:
                        self.M2000.MCM_SET_COMMAND(M2000OIDRead('DCIF 8 OP PFC')['pfc'], set_dcif_pfc)
                    time.sleep(2)
                    for op_pfc_check in range(1, 9):
                        jig_pfc_no = (2 * op_pfc_check) - 1
                        if op_pfc == op_pfc_check:
                            if self.pfc.read_pfc(self.contact.CARD2, jig_pfc_no) == 0:
                                RESULT_TEMP = True
                                self.print_console(f"DCIF OP PFC {op_pfc} NC SLOT IS OK")
                            else:
                                RESULT_TEMP = False
                                self.print_console(f"DCIF OP PFC {op_pfc} NC SLOT IS FAULTY", "RED")
                            RESULT_2.append(RESULT_TEMP)
                            if self.pfc.read_pfc(self.contact.CARD2, jig_pfc_no + 1) == 1:
                                RESULT_TEMP = True
                                self.print_console(f"DCIF OP PFC {op_pfc} NO SLOT IS OK")
                            else:
                                RESULT_TEMP = False
                                self.print_console(f"DCIF OP PFC {op_pfc} NO SLOT IS FAULTY", "RED")
                            RESULT_2.append(RESULT_TEMP)
                        else:
                            if self.pfc.read_pfc(self.contact.CARD2, jig_pfc_no) == 1:
                                RESULT_TEMP = True
                                # self.print_console(f"DCIF OP PFC {op_pfc} NC SLOT IS S")
                            else:
                                RESULT_TEMP = False
                                self.print_console(f"DCIF OP PFC {op_pfc} NC SLOT IS SHORT WITH OP PFC", "RED")
                            RESULT_2.append(RESULT_TEMP)
                            if self.pfc.read_pfc(self.contact.CARD2, jig_pfc_no + 1) == 0:
                                RESULT_TEMP = True
                                self.print_console(f"DCIF OP PFC {op_pfc} NO SLOT IS OK")
                            else:
                                RESULT_TEMP = False
                                self.print_console(f"DCIF OP PFC {op_pfc} NO SLOT IS SHORT WITH OP PFC", "RED")
                            RESULT_2.append(RESULT_TEMP)
                    if self.mcm_type == 1:
                        M1000Telnet.telnet_set_command(OIDRead('DCIF 8 OP PFC')['pfc'], 0)
                        if op_pfc < 3:
                            M1000Telnet.telnet_set_command(OIDRead('DCIF 2 OP PFC')['pfc'], 0)
                    elif self.mcm_type == 2:
                        self.M2000.MCM_SET_COMMAND(M2000OIDRead('DCIF 8 OP PFC')['pfc'], 0)
                        if op_pfc < 3:
                            self.M2000.MCM_SET_COMMAND(M2000OIDRead('DCIF 2 OP PFC')['pfc'], 0)
                RESULT.append(CALCULATE_RESULT(RESULT_2))
            else:
                self.print_console("DCIF 8 OP PFC CARD NOT APPLICABLE")
                RESULT_TEMP = True
                RESULT_2.append(RESULT_TEMP)
                RESULT.append(CALCULATE_RESULT(RESULT_2))
            self.print_console("OP_PFC_CHECK TEST FINISHED...")
            return CALCULATE_RESULT(RESULT)

        else:
            self.print_console("DCIF 8 OP PFC CARD TEST NOT APPLICABLE")
            RESULT_TEMP = True
            RESULT.append(RESULT_TEMP)
        self.print_console("OP_PFC_CHECK TEST FINISHED...")
        return CALCULATE_RESULT(RESULT)

    def IP_PFC_CHECK(self):
        """
        TEST BLOCK OF INPUT PFC

        DEFINES, TEST INPUT PFC(S) OR LVD(S) OF THE RACK SYSTEM

        :return: STATUS OF THE FUNCTION BLOCK IN BOOLEAN FORM (TRUE OR FALSE)
        """

        global RESULT_TEMP, RESULT_TEMP_DOOR_TRIP
        self.print_console("IP_PFC_CHECK TEST STARTED...")
        RESULT = []

        if self.mcm_type == 1:
            M1000Telnet.telnet_set_command(OIDRead('SYSTEM COMMANDS')['ate test'], "TEST_M1000_ATE")

        for i in range(1, 9):
            self.pfc.pfc_stop(0, self.contact.CARD2)
        time.sleep(2)

        pfcio_card_state = ConfigRead('DUT CONFIGURATION')['pfc io card']
        dcif_ip_card_state = ConfigRead('DUT CONFIGURATION')['dcif ip card']
        dcif_type_number = int(ConfigRead('DUT CONFIGURATION')['dcif card type number'])

        if dcif_type_number == 1 or dcif_type_number == 2:
            if dcif_ip_card_state == "PRESENT":
                ip_pfc_count = 8
            else:
                ip_pfc_count = 2

            for i in range(1, ip_pfc_count + 1):
                if self.mcm_type == 1:
                    M1000Telnet.telnet_set_command(OIDRead('DCIF 8 IP PFC')['invert pfc'] + str(i), 0)
                else:
                    self.M2000.MCM_SET_COMMAND(M2000OIDRead('DCIF 8 IP PFC')['invert pfc'] + str(i), 0)

            time.sleep(5)

            if self.mcm_type == 1:
                if int(M1000Telnet.telnet_get_command(OIDRead('DCIF 8 IP PFC')['pfc'])) == 0:
                    RESULT_TEMP = True
                else:
                    RESULT_TEMP = False
                    self.print_console("IP PFC CARD/ CABLE IS FAULTY...", "RED")
                    return RESULT_TEMP
            elif self.mcm_type == 2:
                if int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('DCIF 8 IP PFC')['pfc'])) == 0:
                    RESULT_TEMP = True
                else:
                    RESULT_TEMP = False
                    self.print_console("IP PFC CARD/ CABLE IS FAULTY...", "RED")
                    return RESULT_TEMP

            RESULT.append(RESULT_TEMP)

            for ip_pfc in range(1, ip_pfc_count + 1):
                self.pfc.pfc_set(0, f"pfc {ip_pfc}", 1)
                time.sleep(1)
                ip_pfc_state = pow(2, ip_pfc_count - 1)
                state = 0
                if self.mcm_type == 1:
                    state = int(M1000Telnet.telnet_get_command(OIDRead('DCIF 8 IP PFC')['pfc']))
                elif self.mcm_type == 2:
                    state = int(self.M2000.MCM_GET_COMMAND(M2000OIDRead('DCIF 8 IP PFC')['pfc']))
                if state == ip_pfc_state:
                    RESULT_TEMP = True
                    self.print_console(f"IP PFC {ip_pfc} is OK")
                else:
                    RESULT_TEMP = False
                    self.print_console(f"IP PFC {ip_pfc} is faulty", "RED")
                RESULT.append(RESULT_TEMP)
                self.pfc.pfc_set(0, f"pfc {ip_pfc}", 0)

            self.prompt.TimerPrompt("Remove PFC JIG connector and Insert IP PFC system alarm connector")

        ac_phase_type = ConfigRead("DUT CONFIGURATION")['ac phases type']

        if ac_phase_type == "SINGLE PHASE":
            self.prompt.Message(prompt="REMOVE PHASE SPD")
            if int(self.MCM_READ_COMMAND('ALARM', 'spu fail')) == 1:
                RESULT_TEMP = True
                self.print_console("SPU ALARM FOR PHASE OK")
            else:
                RESULT_TEMP = False
                self.print_console("SPU ALARM FOR PHASE FAIL", 'RED')
            RESULT.append(RESULT_TEMP)

            self.prompt.Message(prompt="INSERT BACK PHASE SPD. REMOVE NEUTRAL SPD")

            if int(self.MCM_READ_COMMAND('ALARM', 'spu fail')) == 1:
                RESULT_TEMP = True
                self.print_console("SPU ALARM FOR NEUTRAL OK")
            else:
                RESULT_TEMP = False
                self.print_console("SPU ALARM FOR NEUTRAL FAIL", 'RED')
            RESULT.append(RESULT_TEMP)

        else:
            self.prompt.Message(prompt="REMOVE R PHASE SPD")
            time.sleep(2)
            if int(self.MCM_READ_COMMAND('ALARM', 'spu fail')) == 1:
                RESULT_TEMP = True
                self.print_console("SPU ALARM FOR R PHASE OK")
            else:
                RESULT_TEMP = False
                self.print_console("SPU ALARM FOR R PHASE FAIL", 'RED')
            RESULT.append(RESULT_TEMP)
            self.prompt.Message(prompt="INSERT BACK R PHASE SPD. REMOVE Y PHASE SPD")
            time.sleep(2)
            if int(self.MCM_READ_COMMAND('ALARM', 'spu fail')) == 1:
                RESULT_TEMP = True
                self.print_console("SPU ALARM FOR Y PHASE OK")
            else:
                RESULT_TEMP = False
                self.print_console("SPU ALARM FOR Y PHASE FAIL", 'RED')
            RESULT.append(RESULT_TEMP)
            self.prompt.Message(prompt="INSERT BACK Y PHASE SPD. REMOVE B PHASE SPD")
            time.sleep(2)
            if int(self.MCM_READ_COMMAND('ALARM', 'spu fail')) == 1:
                RESULT_TEMP = True
                self.print_console("SPU ALARM FOR B PHASE OK")
            else:
                RESULT_TEMP = False
                self.print_console("SPU ALARM FOR B PHASE FAIL", 'RED')
            RESULT.append(RESULT_TEMP)
            self.prompt.Message(prompt="INSERT BACK B PHASE SPD. REMOVE NEUTRAL PHASE SPD")
            time.sleep(2)
            if int(self.MCM_READ_COMMAND('ALARM', 'spu fail')) == 1:
                RESULT_TEMP = True
                self.print_console("SPU ALARM FOR NEUTRAL PHASE OK")
            else:
                RESULT_TEMP = False
                self.print_console("SPU ALARM FOR NEUTRAL PHASE FAIL", 'RED')
            RESULT.append(RESULT_TEMP)
        alarm = True
        while alarm:
            self.prompt.Message(prompt="INSERT BACK ALL SPD(S)")
            time.sleep(2)
            if int(self.MCM_READ_COMMAND('ALARM', 'spu fail')) == 0:
                alarm = False
        self.print_console("DOOR OPEN ALARM TEST STARTED...")

        user_state = self.prompt.User_prompt("DO YOU WANT TO TEST DOOR ALARM. PRESS ENTER TO PROCEED!")

        if user_state:
            read_restore_time = int(self.MCM_READ_COMMAND('DOOR SETTING', 'door open restore time'))
            self.MCM_WRITE_COMMAND('DOOR SETTING', 'door open restore time', 2)
            ip_pfc_state = True
            while ip_pfc_state:
                if not ip_pfc_state:
                    self.prompt.Message(prompt=f"ip_pfc_state {ip_pfc_state}")
                else:
                    self.prompt.Message(prompt="CLEAR DOOR OPEN ALARM, IF PRESENT. PRESS ENTER KEY TO PROCEED")
                    ip_pfc_state = False
                    self.prompt.Message(prompt="OPEN THE DOOR. PRESS ENTER KEY TO PROCEED")
                    self.prompt.TimerPrompt("WAIT FOR 6 SECONDS", 7)

                    if int(self.MCM_READ_COMMAND('ALARM', 'door open alarm')) == 1:
                        RESULT_TEMP_DOOR_TRIP = True
                        self.print_console("DOOR OPEN ALARM TESTED OK")
                    else:
                        RESULT_TEMP_DOOR_TRIP = False
                        self.print_console("DOOR OPEN ALARM TEST FAIL", 'RED')
                self.MCM_WRITE_COMMAND('DOOR SETTING', 'door open restore time', read_restore_time)
        else:
            print("door open alarm not tested")
            RESULT_TEMP_DOOR_TRIP = True
            self.print_console("DOOR OPEN TEST BYPASSED")
        RESULT.append(RESULT_TEMP_DOOR_TRIP)

        self.print_console("DOOR ALARM TEST FINISHED...")

        self.print_console("SMOKE ALARM TEST STARTED...")

        user_state = self.prompt.User_prompt("DO YOU WANT TO TEST SMOKE ALARM. PRESS ENTER TO PROCEED!")

        if user_state:
            ip_pfc_state = True
            while ip_pfc_state:
                if not ip_pfc_state:
                    self.prompt.Message(prompt=f"ip_pfc_state {ip_pfc_state}")
                else:
                    # self.prompt.Message(prompt="CLEAR DOOR OPEN ALARM, IF PRESENT. PRESS ENTER KEY TO PROCEED")
                    ip_pfc_state = False
                    self.prompt.Message(prompt="OPEN THE DOOR. PRESS ENTER KEY TO PROCEED")
                    self.prompt.TimerPrompt("WAIT FOR 6 SECONDS", 7)

                    if int(self.MCM_READ_COMMAND('ALARM', 'smoke alarm')) == 1:
                        RESULT_TEMP_DOOR_TRIP = True
                        self.print_console("SMOKE ALARM TESTED OK")
                    else:
                        RESULT_TEMP_DOOR_TRIP = False
                        self.print_console("SMOKE ALARM TEST FAIL", 'RED')
        else:
            print("smoke alarm not tested")
            RESULT_TEMP_DOOR_TRIP = True
            self.print_console("SMOKE ALARM TEST BYPASSED")
        RESULT.append(RESULT_TEMP_DOOR_TRIP)
        self.print_console("SMOKE ALARM TEST FINISHED...")

        self.print_console("POWER POINT/ AVIATION ALARM TEST STARTED...")

        user_state = self.prompt.User_prompt("DO YOU WANT TO TEST POWER POINT/ AVIATION. PRESS ENTER TO PROCEED!")

        if user_state:
            power_point = self.prompt.User_prompt("IS POWER POINT/ AVIATION CONTINUITY IS OKAY?")
            if power_point:
                RESULT_P_TEMP = True
                self.print_console("POWER POINT/ AVIATION TEST OK")
            else:
                RESULT_P_TEMP = False
                self.print_console("POWER POINT/ AVIATION TEST FAILED", 'RED')
        else:
            print("POWERPOINT NOT alarm not tested")
            RESULT_P_TEMP = True
            self.print_console("POWER POINT/ AVIATION TEST BYPASSED")
        RESULT.append(RESULT_P_TEMP)
        self.print_console("POWER POINT/ AVIATION TEST FINISHED...")

        self.print_console("FAN TEST STARTED...")

        user_state = self.prompt.User_prompt("DO YOU WANT TO TEST FAN FUNCTIONALITY. PRESS ENTER TO PROCEED!")

        if user_state:
            power_point = self.prompt.User_prompt("INCREASE TEMPERATURE OF TEMPERATURE SENSOR, IS FAN RUNNING?")
            if power_point:
                RESULT_P_TEMP = True
                self.print_console("FAN TEST TEST OK")
            else:
                RESULT_P_TEMP = False
                self.print_console("FAN TEST TEST FAILED", 'RED')
        else:
            print("FAN TEST not tested")
            RESULT_P_TEMP = True
            self.print_console("FAN FUNCTIONALITY TEST BYPASSED")
        RESULT.append(RESULT_P_TEMP)
        self.print_console("FAN TEST TEST FINISHED...")
        self.print_console("IP_PFC_CHECK TEST FINISHED...")
        return CALCULATE_RESULT(RESULT)

    def DC_VOLTAGE_MEASUREMENT(self):
        """
        TEST BLOCK OF DC VOLTAGE MEASUREMENT

        DEFINES, TEST DC VOLTAGES FOR THE RACK SYSTEM

        :return: STATUS OF THE FUNCTION BLOCK IN BOOLEAN FORM (TRUE OR FALSE)
        """

        global count_temp
        self.MCM_WRITE_COMMAND('SYSTEM COMMANDS', 'ate test', "TEST_M1000_ATE")
        test_sub_id = 0
        self.print_console("DC_VOLTAGE_MEASUREMENT TEST STARTED...")
        RESULT = []
        RESULT_1 = []
        RESULT_2 = []

        self.pfc.pfc_set(0, 'bus', 1)
        self.pfc.pfc_set(0, 'battery_1', 1)

        SMR_BATTERY_SET_VOLTAGE(53.5)
        DC_LOAD_SET_CURRENT_CC(20, "LOAD")

        if ATE_LOAD_COUNT != 1:  # ONLY 1 LOAD IS CONFIGURED, 19/08/2016
            DC_LOAD_SET_CURRENT_CC(10, "BATT")

        self.pfc.pfc_set(0, 'load_mains', 1)
        self.pfc.pfc_set(0, 'p_load', 1)

        batt_fuse_count = int(ConfigRead('DUT CONFIGURATION')['no. of battery fuses'])
        batt_lvd_count = int(ConfigRead('DUT CONFIGURATION')['no. of battery lvd'])
        load_current_count = int(ConfigRead('DUT CONFIGURATION')['no. of load current'])
        DCIF_CARD_TYPE = ConfigRead('DUT CONFIGURATION')['dcif card type']

        # raw_input("press enter key")

        # CURRENT GAIN AND OFFSET IS MADE 0.
        by_pass = 1
        if DCIF_CARD_TYPE == 'HALL EFFECT' or by_pass == 1:
            for i in range(1, load_current_count + batt_lvd_count + 1):
                self.print_console("CURRENT CHANNEL " + str(i) + " GAIN: " + str(
                    self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(i) + ' gain')))
                self.print_console("CURRENT CHANNEL " + str(i) + " OFFSET: " + str(
                    self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(i) + ' offset')))
                # PRINT_CONSOLE(self,"CURRENT CHANNEL "+str(i)+" DEADBAND: "+str(TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(i)+' deadband'])))
                if (self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(i) + ' gain') != '0') or (
                        self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(
                            i) + ' offset') != '0'):  # or (TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(i)+' deadband'])!='0'):
                    # self.print_console("Resetting Deadband,offset and gain again")
                    self.MCM_WRITE_COMMAND('CALIBRATE CURRENT', 'channel' + str(i) + ' gain', 0)
                    time.sleep(2)
                    self.MCM_WRITE_COMMAND('CALIBRATE CURRENT', 'channel' + str(i) + ' offset', 0)
                    time.sleep(2)
                    # TELNET_SET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(i)+' deadband'],0)
                    # time.sleep(1.5)
                    self.print_console("CURRENT CHANNEL " + str(i) + " GAIN: " + str(
                        self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(i) + ' gain')))
                    self.print_console("CURRENT CHANNEL " + str(i) + " OFFSET: " + str(
                        self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(i) + ' offset')))
                    # PRINT_CONSOLE(self,"CURRENT CHANNEL "+str(i)+" DEADBAND: "+str(TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(i)+' deadband'])))

        # PRINT_CONSOLE(self, "batt lvd count: "+str(batt_lvd_count))
        # TELNET_SET_COMMAND(self.telnet,OIDRead('ALARM MASK')['battery lvd'],1)
        # raw_input("press enter key")
        if batt_fuse_count > 1 and batt_lvd_count == 1:
            self.prompt.Message(prompt='Switch OFF Battery MCBs/Remove Fuses')
            self.MCM_WRITE_COMMAND('SYSTEM COMMANDS', 'system reset', 1)
        ##        SET_JIG_PFC_OP(self.can,'BATT COMMON',0)
        ##        SET_JIG_PFC_OP(self.can,'BATT1',0)
        ##        time.sleep(2)
        ##        SET_JIG_PFC_OP(self.can,'BATT COMMON',1)
        ##        SET_JIG_PFC_OP(self.can,'BATT1',1)
        ##        time.sleep(5)
        else:
            None
            # MESSAGE_PROMPT(self,'Switch OFF Battery MCBs/Remove Fuses') # NOT REQUIRED IN INDIVIDAL BATTERY LVD CONDITION
        SET_INDI_BATTERY_PATH(1)

        # raw_input("press enter key")
        for count in range(1, batt_fuse_count + 1):
            self.print_console("CHECKING FOR BATTERY: " + str(count))
            SET_INDI_BATTERY_PATH(count)
            # raw_input("press enter key")
            SET_INDI_BATTERY_ISOLATE(count, 1)  # this command to be replaced with internal command
            # raw_input("press enter key")
            time.sleep(10)  # TIME INCREASED TO 10 FROM 5
            # PRINT_CONSOLE(self,"checking for batt:"+str(count))
            for count_temp in range(1, batt_fuse_count + 1):
                # PRINT_CONSOLE(self, "count temp: "+str(count_temp))

                # raw_input("press enter key")
                if count == count_temp:
                    actual_voltage = float(READ_DC_VOLTAGE(self, "BATT"))
                    # PRINT_CONSOLE(self, "actual voltage: "+str(actual_voltage))
                    DUT_batt_volt = float(
                        TELNET_GET_COMMAND(self.telnet, OIDRead('DC READ VOLTAGE')['batt' + str(count_temp)]))
                    PRINT_CONSOLE(self, "BATTERY " + str(count) + " VOLTAGE:" + str(DUT_batt_volt))
                    PRINT_CONSOLE(self, "METER VOLTAGE:" + str(actual_voltage))
                    RESULT_TEMP = COMPARE(actual_voltage, DUT_batt_volt, 5)
                    RESULT_1.append(RESULT_TEMP)
                    # PRINT_CONSOLE(self,str(RESULT_1))
                else:
                    DUT_batt_volt = float(
                        TELNET_GET_COMMAND(self.telnet, OIDRead('DC READ VOLTAGE')['batt' + str(count_temp)]))
                    PRINT_CONSOLE(self, "BATTERY " + str(count_temp) + " VOLTAGE:" + str(DUT_batt_volt))
                    # PRINT_CONSOLE(self,"not known")
                    if DUT_batt_volt > 10:
                        RESULT_TEMP = False
                        PRINT_CONSOLE(self, "BATT " + str(count_temp) + "battery sense is", WARNING)
                        PRINT_CONSOLE(self, "short with BATT " + str(count), WARNING)

                    else:
                        RESULT_TEMP = True
                    RESULT_1.append(RESULT_TEMP)
                    # PRINT_CONSOLE(self,str(RESULT_1))
                # count_temp+=1
            # raw_input("check")
            DUT_bus_volt = float(TELNET_GET_COMMAND(self.telnet, OIDRead('DC READ VOLTAGE')['bus']))
            PRINT_CONSOLE(self, "BUS VOLTAGE:" + str(DUT_bus_volt))
            # PRINT_CONSOLE(self, "BUS Voltage"+str(DUT_bus_volt))
            if DUT_bus_volt > 10:
                RESULT_TEMP = False
                PRINT_CONSOLE(self, "check BATT " + str(count_temp) + " LVD contactor wiring", WARNING)
            else:
                RESULT_TEMP = True
            RESULT_1.append(RESULT_TEMP)
            # PRINT_CONSOLE(self,str(RESULT_1))
            SET_INDI_BATTERY_ISOLATE(self, count, 0)
            time.sleep(5)

        id = self.sql.SQL_SELECT_3_QUERY('td_id', 'test_detail_results', 'td_test_item', 'DC_VOLTAGE_MEASUREMENT',
                                         'td_readby', 'BATT VOLTAGE', 'td_mt_id', self.test_id)
        print
        id
        if id != 0:
            print
            "update row"
            self.sql.SQL_TEST_ITEM_RUN_DETAIL_UPDATE_QUERY(CALCULATE_RESULT(RESULT_1), id)
        else:
            print
            "insert row"
            test_sub_id += 1
            self.sql.SQL_TEST_ITEM_RUN_DETAIL_RESULTS_INSERT_QUERY(self.test_id, "'DC_VOLTAGE_MEASUREMENT'",
                                                                   "'BATT VOLTAGE'", test_sub_id, "''", "''",
                                                                   CALCULATE_RESULT(RESULT_1))

        RESULT.append(CALCULATE_RESULT(RESULT_1))
        SET_INDI_BATTERY_PATH(1)
        # PRINT_CONSOLE(self,"CAUTION!!! BATTERY 1 IS ON")
        if batt_fuse_count > 1 and batt_lvd_count == 1:
            MESSAGE_PROMPT(self, 'Switch ON Battery MCBs/Insert Fuses')
        else:
            None
            # MESSAGE_PROMPT(self,'Switch ON Battery MCBs/Insert Fuses')
        # raw_input("Insert all BATTERY Fuse/SWITCH ON BATTERY MCB. Press any key to continue")
        #     PRINT_CONSOLE(self,"setting all battery path")
        #     for i in range(1,batt_fuse_count+1):
        #         SET_INDI_BATTERY_PATH(self,i)
        ## checking bus voltage with all battery voltages
        for count in range(1, batt_fuse_count + 1):
            # PRINT_CONSOLE(self,"count: "+str(count))
            SET_INDI_BATTERY_PATH(count)
            time.sleep(3)
            for count_temp in range(1, batt_fuse_count + 1):
                SET_INDI_BATTERY_PATH(count_temp)
                # PRINT_CONSOLE(self,"count temp: "+str(count_temp))
                time.sleep(3)
                actual_voltage = float(READ_DC_VOLTAGE("BATT"))
                self.print_console("actual voltage: " + str(actual_voltage))
                DUT_batt_volt = float(self.MCM_READ_COMMAND('DC READ VOLTAGE', 'batt' + str(count_temp)))
                self.print_console("Battery Voltage " + str(count_temp) + ": " + str(DUT_batt_volt))
                if abs(actual_voltage - DUT_batt_volt) < 5:
                    RESULT_TEMP = True
                else:
                    RESULT_TEMP = False
                RESULT_2.append(RESULT_TEMP)
            # PRINT_CONSOLE(self,str(RESULT))
            DUT_bus_volt = float(self.MCM_READ_COMMAND('DC READ VOLTAGE', 'bus'))
            self.print_console("BUS Voltage" + str(DUT_bus_volt))
            actual_voltage = float(READ_DC_VOLTAGE("BATT"))
            if abs(actual_voltage - DUT_bus_volt) < 5:
                RESULT_TEMP = True
            else:
                RESULT_TEMP = False
            RESULT_2.append(RESULT_TEMP)
        SET_BATTERY_ISOLATE(batt_lvd_count, 0)
        self.print_console("DC_VOLTAGE_MEASUREMENT TEST FINISHED...")

        # id = self.sql.SQL_SELECT_3_QUERY('td_id', 'test_detail_results', 'td_test_item', 'DC_VOLTAGE_MEASUREMENT',
        #                                  'td_readby', 'LOAD VOLTAGE', 'td_mt_id', self.test_id)
        # print
        # id
        # if id != 0:
        #     print
        #     "update row"
        #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_UPDATE_QUERY(CALCULATE_RESULT(RESULT_2), id)
        # else:
        #     print
        #     "insert row"
        #     test_sub_id += 1
        #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_RESULTS_INSERT_QUERY(self.test_id, "'DC_VOLTAGE_MEASUREMENT'",
        #                                                            "'LOAD VOLTAGE'", test_sub_id, "''", "''",
        #                                                            CALCULATE_RESULT(RESULT_2))

        RESULT.append(CALCULATE_RESULT(RESULT_2))
        return CALCULATE_RESULT(RESULT)

    def CALIBRATE_DC_VOLTAGE(self):

        DCIF_CARD_TYPE = ConfigRead("DUT CONFIGURATION")['dcif card type']

        self.pfc.pfc_set(0, "battery_mains", 1)

        if self.mcm_type == 1:
            self.MCM_WRITE_COMMAND('SYSTEM COMMANDS', 'ate test', 'TEST_M1000_ATE')

        test_sub_id = 0

        RESULT = []

        self.print_console("CALIBRATE DC VOLTAGE TEST STARTED...")

        self.MCM_WRITE_COMMAND('CALIBRATE DC VOLTAGE', 'channel1 deadband', 50)

        self.dcload.DC_LOAD_SET_CURRENT_CC(5)

        self.smrcan.SMR_BATTERY_SET_VOLTAGE(53.5)

        battery_fuse_count = int(ConfigRead("DUT CONFIGURATION")['no. of battery fuses'])

        self.pfc.pfc_set(0, "bus", 1)

        DC_VOLTAGE_CALIBRATION_TOLERANCE = float(CalibrateSetting("GENERAL FACTORS")['dc voltage tolerance'])

        for i in range(1, battery_fuse_count + 1):
            self.pfc.pfc_set(0, 'battery_' + str(i), 1)

        self.MCM_WRITE_COMMAND("CALIBRATE DC VOLTAGE", 'channel1 gain', 0)

        time.sleep(1)

        self.dcload.DC_LOAD_SET_CURRENT_CC(20, "BATT")

        for i in range(0, 6):
            self.print_console("RESETTING VOLTAGE GAIN AND DEADBAND")
            self.MCM_WRITE_COMMAND('CALIBRATE DC VOLTAGE', f'channel{i + 1} deadband', 50)
            time.sleep(1)
            self.print_console(
                f"CHANNEL {i + 1} VOLTAGE DEADBAND: {self.MCM_READ_COMMAND('CALIBRATE DC VOLTAGE', f'channel{i + 1} deadband')}")
            self.MCM_WRITE_COMMAND("CALIBRATE DC VOLTAGE", f"channel{i + 1} gain", 0)
            time.sleep(1)
            self.print_console(
                f"CHANNEL {i + 1} VOLTAGE GAIN: {self.MCM_READ_COMMAND('CALIBRATE DC VOLTAGE', f'channel{i + 1} gain')}")
        if DCIF_CARD_TYPE != "SHUNT SMALL":
            actual_voltage = float(self.dcload.DC_LOAD_READ_OUTPUT_VOLTAGE())
            for i in range(1, battery_fuse_count + 1):
                self.MCM_WRITE_COMMAND("CALIBRATE DC VOLTAGE", f"batt{i + 1}", actual_voltage)
            self.MCM_WRITE_COMMAND("CALIBRATE DC VOLTAGE", 'bus', actual_voltage)
            time.sleep(3)

        self.print_console("VERIFY VOLTAGE CALIBRATION")

        self.smrcan.SMR_BATTERY_SET_VOLTAGE(48)
        time.sleep(3)

        for i in range(1, battery_fuse_count + 1):
            DUTT_BATT_VOLT = float(self.MCM_READ_COMMAND("DC READ VOLTAGE", f'batt{i}'))

            actual_voltage = AVG_METER_VOLTAGE(self, "BATT")
            actual_voltage = round(actual_voltage, 2)

            if abs(DUTT_BATT_VOLT - actual_voltage) < DC_VOLTAGE_CALIBRATION_TOLERANCE:
                RESULT_TEMP = True
            else:
                RESULT_TEMP = False

            time.sleep(3)

            if RESULT_TEMP:
                self.print_console(f'BATTERY {i} VOLTAGE: {DUTT_BATT_VOLT}')
                self.print_console(f'METER VOLTAGE: {actual_voltage}')
                self.print_console(f"BATTERY {i} VOLTAGE CALIBRATION OK")
            else:
                self.print_console(f'BATTERY {i} VOLTAGE: {DUTT_BATT_VOLT}', "RED")
                self.print_console(f'METER VOLTAGE: {actual_voltage}', "RED")
                self.print_console(f"BATTERY {i} VOLTAGE CALIBRATION FAIL", "RED")
            RESULT.append(RESULT_TEMP)

        DUT_BUS_VOLTAGE = float(self.MCM_READ_COMMAND("DC READ VOLTAGE")['bus'])
        actual_voltage = round(float(READ_DC_VOLTAGE("BATT")), 2)

        if abs(DUT_BUS_VOLTAGE - actual_voltage) < DC_VOLTAGE_CALIBRATION_TOLERANCE:
            RESULT_TEMP = True
        else:
            RESULT_TEMP = False

        time.sleep(1)

        if RESULT_TEMP:
            self.print_console(f'BUS VOLTAGE: {DUT_BUS_VOLTAGE}')
            self.print_console(f'METER VOLTAGE: {actual_voltage}')
            self.print_console(f"BUS VOLTAGE CALIBRATION OK")
        else:
            self.print_console(f'BUS VOLTAGE: {DUT_BUS_VOLTAGE}', "RED")
            self.print_console(f'METER VOLTAGE: {actual_voltage}', "RED")
            self.print_console(f"BUS VOLTAGE CALIBRATION FAIL", "RED")
        RESULT.append(RESULT_TEMP)

        self.smrcan.SMR_BATTERY_SET_VOLTAGE(56)
        time.sleep(3)

        for i in range(1, battery_fuse_count + 1):
            DUTT_BATT_VOLT = float(self.MCM_READ_COMMAND("DC READ VOLTAGE", f'batt{i}'))

            actual_voltage = AVG_METER_VOLTAGE(self, "BATT")
            actual_voltage = round(actual_voltage, 2)

            if abs(DUTT_BATT_VOLT - actual_voltage) < DC_VOLTAGE_CALIBRATION_TOLERANCE:
                RESULT_TEMP = True
            else:
                RESULT_TEMP = False

            time.sleep(3)

            if RESULT_TEMP:
                self.print_console(f'BATTERY {i} VOLTAGE: {DUTT_BATT_VOLT}')
                self.print_console(f'METER VOLTAGE: {actual_voltage}')
                self.print_console(f"BATTERY {i} VOLTAGE CALIBRATION OK")
            else:
                self.print_console(f'BATTERY {i} VOLTAGE: {DUTT_BATT_VOLT}', "RED")
                self.print_console(f'METER VOLTAGE: {actual_voltage}', "RED")
                self.print_console(f"BATTERY {i} VOLTAGE CALIBRATION FAIL", "RED")
            RESULT.append(RESULT_TEMP)

        DUT_BUS_VOLTAGE = float(self.MCM_READ_COMMAND("DC READ VOLTAGE")['bus'])
        actual_voltage = round(float(READ_DC_VOLTAGE("BATT")), 2)

        if abs(DUT_BUS_VOLTAGE - actual_voltage) < DC_VOLTAGE_CALIBRATION_TOLERANCE:
            RESULT_TEMP = True
        else:
            RESULT_TEMP = False

        time.sleep(1)

        if RESULT_TEMP:
            self.print_console(f'BUS VOLTAGE: {DUT_BUS_VOLTAGE}')
            self.print_console(f'METER VOLTAGE: {actual_voltage}')
            self.print_console(f"BUS VOLTAGE CALIBRATION OK")
        else:
            self.print_console(f'BUS VOLTAGE: {DUT_BUS_VOLTAGE}', "RED")
            self.print_console(f'METER VOLTAGE: {actual_voltage}', "RED")
            self.print_console(f"BUS VOLTAGE CALIBRATION FAIL", "RED")
        RESULT.append(RESULT_TEMP)

        return CALCULATE_RESULT(RESULT)

    def DC_CURRENT_MEASUREMENT_BATT_DISCHARGE(self):
        global RESULT_TEMP_MCB_TRIP, count_temp
        if self.mcm_type == 1:
            self.MCM_WRITE_COMMAND("SYSTEM COMMANDS", 'ate test', 'TEST_M1000_ATE')

        test_sub_id = 0

        self.print_console("DC CURRENT MEASUREMENT BATT DISCHARGE TEST STARTED...")

        batt_fuse_count = int(ConfigRead('DUT CONFIGURATION')['no. of battery fuses'])
        batt_lvd_count = int(ConfigRead('DUT CONFIGURATION')['no. of battery lvd'])
        load_lvd_count = int(ConfigRead('DUT CONFIGURATION')['no. of load lvd'])
        load_current_count = int(ConfigRead('DUT CONFIGURATION')['no. of load current'])
        load_current_sensor_state = ConfigRead('DUT CONFIGURATION')['load current sensor']
        DC_CURRENT_FACTOR_PERCENTAGE = float(CalibrateSetting('GENERAL FACTORS')['dc current check factor percentage'])
        DC_CURRENT_TOLERANCE_PERCENTAGE = float(
            CalibrateSetting('GENERAL FACTORS')['dc current check tolerance percentage'])
        DCIF_CARD_TYPE = ConfigRead('DUT CONFIGURATION')['dcif card type']

        if DCIF_CARD_TYPE == "HALL EFFECT":
            CURRENT_SENSOR_VALUE = int(ConfigRead("DUT CONFIGURATION")['channel1 hall effect value'])
        else:
            CURRENT_SENSOR_VALUE = int(ConfigRead("DUT CONFIGURATION")['channel1 shunt value'])

        LOAD_SET_CURRENT = int(CURRENT_SENSOR_VALUE * (float(DC_CURRENT_FACTOR_PERCENTAGE) / 100))
        LOAD_CURRENT_OFFSET = int(CURRENT_SENSOR_VALUE * (float(DC_CURRENT_TOLERANCE_PERCENTAGE) / 100))
        self.smrcan.SMR_BATTERY_SET_VOLTAGE(53.5)

        RESULT = []
        self.pfc.pfc_set(0, 'battery_mains', 1)
        SET_INDI_BATTERY_PATH(1)  ## NEED TO MODIFY PFC PART CODE
        self.pfc.pfc_set(0, 'load_mains', 1)
        self.pfc.pfc_set(0, 'n_p_load_1', 1)

        if load_lvd_count == 1:
            self.pfc.pfc_set(0, 'p_load', 1)
        else:
            self.pfc.pfc_set(0, 'p_load', 0)

        self.pfc.pfc_set(0, 'r_phase', 0)
        self.pfc.pfc_set(0, 'y_phase', 0)
        self.pfc.pfc_set(0, 'b_phase', 0)

        self.dcload.DC_LOAD_SET_CURRENT_CC(LOAD_SET_CURRENT, "LOAD")

        for i in range(1, load_lvd_count + 1):
            self.pfc.pfc_set(0, 'n_p_load' + str(i), 1)

        for count in range(1, batt_lvd_count + 1):
            self.print_console(f"CHECKING BATTERY {count} DISCHARGE CURRENT")
            SET_INDI_BATTERY_PATH(count)
            time.sleep(1)

            for count_temp in range(1, batt_lvd_count + 1):
                if count == count_temp or batt_lvd_count < 2:
                    actual_current = float(READ_DC_VOLTAGE("LOAD"))
                    if actual_current > (LOAD_SET_CURRENT - LOAD_CURRENT_OFFSET):
                        actual_current = -1 * actual_current
                        self.print_console(f"METER CURRENT {actual_current}")
                        DUT_BATT_CURRENT = float(self.MCM_READ_COMMAND("DC READ CURRENT", f'batt{count_temp}'))
                        self.print_console(f'DUT BATTERY CURRENT: {DUT_BATT_CURRENT}')
                        if abs(actual_current - DUT_BATT_CURRENT) < LOAD_CURRENT_OFFSET:
                            self.print_console(f"BATTERY {count} CURRENT SENSOR/CABLE IS OK")
                            RESULT.append(True)
                        else:
                            self.print_console(f"BATTERY {count} CURRENT SENSOR/CABLE IS FAULTY", 'RED')
                            RESULT.append(False)

                    else:
                        actual_voltage = float(READ_DC_VOLTAGE("LOAD"))
                        self.print_console(f'METER VOLTAGE: {actual_voltage}')
                        dut_batt_volt = float(self.MCM_READ_COMMAND("DC READ VOLTAGE", f'batt{count_temp}'))
                        self.print_console(f"DUT BATT VOLTAGE: {dut_batt_volt}")
                        if abs(actual_voltage - dut_batt_volt) < 10:
                            self.print_console("LOAD LVD CONTACTOR IS FAULTY", 'RED')
                        else:
                            self.print_console(f"BATTERY {count_temp} LVD CONTACTOR IS FAULT", 'RED')
                        RESULT.append(False)
                elif count != count_temp and batt_lvd_count > 1:
                    DUT_BATT_CURRENT = float(self.MCM_READ_COMMAND("DC READ CURRENT", f'batt{count_temp}'))
                    if DUT_BATT_CURRENT < -5:
                        RESULT_TEMP = False
                    else:
                        RESULT_TEMP = True
                    RESULT.append(RESULT_TEMP)
            load_current_sum = 0
            if load_current_count < 2:
                DUT_load_current = float(self.MCM_READ_COMMAND('DC READ CURRENT', f'load{1}'))
                load_current_sum += DUT_load_current
                self.print_console(f"DUT LOAD CURRENT{DUT_load_current}")
                if load_current_sensor_state == 'ENABLE':
                    actual_current = float(READ_DC_CURRENT("LOAD"))
                    if actual_current > (LOAD_SET_CURRENT - LOAD_CURRENT_OFFSET):
                        # RESULT_TEMP = COMPARE(actual_current, load_current_sum, LOAD_CURRENT_OFFSET)
                        if abs(actual_current - load_current_sum) < LOAD_CURRENT_OFFSET:
                            self.print_console(self, "LOAD CURRENT SENSOR 1 is OK")
                            RESULT.append(True)
                        else:
                            self.print_console(self, "LOAD CURRENT SENSOR 1 is FAULTY", "RED")
                            RESULT.append(False)
                    else:
                        actual_voltage = float(READ_DC_VOLTAGE("LOAD"))
                        self.print_console(f"actual voltage: {actual_current}")
                        DUT_batt_volt = float(self.MCM_READ_COMMAND('DC READ VOLTAGE', f'batt{count_temp}'))
                        if abs(actual_voltage - DUT_batt_volt) > 5:
                            self.print_console("Load LVD contactor is faulty", "RED")
                            RESULT_TEMP = False
                        else:
                            self.print_console("Battery " + str(count_temp) + " LVD contactor is faulty", "RED")
                            RESULT_TEMP = False
                        RESULT.append(RESULT_TEMP)
                        self.print_console(str(RESULT))
                else:
                    self.print_console("Load CURRENT SENSOR NOT AVAILABLE")
                    RESULT_TEMP = True
                    RESULT.append(RESULT_TEMP)

            else:
                for i in range(1, load_current_count + 1):  ##CODE TO BE ADDED FOR INDIVIDUAL LOAD PATH CURRENT CHECK
                    SET_INDI_LOAD_PATH(i)
                    time.sleep(4)
                    DUT_load_current = float(self.MCM_READ_COMMAND('DC READ CURRENT', 'load' + str(i)))
                    actual_current = float(READ_DC_CURRENT("LOAD"))
                    self.print_console("DUT LOAD CURRENT " + str(i) + ": " + str(DUT_load_current))
                    self.print_console("actual_current" + str(actual_current))
                    self.print_console("LOAD_CURRENT_OFFSET: " + str(LOAD_CURRENT_OFFSET))
                    if load_current_sensor_state == 'ENABLE':
                        if actual_current > (LOAD_SET_CURRENT - LOAD_CURRENT_OFFSET):
                            # RESULT_TEMP = COMPARE(actual_current, DUT_load_current, LOAD_CURRENT_OFFSET)
                            if abs(actual_current - DUT_load_current) > LOAD_CURRENT_OFFSET:
                                self.print_console("LOAD CURRENT SENSOR " + str(i) + " is FAULTY", "RED")
                                RESULT.append(False)
                            else:
                                RESULT.append(True)
                                self.print_console("LOAD CURRENT SENSOR " + str(i) + " is OK")


                        else:
                            # PRINT_CONSOLE(self,"CHECKING ELSE CONDITION")
                            actual_voltage = float(READ_DC_VOLTAGE("LOAD"))
                            self.print_console("actual voltage: " + str(actual_voltage))
                            DUT_batt_volt = float(self.MCM_READ_COMMAND('DC READ VOLTAGE', 'batt' + str(count_temp)))
                            if abs(actual_voltage - DUT_batt_volt) < 5:
                                self.print_console("Load " + str(i) + " LVD contactor is faulty", "RED")
                                RESULT_TEMP = False
                            else:
                                self.print_console("Battery " + str(count_temp) + " LVD contactor is faulty", "RED")
                                RESULT_TEMP = False
                            RESULT.append(RESULT_TEMP)
                            self.print_console(str(RESULT))
                    # load_current_sum+=DUT_load_current

                    else:
                        self.print_console("Load CURRENT SENSOR NOT AVAILABLE")
                        RESULT_TEMP = True
                        RESULT.append(RESULT_TEMP)

                    self.print_console(f"load_current_sum: {load_current_sum}")
                    self.print_console(f"Load CURRENT {i} : {DUT_load_current}")
            actual_current = float(READ_DC_CURRENT("LOAD"))
            self.print_console(f"METER CURRENT {actual_current}")

        if load_lvd_count > 1:
            self.prompt.Message(prompt="SWITCH ON SYSTEM PRIORITY LOAD MCBs FOR ALL OPERATORS")
        ## this is for critical load
        if load_lvd_count != 0 and load_current_sensor_state == 'ENABLE':
            self.pfc.pfc_set(0, 'p_load', 1)
            load_current_sum = 0
            SET_LOAD_ISOLATE(self, load_current_count, 1)
            for i in range(1, load_current_count + 1):
                self.pfc.pfc_set(0, 'n_p_load_' + str(i), 0)
            time.sleep(3)
            for i in range(1, load_current_count + 1):
                DUT_load_current = float(self.MCM_READ_COMMAND('DC READ CURRENT', 'load' + str(i)))
                load_current_sum += DUT_load_current
            actual_current = float(READ_DC_CURRENT("LOAD"))

            self.print_console("load_current_sum: " + str(load_current_sum))
            self.print_console("actual_current" + str(actual_current))
            self.print_console("LOAD_CURRENT_OFFSET: " + str(LOAD_CURRENT_OFFSET))
            if actual_current > (LOAD_SET_CURRENT - LOAD_CURRENT_OFFSET):
                if abs(actual_current - load_current_sum) > LOAD_CURRENT_OFFSET:
                    self.print_console("PL LOAD NOT OK", "RED")
                    RESULT.append(False)
                else:
                    self.print_console("PL LOAD OK")
                    RESULT.append(True)
                    # raw_input("check")


            else:
                actual_voltage = float(READ_DC_VOLTAGE("LOAD"))
                self.print_console("actual voltage: " + str(actual_voltage))
                DUT_batt_volt = float(self.MCM_READ_COMMAND('DC READ VOLTAGE', 'batt' + str(count_temp)))
                if abs(actual_voltage - DUT_batt_volt) < 5:
                    self.print_console("Load LVD contactor is faulty", "RED")
                    RESULT_TEMP = False
                else:
                    self.print_console("Battery " + str(count_temp) + " LVD contactor is faulty", "RED")
                    RESULT_TEMP = False
                RESULT.append(RESULT_TEMP)
                self.print_console(str(RESULT))
        SET_LOAD_ISOLATE(self, load_current_count, 0)
        for i in range(1, load_current_count + 1):
            self.pfc.pfc_set(0, 'n_p_load_' + str(i), 1)

        self.print_console("DC_CURRENT_MEASUREMENT_BATT_DISCHARGE TEST FINISHED...")

        user_state = self.prompt.User_prompt(
            "DO YOU WANT TO TEST LOAD FUSE FAIL/DC MCCB TRIP ALARM.PRESS ENTER TO PROCEED!")
        if user_state:
            print("Testing Load MCB TRIP alarm")
            self.print_console("LOAD FUSE FAIL/DC MCB TRIP ALARM TEST STARTED...")
            ip_pfc_state = True
            while ip_pfc_state:
                if int(self.MCM_READ_COMMAND('DCIF 8 IP PFC', 'pfc')) != 0:
                    self.prompt.Message(prompt="CLEAR IP PFC ALARM BEFORE STARTING TEST")
                else:
                    ip_pfc_state = False
                    self.prompt.Message(prompt="SWITCH OFF ALL LOAD PL/NPL MCB(s).PRESS ENTER KEY TO PROCEED!")
                    self.print_console("WAITING FOR 5 SECONDS! ")
                    time.sleep(5)
                    if int(self.MCM_READ_COMMAND('ALARM', 'dccb trip')) == 1:
                        RESULT_TEMP_MCB_TRIP = True
                        self.print_console("DCCB TRIP ALARM TESTED OK ")
                    else:
                        RESULT_TEMP_MCB_TRIP = False
                        self.print_console("DCCB TRIP ALARM TEST FAIL ", "RED")

            self.prompt.Message(prompt="SWITCH 'ON' ALL LOAD PL/NPL MCB(s).PRESS ENTER KEY TO PROCEED!")
            self.print_console("LOAD FUSE FAIL/DC MCB TRIP ALARM TEST FINISHED...")

        else:
            print("Load MCB TRIP alarm not tested")
            RESULT_TEMP_MCB_TRIP = True
            self.print_console("DCCB TRIP TEST BYPASSED")

        RESULT.append(RESULT_TEMP_MCB_TRIP)
        self.pfc.pfc_set(0, 'p_load', 0)
        # SET_JIG_PFC_OP(self.can, 'PL LOAD', 0)

        # id = self.sql.SQL_SELECT_3_QUERY('td_id', 'test_detail_results', 'td_test_item',
        #                                  'DC_CURRENT_MEASUREMENT_BATT_DISCHARGE', 'td_readby', 'DCCB TRIP', 'td_mt_id',
        #                                  self.test_id)
        # print
        # id
        # if id != 0:
        #     print
        #     "update row"
        #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_UPDATE_QUERY(RESULT_TEMP_MCB_TRIP, id)
        # else:
        #     print
        #     "insert row"
        #     test_sub_id += 1
        #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_RESULTS_INSERT_QUERY(self.test_id,
        #                                                            "'DC_CURRENT_MEASUREMENT_BATT_DISCHARGE'",
        #                                                            "'DCCB TRIP'", test_sub_id, "''", "''",
        #                                                            RESULT_TEMP_MCB_TRIP)

        return CALCULATE_RESULT(RESULT)

    def SMR_REGISTRATION(self):

        if self.mcm_type == 1:
            self.MCM_WRITE_COMMAND("SYSTEM COMMANDS", 'ate test', "TEST_M1000_ATE")

        self.dcload.DC_LOAD_SET_CURRENT_CC(10, "LOAD")

        test_sub_id = 0
        RESULT = []

        self.print_console("SMR REGISTRATION TEST STARTED...")

        if self.custom_check.isChecked():
            if DefaultRead('DEFAULT SETTING STATE')['comm smr count'] == "YES":
                smr_count = int(DefaultRead("DEFAULT SETTING")['comm smr count'])
                self.MCM_WRITE_COMMAND("SYSTEM CONFIG", 'smr count', smr_count)
            else:
                smr_count = int(DefaultRead("DUT CONFIGURATION")['smr count'])
        else:
            smr_count = int(DefaultRead("DUT CONFIGURATION")['smr count'])

        self.prompt.Message(prompt="SWITCH OFF ALL SMR MCB. PRESS ENTER KEY TO PROCEED!")
        self.MCM_WRITE_COMMAND("SMR COMMANDS", 'deregister all smr', 1)

        ac_phase_type = ConfigRead('DUT CONFIGURATION')['ac phases type']
        hvlv_card_type = ConfigRead('DUT CONFIGURATION')['ac ip voltage source']

        if ac_phase_type == 'SINGLE PHASE':
            self.pfc.pfc_set(0, 'r_phase', 1)
        elif ac_phase_type == 'THREE PHASE':
            self.pfc.pfc_set(0, 'r_phase', 1)
            self.pfc.pfc_set(0, 'y_phase', 1)
            self.pfc.pfc_set(0, 'b_phase', 1)

        self.smrcan.SMR_BATTERY_SET_VOLTAGE(50.5)
        self.dcload.DC_LOAD_SET_CURRENT_CC(10, "LOAD")

        # if ac_phase_type == 'SINGLE PHASE':
        #     self.pfc.pfc_set(0, 1546, [PFC_control_done.PFC2], 1)
        # elif ac_phase_type == 'THREE PHASE':
        #     self.pfc.pfc_set(0, 1546, [PFC_control_done.PFC2, PFC_control_done.PFC4, PFC_control_done.PFC6], 1)

        if hvlv_card_type == "HVLV PP":
            time.sleep(20)
        else:
            time.sleep(5)

        self.prompt.TimerPrompt(
            f"TESTING FOR {smr_count} SMR(S). SWITCH ON SMR ONE BY ONE TO REGISTER. AFTER REGISTRATION, PRESS ENTER KEY!",
            300)

        for count in range(1, smr_count + 1):
            if self.MCM_READ_COMMAND('SMR COMMANDS', f'smr{count} id') != "":
                self.print_console(f"SMR {count} REGISTERED")
                RESULT_TEMP = True
            else:
                self.print_console(f"SMR {count} NOT REGISTERED", "RED")
                RESULT_TEMP = False
            RESULT.append(RESULT_TEMP)

        max_smr_count = int(DefaultRead('DEFAULT SETTING')["max smr count"])
        remain_smr_count = smr_count - max_smr_count

        if remain_smr_count > 0:
            self.prompt.Message(prompt=f"Turn OFF Last {remain_smr_count} SMR(s).PRESS ENTER TO PROCEED!")

        self.MCM_WRITE_COMMAND('SYSTEM CONFIG', 'smr count', max_smr_count)
        self.print_console("SMR REGISTRATION TEST FINISHED...")

        user_response = self.prompt.User_prompt("DO YOU WANT TO TEST BATTERY SENSING WIRING? PRESS OK TO CONTINUE..")

        if user_response:
            self.print_console("BATTERY SENSE TEST STARTED...")
            self.prompt.Message("SWITCH 'OFF' BATTERY MCB/REMOVE BATTERY FUSE. PRESS ENTER TO PROCEED!")
            time.sleep(16)
            common_battery_fuse_alarm = int(self.MCM_READ_COMMAND('ALARM', 'batt fuse fail'))
            batt1_fuse_alarm = int(self.MCM_READ_COMMAND('ALARM', 'batt1 fuse fail'))
            batt2_fuse_alarm = int(self.MCM_READ_COMMAND('ALARM', 'batt2 fuse fail'))
            batt3_fuse_alarm = int(self.MCM_READ_COMMAND('ALARM', 'batt3 fuse fail'))

            if common_battery_fuse_alarm == 1 and (
                    batt1_fuse_alarm == 1 or batt2_fuse_alarm == 1 or batt3_fuse_alarm == 1):
                RESULT_TEMP_BFF = True
                self.print_console("BATTERY FUSE SENSE OK")
            else:
                RESULT_TEMP_BFF = False
                self.prompt.Message(title="ERROR", prompt="BATTERY FUSE SENSE FAIL")
                self.print_console("BATTERY FUSE SENSE FAIL", 'RED')
            self.print_console("BATTERY SENSE TEST FINISHED...")
            self.prompt.Message(prompt="SWITCH ON BATTERY MCB/ REMOVE BATTERY FUSE. PRESS ENTER TO PROCEED!")
        else:
            self.print_console("BATTERY SENSE TEST BYPASSED...")
            RESULT_TEMP_BFF = True

        RESULT.append(RESULT_TEMP_BFF)

        return CALCULATE_RESULT(RESULT)

    def DC_CURRENT_MEASUREMENT_BATT_CHARGE(self):
        if self.mcm_type == 1:
            self.MCM_WRITE_COMMAND('SYSTEM COMMANDS', 'ate test', "TEST_M1000_ATE")
        test_sub_id = 0
        self.print_console("DC_CURRENT_MEASUREMENT_BATT_CHARGE TEST STARTED...")
        batt_fuse_count = int(ConfigRead('DUT CONFIGURATION')['no. of battery fuses'])
        batt_lvd_count = int(ConfigRead('DUT CONFIGURATION')['no. of battery lvd'])
        load_lvd_count = int(ConfigRead('DUT CONFIGURATION')['no. of load lvd'])
        load_current_count = int(ConfigRead('DUT CONFIGURATION')['no. of load current'])
        load_current_sensor_state = ConfigRead('DUT CONFIGURATION')['load current sensor']
        DC_CURRENT_FACTOR_PERCENTAGE = float(CalibrateSetting('GENERAL FACTORS')['dc current check factor percentage'])
        DC_CURRENT_TOLERANCE_PERCENTAGE = float(
            CalibrateSetting('GENERAL FACTORS')['dc current check tolerance percentage'])
        DCIF_CARD_TYPE = ConfigRead('DUT CONFIGURATION')['dcif card type']
        ac_phase_type = ConfigRead('DUT CONFIGURATION')['ac phases type']

        # if (not (self.manual_checkbox.isChecked())):
        #     ac_source_set_frequency(self, 50)
        #     self.acsource.AC_SOURCE_SET_COMMAND(output_ON)

        if DCIF_CARD_TYPE == 'HALL EFFECT':
            CURRENT_SENSOR_VALUE = int(ConfigRead('DUT CONFIGURATION')['channel1 hall effect value'])
        else:
            CURRENT_SENSOR_VALUE = int(ConfigRead('DUT CONFIGURATION')['channel1 shunt value'])

        LOAD_SET_CURRENT = int(CURRENT_SENSOR_VALUE * (float(DC_CURRENT_FACTOR_PERCENTAGE) / 100))
        LOAD_CURRENT_OFFSET = int(CURRENT_SENSOR_VALUE * (float(DC_CURRENT_TOLERANCE_PERCENTAGE) / 100))
        self.smrcan.SMR_BATTERY_SET_VOLTAGE(47.5)
        # SMR_BATTERY_SET_VOLTAGE(self.can, 47.5)
        # raw_input("ALL BATTERY FUSES SHOULD BE INSERTED/SWITCH ON LOAD/BATTERY MCB. Press any key to continue")
        RESULT = []
        self.pfc.pfc_set('battery_mains', 1)
        SET_INDI_BATTERY_PATH(1)
        self.pfc.pfc_set('load_mains', 1)
        self.pfc.pfc_set('n_p_load_1', 1)

        if ac_phase_type == 'SINGLE PHASE':
            self.pfc.pfc_set(0, 'r_phase', 1)
        elif ac_phase_type == 'THREE PHASE':
            self.pfc.pfc_set(0, 'r_phase', 1)
            self.pfc.pfc_set(0, 'y_phase', 1)
            self.pfc.pfc_set(0, 'b_phase', 1)

        if load_lvd_count != 0:
            self.pfc.pfc_set(0, 'p_Load', 1)
        else:
            self.pfc.pfc_set(0, 'p_load', 0)
        # SET_JIG_PFC_OP(self.can,'AC',0)

        if ATE_LOAD_COUNT != 1:
            DC_LOAD_SET_CURRENT_CC(self.dcload, LOAD_SET_CURRENT, LOAD)  # SET LOAD CURRENT
        else:  # ADDED FOR SINGLE LOAD CONFIGURATION, PARAS MITTAL
            # SET_JIG_PFC_OP(self.can, 'LOAD COMMON', 0)
            SET_JIG_PFC_OP(self.can, 'load_mains', 1)

        self.dcload.DC_LOAD_SET_CURRENT_CC(LOAD_SET_CURRENT, "BATT")  # SET BATTERY CHARGE CURRENT
        time.sleep(5)

        for count in range(1, batt_lvd_count + 1):
            self.print_console("CHECKING BATTERY " + str(count) + " CHARGE CURRENT ")
            SET_INDI_BATTERY_PATH(count)
            time.sleep(5)
            for count_temp in range(1, batt_lvd_count + 1):
                # PRINT_CONSOLE(self, "count temp: "+str(count_temp))
                if count == count_temp or batt_lvd_count < 2:
                    actual_current = float(
                        READ_DC_CURRENT("BATT"))  # READ BATTERY CHARGE CURRENT IN BATTERY PATH LOAD.
                    if actual_current > (LOAD_SET_CURRENT - LOAD_CURRENT_OFFSET):
                        self.print_console("METER CURRENT: " + str(actual_current))

                        DUT_batt_current = float(self.MCM_READ_COMMAND('DC READ CURRENT', 'batt' + str(count_temp)))
                        self.print_console("BATTERY " + str(count) + " CURRENT: " + str(DUT_batt_current))
                        if abs(actual_current - DUT_batt_current) > LOAD_CURRENT_OFFSET:
                            self.print_console("BATTERY " + str(count) + " CURRENT SENSOR/CABLE is FAULTY", "RED")
                            RESULT_TEMP = False
                        else:
                            self.print_console("BATTERY " + str(count) + " CURRENT SENSOR/CABLE is OK")
                            RESULT_TEMP = True
                        # raw_input("check")

                        RESULT.append(RESULT_TEMP)

                    else:
                        actual_voltage = float(READ_DC_VOLTAGE("LOAD"))
                        self.print_console("METER VOLTAGE: " + str(actual_voltage))
                        DUT_batt_volt = float(self.MCM_READ_COMMAND('DC READ VOLTAGE', 'batt' + str(count_temp)))
                        if abs(actual_voltage - DUT_batt_volt) < 10:
                            self.print_console("Load LVD contactor is faulty", "RED")
                        else:
                            self.print_console("Battery " + str(count_temp) + " LVD contactor is faulty", "RED")
                        RESULT_TEMP = False
                        RESULT.append(RESULT_TEMP)
                        self.print_console(str(RESULT))
                elif count != count_temp and batt_lvd_count > 1:
                    DUT_batt_current = float(self.MCM_READ_COMMAND('DC READ CURRENT', 'batt' + str(count_temp)))
                    # PRINT_CONSOLE(self,"not known")
                    if DUT_batt_current > 5:
                        RESULT_TEMP = False
                    else:
                        RESULT_TEMP = True
                    RESULT.append(RESULT_TEMP)
                    self.print_console(str(RESULT))
                # count_temp+=1

        #         load_current_sum=0
        #         if load_current_count<2:
        #             actual_current=float(READ_DC_CURRENT(self,LOAD))
        #             DUT_load_current=float(TELNET_GET_COMMAND(self.telnet,OIDRead('DC READ CURRENT')['load'+str(1)]))
        #             load_current_sum+=DUT_load_current
        #             PRINT_CONSOLE(self,"Load CURRENT"+str(DUT_load_current))
        #
        #         else:
        #             for i in range(1,load_current_count):
        #                 DUT_load_current=float(TELNET_GET_COMMAND(self.telnet,OIDRead('DC READ CURRENT')['load'+str(i)]))
        #                 load_current_sum+=DUT_load_current
        #                 PRINT_CONSOLE(self,"Load CURRENT"+str(DUT_load_current))
        #         actual_current=float(READ_DC_CURRENT(self,LOAD))
        #         PRINT_CONSOLE(self,"METER CURRENT: "+str(actual_current))
        #         if load_current_sensor_state=='ENABLE':
        #             if actual_current>(LOAD_SET_CURRENT-LOAD_CURRENT_OFFSET):
        #                 RESULT_TEMP=COMPARE(actual_current,load_current_sum,LOAD_CURRENT_OFFSET)
        #                 if RESULT_TEMP==False:
        #                     PRINT_CONSOLE(self,"LOAD CURRENT SENSOR "+str(count)+" is FAULTY")
        #                 else:
        #                     PRINT_CONSOLE(self,"LOAD CURRENT SENSOR "+str(count)+" is OK")
        #                     #raw_input("check")
        #                     RESULT.append(RESULT_TEMP)
        #
        #             else:
        #                 actual_voltage=float(READ_DC_VOLTAGE(self,LOAD))
        #                 PRINT_CONSOLE(self,"actual voltage: "+str(actual_voltage))
        #                 DUT_batt_volt=float(TELNET_GET_COMMAND(self.telnet,OIDRead('DC READ VOLTAGE')['batt'+str(count_temp)]))
        #                 if COMPARE(actual_voltage,DUT_batt_volt,5)==True:
        #                     PRINT_CONSOLE(self,"Load LVD contactor is faulty")
        #                     RESUL_TEMP=False
        #                 else:
        #                     PRINT_CONSOLE(self,"Battery "+str(count_temp)+" LVD contactor is faulty")
        #                     RESULT_TEMP=False
        #                 RESULT.append(RESULT_TEMP)
        #                 #PRINT_CONSOLE(self,str(RESULT))
        #         else:
        #             PRINT_CONSOLE(self,"Load CURRENT SENSOR NOT AVAILABLE")
        #             RESULT_TEMP=True
        #             RESULT.append(RESULT_TEMP)

        if ATE_LOAD_COUNT != 1:
            None
            # DC_LOAD_SET_CURRENT_CC(self.dcload,LOAD_SET_CURRENT,LOAD) # SET LOAD CURRENT
        else:  # ADDED FOR SINGLE LOAD CONFIGURATION, KUSHAGRA MITTAL 06/09/2016
            self.pfc.pfc_set(0, 'bus', 0)
            self.pfc.pfc_set(0, 'load_mains', 1)
            # SET_JIG_PFC_OP(self.can,'DC LOAD',1)

        # id = self.sql.SQL_SELECT_3_QUERY('td_id', 'test_detail_results', 'td_test_item',
        #                                  'DC_CURRENT_MEASUREMENT_BATT_CHARGE', 'td_readby', 'CURRENT', 'td_mt_id',
        #                                  self.test_id)
        # print
        # id
        # if id != 0:
        #     print
        #     "update row"
        #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_UPDATE_QUERY(CALCULATE_RESULT(RESULT), id)
        # else:
        #     print
        #     "insert row"
        #     test_sub_id += 1
        #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_RESULTS_INSERT_QUERY(self.test_id, "'DC_CURRENT_MEASUREMENT_BATT_CHARGE'",
        #                                                            "'CURRENT'", test_sub_id, "''", "''",
        #                                                            CALCULATE_RESULT(RESULT))

        self.print_console("DC_CURRENT_MEASUREMENT_BATT_CHARGE TEST FINISHED...")
        return CALCULATE_RESULT(RESULT)

    def CALIBRATE_DC_CURRENT(self):
        global RESULT_TEMP
        if self.mcm_type == 1:
            self.MCM_WRITE_COMMAND('SYSTEM COMMANDS', 'ate test', "TEST_M1000_ATE")
        test_sub_id = 0
        self.pfc.pfc_set(0, 'BATT LOAD', 1)
        self.print_console("CALIBRATE_DC_CURRENT TEST STARTED...")
        batt_fuse_count = int(ConfigRead('DUT CONFIGURATION')['no. of battery fuses'])
        batt_lvd_count = int(ConfigRead('DUT CONFIGURATION')['no. of battery lvd'])
        load_lvd_count = int(ConfigRead('DUT CONFIGURATION')['no. of load lvd'])
        load_current_count = int(ConfigRead('DUT CONFIGURATION')['no. of load current'])
        load_current_sensor_state = ConfigRead('DUT CONFIGURATION')['load current sensor']
        battery_capacity = int(ConfigRead('DUT CONFIGURATION')['battery capacity'])
        battery_type = ConfigRead('DUT CONFIGURATION')['battery type']
        DCIF_CARD_TYPE = ConfigRead('DUT CONFIGURATION')['dcif card type']
        ac_phase_type = ConfigRead('DUT CONFIGURATION')['ac phases type']
        # if ac_phase_type == 'SINGLE PHASE':
        #     AC_SOURCE_SET_VOLTAGE(self, 230, ac_phase_type)
        # elif ac_phase_type == 'THREE PHASE':
        #     AC_SOURCE_SET_VOLTAGE(self, 230, ac_phase_type)
        # if (not (self.checkBox_manual.isChecked())):
        #     ac_source_set_frequency(self, 50)
        #     self.acsource.AC_SOURCE_SET_COMMAND(output_ON)
        if battery_type == 'VRLA':
            battery_capacity = int(ConfigRead('DUT CONFIGURATION')['battery capacity'])
            self.MCM_WRITE_COMMAND('SYSTEM CONFIG', 'vrla battery capacity', 5000)
        elif battery_type == 'LION':
            module_count = ConfigRead('DUT CONFIGURATION')['lion module count']
            self.MCM_WRITE_COMMAND('SYSTEM CONFIG', 'lion module count', 10)
        self.smrcan.SMR_BATTERY_SET_VOLTAGE(48.0)
        self.MCM_WRITE_COMMAND('SYSTEM CONFIG', 'eco mode', 0)
        if DCIF_CARD_TYPE == 'HALL EFFECT':
            for channel_number in range(1, load_current_count + batt_lvd_count + 1):
                if (self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' gain') != '0') \
                        or (self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(
                    channel_number) + ' offset') != '0'):  # or (TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' deadband'])!='0'):
                    self.print_console("Resetting offset and gain again")
                    # TELNET_SET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' deadband'],0)
                    # time.sleep(1)
                    self.MCM_WRITE_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' gain', 0)
                    time.sleep(1)
                    self.MCM_WRITE_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' offset', 0)
                    time.sleep(1)
                    self.print_console("CURRENT CHANNEL " + str(channel_number) + " GAIN: " + str(
                        self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' gain')))
                    self.print_console("CURRENT CHANNEL " + str(channel_number) + " OFFSET: " + str(
                        self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' offset')))
                    # PRINT_CONSOLE(self,"CURRENT CHANNEL "+str(channel_number)+" DEADBAND: "+str(TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' deadband'])))

        # raw_input("ALL BATTERY FUSES SHOULD BE INSERTED/SWITCH ON LOAD/BATTERY MCB. Press any key to continue")
        RESULT = []
        RESULT_1 = []
        RESULT_2 = []
        self.pfc.pfc_set(0, 'batt_mains', 1)
        for batt in range(1, batt_fuse_count + 1):
            self.pfc.pfc_set(0, 'battery_' + str(batt), 1)
        self.pfc.pfc_set(0, 'LOAD COMMON', 1)
        for load in range(1, load_current_count + 1):
            self.pfc.pfc_set(0, 'n_p_load_' + str(load), 1)
        SET_INDI_BATTERY_PATH(1)
        if ac_phase_type == 'SINGLE PHASE':
            self.pfc.pfc_set(0, 'r_phase', 1)
        elif ac_phase_type == 'THREE PHASE':
            self.pfc.pfc_set(0, 'r_phase', 1)
            self.pfc.pfc_set(0, 'y_phase', 1)
            self.pfc.pfc_set(0, 'b_phase', 1)
        if load_lvd_count == 1:
            self.pfc.pfc_set(0, 'p_load', 1)
        else:
            self.pfc.pfc_set(0, 'p_load', 0)
        # SET_JIG_PFC_OP(self.can,'AC',0)
        self.dcload.DC_LOAD_SET_CURRENT_CC(10, "LOAD")
        if ATE_LOAD_COUNT != 1:  # SINGLE LOAD IS CONFIGURED, 19/08/2016
            self.dcload.DC_LOAD_SET_CURRENT_CC(10, "BATT")
        time.sleep(2)

        ### ADDING LOGIC FOR SINGLE LOAD CONFIGURATION

        for count in range(load_current_count + 1, load_current_count + batt_lvd_count + 1):

            #         if ATE_LOAD_COUNT==1:
            #             SET_JIG_PFC_OP(self.can,'LOAD COMMON',0)
            #             SET_JIG_PFC_OP(self.can,'DC LOAD',1)

            self.print_console("count: " + str(count))
            SET_INDI_BATTERY_PATH(count - load_current_count)
            time.sleep(2)
            self.print_console("Start battery calibration")
            if DCIF_CARD_TYPE == 'HALL EFFECT':
                RESULT_TEMP = CALIBRATE_CURRENT_PATH_HALL_EFFECT(self, count, 'BATT')
            elif DCIF_CARD_TYPE == 'SHUNT':
                RESULT_TEMP = CALIBRATE_CURRENT_PATH_SHUNT(self, count, 'BATT')
            elif DCIF_CARD_TYPE == 'SHUNT SMALL':
                if load_current_sensor_state == 'DISABLE' and M1000Telnet.telnet_get_command('TAB.1818.1') == '1':
                    count = count - 1
                self.print_console("count: " + str(count))
                RESULT_TEMP = CALIBRATE_CURRENT_PATH_SHUNT_SMALL(self, count, 'BATT')

            RESULT_1.append(RESULT_TEMP)

        RESULT.append(CALCULATE_RESULT(RESULT_1))

        # id = self.sql.SQL_SELECT_3_QUERY('td_id', 'test_detail_results', 'td_test_item', 'CALIBRATE_DC_CURRENT',
        #                                  'td_readby', 'BATTERY', 'td_mt_id', self.test_id)
        # print
        # id
        # if id != 0:
        #     print
        #     "update row"
        #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_UPDATE_QUERY(CALCULATE_RESULT(RESULT_1), id)
        # else:
        #     print
        #     "insert row"
        #     test_sub_id += 1
        #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_RESULTS_INSERT_QUERY(self.test_id, "'CALIBRATE_DC_CURRENT'", "'BATTERY'",
        #                                                            test_sub_id, "''", "''", CALCULATE_RESULT(RESULT_1))

        ### ADDING LOGIC FOR SINGLE LOAD CONFIGURATION
        if ATE_LOAD_COUNT == 1:
            self.print_console(0, "RESETTING FOR LOAD PATH")
            self.pfc.pfc_set(0, 'DC LOAD', 0)
            self.pfc.pfc_set(0, 'LOAD COMMON', 1)

        if load_current_sensor_state == 'DISABLE':
            self.print_console("CALIBRATION NOT REQUIRED")
        else:

            # if load_lvd_count > 1:
            #     MESSAGE_PROMPT(self, "SWITCH OFF SYSTEM PRIORITY LOAD MCBs FOR ALL OPERATORS")

            for i in range(1, load_current_count + 1):
                SET_INDI_LOAD_PATH(self, i)
                time.sleep(2)
                if DCIF_CARD_TYPE == 'HALL EFFECT':
                    RESULT_TEMP = CALIBRATE_CURRENT_PATH_HALL_EFFECT(self, i, 'LOAD')
                elif DCIF_CARD_TYPE == 'SHUNT':
                    RESULT_TEMP = CALIBRATE_CURRENT_PATH_SHUNT(self, i, 'LOAD')
                elif DCIF_CARD_TYPE == 'SHUNT SMALL':
                    RESULT_TEMP = CALIBRATE_CURRENT_PATH_SHUNT_SMALL(self, i, 'LOAD')
                RESULT_2.append(RESULT_TEMP)
        RESULT.append(CALCULATE_RESULT(RESULT_2))

        # if load_lvd_count > 1:
        #     self.prompt.Message("SWITCH ON SYSTEM PRIORITY LOAD MCBs FOR ALL OPERATORS")

        # id = self.sql.SQL_SELECT_3_QUERY('td_id', 'test_detail_results', 'td_test_item', 'CALIBRATE_DC_CURRENT',
        #                                  'td_readby', 'LOAD', 'td_mt_id', self.test_id)
        # print
        # id
        # if id != 0:
        #     print
        #     "update row"
        #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_UPDATE_QUERY(CALCULATE_RESULT(RESULT_2), id)
        # else:
        #     print
        #     "insert row"
        #     test_sub_id += 1
        #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_RESULTS_INSERT_QUERY(self.test_id, "'CALIBRATE_DC_CURRENT'", "'LOAD'",
        #                                                            test_sub_id, "''", "''", CALCULATE_RESULT(RESULT_2))

        self.print_console("CALIBRATE_DC_CURRENT TEST FINISHED...")
        if load_lvd_count == 1:
            self.pfc.pfc_set(0, 'p_load', 1)
        else:
            self.pfc.pfc_set(0, 'p_load', 0)
        #     if load_lvd_count!=0:
        #         SET_JIG_PFC_OP(self.can,'PL LOAD',0)
        return CALCULATE_RESULT(RESULT)

    def LVD_CONTACTOR_CHECK(self):
        if self.mcm_type == 1:
            TELNET_SET_COMMAND(self.telnet, OIDRead('SYSTEM COMMANDS')['ate test'], "TEST_M1000_ATE")
        test_sub_id = 0
        RESULT_1 = []
        RESULT_2 = []
        self.print_console("LVD_CONTACTOR_CHECK TEST STARTED...")
        batt_fuse_count = int(ConfigRead('DUT CONFIGURATION')['no. of battery fuses'])
        batt_lvd_count = int(ConfigRead('DUT CONFIGURATION')['no. of battery lvd'])
        load_lvd_count = int(ConfigRead('DUT CONFIGURATION')['no. of load lvd'])
        load_current_count = int(ConfigRead('DUT CONFIGURATION')['no. of load current'])
        self.smrcan.SMR_BATTERY_SET_VOLTAGE(53.5)
        # raw_input("ALL BATTERY FUSES SHOULD BE INSERTED/SWITCH ON LOAD/BATTERY MCB. Press any key to continue")
        RESULT = []
        self.dcload.DC_LOAD_SET_CURRENT_CC(5, "BATT")
        self.pfc.pfc_set(0, 'battery_mains', 1)
        SET_INDI_BATTERY_PATH(1)
        self.pfc.pfc_set(0, 'load_mains', 1)
        self.pfc.pfc_set(0, 'n_p_load_1', 1)
        self.pfc.pfc_set(0, 'n_p_load_2', 1)
        self.pfc.pfc_set(0, 'n_p_load_3', 1)
        self.pfc.pfc_set(0, 'n_p_load_4', 1)
        self.pfc.pfc_set(0, 'p_load', 0)
        self.pfc.pfc_set(0, 'r_phase', 0)
        self.pfc.pfc_set(0, 'y_phase', 0)
        self.pfc.pfc_set(0, 'b_phase', 0)
        self.dcload.DC_LOAD_SET_CURRENT_CC(30, "LOAD")
        time.sleep(3)

        # SET_BATTERY_ISOLATE(self,batt_lvd_count,1)
        ## current path will be checked in discharging state
        for count_temp in range(1, batt_lvd_count + 1):
            self.print_console("count temp: " + str(count_temp))
            self.smrcan.SMR_BATTERY_SET_VOLTAGE(45.0)
            SET_INDI_BATTERY_PATH(count_temp)
            time.sleep(2)
            actual_current = float(READ_DC_CURRENT("LOAD"))
            DUT_batt_current = float(self.MCM_READ_COMMAND('DC READ CURRENT', 'batt' + str(count_temp)))
            actual_current = -1 * actual_current
            if actual_current < -20 and abs(
                    actual_current - DUT_batt_current) < 7.0:  # check if current is flowing through load and battery
                SET_INDI_BATTERY_ISOLATE(count_temp, 1)  # if yes, check for battery lvd contactor
                time.sleep(5)
                DUT_batt_current = float(self.MCM_READ_COMMAND('DC READ CURRENT', 'batt' + str(count_temp)))
                if -20 < DUT_batt_current < 20:
                    RESULT_TEMP = True
                    self.print_console("Battery " + str(count_temp) + " LVD contactor is OK")
                else:
                    RESULT_TEMP = False
                    self.print_console("Battery " + str(count_temp) + " LVD contactor is faulty", "RED")
            else:
                actual_voltage = float(READ_DC_VOLTAGE(
                    "LOAD"))  # if current is not flowing, then we check for current sensor and Load/battery contactor faulty.
                self.print_console("actual voltage: " + str(actual_voltage))  # to be changed after understanding
                DUT_batt_volt = float(self.MCM_READ_COMMAND('DC READ VOLTAGE', 'batt' + str(count_temp)))

                if abs(actual_voltage - DUT_batt_volt) < 5:
                    DUT_bus_volt = float(self.MCM_READ_COMMAND('DC READ VOLTAGE', 'bus'))
                    if abs(actual_voltage - DUT_bus_volt) < 2:
                        self.print_console("Battery " + str(count_temp) + " CURRENT SENSOR is faulty", "RED")
                    else:
                        self.print_console("Load LVD contactor is faulty", "RED")
                else:
                    self.print_console("Battery " + str(count_temp) + " LVD contactor is faulty", "RED")
                RESULT_TEMP = False
            self.smrcan.SMR_BATTERY_SET_VOLTAGE(53.5)
            SET_INDI_BATTERY_ISOLATE(count_temp, 0)
            time.sleep(5)
            RESULT_1.append(RESULT_TEMP)
        RESULT.append(CALCULATE_RESULT(RESULT_1))

        # id = self.sql.SQL_SELECT_3_QUERY('td_id', 'test_detail_results', 'td_test_item', 'LVD_CONTACTOR_CHECK',
        #                                  'td_readby', 'BATTERY', 'td_mt_id', self.test_id)
        # print
        # id
        # if id != 0:
        #     print
        #     "update row"
        #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_UPDATE_QUERY(CALCULATE_RESULT(RESULT_1), id)
        # else:
        #     print
        #     "insert row"
        #     test_sub_id += 1
        #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_RESULTS_INSERT_QUERY(self.test_id, "'LVD_CONTACTOR_CHECK'", "'BATTERY'",
        #                                                            test_sub_id, "''", "''", CALCULATE_RESULT(RESULT_1))
        #
        # # SET_INDI_BATTERY_PATH(self,1)
        # time.sleep(2)

        if load_lvd_count == load_current_count and load_lvd_count != 0:
            for count_temp in range(1, load_lvd_count + 1):
                self.print_console("count temp: " + str(count_temp))
                SMR_BATTERY_SET_VOLTAGE(45.0)
                SET_INDI_LOAD_PATH(count_temp)
                time.sleep(2)
                actual_current = float(READ_DC_CURRENT("LOAD"))
                DUT_load_current = float(self.MCM_READ_COMMAND('DC READ CURRENT', 'load' + str(count_temp)))
                if abs(actual_current - DUT_load_current) < 5.0:
                    temp_var = True
                else:
                    temp_var = False
                if actual_current > 25 and temp_var == True:
                    self.MCM_WRITE_COMMAND('SYSTEM COMMANDS', 'ate test', "TEST_M1000_ATE")
                    SET_INDI_LOAD_ISOLATE(count_temp, 1)
                    time.sleep(5)
                    DUT_load_current = float(self.MCM_READ_COMMAND('DC READ CURRENT', 'load' + str(count_temp)))
                    if -20 < DUT_load_current < 20:
                        RESULT_TEMP = True
                        self.print_console("Load " + str(count_temp) + " LVD contactor is OK")
                    else:
                        RESULT_TEMP = False
                        self.print_console("Load " + str(count_temp) + " LVD contactor is faulty", "RED")
                else:
                    actual_voltage = float(READ_DC_VOLTAGE("LOAD"))
                    self.print_console("actual voltage: " + str(actual_voltage))
                    DUT_batt_volt = float(self.MCM_READ_COMMAND('DC READ VOLTAGE', 'batt1'))
                    if abs(actual_voltage - DUT_batt_volt) < 5:
                        self.print_console("Load " + str(count_temp) + " LVD contactor is faulty", "RED")
                    else:
                        self.print_console("Battery 1 LVD contactor is faulty", WARNING)
                    RESULT_TEMP = False
                SMR_BATTERY_SET_VOLTAGE(53.5)
                SET_INDI_LOAD_ISOLATE(count_temp, 0)
                time.sleep(5)
                RESULT_2.append(RESULT_TEMP)
        elif load_lvd_count < 2 and load_current_count > 1:
            for count_temp in range(1, load_lvd_count + 1):
                self.print_console("count temp: " + str(count_temp))
                actual_current = float(READ_DC_CURRENT("BATT"))
                load_current_sum = 0
                for load_current in range(1, load_current_count + 1):
                    DUT_load_current = float(self.MCM_READ_COMMAND('DC READ CURRENT', 'load' + str(count_temp)))
                    load_current_sum += DUT_load_current
                if abs(actual_current - load_current_sum) < 2:
                    temp_var = True
                else:
                    temp_var = False
                if actual_current > 25 and temp_var == True:
                    SET_INDI_LOAD_ISOLATE(count_temp, 1)
                    time.sleep(5)
                    load_current_sum = 0
                    for load_current in range(1, load_current_count + 1):
                        DUT_load_current = float(self.MCM_READ_COMMAND('DC READ CURRENT', 'load' + str(count_temp)))
                        load_current_sum += DUT_load_current
                    if -2 < load_current_sum < 2:
                        RESULT_TEMP = True
                    else:
                        RESULT_TEMP = False
                        self.print_console("Load " + str(count_temp) + " LVD contactor is faulty", "RED")
                else:
                    actual_voltage = float(READ_DC_VOLTAGE("LOAD"))
                    self.print_console("actual voltage: " + str(actual_voltage))
                    DUT_batt_volt = float(self.MCM_READ_COMMAND('DC READ VOLTAGE', 'batt1'))
                    if abs(actual_voltage - DUT_batt_volt) < 5:
                        self.print_console("Load " + str(count_temp) + " LVD contactor is faulty", "RED")
                    else:
                        self.print_console("Battery 1 LVD contactor is faulty", "RED")
                    RESULT_TEMP = False
                    RESULT_2.append(RESULT_TEMP)
                SET_INDI_LOAD_ISOLATE(count_temp, 0)
        self.smrcan.SMR_BATTERY_SET_VOLTAGE(53.5)
        # id = self.sql.SQL_SELECT_3_QUERY('td_id', 'test_detail_results', 'td_test_item', 'LVD_CONTACTOR_CHECK',
        #                                  'td_readby', 'LOAD', 'td_mt_id', self.test_id)
        # print
        # id
        # if id != 0:
        #     print
        #     "update row"
        #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_UPDATE_QUERY(CALCULATE_RESULT(RESULT_2), id)
        # else:
        #     print
        #     "insert row"
        #     test_sub_id += 1
        #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_RESULTS_INSERT_QUERY(self.test_id, "'LVD_CONTACTOR_CHECK'", "'LOAD'",
        #                                                            test_sub_id, "''", "''", CALCULATE_RESULT(RESULT_2))

        RESULT.append(CALCULATE_RESULT(RESULT_2))
        self.print_console("LVD_CONTACTOR_CHECK TEST FINISHED...")

        for i in range(1, load_lvd_count + 1):
            self.pfc.pfc_set(0, 'LOAD' + str(i), 1)

        return CALCULATE_RESULT(RESULT)

    def PHASE_ALLOCATION(self):
        global phase
        if self.mcm_type == 1:
            TELNET_SET_COMMAND(self.telnet, OIDRead('SYSTEM COMMANDS')['ate test'], "TEST_M1000_ATE")
        test_sub_id = 0
        self.dcload.DC_LOAD_SET_CURRENT_CC(5, "BATT")
        self.print_console("PHASE_ALLOCATION TEST STARTED...")
        batt_fuse_count = int(ConfigRead('DUT CONFIGURATION')['no. of battery fuses'])
        batt_lvd_count = int(ConfigRead('DUT CONFIGURATION')['no. of battery lvd'])
        load_lvd_count = int(ConfigRead('DUT CONFIGURATION')['no. of load lvd'])
        load_current_count = int(ConfigRead('DUT CONFIGURATION')['no. of load current'])
        ac_phase_type = ConfigRead('DUT CONFIGURATION')['ac phases type']
        hvlv_card_state = ConfigRead('DUT CONFIGURATION')['hvlv card']
        hvlv_card_type = ConfigRead('DUT CONFIGURATION')['ac ip voltage source']
        self.smrcan.SMR_BATTERY_SET_VOLTAGE(50.5)
        self.dcload.DC_LOAD_SET_CURRENT_CC(10, "LOAD")
        self.dcload.DC_LOAD_SET_CURRENT_CC(15, "BATT")
        phase_voltage = 0

        self.pfc.pfc_set(0, 'bus', 1)
        for batt in range(1, batt_fuse_count + 1):
            self.pfc.pfc_set(0, 'battery_' + str(batt), 1)
        self.pfc.pfc_set(0, 'load_mains', 1)
        for load in range(1, load_current_count + 1):
            self.pfc.pfc_set(0, 'n_p_load_' + str(load), 1)
        self.pfc.pfc_set(0, 'r_phase', 1)
        self.pfc.pfc_set(0, 'y_phase', 1)
        self.pfc.pfc_set(0, 'b_phase', 1)
        RESULT = []

        # if ac_phase_type == 'SINGLE PHASE':
        #     AC_SOURCE_SET_VOLTAGE(self, 230, ac_phase_type)
        # elif ac_phase_type == 'THREE PHASE':
        #     AC_SOURCE_SET_VOLTAGE(self, 230, ac_phase_type)
        # if (not (self.checkBox_manual.isChecked())):
        #     ac_source_set_frequency(self, 50)
        #     self.acsource.AC_SOURCE_SET_COMMAND(output_ON)

        if hvlv_card_state == 'PRESENT':
            time.sleep(3)
            phase_voltage = 75
            alarm_hvlv_comm_fail = int(self.MCM_READ_COMMAND('ALARM', 'hvlv comm fail'))
            if alarm_hvlv_comm_fail == 0:
                RESULT_TEMP = True
            else:
                RESULT_TEMP = False
                self.print_console("HVLV Card not communicating with Controller", "RED")
        else:
            phase_voltage = 0
            RESULT_TEMP = True
        RESULT.append(RESULT_TEMP)

        if hvlv_card_type == 'HVLV PP':
            time.sleep(25)
            if self.custom_check.isChecked():
                # MESSAGE_PROMPT(self,"Custom settings will be programmed to controller")
                if DefaultRead('DEFAULT SETTING STATE')["comm smr count"] == 'YES':
                    smr_count = int(DefaultRead('DEFAULT SETTING')["comm smr count"])
                    self.MCM_WRITE_COMMAND('SYSTEM CONFIG', 'smr count', smr_count)
                else:
                    smr_count = int(ConfigRead('DUT CONFIGURATION')['smr count'])

            # smr_count=SMR_COUNT(self)
            else:
                smr_count = int(ConfigRead('DUT CONFIGURATION')['smr count'])

            max_smr_count = int(DefaultRead('DEFAULT SETTING')["max smr count"])
            remain_smr_count = smr_count - max_smr_count

            if remain_smr_count > 0:
                self.prompt.Message(prompt="Turn ON Last " + str(remain_smr_count) + " SMR(s).PRESS ENTER TO PROCEED!")

            config_smr_count = int(self.MCM_READ_COMMAND('SYSTEM CONFIG', 'smr count'))
            #         alarm_mains_fail=int(TELNET_GET_COMMAND(self.telnet,OIDRead('ALARM')['mains fail']))
            #         if alarm_mains_fail==1:
            #             RESULT_TEMP=True
            #         else:
            #             RESULT_TEMP=False
            #             if hvlv_card_state=='PRESENT':
            #                     PRINT_CONSOLE(self,"CHECK HVLV IP SINGLE PHASE VOLTAGE SENSE WIRING")
            #         RESULT.append(RESULT_TEMP)
            #         voltage_r_phase=int(TELNET_GET_COMMAND(self.telnet,OIDRead('MAINS READ VOLTAGE')['r phase']))
            #         if voltage_r_phase<phase_voltage+3 and voltage_r_phase>phase_voltage-3:
            #             RESULT_TEMP=True
            #         else:
            #             RESULT_TEMP=False
            #             if hvlv_card_state=='PRESENT':
            #                     PRINT_CONSOLE(self,"CHECK HVLV IP SINGLE PHASE VOLTAGE SENSE WIRING")
            #         RESULT.append(RESULT_TEMP)

            for i in range(1, config_smr_count + 1):
                smr_status = int(self.MCM_READ_COMMAND('SMR COMMANDS', 'smr' + str(i) + " status"))
                self.print_console(SMR_STATUS_TEXT(smr_status))
                if smr_status == 1:
                    RESULT_TEMP = True
                    self.print_console("SMR " + str(i) + " WIRING OK ")
                else:
                    RESULT_TEMP = False
                    if hvlv_card_state == 'PRESENT':
                        self.print_console("SMR " + str(i) + " HVLV RELAY / WIRING FAULTY ", "RED")
                    elif hvlv_card_state != 'PRESENT':
                        self.print_console("SMR " + str(i) + " WIRING FAULTY ", 'RED')
                RESULT.append(RESULT_TEMP)

            max_smr_count = int(DefaultRead('DEFAULT SETTING')["max smr count"])
            remain_smr_count = smr_count - max_smr_count

            if remain_smr_count > 0:
                self.prompt.Message(prompt="Turn OFF Last " + str(remain_smr_count) + " SMR(s).PRESS ENTER TO PROCEED!")

            self.MCM_WRITE_COMMAND('SYSTEM CONFIG', 'smr count', max_smr_count)

            # id = self.sql.SQL_SELECT_3_QUERY('td_id', 'test_detail_results', 'td_test_item', 'PHASE_ALLOCATION',
            #                                  'td_readby', 'THREE_PHASE', 'td_mt_id', self.test_id)
            # print
            # id
            # if id != 0:
            #     print
            #     "update row"
            #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_UPDATE_QUERY(CALCULATE_RESULT(RESULT), id)
            # else:
            #     print
            #     "insert row"
            #     test_sub_id += 1
            #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_RESULTS_INSERT_QUERY(self.test_id, "'PHASE_ALLOCATION'",
            #                                                            "'THREE_PHASE'", test_sub_id, "''", "''",
            #                                                            CALCULATE_RESULT(RESULT))

            self.print_console(str(RESULT))
            self.print_console("PHASE_ALLOCATION TEST FINISHED...")
            return CALCULATE_RESULT(RESULT)

        if ac_phase_type == 'SINGLE PHASE':
            self.print_console("Setting IP voltage to " + str(phase_voltage))
            # AC_SOURCE_SET_VOLTAGE(self, phase_voltage, ac_phase_type)

            time.sleep(20)

            config_smr_count = int(self.MCM_READ_COMMAND('SYSTEM CONFIG', 'smr count'))
            alarm_mains_fail = int(self.MCM_READ_COMMAND('ALARM', 'mains fail'))
            if alarm_mains_fail == 1:
                RESULT_TEMP = True
            else:
                RESULT_TEMP = False
                if hvlv_card_state == 'PRESENT':
                    self.print_console("CHECK HVLV IP SINGLE PHASE VOLTAGE SENSE WIRING", "RED")
            RESULT.append(RESULT_TEMP)
            voltage_r_phase = int(self.MCM_READ_COMMAND('MAINS READ VOLTAGE', 'r phase'))
            if phase_voltage + 3 > voltage_r_phase > phase_voltage - 3:
                RESULT_TEMP = True
            else:
                RESULT_TEMP = False
                if hvlv_card_state == 'PRESENT':
                    self.print_console("CHECK HVLV IP SINGLE PHASE VOLTAGE SENSE WIRING", "RED")
            RESULT.append(RESULT_TEMP)

            for i in range(1, config_smr_count + 1):
                smr_status = int(self.MCM_READ_COMMAND('SMR COMMANDS', 'smr' + str(i) + " status"))
                self.print_console(SMR_STATUS_TEXT(smr_status))
                if smr_status == 0:
                    RESULT_TEMP = True
                    self.print_console("SMR " + str(i) + " WIRING OK ")
                else:
                    RESULT_TEMP = False
                    if hvlv_card_state == 'PRESENT':
                        self.print_console("SMR " + str(i) + " HVLV RELAY / WIRING FAULTY ", "RED")
                    elif hvlv_card_state != 'PRESENT':
                        self.print_console("SMR " + str(i) + " WIRING FAULTY ", "RED")
                RESULT.append(RESULT_TEMP)

            # id = self.sql.SQL_SELECT_3_QUERY('td_id', 'test_detail_results', 'td_test_item', 'PHASE_ALLOCATION',
            #                                  'td_readby', 'SINGLE_PHASE', 'td_mt_id', self.test_id)
            # print
            # id
            # if id != 0:
            #     print
            #     "update row"
            #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_UPDATE_QUERY(CALCULATE_RESULT(RESULT), id)
            # else:
            #     print
            #     "insert row"
            # test_sub_id += 1
            # self.sql.SQL_TEST_ITEM_RUN_DETAIL_RESULTS_INSERT_QUERY(self.test_id, "'PHASE_ALLOCATION'", "'SINGLE_PHASE'",
            #                                                        test_sub_id, "''", "''", CALCULATE_RESULT(RESULT))
            # AC_SOURCE_SET_VOLTAGE(self, 230, ac_phase_type)

        elif ac_phase_type == 'THREE PHASE':
            for phase_no in range(1, 4):
                # AC_SOURCE_SET_VOLTAGE(self, 230, ac_phase_type)
                time.sleep(3)
                if phase_no == 1:
                    phase = 'R PHASE'
                elif phase_no == 2:
                    phase = 'Y PHASE'
                elif phase_no == 3:
                    phase = 'B PHASE'
                self.print_console("Setting IP voltage to " + str(phase_voltage))
                # AC_SOURCE_SET_VOLTAGE(self, phase_voltage, phase)
                time.sleep(27)
                alarm_phase_fail = int(self.MCM_READ_COMMAND('ALARM', phase.lower() + ' fail'))
                if alarm_phase_fail == 1:
                    RESULT_TEMP = True
                else:
                    RESULT_TEMP = False
                    if hvlv_card_state == 'PRESENT':
                        self.print_console("CHECK HVLV IP VOLTAGE SENSE WIRING", "RED")
                RESULT.append(RESULT_TEMP)
                self.print_console(str(RESULT))
                voltage_phase = int(self.MCM_READ_COMMAND('MAINS READ VOLTAGE', phase.lower()))
                if phase_voltage + 3 > voltage_phase > phase_voltage - 3:
                    RESULT_TEMP = True
                else:
                    RESULT_TEMP = False
                    if hvlv_card_state == 'PRESENT':
                        self.print_console("CHECK HVLV " + str(phase) + " IP VOLTAGE SENSE WIRING", "RED")

                RESULT.append(RESULT_TEMP)
                self.print_console(str(RESULT))
                config_smr_count = int(self.MCM_READ_COMMAND('SYSTEM CONFIG', 'smr count'))
                for i in range(phase_no, config_smr_count + 1, 3):
                    smr_status = int(
                        self.MCM_READ_COMMAND('SMR COMMANDS', 'smr' + str(i) + " status"))
                    self.print_console(SMR_STATUS_TEXT(smr_status))
                    if smr_status == 0:
                        RESULT_TEMP = True
                        self.print_console("SMR " + str(i) + " WIRING OK ")
                    else:
                        RESULT_TEMP = False
                        if hvlv_card_state == 'PRESENT':
                            self.print_console("SMR " + str(i) + " HVLV RELAY / WIRING FAULTY ", "RED")
                        elif hvlv_card_state != 'PRESENT':
                            self.print_console("SMR " + str(i) + " WIRING FAULTY ", "RED")
                    RESULT.append(RESULT_TEMP)
                    # PRINT_CONSOLE(self,str(RESULT))

            # id = self.sql.SQL_SELECT_3_QUERY('td_id', 'test_detail_results', 'td_test_item', 'PHASE_ALLOCATION',
            #                                  'td_readby', 'THREE_PHASE', 'td_mt_id', self.test_id)
            # print
            # id
            # if id != 0:
            #     print
            #     "update row"
            #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_UPDATE_QUERY(CALCULATE_RESULT(RESULT), id)
            # else:
            #     print
            #     "insert row"
            #     test_sub_id += 1
            #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_RESULTS_INSERT_QUERY(self.test_id, "'PHASE_ALLOCATION'",
            #                                                            "'THREE_PHASE'", test_sub_id, "''", "''",
            #                                                            CALCULATE_RESULT(RESULT))

        # if ac_phase_type == 'SINGLE PHASE':
        #     AC_SOURCE_SET_VOLTAGE(self, 230, ac_phase_type)
        # elif ac_phase_type == 'THREE PHASE':
        #     AC_SOURCE_SET_VOLTAGE(self, 230, ac_phase_type)
        # if (not (self.checkBox_manual.isChecked())):
        #     ac_source_set_frequency(self, 50)
        #     self.acsource.AC_SOURCE_SET_COMMAND(output_ON)

        self.print_console(str(RESULT))
        self.print_console("PHASE_ALLOCATION TEST FINISHED...")
        return CALCULATE_RESULT(RESULT)

    def CURRENT_SHARING(self):
        global SYSTEM_LOAD
        try:
            if self.mcm_type == 1:
                TELNET_SET_COMMAND(self.telnet, OIDRead('SYSTEM COMMANDS')['ate test'], "TEST_M1000_ATE")
            # batt_fuse_count=int(ConfigRead('DUT CONFIGURATION')['no. of battery fuses'])
            # load_current_count=int(ConfigRead('DUT CONFIGURATION')['no. of load current'])
            #     SET_JIG_PFC_OP(self.can,'AC',1)
            #     SET_JIG_PFC_OP(self.can,'BATT2',1)# TO BE CHANGED TO GENERIC
            #     SET_JIG_PFC_OP(self.can,'LOAD COMMON',1)
            #     SET_JIG_PFC_OP(self.can,'LOAD1',1)# for test
            self.smrcan.SMR_BATTERY_SET_VOLTAGE(47.0)
            self.dcload.DC_LOAD_SET_CURRENT_CC(5, "BATT")
            if ATE_LOAD_COUNT == 1:
                self.pfc.pfc_set(0, 'load_mains', 1)
            time.sleep(2)
            self.print_console("CURRENT SHARING TEST STARTED...")
            TOTAL_SMR_CURRENT = 0.0
            smr_count = int(ConfigRead('DUT CONFIGURATION')['smr count'])
            smr_type = ConfigRead('DUT CONFIGURATION')['smr type']
            self.MCM_WRITE_COMMAND('SYSTEM CONFIG', 'eco mode', 0)
            if smr_type == '3KW':
                SYSTEM_LOAD = 55.2 * 0.40 * smr_count
            elif smr_type == '25A':
                SYSTEM_LOAD = 25 * .80 * smr_count
            elif smr_type == '100A':
                SYSTEM_LOAD = 100 * 0.40 * smr_count

            BATTERY_LOAD = float(SYSTEM_LOAD) / 2
            BUS_LOAD = float(SYSTEM_LOAD) / 2
            REF_SMR_AVG_CURRENT = float(SYSTEM_LOAD) / smr_count
            self.dcload.DC_LOAD_SET_CURRENT_CC(BATTERY_LOAD, "BATT")
            self.dcload.DC_LOAD_SET_CURRENT_CC(BUS_LOAD, "LOAD")
            self.prompt.Message(prompt='CHECK INDIVIDUAL SMR CURRENT IN M1000. PRESS ENTER KEY TO PROCEED!')
            self.print_console("CURRENT SHARING TIME: 15 seconds")
            time.sleep(15)
            SMR_CURRENT = []
            SMR_CURRENT_DEVIATION = []
            INDI_SMR_CURRENT_DEVIATION = 0
            for smr_number in range(1, smr_count + 1):
                INDI_SMR_CURRENT = float(self.MCM_READ_COMMAND('SMR COMMANDS', 'smr' + str(smr_number) + ' current'))
                SMR_CURRENT.append(INDI_SMR_CURRENT)
                TOTAL_SMR_CURRENT += INDI_SMR_CURRENT
            ACTUAL_SMR_AVG_CURRENT = float(TOTAL_SMR_CURRENT) / smr_count
            for smr_number in range(1, smr_count + 1):
                INDI_SMR_CURRENT_DEVIATION = (float(
                    abs(ACTUAL_SMR_AVG_CURRENT - SMR_CURRENT[smr_number - 1])) / ACTUAL_SMR_AVG_CURRENT) * 100
                SMR_CURRENT_DEVIATION.append(INDI_SMR_CURRENT_DEVIATION)
            if max(SMR_CURRENT_DEVIATION) < 10:
                RESULT = True
                self.print_console('SMR CURRENT DEVIATION: ' + str(max(SMR_CURRENT_DEVIATION)))
                self.print_console('CURRENT DEVIATION PASS.')
            else:
                RESULT = False
                smr_number = 0
                self.print_console('CURRENT DEVIATION FAIL.', "RED")
                for CURRENT_DEVIATION in SMR_CURRENT_DEVIATION:
                    smr_number += 1
                    if CURRENT_DEVIATION > 10:
                        self.print_console('SMR NUMBER:' + str(smr_number) + ' current deviation is :' + str(
                            CURRENT_DEVIATION), "RED")
                        self.print_console(
                            'SMR CURRENT:' + str(SMR_CURRENT[smr_number - 1]) + ' AVG CURRENT is :' + str(
                                ACTUAL_SMR_AVG_CURRENT))

            self.MCM_WRITE_COMMAND('SYSTEM CONFIG', 'eco mode', 1)
            self.dcload.DC_LOAD_SET_CURRENT_CC(5, "BATT")
            self.dcload.DC_LOAD_SET_CURRENT_CC(5, "LOAD")
            if ATE_LOAD_COUNT == 1:
                self.pfc.pfc_set(0, 'load_mains', 0)
            self.print_console("CURRENT SHARING TEST FINISHED...")
        except:
            RESULT = False
        return RESULT

    def BUS_DROP(self):
        global SYSTEM_LOAD
        try:
            if self.mcm_type == 1:
                TELNET_SET_COMMAND(self.telnet, OIDRead('SYSTEM COMMANDS')['ate test'], "TEST_M1000_ATE")
            self.print_console("BUS DROP TEST STARTED...")
            RESULT = []
            DUT_BATT_VOLATGE = []
            smr_count = int(ConfigRead('DUT CONFIGURATION')['smr count'])
            smr_type = ConfigRead('DUT CONFIGURATION')['smr type']
            self.MCM_WRITE_COMMAND('SYSTEM CONFIG', 'eco mode', 0)
            batt_fuse_count = int(ConfigRead('DUT CONFIGURATION')['no. of battery fuses'])

            if ATE_LOAD_COUNT == 1:
                self.pfc.pfc_set(0, 'DC LOAD', 1)
            #     self.acsource.AC_SOURCE_SET_COMMAND(output_OFF)
            #     SET_JIG_PFC_OP(self.can,'AC',0)
            self.smrcan.SMR_BATTERY_SET_VOLTAGE(48.0)
            if smr_type == '3KW':
                SYSTEM_LOAD = 55.2 * 0.60 * smr_count
            elif smr_type == '25A':
                SYSTEM_LOAD = 25 * 0.60 * smr_count
            elif smr_type == '100A':
                SYSTEM_LOAD = 100 * 0.60 * smr_count
            if SYSTEM_LOAD > 200:
                SYSTEM_LOAD = 200
            BATTERY_LOAD = float(SYSTEM_LOAD) / 2
            BUS_LOAD = float(SYSTEM_LOAD) / 2
            self.dcload.DC_LOAD_SET_CURRENT_CC(BATTERY_LOAD, "BATT")
            self.dcload.DC_LOAD_SET_CURRENT_CC(BUS_LOAD, "LOAD")
            time.sleep(5)

            METER_READ_BATT_VOLTAGE = float(READ_DC_VOLTAGE("BATT"))

            METER_READ_LOAD_VOLTAGE = float(READ_DC_VOLTAGE("LOAD"))

            for batt_number in range(1, batt_fuse_count + 1):
                INDI_DUT_BATT_VOLTAGE = float(
                    self.MCM_READ_COMMAND('DC READ VOLTAGE', 'batt' + str(batt_number)))
                DUT_BATT_VOLATGE.append(INDI_DUT_BATT_VOLTAGE)
            DUT_BUS_VOLTAGE = float(self.MCM_READ_COMMAND('DC READ VOLTAGE', 'bus'))
            min_BATT_VOLTAGE = min(DUT_BATT_VOLATGE)
            max_BATT_VOLTAGE = max(DUT_BATT_VOLATGE)
            RESULT_TEMP = abs(min_BATT_VOLTAGE - max_BATT_VOLTAGE) < 0.20
            RESULT.append(RESULT_TEMP)
            RESULT_TEMP = abs(min_BATT_VOLTAGE - DUT_BUS_VOLTAGE) < 0.40
            RESULT.append(RESULT_TEMP)
            RESULT_TEMP = abs(max_BATT_VOLTAGE - DUT_BUS_VOLTAGE) < 0.40
            RESULT.append(RESULT_TEMP)
            #     RESULT_TEMP=COMPARE(METER_READ_BATT_VOLTAGE, DUT_BUS_VOLTAGE,0.20)
            #     RESULT.append(RESULT_TEMP)
            #     RESULT_TEMP=COMPARE(METER_READ_LOAD_VOLTAGE, DUT_BUS_VOLTAGE,0.20)
            #     RESULT.append(RESULT_TEMP)
            if CALCULATE_RESULT(RESULT) == False:
                self.print_console('BUS VOLTAGE DROP FAIL.CHECK BATTERY BUS BAR ALIGNMENT/SCREWS', 'RED')
                self.print_console('MIN BATTERY V: ' + str(min_BATT_VOLTAGE))
                self.print_console('MAX BATTERY V: ' + str(max_BATT_VOLTAGE))
                self.print_console('BUS V: ' + str(DUT_BUS_VOLTAGE))
                self.print_console('METER BATT V: ' + str(METER_READ_BATT_VOLTAGE))
                self.print_console('METER BUS V: ' + str(METER_READ_LOAD_VOLTAGE))
            else:
                self.print_console('BUS VOLTAGE DROP PASS.')
                self.print_console('MIN BATTERY V: ' + str(min_BATT_VOLTAGE))
                self.print_console('MAX BATTERY V: ' + str(max_BATT_VOLTAGE))
                self.print_console('BUS V: ' + str(DUT_BUS_VOLTAGE))
                self.print_console('METER BATT V: ' + str(METER_READ_BATT_VOLTAGE))
                self.print_console('METER BUS V: ' + str(METER_READ_LOAD_VOLTAGE))

            self.print_console("BUS DROP TEST FINISHED...")
            self.dcload.DC_LOAD_SET_CURRENT_CC(5, "BATT")
            self.dcload.DC_LOAD_SET_CURRENT_CC(5, "LOAD")

            if ATE_LOAD_COUNT == 1:
                self.pfc.pfc_set(0, 'DC LOAD', 0)
        except:
            return False
        return CALCULATE_RESULT(RESULT)

    def RS_485_CHECK(self):
        if self.mcm_type == 1:
            TELNET_SET_COMMAND(self.telnet, OIDRead('SYSTEM COMMANDS')['ate test'], "TEST_M1000_ATE")
        test_sub_id = 0
        PRINT_CONSOLE(self, "RS_485_CHECK TEST STARTED...")

        RESULT = []
        lower_port_number = 4
        upper_port_number = 0
        none_port_number = 255
        lower_port_baudrate = int(ConfigRead('DUT CONFIGURATION')['lower port baudrate'])
        upper_port_baudrate = int(ConfigRead('DUT CONFIGURATION')['upper port baudrate'])
        lithium_ion_comm_port = int(ConfigRead('DUT CONFIGURATION')['lithium ion comm'])
        acem_comm_port = int(ConfigRead('DUT CONFIGURATION')['acem comm'])
        dg_amf_comm_port = int(ConfigRead('DUT CONFIGURATION')['dg amf comm'])
        solar_hvlv_comm_port = int(ConfigRead('DUT CONFIGURATION')['solar hvlv comm'])
        ext_dcem_comm_port = int(ConfigRead('DUT CONFIGURATION')['ext dcem comm'])
        bnms_comm_port = int(ConfigRead('DUT CONFIGURATION')['bnms comm'])
        modbus_comm_port = int(ConfigRead('DUT CONFIGURATION')['modbus comm'])
        #     TELNET_SET_COMMAND(self.telnet,OIDRead('RS 485')['lithium ion comm'],none_port_number)
        #     TELNET_SET_COMMAND(self.telnet,OIDRead('RS 485')['acem comm'],none_port_number)
        #     TELNET_SET_COMMAND(self.telnet,OIDRead('RS 485')['dg amf comm'],none_port_number)
        #     TELNET_SET_COMMAND(self.telnet,OIDRead('RS 485')['solar hvlv comm'],none_port_number)
        #     TELNET_SET_COMMAND(self.telnet,OIDRead('RS 485')['ext dcem comm'],none_port_number)
        #     TELNET_SET_COMMAND(self.telnet,OIDRead('RS 485')['bnms comm'],none_port_number)

        if acem_comm_port == lower_port_number or lithium_ion_comm_port == lower_port_number or dg_amf_comm_port == lower_port_number or modbus_comm_port == lower_port_number:
            if acem_comm_port == lower_port_number:
                self.MCM_WRITE_COMMAND('RS 485', 'acem comm', none_port_number)
            if lithium_ion_comm_port == lower_port_number:
                self.MCM_WRITE_COMMAND('RS 485', 'lithium ion comm', none_port_number)
            if dg_amf_comm_port == lower_port_number:
                self.MCM_WRITE_COMMAND('RS 485', 'dg amf comm', none_port_number)

            self.MCM_WRITE_COMMAND('RS 485', 'modbus comm', lower_port_number)
            self.MCM_WRITE_COMMAND('SYSTEM COMMANDS', 'system reset', 1)
            # SET_JIG_PFC_OP(self.can,'ALL PFC',0)
            time.sleep(5)
            #         SET_JIG_PFC_OP(self.can,'BATT LOAD',1,1)
            #         SET_JIG_PFC_OP(self.can,'BATT COMMON',1)
            #         SET_JIG_PFC_OP(self.can,'BATT1',1)
            #
            #         time.sleep(10)
            charge_voltage_telnet = float(self.MCM_READ_COMMAND('BATTERY SETTING', 'charge voltage'))
            charge_voltage_modbus = float(MODBUS_CHECK('lower', lower_port_baudrate)) / 10
            # print
            # charge_voltage_modbus

            if charge_voltage_modbus == charge_voltage_telnet:
                RESULT_TEMP = True
                self.print_console("MODBUS CHARGE VOLTAGE:" + str(charge_voltage_modbus))
                self.print_console("TELNET CHARGE VOLTAGE:" + str(charge_voltage_telnet))
                self.print_console("LOWER PORT TESTED OK")
            else:
                RESULT_TEMP = False
                self.print_console("MODBUS CHARGE VOLTAGE:" + str(charge_voltage_modbus))
                self.print_console("TELNET CHARGE VOLTAGE:" + str(charge_voltage_telnet))
                self.print_console("LOWER PORT TESTED FAIL", "RED")
            RESULT.append(RESULT_TEMP)
            # print
            # RESULT
            # id = self.sql.SQL_SELECT_3_QUERY('td_id', 'test_detail_results', 'td_test_item', 'RS_485_CHECK',
            #                                  'td_readby', 'LOWER_PORT', 'td_mt_id', self.test_id)
            # print
            # id
            # if id != 0:
            #     print
            #     "update row"
            #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_UPDATE_QUERY(RESULT_TEMP, id)
            # else:
            #     print
            #     "insert row"
            #     test_sub_id += 1
            #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_RESULTS_INSERT_QUERY(self.test_id, "'RS_485_CHECK'", "'LOWER_PORT'",
            #                                                            test_sub_id, "''", "''", RESULT_TEMP)

        else:
            RESULT_TEMP = True
            self.print_console("LOWER PORT TESTING NOT APPLICABLE")
            # test_sub_id += 1
            # self.sql.SQL_TEST_ITEM_RUN_DETAIL_RESULTS_INSERT_QUERY(self.test_id, "'RS_485_CHECK'", "'LOWER_PORT'",
            #                                                        test_sub_id, "''", "'NA'", RESULT_TEMP)

        if acem_comm_port == upper_port_number or lithium_ion_comm_port == upper_port_number or dg_amf_comm_port == upper_port_number or modbus_comm_port == upper_port_number:
            if acem_comm_port == upper_port_number:
                self.MCM_WRITE_COMMAND('RS 485', 'acem comm', none_port_number)
            if lithium_ion_comm_port == upper_port_number:
                self.MCM_WRITE_COMMAND('RS 485', 'lithium ion comm', none_port_number)
            if dg_amf_comm_port == upper_port_number:
                self.MCM_WRITE_COMMAND('RS 485', 'dg amf comm', none_port_number)

            self.MCM_WRITE_COMMAND('RS 485', 'modbus comm', upper_port_number)
            self.MCM_WRITE_COMMAND('SYSTEM COMMANDS', 'system reset', 1)
            # SET_JIG_PFC_OP(self.can,'ALL PFC',0)
            time.sleep(5)
            # SET_JIG_PFC_OP(self.can,'BATT LOAD',1,1)
            # SET_JIG_PFC_OP(self.can,'BATT COMMON',1)
            # SET_JIG_PFC_OP(self.can,'BATT1',1)

            # time.sleep(10)
            charge_voltage_telnet = float(self.MCM_READ_COMMAND('BATTERY SETTING', 'charge voltage'))
            charge_voltage_modbus = float(MODBUS_CHECK('upper', upper_port_baudrate)) / 10

            if charge_voltage_modbus == charge_voltage_telnet:
                RESULT_TEMP = True
                self.print_console("MODBUS CHARGE VOLTAGE:" + str(charge_voltage_modbus))
                self.print_console("TELNET CHARGE VOLTAGE:" + str(charge_voltage_telnet))
                self.print_console("UPPER PORT TESTED OK")
            else:
                RESULT_TEMP = False
                self.print_console("MODBUS CHARGE VOLTAGE:" + str(charge_voltage_modbus))
                self.print_console("TELNET CHARGE VOLTAGE:" + str(charge_voltage_telnet))
                self.print_console("UPPER PORT TESTED FAIL", "RED")
            RESULT.append(RESULT_TEMP)

        #     print
        #     RESULT
        #     id = self.sql.SQL_SELECT_3_QUERY('td_id', 'test_detail_results', 'td_test_item', 'RS_485_CHECK',
        #                                      'td_readby', 'UPPER_PORT', 'td_mt_id', self.test_id)
        #     print
        #     id
        #     if id != 0:
        #         print
        #         "update row"
        #         self.sql.SQL_TEST_ITEM_RUN_DETAIL_UPDATE_QUERY(RESULT_TEMP, id)
        #     else:
        #         print
        #         "insert row"
        #         test_sub_id += 1
        #         self.sql.SQL_TEST_ITEM_RUN_DETAIL_RESULTS_INSERT_QUERY(self.test_id, "'RS_485_CHECK'", "'UPPER_PORT'",
        #                                                                test_sub_id, "''", "''", RESULT_TEMP)
        #
        # else:
        #     RESULT_TEMP = True
        #     PRINT_CONSOLE(self, "LOWER PORT TESTING NOT APPLICABLE")
        #     test_sub_id += 1
        #     self.sql.SQL_TEST_ITEM_RUN_DETAIL_RESULTS_INSERT_QUERY(self.test_id, "'RS_485_CHECK'", "'UPPER_PORT'",
        #                                                            test_sub_id, "''", "'NA'", RESULT_TEMP)

        self.print_console("RS_485_CHECK TEST FINISHED...")
        return CALCULATE_RESULT(RESULT)

    def DEFAULT_SETTING(self):
        self.MCM_WRITE_COMMAND('SYSTEM COMMANDS', 'factory restore', 1)
        self._prevent_gui_hang()
        time.sleep(5)
        self._prevent_gui_hang()

        if self.mcm_type == 1:
            self.MCM_WRITE_COMMAND('SYSTEM COMMANDS', 'ate test', "TEST_M1000_ATE")

        site_id = self.MCM_READ_COMMAND('SYSTEM CONFIG', 'site id')
        self.print_console("Controller Healthy") if site_id is not None else self.print_console("Controller OFF")
        RESULT_TEMP = True if site_id is not None else False

        if self.custom_check.isChecked():
            self._set_custom_settings()
        else:
            self._set_default_settings()

        float_voltage, charge_voltage, battery_lvd_set, battery_lvd_restore, load_lvd_count, \
            load_lvd_set, load_lvd_restore, dc_v_low_set, dc_v_low_restore, \
            main_low_fail_set, main_low_fail_restore, main_high_fail_set, \
            main_high_fail_restore, smr_count, m1000_mac_id, m1000_serial_number = self._get_battery_settings()

        battery_capacity_vrla, bcl_factor_vrla = self._get_battery_config_vrla()
        battery_capacity, bcl_factor, module_count = self._get_battery_config_lion()

        self._prevent_gui_hang()
        self._update_excel_handler(float_voltage, charge_voltage, battery_lvd_set, battery_lvd_restore,
                                   load_lvd_set, load_lvd_restore, dc_v_low_set, dc_v_low_restore,
                                   main_low_fail_set, main_low_fail_restore, main_high_fail_set,
                                   main_high_fail_restore, smr_count, m1000_mac_id, m1000_serial_number,
                                   battery_capacity_vrla, bcl_factor_vrla, battery_capacity, bcl_factor, module_count)

        return RESULT_TEMP

    def _prevent_gui_hang(self):
        QtGui.qApp.processEvents()

    def _set_custom_settings(self):
        self.print_console("Custom settings will be programmed to controller")
        default_settings = DefaultRead('DEFAULT SETTING')
        for setting in ['smr count', 'system overload', 'battery ah']:
            if default_settings[setting] == 'YES':
                self.MCM_WRITE_COMMAND('SYSTEM CONFIG', setting, int(default_settings[setting]))

    def _set_default_settings(self):
        self.print_console("Default setting are as per Config file")

    def _get_battery_settings(self):
        settings = ['float voltage', 'charge voltage', 'battery lvd set', 'battery lvd restore',
                    'no. of load lvd', 'load1 lvd set', 'load1 lvd restore', 'dc voltage low set',
                    'dc voltage low restore', 'mains low fail set', 'mains low fail restore',
                    'mains high fail set', 'mains high fail restore', 'smr count', 'm1000 mac id',
                    'serial number']
        return [float(self.MCM_READ_COMMAND('BATTERY SETTING', setting)) for setting in settings]

    def _get_battery_config_vrla(self):
        return int(self.MCM_READ_COMMAND('SYSTEM CONFIG', 'vrla battery capacity')), \
            int(self.MCM_READ_COMMAND('SYSTEM CONFIG', 'vrla bcl factor'))

    def _get_battery_config_lion(self):
        return int(self.MCM_READ_COMMAND('SYSTEM CONFIG', 'lion battery capacity')), \
            int(self.MCM_READ_COMMAND('SYSTEM CONFIG', 'lion bcl factor')), \
            int(self.MCM_READ_COMMAND('SYSTEM CONFIG', 'lion module count'))

    def _update_excel_handler(self, float_voltage, charge_voltage, battery_lvd_set, battery_lvd_restore,
                              load_lvd_set, load_lvd_restore, dc_v_low_set, dc_v_low_restore,
                              main_low_fail_set, main_low_fail_restore, main_high_fail_set,
                              main_high_fail_restore, smr_count, m1000_mac_id, m1000_serial_number,
                              battery_capacity_vrla, bcl_factor_vrla, battery_capacity, bcl_factor, module_count):
        self.excel_handler.update_cell("FLOAT VOLTAGE (VDC)", str(float_voltage))
        self.excel_handler.update_cell("CHARGE VOLTAGE (VDC)", str(charge_voltage))
        self.excel_handler.update_cell("BATTERY LVD SET(VDC)/RESTORE(VDC)", f"{battery_lvd_set}/{battery_lvd_restore}")
        self.excel_handler.update_cell("LOAD LVD SET(VDC)/RESTORE(VDC)", f"{load_lvd_set}/{load_lvd_restore}")
        self.excel_handler.update_cell("DC VOLTAGE LOW(VDC)/RESTORE(VDC)", f"{dc_v_low_set}/{dc_v_low_restore}")
        self.excel_handler.update_cell("AC LOW CUT-OFF(VAC)/CUT-IN(VAC)",
                                       f"{main_low_fail_set}/{main_low_fail_restore}")
        self.excel_handler.update_cell("AC HIGH CUT-OFF(VAC)/CUT-IN(VAC)",
                                       f"{main_high_fail_set}/{main_high_fail_restore}")
        self.excel_handler.update_cell("SMR COUNT/ SOLAR CHARGER COUNT", f"{smr_count}/NA")
        self.excel_handler.update_cell("VRLA: BATTERY CAPACITY/ FACTOR", f"{battery_capacity_vrla}/{bcl_factor_vrla}")
        self.excel_handler.update_cell("LI-ON BATTERY/ FACTOR", f"{battery_capacity}/{bcl_factor}/{module_count}")
        self._prevent_gui_hang()

    def DEFAULT_SETTING1(self):

        global battery_capacity_vrla, bcl_factor_vrla, battery_capacity, bcl_factor, module_count
        self.MCM_WRITE_COMMAND('SYSTEM COMMANDS', 'factory restore', 1)
        QtGui.qApp.processEvents()  # ADDED TO PREVENT GUI HANG PROBLEM,PARAS MITTAL
        time.sleep(5)
        QtGui.qApp.processEvents()  # ADDED TO PREVENT GUI HANG PROBLEM,PARAS MITTAL
        if self.mcm_type == 1:
            self.MCM_WRITE_COMMAND('SYSTEM COMMANDS', 'ate test', "TEST_M1000_ATE")
        site_id = self.MCM_READ_COMMAND('SYSTEM CONFIG', 'site id')
        if site_id is not None:
            self.print_console("Controller Healthy")
            RESULT_TEMP = True
        else:
            self.print_console("Controller OFF")
            RESULT_TEMP = False
        '''
        ## TO BE OPENED AFTER SERIAL NUMBER/PART NUMBER IMPLEMENTATION IN 15.XX/10.XX
        DUT_Part_Number=str(self.lineEdit_DUTPartNumber.text())
        DUT_Serial_Number=str(self.lineEdit_DUTSerialNumber.text())

        TELNET_SET_COMMAND(self.telnet,OIDRead('SYSTEM COMMANDS')['system part number'],DUT_Part_Number)
        PRINT_CONSOLE(self, "SYSTEM PART NUMBER ENTERED IN M1000: "+DUT_Part_Number)

        TELNET_SET_COMMAND(self.telnet,OIDRead('SYSTEM COMMANDS')['system serial number'],DUT_Serial_Number)
        PRINT_CONSOLE(self, "SYSTEM SERIAL NUMBER ENTERED IN M1000: "+DUT_Serial_Number)
        '''

        if self.custom_check.isChecked():
            self.print_console("Custom settings will be programmed to controller")
            # MESSAGE_PROMPT(self,"Custom settings will be programmed to controller")
            if DefaultRead('DEFAULT SETTING STATE')["smr count"] == 'YES':
                default_smr_count = int(DefaultRead('DEFAULT SETTING')["smr count"])
                self.MCM_WRITE_COMMAND('SYSTEM CONFIG', 'smr count', default_smr_count)
            if DefaultRead('DEFAULT SETTING STATE')["system overload"] == 'YES':
                default_system_overload = int(DefaultRead('DEFAULT SETTING')["system overload"])
                self.MCM_WRITE_COMMAND('SYSTEM CONFIG', 'system overload', default_system_overload)
            if DefaultRead('DEFAULT SETTING STATE')["battery ah"] == 'YES':
                default_battery_ah = int(DefaultRead('DEFAULT SETTING')["battery ah"])
                self.MCM_WRITE_COMMAND('SYSTEM CONFIG', 'vrla battery capacity', default_battery_ah)
        else:
            self.print_console("Default setting are as per Config file")
            # MESSAGE_PROMPT(self,"Default setting are as per Config file ")

        ## load default setting for report
        float_voltage = float(self.MCM_READ_COMMAND('BATTERY SETTING', 'float voltage'))
        charge_voltage = float(self.MCM_READ_COMMAND('BATTERY SETTING', 'charge voltage'))
        battery_lvd_set = float(self.MCM_READ_COMMAND('BATTERY SETTING', 'battery lvd set'))
        battery_lvd_restore = float(self.MCM_READ_COMMAND('BATTERY SETTING', 'battery lvd restore'))
        load_lvd_count = int(self.MCM_READ_COMMAND('SYSTEM CONFIG', 'no. of load lvd'))
        if load_lvd_count != 0:
            load_lvd_set = float(self.MCM_READ_COMMAND('BATTERY SETTING', 'load1 lvd set'))
            load_lvd_restore = float(self.MCM_READ_COMMAND('BATTERY SETTING', 'load1 lvd restore'))

        else:
            load_lvd_set = 'NA'
            load_lvd_restore = 'NA'
        dc_v_low_set = float(self.MCM_READ_COMMAND('BATTERY SETTING', 'dc voltage low set'))
        dc_v_low_restore = float(self.MCM_READ_COMMAND('BATTERY SETTING', 'dc voltage low restore'))
        dc_v_low_set = float(self.MCM_READ_COMMAND('BATTERY SETTING', 'dc voltage low set'))
        dc_v_low_restore = float(self.MCM_READ_COMMAND('BATTERY SETTING', 'dc voltage low restore'))
        dc_v_low_restore += dc_v_low_set
        main_low_fail_set = int(self.MCM_READ_COMMAND('MAINS SETTING', 'mains low fail set'))
        main_low_fail_restore = int(self.MCM_READ_COMMAND('MAINS SETTING', 'mains low fail restore'))
        main_low_fail_restore = main_low_fail_set + main_low_fail_restore
        main_high_fail_set = int(self.MCM_READ_COMMAND('MAINS SETTING', 'mains high fail set'))
        main_high_fail_restore = int(self.MCM_READ_COMMAND('MAINS SETTING', 'mains high fail restore'))
        main_high_fail_restore = main_high_fail_set + main_high_fail_restore
        smr_count = self.MCM_READ_COMMAND('SYSTEM CONFIG', 'smr count')
        m1000_mac_id = self.MCM_READ_COMMAND('SYSTEM COMMANDS', 'm1000 mac id')
        m1000_serial_number = self.MCM_READ_COMMAND('SYSTEM COMMANDS', 'serial number')
        QtGui.qApp.processEvents()  # ADDED TO PREVENT GUI HANG PROBLEM, PARAS MITTAL, 12/03/2024
        battery_type = ConfigRead('DUT CONFIGURATION')['battery type']
        if battery_type == 'VRLA':
            battery_capacity_vrla = int(self.MCM_READ_COMMAND('SYSTEM CONFIG', 'vrla battery capacity'))
            bcl_factor_vrla = int(self.MCM_READ_COMMAND('SYSTEM CONFIG', 'vrla bcl factor'))

        elif battery_type == 'LION':
            battery_capacity = int(self.MCM_READ_COMMAND('SYSTEM CONFIG', 'lion battery capacity'))
            module_count = int(self.MCM_READ_COMMAND('SYSTEM CONFIG', 'lion module count'))
            bcl_factor = int(self.MCM_READ_COMMAND('SYSTEM CONFIG', 'lion bcl factor'))
            battery_capacity_vrla = int(self.MCM_READ_COMMAND('SYSTEM CONFIG', 'vrla battery capacity'))
            bcl_factor_vrla = int(self.MCM_READ_COMMAND('SYSTEM CONFIG', 'vrla bcl factor'))
        RESULT_DEFAULT = True
        test_sub_id = 0
        test_sub_id += 1

        QtGui.qApp.processEvents()  # ADDED TO PREVENT GUI HANG PROBLEM,Paras MITTAL,24/10/2016
        self.excel_handler.update_cell("FLOAT VOLTAGE (VDC)", str(float_voltage))
        self.excel_handler.update_cell("CHARGE VOLTAGE (VDC)", str(charge_voltage))
        self.excel_handler.update_cell("BATTERY LVD SET(VDC)/RESTORE(VDC)", str(battery_lvd_set)+"/"+str(battery_lvd_restore))
        self.excel_handler.update_cell("LOAD LVD SET(VDC)/RESTORE(VDC)", str(load_lvd_set) + "/" + str(load_lvd_restore))
        self.excel_handler.update_cell("DC VOLTAGE LOW(VDC)/RESTORE(VDC)", str(dc_v_low_set) + "/" + str(dc_v_low_restore))
        self.excel_handler.update_cell("AC LOW CUT-OFF(VAC)/CUT-IN(VAC)", str(main_low_fail_set) + "/" + str(main_low_fail_restore))
        self.excel_handler.update_cell("AC HIGH CUT-OFF(VAC)/CUT-IN(VAC)", str(main_high_fail_set) + "/" + str(main_high_fail_restore))
        self.excel_handler.update_cell("SMR COUNT/ SOLAR CHARGER COUNT", str(smr_count) + "/" + str("NA"))
        self.excel_handler.update_cell("VRLA: BATTERY CAPACITY/ FACTOR", str(battery_capacity_vrla) + "/" + str(bcl_factor_vrla))
        self.excel_handler.update_cell("LI-ON BATTERY/ FACTOR", str(battery_capacity) + "/" + str(bcl_factor)+"/"+str(module_count))
        QtGui.qApp.processEvents()  # ADDED TO PREVENT GUI HANG PROBLEM,Paras MITTAL,24/10/2016
        return RESULT_TEMP

    def CHECK_DEVICES(self):
        self.print_console("CHECK DEVICES TEST STARTED....")
        self.HEALTH_CHECK_SMR_BATTERY()
        self.HEALTH_CHECK_DC_LOAD()
        ATE_LOAD_COUNT = int(SettingRead("SETTING")['ate load count'])
        if ATE_LOAD_COUNT != 1:
            self.HEALTH_CHECK_DC_LOAD()
        # self.dcload.DC_LOAD_SET_CURRENT_CC()
        self.dcload.DC_LOAD_SET_CURRENT_CC(0, load_type="LOAD")
        self.dcload.DC_LOAD_SET_CURRENT_CC(0, load_type="BATT")
        self.print_console("CHECK DEVICES TEST FINISHED...")

    def ATS_INITIALIZE(self):
        self.print_console("ATS INITIALIZING....")
        self.HEALTH_CHECK_SMR_BATTERY()
        InitChromaLoad(self.dcload.DC_LOAD, "LOAD")
        InitChromaLoad(self.dcload.DC_LOAD, "BATT")
        self.INITIAL_LOAD(type=LOAD)
        self.INITIAL_LOAD(type=BATT)
        self.print_console("ATS INITIALIZED....")
        return True

    def HEALTH_CHECK_SMR_BATTERY(self):
        self.smrcan.SMR_BATTERY_SET_VOLTAGE(50.0)

    def HEALTH_CHECK_DC_LOAD(self):
        self.dcload.DC_LOAD.DC_LOAD_READ_COMMAND(self.dcload.DC_LOAD, self.dcload.identify_unit)

    def CLEAR_JIG(self):
        self.print_console('CLEARING JIG....')
        self.pfc.pfc_set("0", "all", 0)  ## PENDING DCLOAD RESET
        self.dcload.DC_LOAD.DC_LOAD_SET_COMMAND(self.dcload.DC_LOAD, self.dcload.load_OFF)
        self.dcload.DC_LOAD.DC_LOAD_SET_COMMAND(self.dcload.DC_LOAD, self.dcload.load_OFF, "BATT")
        time.sleep(1)
        self.print_console("JIG CLEARED....")

    def MCM_READ_COMMAND(self, command='', section=""):
        if self.mcm_type == 1:
            # OIDRead('ALARM')['spu fail']
            return M1000Telnet.telnet_get_command(OIDRead(command)[section])
        elif self.mcm_type == 2:
            # M2000OIDRead('ALARM')['spu fail']
            return self.M2000.MCM_GET_COMMAND(M2000OIDRead(command)[section])

    def MCM_WRITE_COMMAND(self, command='', section='', value=''):
        if self.mcm_type == 1:
            M1000Telnet.telnet_set_command(OIDRead(command)[section], value)
        elif self.mcm_type == 2:
            self.M2000.MCM_SET_COMMAND(M2000OIDRead(command)[section], value)


def SET_INDI_LOAD_ISOLATE(self, load_no, state):
    self.MCM_WRITE_COMMAND('LOAD ISOLATE', 'load' + str(load_no), state)


def CALIBRATE_CURRENT_PATH_HALL_EFFECT(self, channel_number, load_type):
    if self.mcm_type == 1:
        self.MCM_WRITE_COMMAND('SYSTEM COMMANDS', 'ate test', "TEST_M1000_ATE")
    RESULT = []
    self.smrcan.SMR_BATTERY_SET_VOLTAGE(53.5)
    if self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' gain') != '0' or (
            self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(
                channel_number) + ' offset') != '0'):  # or (TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' deadband'])!='0')
        self.print_console("Resetting offset and gain again")
        # TELNET_SET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' deadband'],0)
        # time.sleep(1)
        self.MCM_WRITE_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' gain', 0)
        time.sleep(2)
        self.MCM_WRITE_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' offset', 0)
        time.sleep(2)
        self.print_console("CURRENT CHANNEL " + str(channel_number) + " GAIN: " + str(
            self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' gain')))
        self.print_console("CURRENT CHANNEL " + str(channel_number) + " OFFSET: " + str(
            self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' offset')))
        # PRINT_CONSOLE(self,"CURRENT CHANNEL "+str(channel_number)+" DEADBAND: "+str(TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' deadband'])))

    channel_hall_effect_value = int(
        ConfigRead('DUT CONFIGURATION')['channel' + str(channel_number) + ' hall effect value'])
    SET_CURRENT_LOW = int(CalibrateRead('HALL EFFECT')['current low'])
    SET_CURRENT_HIGH = int(CalibrateRead('HALL EFFECT')['current high'])
    NUMBER_OF_BITS = int(CalibrateRead('HALL EFFECT')['number of bits'])
    FACTOR = float(CalibrateRead('HALL EFFECT')['factor'])
    ADC_MULTIPLIER = int(CalibrateRead('HALL EFFECT')['adc multiplier'])
    DEADBAND = int(CalibrateRead('HALL EFFECT')['deadband'])
    VERIFY_CURRENT_LOW = int(CalibrateRead('HALL EFFECT')['verify current low'])
    VERIFY_CURRENT_MID = int(CalibrateRead('HALL EFFECT')['verify current mid'])
    VERIFY_CURRENT_HIGH = int(CalibrateRead('HALL EFFECT')['verify current high'])
    CURRENT_TOLERANCE = float(CalibrateRead('HALL EFFECT')['current tolerance'])
    NEGATIVE_SET_CURRENT_LOW = int(CalibrateRead('HALL EFFECT')['negative current low'])
    NEGATIVE_CURRENT_CAL = str(CalibrateRead('HALL EFFECT')['negative current cal'])

    if load_type == 'BATT' and NEGATIVE_CURRENT_CAL == 'YES':
        if ATE_LOAD_COUNT == 1:  # ADDED FOR SINGLE LOAD CONFIGURATION, KUSHAGRA MITTAL 06/09/2016
            # self.pfc.pfc_set(0, 'DC LOAD', 0)
            self.pfc.pfc_set(0, 'load_mains', 1)
            time.sleep(3)

        self.MCM_WRITE_COMMAND('BATTERY SETTING', 'float voltage', 51)
        self.MCM_WRITE_COMMAND('BATTERY SETTING', 'charge voltage', 51.5)
        self.MCM_WRITE_COMMAND('BATTERY SETTING', 'lion charge voltage', 51)
        # SET_JIG_PFC_OP(self.can,'AC',0)

        self.dcload.DC_LOAD_SET_CURRENT_CC(NEGATIVE_SET_CURRENT_LOW, "LOAD")
        time.sleep(4)
        METER_READ_CURRENT_LOW = float(READ_DC_CURRENT("LOAD"))
        METER_READ_CURRENT_LOW = (-1 * METER_READ_CURRENT_LOW) - float(
            CalibrateSetting('HALL EFFECT')['batt discharge compensation'])
    else:
        if ATE_LOAD_COUNT == 1 and load_type == 'BATT':
            self.print_console("RESETTING FOR BATTERY PATH")
            # ADDED FOR SINGLE LOAD CONFIGURATION, KUSHAGRA MITTAL 06/09/2016
            self.pfc.pfc_set(0, 'load_mains', 1)
            # self.pfc.pfc_set(0, 'DC LOAD', 1)
            time.sleep(3)
        self.dcload.DC_LOAD_SET_CURRENT_CC(SET_CURRENT_LOW, load_type)
        time.sleep(4)
        METER_READ_CURRENT_LOW = float(READ_DC_CURRENT(load_type))

    DUT_READ_CURRENT_LOW = float(self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number))) / 10
    BATT_CHARGE_CURRENT_COMPENSATION = 0
    self.print_console("CH :" + str(channel_number) + " DUT LOW: " + str(DUT_READ_CURRENT_LOW))
    self.print_console("CH :" + str(channel_number) + " METER LOW: " + str(METER_READ_CURRENT_LOW))
    if load_type == 'BATT' and NEGATIVE_CURRENT_CAL == 'YES':
        self.dcload.DC_LOAD_SET_CURRENT_CC(5, "LOAD")
        self.dcload.DC_LOAD_SET_CURRENT_CC(5, "BATT")
        if ATE_LOAD_COUNT == 1:  # ADDED FOR SINGLE LOAD CONFIGURATION, PARAS MITTAL 06/09/2016
            self.pfc.pfc_set(0, 'load_mains', 1)
            # self.pfc.pfc_set(0, 'DC LOAD', 1)
            time.sleep(3)

        self.MCM_WRITE_COMMAND('BATTERY SETTING', 'charge voltage', 55.2)
        self.MCM_WRITE_COMMAND('BATTERY SETTING', 'float voltage', 54)
        self.MCM_WRITE_COMMAND('BATTERY SETTING', 'lion charge voltage', 54)

        time.sleep(10)
        self.dcload.SMR_BATTERY_SET_VOLTAGE(47.0)

        # SET_JIG_PFC_OP(self.can,'AC',1)
        BATT_CHARGE_CURRENT_COMPENSATION = float(CalibrateSetting('HALL EFFECT')['batt charge compensation'])
        # time.sleep(2)
    # time.sleep(5)
    if ATE_LOAD_COUNT == 1:  # ADDED FOR SINGLE LOAD CONFIGURATION, KUSHAGRA MITTAL 06/09/2016
        load_type = LOAD

    self.dcload.DC_LOAD_SET_CURRENT_CC(SET_CURRENT_HIGH, str(load_type))

    time.sleep(4)
    DUT_READ_CURRENT_HIGH = float(self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number))) / 10
    METER_READ_CURRENT_HIGH = float(READ_DC_CURRENT(load_type)) + BATT_CHARGE_CURRENT_COMPENSATION
    self.print_console("CH :" + str(channel_number) + " DUT HIGH: " + str(DUT_READ_CURRENT_HIGH))
    self.print_console("CH :" + str(channel_number) + " METER HIGH: " + str(METER_READ_CURRENT_HIGH))
    self.dcload.DC_LOAD_SET_CURRENT_CC(SET_CURRENT_LOW, str(load_type))

    try:
        SLOPE = ((DUT_READ_CURRENT_HIGH - DUT_READ_CURRENT_LOW) / (
                METER_READ_CURRENT_HIGH - METER_READ_CURRENT_LOW)) * (
                        float(NUMBER_OF_BITS) / (channel_hall_effect_value * FACTOR))
        self.print_console("CH :" + str(channel_number) + " SLOPE: " + str(SLOPE))
        Z_OFFSET = ((DUT_READ_CURRENT_HIGH * NUMBER_OF_BITS) / (
                channel_hall_effect_value * FACTOR)) - SLOPE * METER_READ_CURRENT_HIGH
        self.print_console("CH :" + str(channel_number) + " Z_OFFSET: " + str(Z_OFFSET))
        GAIN_OFFSET = (FACTOR * channel_hall_effect_value * (((METER_READ_CURRENT_HIGH - METER_READ_CURRENT_LOW) / (
                DUT_READ_CURRENT_HIGH - DUT_READ_CURRENT_LOW)) - 1)) / 1
        GAIN_OFFSET = round(GAIN_OFFSET, 0)
        self.print_console("CH :" + str(channel_number) + " GAIN OFFSET: " + str(GAIN_OFFSET))
        ZERO_OFFSET = -1 * ADC_MULTIPLIER * Z_OFFSET / SLOPE
        ZERO_OFFSET = round(ZERO_OFFSET, 0)
        self.print_console("CH :" + str(channel_number) + " ZERO OFFSET: " + str(ZERO_OFFSET))
    except:
        SLOPE = 0
        Z_OFFSET = 0
        GAIN_OFFSET = 0
        ZERO_OFFSET = 0
        self.print_console("EXCEPTION OCCURRED.TEST FAILED.CALIBRATION WILL BE DONE AGAIN", "RED")
        self.print_console("CH :" + str(channel_number) + " SLOPE: " + str(SLOPE))
        self.print_console("CH :" + str(channel_number) + " Z_OFFSET: " + str(Z_OFFSET))
        self.print_console("CH :" + str(channel_number) + " GAIN OFFSET: " + str(GAIN_OFFSET))
        self.print_console("CH :" + str(channel_number) + " ZERO OFFSET: " + str(ZERO_OFFSET))

    CALIBRATION_NOT_DONE = True
    cal_try_count = 0
    while CALIBRATION_NOT_DONE and cal_try_count < 5:
        cal_try_count = cal_try_count + 1
        self.MCM_WRITE_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' gain', GAIN_OFFSET)
        time.sleep(2)
        self.MCM_WRITE_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' offset',
                               ZERO_OFFSET)
        time.sleep(2)
        self.MCM_WRITE_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' deadband',
                               DEADBAND)
        time.sleep(2)
        if (float(self.MCM_READ_COMMAND('CALIBRATE CURRENT', "channel" + str(channel_number) + " gain")) != GAIN_OFFSET) \
                or (float(
            self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' offset')) != ZERO_OFFSET) \
                or (self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' deadband') != str(
            DEADBAND)):
            CALIBRATION_NOT_DONE = True
        else:
            CALIBRATION_NOT_DONE = False

    #     TELNET_SET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' gain'],GAIN_OFFSET)
    #     time.sleep(1)
    #     TELNET_SET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' offset'],ZERO_OFFSET)
    #     time.sleep(1)
    #     TELNET_SET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' deadband'],DEADBAND)
    #     time.sleep(1)
    self.print_console("PROGRAMMED CURRENT CHANNEL " + str(channel_number) + " GAIN: " + str(
        self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' gain')))
    self.print_console("PROGRAMMED CURRENT CHANNEL " + str(channel_number) + " OFFSET: " + str(
        self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' offset')))
    self.print_console("PROGRAMMED CURRENT CHANNEL " + str(channel_number) + " DEADBAND: " + str(
        self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' deadband')))

    ## verify current calibration
    self.dcload.DC_LOAD_SET_CURRENT_CC(VERIFY_CURRENT_LOW, load_type)
    time.sleep(3)
    DUT__VERIFY_READ_CURRENT_LOW = float(
        self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number))) / 10
    METER__VERIFY_READ_CURRENT_LOW = float(READ_DC_CURRENT(load_type)) + BATT_CHARGE_CURRENT_COMPENSATION
    RESULT_TEMP = (abs(DUT__VERIFY_READ_CURRENT_LOW - METER__VERIFY_READ_CURRENT_LOW) < CURRENT_TOLERANCE and (
            abs(METER__VERIFY_READ_CURRENT_LOW - VERIFY_CURRENT_LOW) < 3))
    if RESULT_TEMP == False:
        COLOR_STATUS = "RED"
    else:
        COLOR_STATUS = 'BLUE'

    self.print_console("CH :" + str(channel_number) + " CURRENT_TOLERANCE: " + str(CURRENT_TOLERANCE), COLOR_STATUS)
    self.print_console(
        "CH :" + str(channel_number) + " METER__VERIFY_READ_CURRENT_LOW: " + str(METER__VERIFY_READ_CURRENT_LOW),
        COLOR_STATUS)
    self.print_console(
        "CH :" + str(channel_number) + " DUT__VERIFY_READ_CURRENT_LOW: " + str(DUT__VERIFY_READ_CURRENT_LOW),
        COLOR_STATUS)
    RESULT.append(RESULT_TEMP)

    self.dcload.DC_LOAD_SET_CURRENT_CC(VERIFY_CURRENT_MID, str(load_type))
    time.sleep(3)
    DUT__VERIFY_READ_CURRENT_MID = float(
        self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number))) / 10
    METER__VERIFY_READ_CURRENT_MID = float(READ_DC_CURRENT(load_type)) + BATT_CHARGE_CURRENT_COMPENSATION
    RESULT_TEMP = (abs(DUT__VERIFY_READ_CURRENT_MID - METER__VERIFY_READ_CURRENT_MID) < CURRENT_TOLERANCE and (
            abs(METER__VERIFY_READ_CURRENT_MID - VERIFY_CURRENT_MID) < 3))
    if RESULT_TEMP == False:
        COLOR_STATUS = "RED"
    else:
        COLOR_STATUS = 'BLUE'
    self.print_console("CH :" + str(channel_number) + " CURRENT_TOLERANCE: " + str(CURRENT_TOLERANCE), COLOR_STATUS)
    self.print_console("CH :" + str(channel_number) + " METER__VERIFY_READ_CURRENT_MID: " + str(
        METER__VERIFY_READ_CURRENT_MID), COLOR_STATUS)
    self.print_console(
        "CH :" + str(channel_number) + " DUT__VERIFY_READ_CURRENT_MID: " + str(DUT__VERIFY_READ_CURRENT_MID),
        COLOR_STATUS)
    RESULT.append(RESULT_TEMP)

    self.dcload.DC_LOAD_SET_CURRENT_CC(VERIFY_CURRENT_HIGH, load_type)
    time.sleep(3)
    DUT__VERIFY_READ_CURRENT_HIGH = float(
        self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number))) / 10
    METER__VERIFY_READ_CURRENT_HIGH = float(READ_DC_CURRENT(load_type)) + BATT_CHARGE_CURRENT_COMPENSATION
    RESULT_TEMP = (abs(DUT__VERIFY_READ_CURRENT_HIGH - METER__VERIFY_READ_CURRENT_HIGH) < CURRENT_TOLERANCE and (
            abs(METER__VERIFY_READ_CURRENT_HIGH - VERIFY_CURRENT_HIGH) < 3))
    if RESULT_TEMP == False:
        COLOR_STATUS = "RED"
    else:
        COLOR_STATUS = 'BLUE'
    self.print_console("CH :" + str(channel_number) + " CURRENT_TOLERANCE: " + str(CURRENT_TOLERANCE), COLOR_STATUS)
    self.print_console(
        "CH :" + str(channel_number) + " METER__VERIFY_READ_CURRENT_HIGH: " + str(METER__VERIFY_READ_CURRENT_HIGH),
        COLOR_STATUS)
    self.print_console(
        "CH :" + str(channel_number) + " DUT__VERIFY_READ_CURRENT_HIGH: " + str(DUT__VERIFY_READ_CURRENT_HIGH),
        COLOR_STATUS)
    RESULT.append(RESULT_TEMP)
    # PRINT_CONSOLE(self,"RESULT: "+str(RESULT))
    self.dcload.DC_LOAD_SET_CURRENT_CC(10, "LOAD")
    self.dcload.DC_LOAD_SET_CURRENT_CC(10, "BATT")
    return CALCULATE_RESULT(RESULT)


def CALIBRATE_CURRENT_PATH_SHUNT(self, channel_number, load_type):
    global check_shunt_value
    if self.mcm_type == 1:
        self.MCM_READ_COMMAND('SYSTEM COMMANDS', 'ate test', 'TEST_M1000_ATE')
    RESULT = []
    self.smrcan.SMR_BATTERY_SET_VOLTAGE(53.5)
    if (self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' gain') != '0') or (
            self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(
                channel_number) + ' offset') != '0'):  # or (TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' deadband'])!='0'):
        self.print_console("Resetting offset and gain again")
        self.MCM_WRITE_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' deadband', 0)
        time.sleep(2)
        self.MCM_WRITE_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' gain', 0)
        time.sleep(2)
        self.MCM_WRITE_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' offset', 0)
        time.sleep(2)
        self.print_console("CURRENT CHANNEL " + str(channel_number) + " GAIN: " + str(
            self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' gain')))
        self.print_console("CURRENT CHANNEL " + str(channel_number) + " OFFSET: " + str(
            self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' offset')))
        # PRINT_CONSOLE(self,"CURRENT CHANNEL "+str(channel_number)+" DEADBAND: "+str(TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' deadband'])))

    channel_shunt_value = int(ConfigRead('DUT CONFIGURATION')['channel' + str(channel_number) + ' shunt value'])
    print("channel shunt value: " + str(channel_shunt_value))
    # SET_CURRENT_LOW=int(CalibrateRead('SHUNT')['current low'])
    # SET_CURRENT_HIGH=int(CalibrateRead('SHUNT')['current high'])
    NUMBER_OF_BITS = int(CalibrateSetting('SHUNT')['number of bits'])
    FACTOR = float(CalibrateSetting('SHUNT')['factor'])
    ADC_MULTIPLIER = int(CalibrateSetting('SHUNT')['adc multiplier'])
    DEADBAND_PERCENTAGE = float(CalibrateSetting('SHUNT')['deadband percentage'])
    DEADBAND = int(channel_shunt_value * DEADBAND_PERCENTAGE) / 100
    CURRENT_TOLERANCE_PERCENTAGE = float(CalibrateSetting('SHUNT')['current tolerance percentage'])
    CURRENT_TOLERANCE = float(channel_shunt_value * CURRENT_TOLERANCE_PERCENTAGE) / 100
    NEGATIVE_CURRENT_CAL = str(CalibrateSetting('SHUNT')['negative current cal'])

    if channel_shunt_value <= 50:
        check_shunt_value = 50
    elif 100 >= channel_shunt_value > 50:
        check_shunt_value = 100
    elif 200 >= channel_shunt_value > 100:
        check_shunt_value = 200
    elif 400 >= channel_shunt_value > 200:
        check_shunt_value = 400
    elif 600 >= channel_shunt_value > 400:
        check_shunt_value = 600
    elif 800 >= channel_shunt_value > 600:
        check_shunt_value = 800
    elif 1000 >= channel_shunt_value > 800:
        check_shunt_value = 1000
    elif 1200 >= channel_shunt_value > 1000:
        check_shunt_value = 1200
    elif 2100 >= channel_shunt_value > 1900:
        check_shunt_value = 2100

    SET_CURRENT_LOW = int(CalibrateSetting('SHUNT')['current low upto ' + str(check_shunt_value)])
    SET_CURRENT_HIGH = int(CalibrateSetting('SHUNT')['current high upto ' + str(check_shunt_value)])
    VERIFY_CURRENT_LOW = int(CalibrateSetting('SHUNT')['verify current low upto ' + str(check_shunt_value)])
    VERIFY_CURRENT_MID = int(CalibrateSetting('SHUNT')['verify current mid upto ' + str(check_shunt_value)])
    VERIFY_CURRENT_HIGH = int(CalibrateSetting('SHUNT')['verify current high upto ' + str(check_shunt_value)])
    NEGATIVE_SET_CURRENT_LOW = int(CalibrateSetting('SHUNT')['negative current low upto ' + str(check_shunt_value)])

    if load_type == 'BATT' and NEGATIVE_CURRENT_CAL == 'YES':
        if ATE_LOAD_COUNT == 1:  # ADDED FOR SINGLE LOAD CONFIGURATION, KUSHAGRA MITTAL 06/09/2016
            # self.pfc.pfc_set(0, 'DC LOAD', 0)
            self.pfc.pfc_set(0, 'load_mains', 1)
            time.sleep(3)

        self.MCM_WRITE_COMMAND('BATTERY SETTING', 'float voltage', 51)
        self.MCM_WRITE_COMMAND('BATTERY SETTING', 'charge voltage', 51.5)
        self.MCM_WRITE_COMMAND('BATTERY SETTING', 'lion charge voltage', 51)
        # SET_JIG_PFC_OP(self.can,'AC',0)

        self.dcload.DC_LOAD_SET_CURRENT_CC(NEGATIVE_SET_CURRENT_LOW, "LOAD")
        time.sleep(4)

        METER_READ_CURRENT_LOW = float(READ_DC_CURRENT(LOAD))
        METER_READ_CURRENT_LOW = (-1 * METER_READ_CURRENT_LOW) - float(
            CalibrateSetting('SHUNT')['batt discharge compensation'])
    else:
        if ATE_LOAD_COUNT == 1 and load_type == 'BATT':
            self.print_console("RESETTING FOR BATTERY PATH")
            # ADDED FOR SINGLE LOAD CONFIGURATION, KUSHAGRA MITTAL 06/09/2016
            # self.pfc.pfc_set(0, 'LOAD COMMON', 0)
            self.pfc.pfc_set(0, 'load_mains', 1)
            time.sleep(3)
        self.dcload.DC_LOAD_SET_CURRENT_CC(SET_CURRENT_LOW, load_type)
        time.sleep(4)
        METER_READ_CURRENT_LOW = float(READ_DC_CURRENT(load_type))

    DUT_READ_CURRENT_LOW = float(self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number)))
    BATT_CHARGE_CURRENT_COMPENSATION = 0
    self.print_console("CH :" + str(channel_number) + " DUT LOW: " + str(DUT_READ_CURRENT_LOW))
    self.print_console("CH :" + str(channel_number) + " METER LOW: " + str(METER_READ_CURRENT_LOW))
    if load_type == 'BATT' and NEGATIVE_CURRENT_CAL == 'YES':
        self.dcload.DC_LOAD_SET_CURRENT_CC(5, "LOAD")
        self.dcload.DC_LOAD_SET_CURRENT_CC(5, "BATT")
        if ATE_LOAD_COUNT == 1:  # ADDED FOR SINGLE LOAD CONFIGURATION, KUSHAGRA MITTAL 06/09/2016
            # self.pfc.pfc_set(0, 'LOAD COMMON', 0)
            self.pfc.pfc_set(0, 'load_mains', 1)
            time.sleep(3)

        self.MCM_WRITE_COMMAND('BATTERY SETTING', 'charge voltage', 55.2)
        self.MCM_WRITE_COMMAND('BATTERY SETTING', 'float voltage', 54)
        self.MCM_WRITE_COMMAND('BATTERY SETTING', 'lion charge voltage', 54)

        time.sleep(10)
        self.smrcan.SMR_BATTERY_SET_VOLTAGE(47.0)

        # SET_JIG_PFC_OP(self.can,'AC',1)
        BATT_CHARGE_CURRENT_COMPENSATION = float(CalibrateSetting('SHUNT')['batt charge compensation'])
        # time.sleep(2)
    # time.sleep(5)

    if ATE_LOAD_COUNT == 1:  # ADDED FOR SINGLE LOAD CONFIGURATION, KUSHAGRA MITTAL 06/09/2016
        load_type = "LOAD"

    DC_LOAD_SET_CURRENT_CC(self.dcload, SET_CURRENT_HIGH, load_type)

    time.sleep(4)
    DUT_READ_CURRENT_HIGH = float(self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number)))
    METER_READ_CURRENT_HIGH = float(READ_DC_CURRENT(load_type)) + BATT_CHARGE_CURRENT_COMPENSATION
    self.print_console("CH :" + str(channel_number) + " DUT HIGH: " + str(DUT_READ_CURRENT_HIGH))
    self.print_console("CH :" + str(channel_number) + " METER HIGH: " + str(METER_READ_CURRENT_HIGH))
    self.dcload.DC_LOAD_SET_CURRENT_CC(SET_CURRENT_LOW, load_type)

    try:
        SLOPE = ((DUT_READ_CURRENT_HIGH - DUT_READ_CURRENT_LOW) / (
                METER_READ_CURRENT_HIGH - METER_READ_CURRENT_LOW)) * (
                        float(NUMBER_OF_BITS) / (channel_shunt_value * FACTOR))
        self.print_console("CH :" + str(channel_number) + " SLOPE: " + str(SLOPE))
        Z_OFFSET = ((DUT_READ_CURRENT_HIGH * NUMBER_OF_BITS) / (
                channel_shunt_value * FACTOR)) - SLOPE * METER_READ_CURRENT_HIGH
        self.print_console("CH :" + str(channel_number) + " Z_OFFSET: " + str(Z_OFFSET))
        GAIN_OFFSET = (FACTOR * channel_shunt_value * (((METER_READ_CURRENT_HIGH - METER_READ_CURRENT_LOW) / (
                DUT_READ_CURRENT_HIGH - DUT_READ_CURRENT_LOW)) - 1)) / 1
        GAIN_OFFSET = round(GAIN_OFFSET, 0)
        self.print_console("CH :" + str(channel_number) + " GAIN OFFSET: " + str(GAIN_OFFSET))
        ZERO_OFFSET = -1 * ADC_MULTIPLIER * Z_OFFSET / SLOPE
        ZERO_OFFSET = round(ZERO_OFFSET, 0)
        self.print_console("CH :" + str(channel_number) + " ZERO OFFSET: " + str(ZERO_OFFSET))
    except:
        SLOPE = 0
        Z_OFFSET = 0
        GAIN_OFFSET = 0
        ZERO_OFFSET = 0
        self.print_console("EXCEPTION OCCURRED.TEST FAILED.CALIBRATION WILL BE DONE AGAIN")
        self.print_console("CH :" + str(channel_number) + " SLOPE: " + str(SLOPE))
        self.print_console("CH :" + str(channel_number) + " Z_OFFSET: " + str(Z_OFFSET))
        self.print_console("CH :" + str(channel_number) + " GAIN OFFSET: " + str(GAIN_OFFSET))
        self.print_console("CH :" + str(channel_number) + " ZERO OFFSET: " + str(ZERO_OFFSET))

    CALIBRATION_NOT_DONE = True
    cal_try_count = 0
    while CALIBRATION_NOT_DONE and cal_try_count < 5:
        cal_try_count = cal_try_count + 1
        self.MCM_WRITE_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' gain', GAIN_OFFSET)
        time.sleep(2)
        self.MCM_WRITE_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' offset', ZERO_OFFSET)
        time.sleep(2)
        self.MCM_WRITE_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' deadband', DEADBAND)
        time.sleep(2)
        if (float(self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' gain')) != GAIN_OFFSET) \
                or (float(
            self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' offset')) != ZERO_OFFSET) \
                or (self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' deadband') != str(
            DEADBAND)):
            CALIBRATION_NOT_DONE = True
        else:
            CALIBRATION_NOT_DONE = False

    #     TELNET_SET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' gain'],GAIN_OFFSET)
    #     time.sleep(1)
    #     TELNET_SET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' offset'],ZERO_OFFSET)
    #     time.sleep(1)
    #     TELNET_SET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' deadband'],DEADBAND)
    #     time.sleep(1)
    self.print_console("PROGRAMMED CURRENT CHANNEL " + str(channel_number) + " GAIN: " + str(
        self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' gain')))
    self.print_console("PROGRAMMED CURRENT CHANNEL " + str(channel_number) + " OFFSET: " + str(
        self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' offset')))
    self.print_console("PROGRAMMED CURRENT CHANNEL " + str(channel_number) + " DEADBAND: " + str(
        self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' deadband')))

    ## verify current calibration
    self.dcload.DC_LOAD_SET_CURRENT_CC(VERIFY_CURRENT_LOW, load_type)
    time.sleep(3)
    DUT__VERIFY_READ_CURRENT_LOW = float(self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number)))
    METER__VERIFY_READ_CURRENT_LOW = float(READ_DC_CURRENT(load_type)) + BATT_CHARGE_CURRENT_COMPENSATION
    RESULT_TEMP = (abs(DUT__VERIFY_READ_CURRENT_LOW - METER__VERIFY_READ_CURRENT_LOW) < CURRENT_TOLERANCE and (
            abs(METER__VERIFY_READ_CURRENT_LOW - VERIFY_CURRENT_LOW) < 3))
    if RESULT_TEMP == False:
        COLOR_STATUS = "RED"
    else:
        COLOR_STATUS = 'BLUE'
    self.print_console("CH :" + str(channel_number) + " CURRENT_TOLERANCE: " + str(CURRENT_TOLERANCE), COLOR_STATUS)
    self.print_console("CH :" + str(channel_number) + " METER__VERIFY_READ_CURRENT_LOW: " + str(
        METER__VERIFY_READ_CURRENT_LOW), COLOR_STATUS)
    self.print_console(
        "CH :" + str(channel_number) + " DUT__VERIFY_READ_CURRENT_LOW: " + str(DUT__VERIFY_READ_CURRENT_LOW),
        COLOR_STATUS)
    RESULT.append(RESULT_TEMP)

    self.dcload.DC_LOAD_SET_CURRENT_CC(VERIFY_CURRENT_MID, load_type)
    time.sleep(3)
    DUT__VERIFY_READ_CURRENT_MID = float(self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number)))
    METER__VERIFY_READ_CURRENT_MID = float(READ_DC_CURRENT(load_type)) + BATT_CHARGE_CURRENT_COMPENSATION
    RESULT_TEMP = (abs(DUT__VERIFY_READ_CURRENT_MID - METER__VERIFY_READ_CURRENT_MID) < CURRENT_TOLERANCE and (
            abs(METER__VERIFY_READ_CURRENT_MID - VERIFY_CURRENT_MID) < 3))
    if RESULT_TEMP == False:
        COLOR_STATUS = "RED"
    else:
        COLOR_STATUS = 'BLUE'
    self.print_console("CH :" + str(channel_number) + " CURRENT_TOLERANCE: " + str(CURRENT_TOLERANCE), COLOR_STATUS)
    self.print_console(
        "CH :" + str(channel_number) + " METER__VERIFY_READ_CURRENT_MID: " + str(METER__VERIFY_READ_CURRENT_MID),
        COLOR_STATUS)
    self.print_console(
        "CH :" + str(channel_number) + " DUT__VERIFY_READ_CURRENT_MID: " + str(DUT__VERIFY_READ_CURRENT_MID),
        COLOR_STATUS)
    RESULT.append(RESULT_TEMP)

    self.dcload.DC_LOAD_SET_CURRENT_CC(VERIFY_CURRENT_HIGH, load_type)
    time.sleep(3)
    DUT__VERIFY_READ_CURRENT_HIGH = float(self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number)))
    METER__VERIFY_READ_CURRENT_HIGH = float(READ_DC_CURRENT(load_type)) + BATT_CHARGE_CURRENT_COMPENSATION
    RESULT_TEMP = (abs(DUT__VERIFY_READ_CURRENT_HIGH - METER__VERIFY_READ_CURRENT_HIGH) < CURRENT_TOLERANCE and (
            abs(METER__VERIFY_READ_CURRENT_HIGH - VERIFY_CURRENT_HIGH) < 3))
    if RESULT_TEMP == False:
        COLOR_STATUS = "RED"
    else:
        COLOR_STATUS = 'BLUE'
    self.print_console("CH :" + str(channel_number) + " CURRENT_TOLERANCE: " + str(CURRENT_TOLERANCE), COLOR_STATUS)
    self.print_console("CH :" + str(channel_number) + " METER__VERIFY_READ_CURRENT_HIGH: " + str(
        METER__VERIFY_READ_CURRENT_HIGH), COLOR_STATUS)
    self.print_console("CH :" + str(channel_number) + " DUT__VERIFY_READ_CURRENT_HIGH: " + str(
        DUT__VERIFY_READ_CURRENT_HIGH), COLOR_STATUS)
    RESULT.append(RESULT_TEMP)
    # PRINT_CONSOLE(self,"RESULT: "+str(RESULT))
    self.dcload.DC_LOAD_SET_CURRENT_CC(10, "LOAD")
    self.dcload.DC_LOAD_SET_CURRENT_CC(10, "BATT")
    return CALCULATE_RESULT(RESULT)


def CALIBRATE_CURRENT_PATH_SHUNT_SMALL(self, channel_number, load_type):
    global check_shunt_value
    if self.mcm_type == 1:
        self.MCM_WRITE_COMMAND('SYSTEM COMMANDS', 'ate test', "TEST_M1000_ATE")
    RESULT = []
    self.smrcan.SMR_BATTERY_SET_VOLTAGE(48.5)
    dcif_type_number = int(ConfigRead('DUT CONFIGURATION')['dcif card type number'])
    load_current_count = int(ConfigRead('DUT CONFIGURATION')['no. of load current'])
    #     if (TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' gain'])!='0') or (TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' offset'])!='0'):# or (TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' deadband'])!='0'):
    #         PRINT_CONSOLE(self,"Resetting offset and gain again")
    #         TELNET_SET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' deadband'],0)
    #         time.sleep(2)
    #         TELNET_SET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' gain'],0)
    #         time.sleep(2)
    #         TELNET_SET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' offset'],0)
    #         time.sleep(2)
    #         PRINT_CONSOLE(self,"CURRENT CHANNEL "+str(channel_number)+" GAIN: "+str(TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' gain'])))
    #         PRINT_CONSOLE(self,"CURRENT CHANNEL "+str(channel_number)+" OFFSET: "+str(TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' offset'])))
    #         #PRINT_CONSOLE(self,"CURRENT CHANNEL "+str(channel_number)+" DEADBAND: "+str(TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' deadband'])))
    #
    #
    channel_shunt_value = int(ConfigRead('DUT CONFIGURATION')['channel' + str(channel_number) + ' shunt value'])
    # print
    # "channel shunt value: " + str(channel_shunt_value)

    #     NUMBER_OF_BITS=int(CalibrateRead('SHUNT')['number of bits'])
    #     FACTOR=float(CalibrateRead('SHUNT')['factor'])
    #     ADC_MULTIPLIER=int(CalibrateRead('SHUNT')['adc multiplier'])
    DEADBAND_PERCENTAGE = float(CalibrateSetting('SHUNT')['deadband percentage'])
    DEADBAND = (int(channel_shunt_value * DEADBAND_PERCENTAGE) / 100) * 10
    CURRENT_TOLERANCE_PERCENTAGE = float(CalibrateSetting('SHUNT')['current tolerance percentage'])
    CURRENT_TOLERANCE = float(channel_shunt_value * CURRENT_TOLERANCE_PERCENTAGE) / 100
    NEGATIVE_CURRENT_CAL = str(CalibrateSetting('SHUNT')['negative current cal'])

    if channel_shunt_value <= 50:
        check_shunt_value = 50
    elif 100 >= channel_shunt_value > 50:
        check_shunt_value = 100
    elif 200 >= channel_shunt_value > 100:
        check_shunt_value = 200
    elif 400 >= channel_shunt_value > 200:
        check_shunt_value = 400
    elif 600 >= channel_shunt_value > 400:
        check_shunt_value = 600
    elif 800 >= channel_shunt_value > 600:
        check_shunt_value = 800
    elif 1000 >= channel_shunt_value > 800:
        check_shunt_value = 1000
    elif 1200 >= channel_shunt_value > 1000:
        check_shunt_value = 1200
    elif 2100 >= channel_shunt_value > 1900:
        check_shunt_value = 2100

    # print
    # "check_shunt_value: " + str(check_shunt_value)
    SET_CURRENT_LOW = int(CalibrateSetting('SHUNT')['current low upto ' + str(check_shunt_value)])
    SET_CURRENT_HIGH = int(CalibrateSetting('SHUNT')['current high upto ' + str(check_shunt_value)])
    VERIFY_CURRENT_LOW = int(CalibrateSetting('SHUNT')['verify current low upto ' + str(check_shunt_value)])
    VERIFY_CURRENT_MID = int(CalibrateSetting('SHUNT')['verify current mid upto ' + str(check_shunt_value)])
    VERIFY_CURRENT_HIGH = int(CalibrateSetting('SHUNT')['verify current high upto ' + str(check_shunt_value)])
    NEGATIVE_SET_CURRENT_LOW = int(CalibrateSetting('SHUNT')['negative current low upto ' + str(check_shunt_value)])
    #
    #
    #     if load_type=='BATT' and NEGATIVE_CURRENT_CAL=='YES':
    #         if ATE_LOAD_COUNT==1: # ADDED FOR SINGLE LOAD CONFIGURATION, KUSHAGRA MITTAL 06/09/2016
    #             SET_JIG_PFC_OP(self.can,'DC LOAD',0)
    #             SET_JIG_PFC_OP(self.can,'LOAD COMMON',1)
    #             time.sleep(3)
    #
    #         TELNET_SET_COMMAND(self.telnet,OIDRead('BATTERY SETTING')['float voltage'],51)
    #         TELNET_SET_COMMAND(self.telnet,OIDRead('BATTERY SETTING')['charge voltage'],51.5)
    #         TELNET_SET_COMMAND(self.telnet,OIDRead('BATTERY SETTING')['lion charge voltage'],51)
    #         #SET_JIG_PFC_OP(self.can,'AC',0)
    #
    #         DC_LOAD_SET_CURRENT_CC(self.dcload,NEGATIVE_SET_CURRENT_LOW,LOAD)
    #         time.sleep(4)
    #
    #         METER_READ_CURRENT_LOW=float(READ_DC_CURRENT(self,LOAD))
    #         METER_READ_CURRENT_LOW=(-1*METER_READ_CURRENT_LOW)-float(CalibrateRead('SHUNT')['batt discharge compensation'])
    #     else:
    #         DC_LOAD_SET_CURRENT_CC(self.dcload,SET_CURRENT_LOW,load_type)
    #         time.sleep(4)
    #         METER_READ_CURRENT_LOW=float(READ_DC_CURRENT(self,load_type))
    #
    #     DUT_READ_CURRENT_LOW=float(TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)]))
    #     BATT_CHARGE_CURRENT_COMPENSATION=0
    #     PRINT_CONSOLE(self,"CH :"+str(channel_number)+" DUT LOW: "+str(DUT_READ_CURRENT_LOW))
    #     PRINT_CONSOLE(self,"CH :"+str(channel_number)+" METER LOW: "+str(METER_READ_CURRENT_LOW))
    #     if load_type=='BATT' and NEGATIVE_CURRENT_CAL=='YES':
    #         DC_LOAD_SET_CURRENT_CC(self.dcload,5,LOAD)
    #         DC_LOAD_SET_CURRENT_CC(self.dcload,5,BATT)
    test_load_type = 'LOAD'
    if ATE_LOAD_COUNT == 1 and load_type == 'BATT':
        self.print_console("RESETTING FOR BATTERY PATH")
        # ADDED FOR SINGLE LOAD CONFIGURATION, KUSHAGRA MITTAL 06/09/2016
        # self.pfc.pfc_set(0, 'LOAD COMMON', 0)
        self.pfc.pfc_set(0, 'load_mains', 1)
        time.sleep(3)
        test_load_type = 'BATT'
    #
    #         TELNET_SET_COMMAND(self.telnet,OIDRead('BATTERY SETTING')['charge voltage'],55.2)
    #         TELNET_SET_COMMAND(self.telnet,OIDRead('BATTERY SETTING')['float voltage'],54)
    #         TELNET_SET_COMMAND(self.telnet,OIDRead('BATTERY SETTING')['lion charge voltage'],54)
    #
    #         time.sleep(10)
    #         SMR_BATTERY_SET_VOLTAGE(self.can,47.0)
    #
    #         #SET_JIG_PFC_OP(self.can,'AC',1)
    # BATT_CHARGE_CURRENT_COMPENSATION=float(CalibrateRead('SHUNT')['batt charge compensation'])
    #         #time.sleep(2)
    #     #time.sleep(5)
    #
    if ATE_LOAD_COUNT == 1:  # ADDED FOR SINGLE LOAD CONFIGURATION, KUSHAGRA MITTAL 06/09/2016
        load_type = "LOAD"
    #
    #     DC_LOAD_SET_CURRENT_CC(self.dcload,SET_CURRENT_HIGH,load_type)
    #
    #     time.sleep(4)
    #     DUT_READ_CURRENT_HIGH=float(TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)]))
    #     METER_READ_CURRENT_HIGH=float(READ_DC_CURRENT(self,load_type))+BATT_CHARGE_CURRENT_COMPENSATION
    #     PRINT_CONSOLE(self,"CH :"+str(channel_number)+" DUT HIGH: "+str(DUT_READ_CURRENT_HIGH))
    #     PRINT_CONSOLE(self,"CH :"+str(channel_number)+" METER HIGH: "+str(METER_READ_CURRENT_HIGH))
    #     DC_LOAD_SET_CURRENT_CC(self.dcload,SET_CURRENT_LOW,load_type)
    #
    #     try:
    #         #SLOPE=((DUT_READ_CURRENT_HIGH-DUT_READ_CURRENT_LOW)/(METER_READ_CURRENT_HIGH-METER_READ_CURRENT_LOW))*(float(NUMBER_OF_BITS)/(channel_shunt_value*FACTOR))
    #         PRINT_CONSOLE(self,"CH :"+str(channel_number)+" SLOPE: "+str(SLOPE))
    #         #Z_OFFSET=((DUT_READ_CURRENT_HIGH*NUMBER_OF_BITS)/(channel_shunt_value*FACTOR))-SLOPE*METER_READ_CURRENT_HIGH
    #         PRINT_CONSOLE(self,"CH :"+str(channel_number)+" Z_OFFSET: "+str(Z_OFFSET))
    #         GAIN_OFFSET=(METER_READ_CURRENT_HIGH-METER_READ_CURRENT_LOW)/(DUT_READ_CURRENT_HIGH-DUT_READ_CURRENT_LOW)
    #         CAL_GAIN_OFFSET=int((GAIN_OFFSET-1)*1000)
    #         PRINT_CONSOLE(self,"CH :"+str(channel_number)+" CAL_GAIN_OFFSET: "+str(CAL_GAIN_OFFSET))
    #         ZERO_OFFSET=DUT_READ_CURRENT_LOW-(DUT_READ_CURRENT_LOW *(METER_READ_CURRENT_HIGH-METER_READ_CURRENT_LOW)/(DUT_READ_CURRENT_HIGH-DUT_READ_CURRENT_LOW) )
    #         CAL_ZERO_OFFSET=int(ZERO_OFFSET*100)
    #         PRINT_CONSOLE(self,"CH :"+str(channel_number)+" CAL_ZERO_OFFSET: "+str(CAL_ZERO_OFFSET))
    #     except:
    #         GAIN_OFFSET=0
    #         ZERO_OFFSET=0
    #         CAL_GAIN_OFFSET=0
    #         CAL_ZERO_OFFSET=0
    #

    #         PRINT_CONSOLE(self,"EXCEPTION OCCURRED.TEST FAILED.CALIBRATION WILL BE DONE AGAIN")
    #         PRINT_CONSOLE(self,"CH :"+str(channel_number)+" GAIN_OFFSET: "+str(GAIN_OFFSET))
    #         PRINT_CONSOLE(self,"CH :"+str(channel_number)+" ZERO_OFFSET: "+str(ZERO_OFFSET))
    #         PRINT_CONSOLE(self,"CH :"+str(channel_number)+" CAL_GAIN_OFFSET: "+str(CAL_GAIN_OFFSET))
    #         PRINT_CONSOLE(self,"CH :"+str(channel_number)+" CAL_ZERO_OFFSET: "+str(CAL_ZERO_OFFSET))
    #
    CALIBRATION_NOT_DONE = True
    cal_try_count = 0
    while CALIBRATION_NOT_DONE and cal_try_count < 5:
        cal_try_count = cal_try_count + 1
        #         TELNET_SET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' gain'],GAIN_OFFSET)
        #         time.sleep(2)
        #         TELNET_SET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' offset'],ZERO_OFFSET)
        #         time.sleep(2)
        self.MCM_WRITE_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' deadband', DEADBAND)
        time.sleep(2)
        # if (float(TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' gain']))!=GAIN_OFFSET) or (float(TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' offset']))!=ZERO_OFFSET) or (TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' deadband'])!=str(DEADBAND)):
        if self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' deadband') != str(DEADBAND):
            CALIBRATION_NOT_DONE = True
        else:
            CALIBRATION_NOT_DONE = False

    #     TELNET_SET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' gain'],GAIN_OFFSET)
    #     time.sleep(1)
    #     TELNET_SET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' offset'],ZERO_OFFSET)
    #     time.sleep(1)
    #     TELNET_SET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' deadband'],DEADBAND)
    #     time.sleep(1)
    # PRINT_CONSOLE(self,"PROGRAMMED CURRENT CHANNEL "+str(channel_number)+" GAIN: "+str(TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' gain'])))
    # PRINT_CONSOLE(self,"PROGRAMMED CURRENT CHANNEL "+str(channel_number)+" OFFSET: "+str(TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)+' offset'])))
    self.print_console("PROGRAMMED CURRENT CHANNEL " + str(channel_number) + " DEADBAND: " + str(
        self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number) + ' deadband')))
    ## verify current calibration
    #     DC_LOAD_SET_CURRENT_CC(self.dcload,VERIFY_CURRENT_LOW,load_type)
    #     time.sleep(6)
    #     DUT__VERIFY_READ_CURRENT_LOW=float(TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)]))/10
    #     METER__VERIFY_READ_CURRENT_LOW=float(READ_DC_CURRENT(self,load_type))#+BATT_CHARGE_CURRENT_COMPENSATION
    #     RESULT_TEMP=COMPARE(DUT__VERIFY_READ_CURRENT_LOW, METER__VERIFY_READ_CURRENT_LOW,CURRENT_TOLERANCE )
    #     if RESULT_TEMP==False:
    #         COLOR_STATUS=WARNING
    #     else:
    #         COLOR_STATUS='BLUE'
    #     PRINT_CONSOLE(self,"CH :"+str(channel_number)+" CURRENT_TOLERANCE: "+str(CURRENT_TOLERANCE),COLOR_STATUS)
    #     PRINT_CONSOLE(self,"CH :"+str(channel_number)+" METER__VERIFY_READ_CURRENT_LOW: "+str(METER__VERIFY_READ_CURRENT_LOW),COLOR_STATUS)
    #     PRINT_CONSOLE(self,"CH :"+str(channel_number)+" DUT__VERIFY_READ_CURRENT_LOW: "+str(DUT__VERIFY_READ_CURRENT_LOW),COLOR_STATUS)
    #     RESULT.append(RESULT_TEMP)
    #
    #     DC_LOAD_SET_CURRENT_CC(self.dcload,VERIFY_CURRENT_MID,load_type)
    #     time.sleep(6)
    #     DUT__VERIFY_READ_CURRENT_MID=float(TELNET_GET_COMMAND(self.telnet,OIDRead('CALIBRATE CURRENT')['channel'+str(channel_number)]))/10
    #     METER__VERIFY_READ_CURRENT_MID=float(READ_DC_CURRENT(self,load_type))#+BATT_CHARGE_CURRENT_COMPENSATION
    #     RESULT_TEMP=COMPARE(DUT__VERIFY_READ_CURRENT_MID, METER__VERIFY_READ_CURRENT_MID,CURRENT_TOLERANCE )
    #     if RESULT_TEMP==False:
    #         COLOR_STATUS=WARNING
    #     else:
    #         COLOR_STATUS='BLUE'
    #     PRINT_CONSOLE(self,"CH :"+str(channel_number)+" CURRENT_TOLERANCE: "+str(CURRENT_TOLERANCE),COLOR_STATUS)
    #     PRINT_CONSOLE(self,"CH :"+str(channel_number)+" METER__VERIFY_READ_CURRENT_MID: "+str(METER__VERIFY_READ_CURRENT_MID),COLOR_STATUS)
    #     PRINT_CONSOLE(self,"CH :"+str(channel_number)+" DUT__VERIFY_READ_CURRENT_MID: "+str(DUT__VERIFY_READ_CURRENT_MID),COLOR_STATUS)
    #     RESULT.append(RESULT_TEMP)

    self.dcload.DC_LOAD_SET_CURRENT_CC(VERIFY_CURRENT_HIGH, load_type)
    time.sleep(6)
    if dcif_type_number == 3:
        if test_load_type == 'BATT':
            temp_channel_count = 4 - load_current_count  ## added for DCIO channel selection, 03052019
            channel_number = channel_number + temp_channel_count
        DUT__VERIFY_READ_CURRENT_HIGH = float(
            self.MCM_READ_COMMAND('CALIBRATE CURRENT DCIO', 'channel' + str(channel_number)))
    else:
        DUT__VERIFY_READ_CURRENT_HIGH = float(
            self.MCM_READ_COMMAND('CALIBRATE CURRENT', 'channel' + str(channel_number))) / 10
    METER__VERIFY_READ_CURRENT_HIGH = float(READ_DC_CURRENT(load_type))  # +BATT_CHARGE_CURRENT_COMPENSATION
    RESULT_TEMP = (abs(DUT__VERIFY_READ_CURRENT_HIGH - METER__VERIFY_READ_CURRENT_HIGH) < CURRENT_TOLERANCE and (
            abs(METER__VERIFY_READ_CURRENT_HIGH - VERIFY_CURRENT_HIGH) < 3))
    if RESULT_TEMP == False:
        COLOR_STATUS = "RED"
    else:
        COLOR_STATUS = 'BLUE'
    self.print_console("CH :" + str(channel_number) + " CURRENT_TOLERANCE: " + str(CURRENT_TOLERANCE), COLOR_STATUS)
    self.print_console(
        "CH :" + str(channel_number) + " METER__VERIFY_READ_CURRENT_HIGH: " + str(METER__VERIFY_READ_CURRENT_HIGH),
        COLOR_STATUS)
    self.print_console(
        "CH :" + str(channel_number) + " DUT__VERIFY_READ_CURRENT_HIGH: " + str(DUT__VERIFY_READ_CURRENT_HIGH),
        COLOR_STATUS)
    RESULT.append(RESULT_TEMP)
    # PRINT_CONSOLE(self,"RESULT: "+str(RESULT))
    self.dcload.DC_LOAD_SET_CURRENT_CC(10, "LOAD")
    self.dcload.DC_LOAD_SET_CURRENT_CC(10, "BATT")
    if ATE_LOAD_COUNT == 1:
        # ADDED FOR SINGLE LOAD CONFIGURATION, KUSHAGRA MITTAL 06/09/2016
        self.print_console("RESETTING FOR LOAD PATH")
        self.pfc.pfc_set(0, 'load_mains', 1)
        # self.pfc.pfc_set(0, 'DC LOAD', 0)
        time.sleep(3)
    return CALCULATE_RESULT(RESULT)


def CALCULATE_RESULT(RESULT):
    for RESULT_TEMP in RESULT:
        if RESULT_TEMP == False:
            return False
    return True


def AVG_METER_VOLTAGE(self, load_type):
    sum = 0
    for i in range(0, 5):
        actual_voltage = float(CommandSetDcLoadUsb.DC_LOAD_READ_OUTPUT_VOLTAGE(self, load_type))
        sum += actual_voltage

    return float(sum) / 5


def SET_INDI_BATTERY_PATH(battery_number):
    batt_fuse_count = int(ConfigRead('DUT CONFIGURATION')['no. of battery fuses'])
    # PRINT_CONSOLE(self,"batt fuse: "+str(batt_fuse_count))
    for count in range(1, batt_fuse_count + 1):
        if count == battery_number:
            self.pfc.pfc_set(0, 'BATT' + str(count), 1)

    for count in range(1, batt_fuse_count + 1):
        if count != battery_number:
            self.pfc.pfc_set(0, 'BATT' + str(count), 0)


def READ_DC_VOLTAGE(load_type='LOAD'):
    global DATA
    try:

        DATA = CommandSetDcLoadUsb.DC_LOAD_READ_OUTPUT_VOLTAGE(load_type)
        test_data = float(DATA)

    except:
        PRINT_CONSOLE(self, 'ELECTRONIC DC LOAD (' + str(load_type) + ') PATH RESPONDING GARBAGE VOLTAGE VALUES!',
                      WARNING)
        PRINT_CONSOLE(self, 'VALUE IS: ' + str(DATA), WARNING)
        DATA = 999992
        ERROR_PROMPT(self, 'ELECTRONIC DC LOAD (' + str(load_type) + ') PATH RESPONDING GARBAGE VALUES!')
        pass

    return DATA


def SET_LOAD_ISOLATE(self, load_lvd_count, state):
    # PRINT_CONSOLE(self,"set load isolate")
    for i in range(1, load_lvd_count + 1):
        self.MCM_WRITE_COMMAND('LOAD ISOLATE', 'load' + str(i), state)


def READ_DC_CURRENT(load_type='LOAD'):
    global DATA
    try:
        DATA = CommandSetDcLoadUsb.DC_LOAD_READ_OUTPUT_CURRENT(DC_Load, load_type)
        test_data = float(DATA)

    except:
        Ui_Test.print_console(Ui_Test,
                              'ELECTRONIC DC LOAD (' + str(load_type) + ') PATH RESPONDING GARBAGE CURRENT VALUES!',
                              "RED")
        Ui_Test.print_console(Ui_Test, 'VALUE IS: ' + str(DATA), WARNING)
        DATA = 999991
        Prompt.Message(title="ERROR!",
                       prompt='ELECTRONIC DC LOAD (' + str(load_type) + ') PATH RESPONDING GARBAGE VALUES!')
        pass

    return DATA


def InitChromaLoad(dcload, type_load: str):
    dcload.DC_LOAD_READ_COMMAND(id, type_load)
    dcload.DC_LOAD_SET_COMMAND(RESET, type_load)
    dcload.DC_LOAD_SET_COMMAND(set_load_sense, type_load)
    dcload.DC_LOAD_SET_COMMAND(load_ON, type_load)


def ACSET(pfc, phase, state):
    if phase == 1:
        pfc.pfc_set(0, 'r_phase', state)
    elif phase == 3:
        pfc.pfc_set(0, 'r_phase', state)
        pfc.pfc_set(0, 'y_phase', state)
        pfc.pfc_set(0, 'b_phase', state)


def width(value: object) -> object:
    global w, factor
    return int(w * (value / 1366) * factor)


def height(value):
    global h, factor
    return int(h * (value / 768) * factor)


if __name__ == "__main__":
    import sys
    global ate_name
    app = QtWidgets.QApplication(sys.argv)
    ate_name = sys.argv[0].split("\\")[-1].split(".")[0]
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Test()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
