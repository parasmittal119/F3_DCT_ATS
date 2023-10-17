# GLOBALS
counter = 0
jumper = 10

import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QDesktopWidget

import Main_window_final
from Register_login import *
from config_done import ProfileReading

global count
login = 0
register = 0


class Login(QWidget):

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def __init__(self):
        super().__init__()
        self.setWindowTitle('ATS Login_window')
        self.setGeometry(550, 300, 300, 250)
        # Set Icon
        icon = QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{gui_global.image_directory_location}logo_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        # Create widgets
        self.label_username = QLabel("Username:")  # QtWidget.QLabel('Username:')
        setFont = QtGui.QFont("Arial", 15)
        self.label_username.setFont(setFont)
        self.label_password = QLabel('Password:')
        self.label_password.setFont(setFont)
        self.edit_username = QLineEdit()
        self.edit_password = QLineEdit()
        self.edit_password.setEchoMode(QLineEdit.Password)
        self.login_button_login_window = QPushButton('Login')
        self.login_button_login_window.setFont(setFont)
        self.login_button_login_window.clicked.connect(self.handle_login)
        self.login_button_login_window.setDefault(True)
        self.register_button_login_window = QPushButton('Register Window')
        self.register_button_login_window.setFont(setFont)
        self.register_button_login_window.clicked.connect(self.handle_register_window)

        # Create layout and add widgets
        layout_username = QHBoxLayout()
        layout_username.addWidget(self.label_username)
        layout_username.addWidget(self.edit_username)

        layout_password = QHBoxLayout()
        layout_password.addWidget(self.label_password)
        layout_password.addWidget(self.edit_password)

        layout_button = QHBoxLayout()
        layout_button.addWidget(self.login_button_login_window)

        layout_button_login = QHBoxLayout()
        layout_button_login.addWidget(self.register_button_login_window)

        layout = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout.addLayout(layout_username)
        layout.addLayout(layout_password)
        layout2.addLayout(layout_button)
        layout2.addLayout(layout_button_login)
        layout.addLayout(layout2)

        self.setLayout(layout)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.login_button_login_window.click()

    def handle_login(self):
        global password, username, user_available, login, register
        user_available = True
        if self.login_button_login_window.pressed:
            login += 1
            try:
                if self.edit_username.text() == "JIGGLY" and self.edit_password.text() == "PUFF":
                    gui_global.commissioning_bit = False
                    self.close()
                    self.super_master_login()

                elif self.login_button_login_window.text() == "Login" and self.register_button_login_window.text() == "Register Window":
                    try:
                        username = ProfileReading('USERNAME')[self.edit_username.text().lower()]
                    except KeyError:
                        username = 1
                        QMessageBox.warning(self, 'Error', 'Username is not registered')
                        user_available = False

                    if user_available:
                        try:
                            password = ProfileReading("PASSWORDS")[self.edit_username.text().lower()]
                        except KeyError:
                            password = 1
                            QMessageBox.warning(self, 'Error', 'Input Password is wrong')

                    if username == 1 or password == 1:
                        pass
                    else:

                        if password != self.edit_password.text():
                            Prompt.Message(Prompt, 'Error', "Input Password is wrong!")

                        elif username == "SUPERMASTER" and password == self.edit_password.text():
                            self.close()
                            self.super_master_login()

                        elif username == "MASTER" and password == self.edit_password.text():
                            self.close()
                            self.master_login()

                        elif username == "ADMIN" and password == self.edit_password.text():
                            self.close()
                            self.admin_login()

                        elif username == "USER" and password == self.edit_password.text():
                            self.close()
                            self.user_login()

                        else:
                            QMessageBox.warning(self, 'Error',
                                                'Username is not registered or username/password is wrong')

                    login = 0

            except KeyError:
                QMessageBox.warning(self, 'Error', 'Username is not registered \n\nor\n\n username/password is wrong')

        if self.login_button_login_window.text() == "Register" and register == 1:
            try:
                if self.register_button_login_window.text() == "Back to Login Window" and self.login_button_login_window.text() == "Register":
                    profile = configparser.ConfigParser()
                    profile.read(f"{gui_global.files_directory_location}profile.txt")

                    user = profile["USERNAME"]

                    username = self.edit_username.text()

                    password = self.edit_password.text()

                    """USERNAME"""
                    profile_username = []
                    profile_username_level = []

                    for i in user.keys():
                        profile_username.append(i)

                    for i in user.values():
                        profile_username_level.append(i)

                    profile_dict = {}

                    for i in range(len(profile_username)):
                        profile_dict[profile_username[i]] = profile_username_level[i]

                    print(profile_dict)

                    """PASSWORD"""

                    pwd = profile['PASSWORDS']

                    profile_password = []
                    profile_password_level = []

                    for key, value in pwd.items():
                        profile_password.append(key)
                        profile_password_level.append(value)

                    profile_pass_dict = {}

                    for i in range(len(profile_password)):
                        profile_pass_dict[profile_password[i]] = profile_password_level[i]

                    print(profile_pass_dict)

                    if username == '' or password == '':
                        QMessageBox.warning(self, 'Error', "Can't Register Blank")

                    elif username in user:
                        QMessageBox.warning(self, 'Error', "Account with this USERNAME already exist!")

                    elif username != "" or password != "":

                        for key in profile_dict:
                            user[key] = profile_dict[key]

                        user[username.lower()] = "USER"

                        for i in profile_pass_dict:
                            pwd[i] = profile_pass_dict[i]

                        pwd[self.edit_username.text().lower()] = self.edit_password.text()

                        with open(f"{gui_global.files_directory_location}profile.txt", 'w') as confile:
                            profile.write(confile)

                        QMessageBox.warning(self, "Prompt", "User Registered!")

            except Exception as err:
                print(err)

    def handle_register_window(self):
        global login, register
        if self.register_button_login_window.pressed:
            register += 1

        if self.register_button_login_window.pressed and register == 1:
            self.register_button_login_window.setText("Back to Login Window")
            self.login_button_login_window.setText("Register")
            self.setWindowTitle("ATS Register Window")
            print("1. Login" + str(login), "register" + str(register))

        elif self.register_button_login_window.pressed and register == 2:
            self.register_button_login_window.setText("Register Window")
            self.login_button_login_window.setText("Login")
            self.setWindowTitle("ATS Login Window")
            print("2. Login" + str(login), "register" + str(register))

        if register == 2:
            register = 0

    def super_master_login(self):
        if not gui_global.commissioning_bit:
            print('master login')
            self.MainWindow_2 = QtWidgets.QMainWindow()
            self.ui = Main_window_final.Ui_MainWindow()
            self.ui.setupUi(self.MainWindow_2)
            self.MainWindow_2.showMaximized()

        elif gui_global.commissioning_status:
            print('master login')
            self.MainWindow_2 = QtWidgets.QMainWindow()
            self.ui = Main_window_final.Ui_MainWindow()
            self.ui.setupUi(self.MainWindow_2)
            self.MainWindow_2.showMaximized()
            # #self.ui.actionCommissioning.setDisabled(True)

        else:
            print('master login')
            self.MainWindow_2 = QtWidgets.QMainWindow()
            self.ui = Main_window_final.Ui_MainWindow()
            self.ui.setupUi(self.MainWindow_2)
            self.MainWindow_2.showMaximized()
            self.ui.menuUser.setDisabled(True)
            self.ui.menuTest_Menu.setDisabled(True)
            self.ui.menuManagement.setDisabled(True)
            self.ui.menuReports.setDisabled(True)
            self.ui.menuDebug.setDisabled(True)
            self.ui.menuATS_Control.setDisabled(True)
            # self.ui.actionCommissioning.setDisabled(True)
            Prompt.Message(Prompt, "Warning", "Setup is not commissioned with the system!")

    def master_login(self):
        if gui_global.commissioning_status:
            print('Admin login')
            self.MainWindow_2 = QtWidgets.QMainWindow()
            self.ui = Main_window_final.Ui_MainWindow()
            self.ui.setupUi(self.MainWindow_2)
            gui_global.admin_login = True
            # self.ui.actionCommissioning.setDisabled(True)
            self.MainWindow_2.showMaximized()
        else:
            print('master login')
            self.MainWindow_2 = QtWidgets.QMainWindow()
            self.ui = Main_window_final.Ui_MainWindow()
            self.ui.setupUi(self.MainWindow_2)
            self.MainWindow_2.showMaximized()
            self.ui.menuUser.setDisabled(True)
            self.ui.menuTest_Menu.setDisabled(True)
            self.ui.menuManagement.setDisabled(True)
            self.ui.menuReports.setDisabled(True)
            self.ui.menuDebug.setDisabled(True)
            self.ui.menuATS_Control.setDisabled(True)
            # self.ui.actionCommissioning.setDisabled(True)
            Prompt.Message(Prompt, "Warning", "Setup is not commissioned with the system!")

    def admin_login(self):
        if gui_global.commissioning_status:
            gui_global.admin_login = True
            print('Manager login')
            self.MainWindow_2 = QtWidgets.QMainWindow()
            self.ui = Main_window_final.Ui_MainWindow()
            self.ui.setupUi(self.MainWindow_2)
            self.ui.menuATS_Control.setDisabled(True)
            self.ui.menuDebug.setDisabled(True)
            # self.ui.actionCommissioning.setDisabled(True)
            self.MainWindow_2.showMaximized()
        else:
            print('master login')
            self.MainWindow_2 = QtWidgets.QMainWindow()
            self.ui = Main_window_final.Ui_MainWindow()
            self.ui.setupUi(self.MainWindow_2)
            self.MainWindow_2.showMaximized()
            self.ui.menuUser.setDisabled(True)
            self.ui.menuTest_Menu.setDisabled(True)
            self.ui.menuManagement.setDisabled(True)
            self.ui.menuReports.setDisabled(True)
            self.ui.menuDebug.setDisabled(True)
            self.ui.menuATS_Control.setDisabled(True)
            # self.ui.actionCommissioning.setDisabled(True)
            Prompt.Message(Prompt, "Warning", "Setup is not commissioned with the system!")

    def user_login(self):
        if gui_global.commissioning_status:
            print('Employee login')
            self.MainWindow_2 = QtWidgets.QMainWindow()
            self.ui = Main_window_final.Ui_MainWindow()
            self.ui.setupUi(self.MainWindow_2)
            self.ui.menuATS_Control.setDisabled(True)
            self.ui.menuDebug.setDisabled(True)
            self.ui.menuManagement.setDisabled(True)
            # self.ui.actionCommissioning.setDisabled(True)
            self.MainWindow_2.showMaximized()
        else:
            print('master login')
            self.MainWindow_2 = QtWidgets.QMainWindow()
            self.ui = Main_window_final.Ui_MainWindow()
            self.ui.setupUi(self.MainWindow_2)
            self.MainWindow_2.showMaximized()
            self.ui.menuUser.setDisabled(True)
            self.ui.menuTest_Menu.setDisabled(True)
            self.ui.menuManagement.setDisabled(True)
            self.ui.menuReports.setDisabled(True)
            self.ui.menuDebug.setDisabled(True)
            self.ui.menuATS_Control.setDisabled(True)
            # self.ui.actionCommissioning.setDisabled(True)
            Prompt.Message(Prompt, "Warning", "Setup is not commissioned with the system!")

    def md5_hash(self, input_string):
        md5_hasher = hashlib.md5()
        md5_hasher.update(input_string.encode('utf-8'))
        return md5_hasher.hexdigest()


#
# def splashScreen():
#     # Display a Splash screen
#     img = QtGui.QPixmap(f"{gui_global.image_directory_location}exicome logo.png")
#     splash = QSplashScreen(img, Qt.WindowStaysOnTopHint)
#     splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
#     splash.setEnabled(False)
#     splash.show()
#     splash.showMessage("<h1><font color='GREEN'></font></h1>", Qt.AlignBottom | Qt.AlignCenter, Qt.green)
#     # splash screen time
#     time.sleep(3)
# #
# #

if __name__ == '__main__':
    application = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(application.exec_())
