from PyQt5.QtWidgets import QMessageBox, QInputDialog
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets, QtGui, QtCore
import gui_global


class Prompt:
    def __init__(self):
        pass

    def Message(self, title: str = "MESSAGE", prompt: str=""):
        self.message = QMessageBox()
        self.message.setWindowTitle(title)
        self.message.setWindowIcon(QIcon(f"{gui_global.image_directory_location}logo_1.png"))
        self.message.setText(prompt)
        self.message.setStandardButtons(QMessageBox.StandardButton.Ok)
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
        msg_box = QMessageBox()
        msg_box.setWindowIcon(QtGui.QIcon(QtGui.QPixmap(f"{gui_global.image_directory_location}logo_1.png")))
        response = msg_box.question(QtWidgets.QDialog(), "USER PROMPT", user_prompt,
                                                  QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)
        if response == QtWidgets.QMessageBox.StandardButton.Yes:
            self.prompt = True
        elif response == QtWidgets.QMessageBox.StandardButton.No:
            self.prompt = False
        return self.prompt

    def TimerPrompt(self, prompt_message, timeout='5', title='MESSAGE!'):
        # self.response = None
        messagebox = TimerMessageBox(title, prompt_message, int(timeout))
        messagebox.exec_()
        # self.response = True


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