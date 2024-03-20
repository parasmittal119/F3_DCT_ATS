import os
import sys
import time

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtGui, QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtChart import *
import manual_global

from screeninfo import get_monitors

from CommandSetSmrBatteryCan import *
from PFC_control_done import *


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi(f'{gui_global.directory_location}\\src\\new_manual.ui', self)
        self.exit.setIcon(QIcon(QtGui.QPixmap(f"{gui_global.image_directory_location}exit.png")))
        self.label_2.setGeometry(QRect(710, 550, 50, 50))
        self.groupBox.setEnabled(False)
        self.groupBox_2.setEnabled(False)
        self.groupBox_3.setEnabled(False)
        self.groupBox_4.setEnabled(False)
        self.groupBox_5.setEnabled(False)

        #BUTTON LINKS
        self.exit.clicked.connect(QApplication.quit)
        # self.doubleSpinBox.valueChanged.connect(self.smrVoltageSet)
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
        self.pushButton_11.clicked.connect(self.DcBus)
        self.pushButton_29.clicked.connect(self.smrVoltageSet)
        # self.pushButton_29.hide()

        #INCLUDES
        self.pfc = pfc_control()

        #TIMERS
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.moonanimation)
        self.timer1.start(500)


    def resetGraphics(self):
        button_list = []
        button_list.append(self.pushButton)
        for i in range(2, 15):
            if i == 12:
                pass
            else:
                button_list.append(getattr(self, f"pushButton_{i}"))
        button_list.append(self.r_indicator)
        button_list.append(self.y_indicator)
        button_list.append(self.b_indicator)

        for i in range(len(button_list)-3):
            self.shadowFunction(button_name=button_list[i], invert=False)

        for i in button_list[13:]:
            i.setStyleSheet(f"""border-radius:19px;background-color:rgba(150,150,150,255);border:1px solid black;""")


    def moonanimation(self):
        x = 0
        for i in range(90):
            self.label_2.setGeometry(QRect(710, 550-x, 50, 50))
            x += 6
            time.sleep(0.00001)
            qApp.processEvents()
        self.timer1.stop()
        print(x)


    def startATS(self):
        manual_global.startats += 1
        if manual_global.startats % 2:
            self.pushButton_14.setText("CLEAR ATS")
            self.shadowFunction(alpha=100)
            self.groupBox.setEnabled(True)
            self.groupBox_2.setEnabled(True)
            self.groupBox_3.setEnabled(True)
            self.groupBox_4.setEnabled(True)
            self.groupBox_5.setEnabled(True)
        else:
            self.pushButton_14.setText("START ATS")
            self.shadowFunction(invert=False)
            self.pfc.pfc_set("0", 'all', 0)
            self.resetGraphics()
            self.groupBox.setEnabled(False)
            self.groupBox_2.setEnabled(False)
            self.groupBox_3.setEnabled(False)
            self.groupBox_4.setEnabled(False)
            self.groupBox_5.setEnabled(False)


    def ACActive(self):
        self.status(self.pushButton_13, ["r_phase", "y_phase", "b_phase"])


    def LOAD1(self):
        self.status(pfc_name=['p_load'])
        qApp.processEvents()
        if self.getalphavalue() == 130 and self.getalphavalue(self.pushButton_6) == 0:
            self.status(button_name=self.pushButton_6, pfc_name=["load_mains"])
        self.BusCheck(self.pushButton_6)


    def LOAD2(self):
        self.status(pfc_name=['n_p_load_1'])
        qApp.processEvents()
        if self.getalphavalue() == 130 and self.getalphavalue(self.pushButton_6) == 0:
            self.status(button_name=self.pushButton_6, pfc_name=["load_mains"])
        self.BusCheck(self.pushButton_6)


    def LOAD3(self):
        self.status(pfc_name=['n_p_load_2'])
        qApp.processEvents()
        if self.getalphavalue() == 130 and self.getalphavalue(self.pushButton_6) == 0:
            self.status(button_name=self.pushButton_6, pfc_name=["load_mains"])
        self.BusCheck(self.pushButton_6)


    def LOAD4(self):
        self.status(pfc_name=['n_p_load_3'])
        qApp.processEvents()
        if self.getalphavalue() == 130 and self.getalphavalue(self.pushButton_6) == 0:
            self.status(button_name=self.pushButton_6, pfc_name=["load_mains"])
        self.BusCheck(self.pushButton_6)


    def LOAD5(self):
        self.status(pfc_name=['n_p_load_4'])
        qApp.processEvents()
        if self.getalphavalue() == 130 and self.getalphavalue(self.pushButton_6) == 0:
            self.status(button_name=self.pushButton_6, pfc_name=["load_mains"])
        self.BusCheck(self.pushButton_6)

    def LOADCommon(self):
        self.status(button_name=self.pushButton_6,pfc_name=['load_mains'])


    def BusCheck(self, button):
        if self.getalphavalue(button) == 130 and int(self.pushButton_11.palette().color(self.pushButton_11.backgroundRole()).alpha()) == 0:
            self.status(button_name=self.pushButton_11, pfc_name=['bus'])


    def BATT1(self):
        self.status(self.pushButton_7, ['battery_1'])
        if self.getalphavalue() == 130 and self.getalphavalue(self.pushButton_10) == 0:
            self.status(self.pushButton_10, ['battery_mains'])
        self.BusCheck(self.pushButton_10)

    def BATT2(self):
        self.status(self.pushButton_9, ['battery_2'])
        if self.getalphavalue() == 130 and self.getalphavalue(self.pushButton_10) == 0:
            self.status(self.pushButton_10, ['battery_mains'])
        self.BusCheck(self.pushButton_10)

    def BATT3(self):
        self.status(self.pushButton_8, ['battery_3'])
        if self.getalphavalue() == 130 and self.getalphavalue(self.pushButton_10) == 0:
            self.status(self.pushButton_10, ['battery_mains'])
        self.BusCheck(self.pushButton_10)


    def BATTMAINS(self):
        self.status(self.pushButton_10, ['battery_mains'])

    def DcBus(self):
        self.status(self.pushButton_11, ['bus'])


    def smrVoltageSet(self):
        SMR_BATTERY_SET_VOLTAGE(self.doubleSpinBox.value())


    def shadowFunction(self, button_name="", alpha=0, blurRadius=20, offset=(10, 10), invert=True):
        if button_name == "":
            button = getattr(self, self.sender().objectName())
        else:
            button = button_name
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(blurRadius)
        effect.setColor(QColor(0, 0, 0, alpha))
        effect.setOffset(offset[0], offset[1])
        button.setGraphicsEffect(effect)
        if invert:
            button.setStyleSheet(
                f"QPushButton{{background-color: rgba(255,255,255,130); border-radius: {int(button.geometry().height() / 2)}px; color: rgba(255,255,255,255);}}")
        else:
            button.setStyleSheet(
                f"""QPushButton{{background-color:rgba(0,0,0,0);border-radius:{int(button.geometry().height() / 2)}px;color:rgba(255,255,255,255);\n}}
                        QPushButton::hover{{\nbackground-color:rgba(255,255,255,50);border-radius:{int(button.geometry().height() / 2)}px;color:rgba(255,255,255,255);\n}}
                        QPushButton::pressed{{\nbackground-color:rgba(255,255,255,130);border-radius:{int(button.geometry().height() / 2)}px;color:rgba(255,255,255,255);\n}}""")


    def status(self, button_name:str = "", pfc_name: list = []):
        voltages = ['r_phase', 'y_phase', 'b_phase']
        indicators = ['r_indicator', 'y_indicator', "b_indicator"]
        colors = ["rgba(255,0,0,255);", "rgba(255,255,0,255);", "rgba(0,151,226,255);"]
        if button_name == "":
            button = getattr(self, self.sender().objectName())
            alpha_value = int(button.palette().color(self.pushButton_11.backgroundRole()).alpha())
            print("no button_name ", alpha_value)
            if alpha_value == 0:
                for itr in pfc_name:
                    print(itr)
                    value = self.pfc.pfc_set(0, itr, 1)
                    if value == "NA":
                        break
                    else:
                        self.shadowFunction(alpha=100)
            else:
                for itr in pfc_name:
                    print(itr)
                    value = self.pfc.pfc_set(0, itr, 0)
                    if value == "NA":
                        break
                    else:
                        self.shadowFunction(invert=False)


            QtWidgets.qApp.processEvents()
        else:
            alpha_value = int(button_name.palette().color(self.pushButton_11.backgroundRole()).alpha())
            print(f"With alpha name : {alpha_value}")
            if alpha_value == 0:
                for itr in pfc_name:
                    if itr in voltages:
                        attribute = getattr(self, indicators[voltages.index(itr)])
                        attribute.setStyleSheet(f"""border-radius:19px;background-color:{colors[voltages.index(itr)]}border:1px solid black;""")
                        time.sleep(0.00001)
                        qApp.processEvents()
                    value = self.pfc.pfc_set(0, itr, 1)
                    if value == "NA":
                        break
                    else:
                        self.shadowFunction(button_name=button_name, alpha=100)
            elif alpha_value == 130:
                for itr in pfc_name:
                    if itr in voltages:
                        attribute = getattr(self, indicators[voltages.index(itr)])
                        attribute.setStyleSheet(f"""border-radius:19px;background-color:rgba(150,150,150,255);border:1px solid black;""")
                        time.sleep(0.00001)
                        qApp.processEvents()
                    value = self.pfc.pfc_set(0, itr, 0)
                    if value == "NA":
                        break
                    else:
                        self.shadowFunction(button_name=button_name, invert=False)
            QtWidgets.qApp.processEvents()


    def getalphavalue(self, pushbutton:str=""):
        if pushbutton == "":
            button = getattr(self, self.sender().objectName())
            alpha_value = int(button.palette().color(self.pushButton_11.backgroundRole()).alpha())
            return alpha_value
        else:
            alpha_value = int(pushbutton.palette().color(self.pushButton_11.backgroundRole()).alpha())
            return alpha_value



if __name__ == "__main__":
    import prompts
    app = QApplication(sys.argv)

    if os.path.exists(f"{gui_global.files_directory_location}pfcjig.txt"):
        window = MyWindow()
        window.setWindowFlag(Qt.FramelessWindowHint, True)
        window.setAttribute(Qt.WA_NoSystemBackground, True)
        window.setAttribute(Qt.WA_TranslucentBackground, True)
        window.show()
        sys.exit(app.exec_())
    else:
        prompts.Prompt.Message(prompts.Prompt, "Error!",
                               "Required File is missing, Kindly run DCT ATS application first.\nThen re-run this program! THANK YOU!")
        prompts.Prompt.Message(prompts.Prompt, prompt="Hope to see you soon! ;)")
        app.quit()

