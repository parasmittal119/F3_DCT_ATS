import csv
import datetime
import getpass
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
import threading

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel

import data_file
from Hardware_detection import Hardware_check
from config_done import *
from prompts import *

file_data = [data_file.alarmIndex, data_file.calibrate, data_file.config, data_file.default, data_file.filetime,
             data_file.oid,
             data_file.orderedtelnet, data_file.pfcjig, data_file.profile, data_file.RequiredParameter,
             data_file.setting, data_file.smrdetail, data_file.systemversion, data_file.telnetgetcommand,
             data_file.testorder,
             data_file.todo]
list_of_files = ['AlarmIndex.txt', 'calibrate.txt', 'config.ini', 'default.txt', 'filetime.txt', 'oid.txt',
                 'ordered telnet get commands.txt', 'pfcjig.txt', 'profile.txt', 'RequiredParameters.txt',
                 'setting.txt',
                 'smrdetailoid.txt',
                 'systemversion.txt', 'telnetgetcommandparameters.txt', 'test_order.txt', 'tO DO.txt']

'''IMAGES AND SOURCES'''
source_path = [r'\\SLICE\Data_Share_Temp\Paras\about.png', r'\\SLICE\Data_Share_Temp\Paras\exicome logo.png',
               r'\\SLICE\Data_Share_Temp\Paras\logo_1.png', r'\\SLICE\Data_Share_Temp\Paras\logo.png',
               r'\\SLICE\Data_Share_Temp\Paras\report_format_page.jpg']

'''CRC MODULES SOURCES'''
module_source = [r'\\SLICE\\Data_Share_Temp\\Paras\\CRC16.py', r'\\SLICE\\Data_Share_Temp\\Paras\\CRC16DNP.py',
                 r'\\SLICE\\Data_Share_Temp\\Paras\\CRC16Kermit.py', r'\\SLICE\\Data_Share_Temp\\Paras\\CRC16SICK.py',
                 r'\\SLICE\\Data_Share_Temp\\Paras\\CRC32.py', r'\\SLICE\\Data_Share_Temp\\Paras\\CRCCCITT.py',
                 r'\\SLICE\\Data_Share_Temp\\Paras\\__init__.py']

account_user = getpass.getuser()
directory_path = f"C:/Users/{account_user}/AppData/Local/DCT_ATS"


