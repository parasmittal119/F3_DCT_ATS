import csv
import getpass
import os
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel

import data_file
import gui_global
from Hardware_detection import Hardware_check
from User_login import Login
from config_done import *
from prompts import *

file_data = [data_file.alarmIndex, data_file.calibrate, data_file.config, data_file.default, data_file.filetime, data_file.oid,
             data_file.orderedtelnet, data_file.pfcjig, data_file.profile, data_file.RequiredParameter,
             data_file.setting, data_file.smrdetail, data_file.systemversion, data_file.telnetgetcommand, data_file.testorder,
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
            self.login_window = Login()
            # self.login_window.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            # self.login_window.setAttribute(Qt.WA_NoSystemBackground, True)
            # self.login_window.setAttribute(Qt.WA_TranslucentBackground, True)
            self.login_window.center()
            self.login_window.show()
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
        outer_radius = int(min(width, height) / 2 - 10)
        outer_center = int(width / 2), int(height / 2)
        outer_circle = QColor(50, 50, 50)
        painter.setPen(QPen(outer_circle, 20))
        painter.drawEllipse(outer_center[0] - outer_radius, outer_center[1] - outer_radius, 2 * outer_radius, 2 * outer_radius)

        # Inner circle
        inner_radius = int(outer_radius - 10)
        inner_circle = QColor(150, 150, 150)
        painter.setPen(QPen(inner_circle, 10))
        painter.drawEllipse(outer_center[0] - inner_radius, outer_center[1] - inner_radius, 2 * inner_radius, 2 * inner_radius)

        # Progress arc
        progress_angle = int(360 * self.progress / 100)
        progress_color = QColor(0, 100, 150)  # Green color
        painter.setPen(QPen(progress_color, 12))
        painter.drawArc(outer_center[0] - outer_radius, outer_center[1] - outer_radius, 2 * outer_radius, 2 * outer_radius, -90 * 16, -progress_angle * 16)

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
    return_code = process.returncode
    serial_number = str(output).split(" ")[2].split("n")[1]
    return serial_number


def files_and_values():
    # CHECKING FOR ALL PRESENT DIRECTORIES/ ELSE CREATING THEM
    account_user = getpass.getuser()  # to get login account INFO

    list_of_dir = ['CRCModules', 'files', 'images', 'logs', 'records', 'reports', 'src',
                   'summary']  # List of DIRECTORY REQUIRED

    directory_path = f"C:/Users/{account_user}/AppData/Local/DCT_ATS"  # MAIN DIRECTORY PATH

    # LOOP FOR ALL DIRECTORY

    for n in range(len(list_of_dir)):
        # TO CHECK PRESENCE OF DIRECTORY
        if not os.path.exists(os.path.join(directory_path, list_of_dir[n])):
            # If it doesn't exist, create the folder
            os.makedirs(os.path.join(directory_path, list_of_dir[n]))
        # TO PASS REQUIRED DIRECTORY FOUND
        else:
            pass

    # CHECKING FOR ALL FILES/ ELSE CREATING THEM WITH DEFAULT DATA
    for i in range(len(list_of_files)):
        # TO CHECK PRESENCE OF FILES
        if os.path.exists(os.path.join(directory_path + "/files/", list_of_files[i])):
            # TO CHECK IS FILE IS EMPTY
            if is_file_empty(os.path.join(directory_path + "/files/", list_of_files[i])):
                # TO WRITE DEFAULT DATA IN FILES
                with open(os.path.join(directory_path + "/files/", list_of_files[i]), 'w') as file:
                    file.write(file_data[i])
            else:
                # TO PASS IF DATA IS FOUND IN FILE
                pass
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
            # print(module_source[n].split("\\")[-1])
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

    gui_global.commissioning_status = (systemSerialNumber == stored_value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
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
    main_window.setGeometry(450, 200, 400, 400)
    main_window.show()
    sys.exit(app.exec_())
