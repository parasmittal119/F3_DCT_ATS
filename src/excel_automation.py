import configparser
import csv
import datetime
import os

import gui_global
# from macpath import split
from config_done import *

config = configparser.ConfigParser()



def get_date_time():
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month)
    if len(month) == 1:
        month = '0' + month
    day = str(now.day)
    if len(day) == 1:
        day = '0' + day
    hour = str(now.hour)
    if len(hour) == 1:
        hour = '0' + hour
    minute = str(now.minute)
    if len(minute) == 1:
        minute = '0' + minute
    second = str(now.second)
    if len(second) == 1:
        second = '0' + second
    time = hour + ":" + minute + ":" + second
    return time


def get_date():
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month)
    if len(month) == 1:
        month = '0' + month
    day = str(now.day)
    if len(day) == 1:
        day = '0' + day
    date = year + '-' + month + '-' + day

    return date


class CSV:
    def __init__(self):
        print("CSV Module")

    def Update_CSV_Test_Item(self, filename, parameter_list=[]):
        if parameter_list == []:
            return None
        new_rows = parameter_list
        # print(new_rows)
        with open(f"{gui_global.directory_location}records/"+filename, 'a', newline="") as file:
            writer = csv.writer(file)
            writer.writerows(new_rows)

    def Update_CSV_Test_Result(self, filename):
        new_rows = []

        with open(filename) as csvfile:

            reader = csv.reader(csvfile)

            for row in reader:
                new_row = row
                if new_row[0] == str(sno):
                    new_row[12] == "YES"
                new_rows.append(new_row)

        with open(filename, "w") as f:
            writer = csv.writer(f)
            writer.writerows(new_rows)


    def Create_CSV(self):
        date = get_date()
        station_id = str(SettingRead("STATION")["id"])
        filename = "active_"+str(station_id)+".csv"
        # print(filename)
        PARAMETERS = "SR NO,CUSTOMER NAME,PART NUMBER,SERIAL NUMBER,CONFIG VERSION,M1000 MAC ID,OPERATOR,TEST DATE,TEST TIME,PHYSICAL TEST,CONTROLLER TEST,COMMUNICATION TEST,TEMPERATURE TEST,OUTPUT/INPUT PFC,DC VOLTAGE TEST,DC VOLTAGE CALIBRATION,DC CURRENT TEST,DC CURRENT CALIBRATION,LVD TEST,SMR REGISTRATION TEST,AC PHASE ALLOCATION TEST,DC CURRENT SHARING/ BUS DROP TEST,RS-485 TEST,DEFAULT SETTING,FLOAT VOLTAGE (VDC),CHARGE VOLTAGE (VDC),BATTERY LVD SET(VDC)/RESTORE(VDC),LOAD LVD SET(VDC)/RESTORE(VDC),DC VOLTAGE LOW(VDC)/RESTORE(VDC),AC LOW CUT-OFF(VAC)/CUT-IN(VAC),AC HIGH CUT-OFF(VAC)/CUT-IN(VAC),SMR COUNT/ SOLAR CHARGER COUNT,VRLA: BATTERY CAPACITY/ FACTOR,LI-ON BATTERY/ FACTOR,RESULT"
        ARR = os.listdir(f"{gui_global.directory_location}records/")
        for file in ARR:
            if file == filename:
                return filename
        detail_file = open(f"{gui_global.directory_location}records/"+filename, 'w')
        # sys.stdout.write(PARAMETERS)
        # sys.stdout.write("\n")
        detail_file.write(PARAMETERS)
        detail_file.write('\n')
        detail_file.close()
        return filename