class CircularProgressBar(QWidget):
    def __init__(self, parent=None):

        super().__init__(parent)
        self.progress = 1
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateProgress)
        self.timer.start(20)  # Update every 50 ms
        self.is_running = False

        # Create a label to display in the center
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 20px;")

        # Set the fixed size of the label
        label_width = 330
        label_height = 100
        self.label.setFixedSize(label_width, label_height)

    def toggleProgress(self):
        if self.is_running:
            self.timer.stop()
            self.button.setText("Start")
        else:
            self.timer.start(100)
            self.button.setText("Stop")
        self.is_running = not self.is_running

    def updateProgress(self):
        self.progress += 1
        value_set = 0
        if self.progress > 100:
            self.progress = 0
            self.timer.stop()
            value_set = 1
        self.update()

        # Update the label text with the progress percentage
        self.label.setPixmap(QtGui.QPixmap(f"{gui_global.image_directory_location}exicome logo.png"))
        self.label.setScaledContents(True)
        if value_set == 1:
            self.User_login()
        if value_set == 1:
            self.close()

    def User_login(self):
        if Hardware_check():
            self.login_window = Ui_MainWindow()  # Login()
            self.temp_window = QtWidgets.QWidget()
            self.login_window.setupUi(self.temp_window)
            self.temp_window.setWindowFlags(Qt.FramelessWindowHint)
            self.temp_window.setAttribute(Qt.WA_NoSystemBackground, True)
            self.temp_window.setAttribute(Qt.WA_TranslucentBackground, True)
            self.temp_window.show()
            # self.login_window.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            # self.login_window.setAttribute(Qt.WA_NoSystemBackground, True)
            # self.login_window.setAttribute(Qt.WA_TranslucentBackground, True)
            # self.login_window.center()
            # self.login_window.show()
            self.close()
        else:
            error_list = []
            if gui_global.pfc_status:
                error_list.append("PFCs irregular assigned/ duplicacy found")
            if gui_global.can_status:
                error_list.append("CAN Bus error/ unavailable")
            if gui_global.port_status:
                error_list.append("Port unavailable")
            if gui_global.hardware_status:
                error_list.append("Hardware Settings not valid!")

            Prompt.Message(Prompt, "Hardware Error",
                           "System can't run!, Due to following error(s):\n\n" + str(error_list))

            QApplication.exit()

    def paintEvent(self, event):
        width = int(self.width())
        height = int(self.height())

        # Create a QPainter
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Outer circle
        outer_radius = int(min(width, height) / 2 - 15)
        outer_center = int(width / 2), int(height / 2)
        outer_circle = QColor(50, 50, 50)
        painter.setPen(QPen(outer_circle, 20))
        painter.drawEllipse(outer_center[0] - outer_radius, outer_center[1] - outer_radius, 2 * outer_radius,
                            2 * outer_radius)

        # Inner circle
        inner_radius = int(outer_radius - 15)
        inner_circle = QColor(150, 150, 150)
        painter.setPen(QPen(inner_circle, 10))
        painter.drawEllipse(outer_center[0] - inner_radius, outer_center[1] - inner_radius, 2 * inner_radius,
                            2 * inner_radius)

        # Progress arc
        progress_angle = int(360 * self.progress / 100)
        progress_color = QColor(0, 100, 150)  # Blue color
        painter.setPen(QPen(progress_color, 15))
        painter.drawArc(outer_center[0] - outer_radius, outer_center[1] - outer_radius, 2 * outer_radius,
                        2 * outer_radius, -90 * 16, -progress_angle * 16)

        # Position the label in the center
        label_width = self.label.width()
        label_height = self.label.height()
        self.label.move(int(outer_center[0] - label_width / 2), int(outer_center[1] - label_height / 2))

        if self.progress == 0:
            self.close()


def is_file_empty(file):
    return os.path.getsize(file) == 0


def downloadFunction(url):
    x = 0
    if os.path.exists(os.path.join(gui_global.directory_location + "/images/", url.split("\\")[-1])):
        x = 1
    else:
        shutil.copy(url, directory_path + '/images/')


def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future = executor.map(downloadFunction, source_path)
        x = 0
        for result in future:
            x += 1


def systemSerial():
    cmd = 'wmic bios get serialnumber'
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    # return_code = process.returncode
    serial_number = str(output).split("\\n")[1].split(" ")[0]
    return serial_number


