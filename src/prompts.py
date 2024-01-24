import time

from PyQt5.QtWidgets import QMessageBox, QInputDialog
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets, QtGui, QtCore
import gui_global
from PyQt5.QtCore import QTimer

from PyQt5.QtWidgets import QMessageBox, QInputDialog, QDialog,  QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QShortcut
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
# import global_parameters

import gui_global


class Prompt:
    def __init__(self):
        pass

    def Message(self, title: str = "MESSAGE", prompt: str = ""):
        self.message = QMessageBox()
        self.message.setWindowTitle(title)
        self.message.setWindowIcon(QIcon(f"{gui_global.image_directory_location}logo_1.png"))
        self.message.setText(prompt)
        self.message.setStandardButtons(QMessageBox.StandardButton.Ok)
        # self.message.setWindowFlag(Qt.FramelessWindowHint)
        # self.message.setAttribute(Qt.WA_TranslucentBackground, True)
        # self.message.setAttribute(Qt.WA_NoSystemBackground, True)
        self.message.exec_()

    def user_value_2(self, parameter_to_measure, unit):
        value = True
        test = None
        while value:
            test, ok = QInputDialog.getInt(None, "Enter parameter", parameter_to_measure)
            test = str(test)
            print(str(parameter_to_measure) + str(test))
            if test == "":
                QMessageBox.warning(self, "Warning!", "Can't proceed with Blank...\n\nKindly enter value to proceed!")
                value = True
            else:
                self.log_center.setTextColor(QtCore.Qt.blue)
                self.log_center.append(parameter_to_measure + " measured: " + str(test) + " " + unit)
                # self.log_center.setTextColor(QtCore.Qt.blue)
                value = False
        return test

    def User_prompt(self, user_prompt):
        # print(user_prompt)
        self.prompt = None
        # msg_box = QMessageBox()
        # msg_box.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(f"{gui_global.image_directory_location}logo_1.png")))
        # response = msg_box.question(QtWidgets.QDialog(), "USER PROMPT", user_prompt,
        #                             QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        msg_box = QMessageBox()
        msg_box.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(f"{gui_global.image_directory_location}logo_1.png")))

        # Apply style sheet properties
        msg_box.setStyleSheet("""
            background-color: #f0f0f0;
            color: #333333;
            font-family: Arial, sans-serif;
            font-size: 14px;
        """)

        response = msg_box.question(QtWidgets.QDialog(), "USER PROMPT", user_prompt,
                                    QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        if response == QtWidgets.QMessageBox.StandardButton.Yes:
            self.prompt = True
        elif response == QtWidgets.QMessageBox.StandardButton.No:
            self.prompt = False
        return self.prompt

    def userPrompt(self, title: str):
        message_box = QMessageBox()
        message_box.setText(f"{title}")

        ok_button = QPushButton("  YES  ")
        cancel_button = QPushButton("  NO  ")


        ok_button.setGeometry(QtCore.QRect(10, 10, 500, 100))

        ok_button.setStyleSheet("background-color: rgb(42,58,86); color: white;")
        cancel_button.setStyleSheet("background-color: rgb(42,58,86); color: white;")

        message_box.addButton(ok_button, QMessageBox.AcceptRole)
        message_box.addButton(cancel_button, QMessageBox.RejectRole)

        message_box.setStyleSheet(
            "background-color:rgba(250,250,250,255);font: 75 20pt 'MS Shell Dlg 2'; border-top: 3px solid black; border-left: 3px solid black; border-right: 3px solid black; border-bottom: 3px solid black; border-radius: 10px;")
        message_box.setWindowFlag(Qt.FramelessWindowHint)
        message_box.setAttribute(Qt.WA_TranslucentBackground, True)
        message_box.setAttribute(Qt.WA_NoSystemBackground, True)

        def on_yes():
            message_box.done(QMessageBox.Accepted)


        def on_no():
            message_box.done(QMessageBox.Rejected)


        shortcut_yes = QShortcut(QKeySequence(Qt.Key_Y), message_box)
        shortcut_yes.activated.connect(on_no)

        shortcut_no = QShortcut(QKeySequence(Qt.Key_N), message_box)
        shortcut_no.activated.connect(on_yes)

        result = message_box.exec_()
        if result == QMessageBox.AcceptRole:
            return True
        else:
            return False


def TimerPrompt(self, prompt_message, timeout='5', title='MESSAGE!'):
        # self.response = None
        messagebox = TimerMessageBox(title, prompt_message, int(timeout))
        messagebox.exec_()


class TimerMessageBox(QMessageBox):
    def __init__(self, title='MESSAGE!', text='None', timeout=10, parent=None):
        super(TimerMessageBox, self).__init__(parent)
        self.setWindowTitle(title)
        if timeout == 0:
            self.time_to_wait = 90
        else:
            self.time_to_wait = timeout
        self.text_to_set = text
        self.setText(self.text_to_set + " ({0})".format(self.time_to_wait))
        self.setIcon(1)
        self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(f"{gui_global.image_directory_location}logo_1.png")))
        # self.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.changeContent)
        self.timer.start()

    def changeContent(self):
        self.setText(self.text_to_set + " ({0})".format(self.time_to_wait))
        self.time_to_wait -= 1
        if self.time_to_wait <= 0:
            self.close()

    def closeEvent(self, event):
        self.timer.stop()
        event.accept()
