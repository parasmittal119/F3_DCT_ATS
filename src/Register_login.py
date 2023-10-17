from Hardware_detection import Hardware_check
from Main_window_final import *
from config_done import *
from pfc_window import *

global login, register
login = 0
register = 0


class Register(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('ATS Register_window')
        self.setGeometry(550, 300, 300, 150)

        # Set Icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{gui_global.image_directory_location}logo_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        # Create widgets
        self.label_username = QLabel('Username:')
        self.label_password = QLabel('Password:')
        self.edit_username = QLineEdit()
        self.edit_password = QLineEdit()
        self.edit_password.setEchoMode(QLineEdit.Password)
        self.register_button_register_window = QPushButton('Register')
        self.register_button_register_window.clicked.connect(self.handle_register)
        self.login_button_register_window = QPushButton('Back to Login Window')
        self.login_button_register_window.clicked.connect(self.handle_login_window)

        # Create layout and add widgets
        layout_username = QHBoxLayout()
        layout_username.addWidget(self.label_username)
        layout_username.addWidget(self.edit_username)

        layout_password = QHBoxLayout()
        layout_password.addWidget(self.label_password)
        layout_password.addWidget(self.edit_password)

        layout_button = QHBoxLayout()
        layout_button.addWidget(self.register_button_register_window)

        layout_button_login = QHBoxLayout()
        layout_button_login.addWidget(self.login_button_register_window)

        layout = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout.addLayout(layout_username)
        layout.addLayout(layout_password)
        layout2.addLayout(layout_button)
        # layout2.addLayout(layout_button_login)
        layout.addLayout(layout2)

        self.setLayout(layout)

    def handle_register(self):
        try:
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

            pwd = profile['PASSWORD']

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

                value = "SUPERMASTER"

                for key in profile_dict:
                    user[key] = profile_dict[key]

                user[username.lower()] = value

                for i in profile_pass_dict:
                    pwd[i] = profile_pass_dict[i]

                pwd[password.lower()] = value


                with open(f'{gui_global.files_directory_location}profile.txt', 'w') as confile:
                    profile.write(confile)

                QMessageBox.warning(self, "Prompt", "User Registered!")

        except Exception as err:
            print(err)


    def handle_login_window(self):
        self.login = User_login.Login()
        self.login.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    if Hardware_check():
        register = Register()
        register.show()

        sys.exit(app.exec_())