def files_and_values():
    # CHECKING FOR ALL PRESENT DIRECTORIES/ ELSE CREATING THEM
    global return_dict
    account_user = getpass.getuser()  # to get login account INFO

    list_of_dir = ['CRCModules', 'files', 'images', 'logs', 'records', 'reports', 'src',
                   'summary']  # List of DIRECTORY REQUIRED

    directory_path = f"C:/Users/{account_user}/AppData/Local/DCT_ATS"  # MAIN DIRECTORY PATH

    # LOOP FOR ALL DIRECTORY

    for n in list_of_dir:
        # TO CHECK PRESENCE OF DIRECTORY
        if not os.path.exists(os.path.join(directory_path, n)):
            # If it doesn't exist, create the folder
            os.makedirs(os.path.join(directory_path, n))

    # CHECKING FOR ALL FILES/ ELSE CREATING THEM WITH DEFAULT DATA
    for i in range(len(list_of_files)):
        # TO CHECK PRESENCE OF FILES
        if os.path.exists(os.path.join(directory_path + "/files/", list_of_files[i])):
            # TO CHECK IF FILE IS EMPTY
            if is_file_empty(os.path.join(directory_path + "/files/", list_of_files[i])):
                # TO WRITE DEFAULT DATA IN FILES
                with open(os.path.join(directory_path + "/files/", list_of_files[i]), 'w') as file:
                    file.write(file_data[i])
        else:
            # TO CREATE AND WRITE DATA IN FILE
            with open(os.path.join(directory_path + "/files/", list_of_files[i]), 'w') as file:
                file.write(file_data[i])

    # CREATING REQUIRED CSV
    if os.path.exists(os.path.join(directory_path + "/files/", "customer_detail.csv")):
        if is_file_empty(os.path.join(directory_path + "/files/", "customer_detail.csv")):
            with open(os.path.join(directory_path + "/files/", "customer_detail.csv"), "w", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['PART NUMBER', 'CONFIG VERSION', 'CUSTOMER NAME', 'MCM TYPE'])
                writer.writerows(data_file.csv_data)
        else:
            pass
    else:
        with open(os.path.join(directory_path + "/files/", "customer_detail.csv"), "w",
                  newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['PART NUMBER', 'CONFIG VERSION', 'CUSTOMER NAME', "MCM TYPE"])
            writer.writerows(data_file.csv_data)

    for n in range(len(module_source)):
        if os.path.exists(
                os.path.join(gui_global.directory_location + "/CRCModules/", module_source[n].split("\\")[-1])):
            x = 1
        else:
            shutil.copy(module_source[n], directory_path + '/CRCModules/')

    import excel_automation

    if os.path.exists(os.path.join(gui_global.directory_location + "/records/",
                                   "active_" + str(SettingRead("STATION")['id']) + ".csv")):
        pass
    else:
        excel_automation.CSV.Create_CSV(excel_automation.CSV)

    poolingDemo()

    systemSerialNumber = systemSerial()
    stored_value = ProfileReading('COMMISSION')['serial']

    # print(f"system num ; {systemSerialNumber}")
    #
    # print(f"serial number: {stored_value}")

    gui_global.commissioning_status = (systemSerialNumber == stored_value)

    '''
    CREATING LOCAL BACKUP LOCATION AND DIRECTORIES
    '''
    backup_list = [f"D:/backup/backup", "D:/backup/backup/files_backup/original", "D:/backup/backup/records_backup",
                   "D:/backup/backup/log_backup"]
    for i in range(len(backup_list)):
        if os.path.exists(backup_list[i]):
            pass
        else:
            os.makedirs(backup_list[i])

    '''
    CONFIGURING DATE AND TIME
    '''
    date_time = str(datetime.datetime.today().date())
    date_time = date_time.split("-")
    day = date_time[2]
    month = date_time[1]
    year = date_time[0]

    file_dict = get_last_modified_dict("D:/backup/backup/files_backup/original/.")
    dict1 = get_last_modified_dict(f"{gui_global.files_directory_location}.")

    if os.path.exists("D:/backup/backup/date_modified.txt"):
        with open("D:/backup/backup/date_modified.txt") as file:
            var = file.read()
        return_dict = eval(var)
    else:
        return_dict = {}
        with open("D:/backup/backup/date_modified.txt", 'w') as file:
            file.write(str(dict1))
        file.close()

    if file_dict == {}:
        for i in dict1.keys():
            shutil.copy(i, f"D:/backup/backup/files_backup/original")

    for i in dict1.keys():
        if return_dict == {}:
            pass
        elif dict1[i] == return_dict[i]:
            pass
        else:
            try:
                os.makedirs(f"D:/backup/backup/files_backup/backup_{day}_{month}_{year}")
                shutil.copy(j, f"D:/backup/backup/files_backup/backup_{day}_{month}_{year}/")
            except:
                if os.path.exists(f"D:/backup/backup/files_backup/backup_{day}_{month}_{year}"):
                    os.makedirs(
                        f"D:/backup/backup/files_backup/backup_{day}_{month}_{year}/backup_{day}_{month}_{year}_{int(time.time())}")
                    shutil.copy(i,
                                f"D:/backup/backup/files_backup/backup_{day}_{month}_{year}/backup_{day}_{month}_{year}_{int(time.time())}/")
            with open("D:/backup/backup/date_modified.txt", 'w') as file:
                file.write(str(dict1))
            file.close()
            break

    """
    UPLOADING TO SERVER AND CHECKING
    """
    if os.path.exists(r"\\SLICE\Data_Share_Temp\temp_folder_to_upload"):
        print("connection is stable to server")
        file = open("D:/backup/backup/last_update.txt", 'r')

        last_upload = eval(file.read())
        list_of_last_upload, files = backup_on_server()
        if eval(str(max(list_of_last_upload))) == last_upload:
            pass
        else:
            print("previous backup uploading....")
            Prompt.Message(Prompt, title="Uploading Backup", prompt="Uploading to server.....")
            for i in range(len(list_of_last_upload)):
                if list_of_last_upload[i] > last_upload:
                    shutil.copy(f"D:/backup/backup/records_backup/{files[i]}",
                                r'\\SLICE\Data_Share_Temp\temp_folder_to_upload')

            with open("D:/backup/backup/last_update.txt", 'w') as file:
                file.write(str(max(list_of_last_upload)))
            print("uploading done")
            Prompt.Message(Prompt, title="Done!", prompt="Uploading Done")
    else:
        print("not connected to server, going offline")

    """
    SETTING UP LOCAL BACKUP AND LAST UPLOAD
    """
    if os.path.exists(f"D:/backup/backup/records_backup/"):
        arr = os.listdir(f"{directory_path}/records/")
        if "active" in arr[0]:
            if os.path.exists(f"D:/backup/backup/records_backup/{arr[0][:8]}_{day}_{month}_{year}.csv"):
                pass
            else:
                station_id = SettingRead("STATION")['id']
                shutil.copy(f"{directory_path}/records/active_{station_id}.csv", f"D:/backup/backup/records_backup/")
                os.renames(f"D:/backup/backup/records_backup/active_{station_id}.csv",
                           f"D:/backup/backup/records_backup/{arr[0][:8]}_{day}_{month}_{year}.csv")
                try:
                    shutil.copy(f"D:/backup/backup/records_backup/{arr[0][:8]}_{day}_{month}_{year}.csv",
                                r'\\SLICE\Data_Share_Temp\temp_folder_to_upload')
                    # with open("D:/backup/backup/last_update.txt", 'w') as last_upload:
                    #     last_upload.write(str(os.stat(f"D:/backup/backup/records_backup/{arr[0][:8]}_{day}_{month}_{year}.csv").st_atime))
                except:
                    Prompt.Message(Prompt, "Error!",
                                   "Error Connecting to server, kindly check internet connectivity to local server!")
                    Prompt.Message(Prompt, "Error!",
                                   "Failed to upload <b>BACKUP</b> to local server!, due to non-connectivity to local server!")


