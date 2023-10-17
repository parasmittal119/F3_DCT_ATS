import datetime
from config_done import *
from PyQt5 import QtCore, QtGui, QtWidgets
from prompts import Prompt
import test_order_done
test_order = test_order_done.Ui_Form.get_values(test_order_done.Ui_Form)
import time
import os
from excel_automation import CSV
from config_done import *
import ByteConvertor
import CanModule
import CommandDCLoad
import gui_global
from M1000Telnet import *
import M2000
from prompts import Prompt

if SettingRead("SETTING")['ate load comm type'] == "RS232C":
    from CommandDCLoad import *
if SettingRead("SETTING")['ate load comm type'] == "USB" or\
    SettingRead("SETTING")['ate load comm type'] == "GPIB":
    from CommandDCLoad import *

ATE_LOAD_COUNT = int(SettingRead("SETTING")['ate load count'])


def get_date_time(date=0, time=0):
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month)
    day = str(now.day)
    if len(month) == 1:
        month = '0'+month
    if len(day) == 1:
        day = "0" + day
    date_only = day+"-"+month+"-"+year
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


def controller_health_method():
    final_result = []
