# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file '.\communication_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from config_done import SettingRead
import gui_global
import pyvisa
# pyvisa.log_to_screen()


class Ui_load(object):
    def setupUi(self, load):
        load.setObjectName("load")
        load.resize(401, 92)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{gui_global.image_directory_location}logo_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        load.setWindowIcon(icon)
        self.groupBox = QtWidgets.QGroupBox(load)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 371, 71))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 15, 351, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.label_2.setFont(QtGui.QFont("arial", 23))
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.communication)
        self.horizontalLayout.addWidget(self.pushButton)
        # self.rm = pyvisa.ResourceManager()
        # self.chroma = None

        self.retranslateUi(load)
        QtCore.QMetaObject.connectSlotsByName(load)

    def communication(self):
        import pyvisa
        global return_value, address
        return_value = ""

        self.rm = pyvisa.ResourceManager()  # Create resource manager outside try/except

        while True:  # Reconnection loop
            try:
                list1 = self.rm.list_resources()
                for i in list1:
                    if "GPIB" in i:
                        address = str(i).split("::INSTR")[0]
                    elif "USB" in i:
                        address = str(i).split("::INSTR")[0]
                    self.chroma = self.rm.open_resource(address)
                    return_value = str(self.chroma.query("*IDN?")).split(",")[1]
                    break  # Exit loop if device found
                print(return_value)
                if "632" in return_value:
                    self.label_2.setText("PASS")
                    self.label_2.setStyleSheet("color:GREEN")
                else:
                    self.label_2.setText("FAIL")
                    self.label_2.setStyleSheet("color:RED")
                return  # Exit function if communication successful

            except Exception as e:
                print(f"Error: {e}")
                time.sleep(5)  # Delay before retrying

        # Close resources (only reached if all connection attempts fail)
        self.chroma.close()
        self.rm.close()

    def retranslateUi(self, load):
        _translate = QtCore.QCoreApplication.translate
        load.setWindowTitle(_translate("load", "DC Load Communication Window"))
        self.groupBox.setTitle(_translate("load", ""))
        self.label.setText(_translate("load", "DC Load Communication Check:"))
        self.pushButton.setText(_translate("load", "Check"))
        self.label_2.setText(_translate("load", ""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    load = QtWidgets.QWidget()
    ui = Ui_load()
    ui.setupUi(load)
    load.show()
    sys.exit(app.exec_())