def get_last_modified_dict(path: str) -> dict:
    """
    GETTING LAST MODIFICATION TIME
    """
    data = os.walk(path)
    return_data = dict()
    for root, _, files in data:
        for file in files:
            file = os.path.join(root, file)
            return_data[file] = os.stat(file).st_mtime
    return return_data




def backup_on_server():
    """
    GETTING LAST MODIFICATION TIME STAMPS FROM LOCAL BACKUP
    """
    data_entry = os.listdir(f"D:/backup/backup/records_backup")
    dates = []
    time_date = []
    for i in data_entry:
        dates.append(i)
        time_date.append(os.stat(r"D:/backup/backup/records_backup/" + i).st_mtime)

    return time_date, dates


if __name__ == '__main__':
    global return_dict, m
    from screeninfo import get_monitors

    for m in get_monitors():
        # print(m)
        pass
    from exicom_login import Ui_MainWindow

    return_dict = []
    app = QApplication(sys.argv)
    gui_global.ate_name = sys.argv[0].split("\\")[-1].split(".")[0]
    files_and_values()
    main_window = QMainWindow()
    main_widget = QWidget()
    main_layout = QVBoxLayout()
    circular_progress = CircularProgressBar()
    main_layout.addWidget(circular_progress)
    main_widget.setLayout(main_layout)
    main_window.setCentralWidget(main_widget)
    main_window.setWindowFlag(Qt.FramelessWindowHint)
    main_window.setAttribute(Qt.WA_NoSystemBackground, True)
    main_window.setAttribute(Qt.WA_TranslucentBackground, True)
    main_window.setGeometry(int(m.width * (450 / 1366)), int(m.height * (200 / 768)), int(m.width * (400 / 1366)),
                            int(m.height * (400 / 768)))
    main_window.show()
    sys.exit(app.exec_())
