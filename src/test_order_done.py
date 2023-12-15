# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\test_order.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import gui_global


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(527, 578)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 0, 331, 61))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{gui_global.image_directory_location}logo_1.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 60, 511, 511))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 471, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.test1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test1.setFont(font)
        self.test1.setObjectName("test1")
        self.horizontalLayout.addWidget(self.test1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBox_1 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_1.addItem("1")
        self.comboBox_1.addItem("2")
        self.comboBox_1.addItem("3")
        self.comboBox_1.addItem("4")
        self.comboBox_1.addItem("5")
        self.comboBox_1.addItem("6")
        self.comboBox_1.addItem("7")
        self.comboBox_1.addItem("8")
        self.comboBox_1.addItem("9")
        self.comboBox_1.addItem("10")
        self.comboBox_1.addItem("11")
        self.comboBox_1.addItem("12")
        self.comboBox_1.addItem("13")
        self.comboBox_1.addItem("14")
        self.comboBox_1.addItem("15")
        self.comboBox_1.addItem("16")
        self.comboBox_1.setCurrentIndex(0)
        self.comboBox_1.setObjectName("comboBox_1")
        self.horizontalLayout.addWidget(self.comboBox_1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 471, 22))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.test2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test2.setFont(font)
        self.test2.setObjectName("test2")
        self.horizontalLayout_2.addWidget(self.test2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("1")
        self.comboBox_2.addItem("2")
        self.comboBox_2.addItem("3")
        self.comboBox_2.addItem("4")
        self.comboBox_2.addItem("5")
        self.comboBox_2.addItem("6")
        self.comboBox_2.addItem("7")
        self.comboBox_2.addItem("8")
        self.comboBox_2.addItem("9")
        self.comboBox_2.addItem("10")
        self.comboBox_2.addItem("11")
        self.comboBox_2.addItem("12")
        self.comboBox_2.addItem("13")
        self.comboBox_2.addItem("14")
        self.comboBox_2.addItem("15")
        self.comboBox_2.addItem("16")
        self.comboBox_2.setCurrentIndex(1)
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 80, 471, 22))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.test3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test3.setFont(font)
        self.test3.setObjectName("test3")
        self.horizontalLayout_3.addWidget(self.test3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.comboBox_3 = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("1")
        self.comboBox_3.addItem("2")
        self.comboBox_3.addItem("3")
        self.comboBox_3.addItem("4")
        self.comboBox_3.addItem("5")
        self.comboBox_3.addItem("6")
        self.comboBox_3.addItem("7")
        self.comboBox_3.addItem("8")
        self.comboBox_3.addItem("9")
        self.comboBox_3.addItem("10")
        self.comboBox_3.addItem("11")
        self.comboBox_3.addItem("12")
        self.comboBox_3.addItem("13")
        self.comboBox_3.addItem("14")
        self.comboBox_3.addItem("15")
        self.comboBox_3.addItem("16")
        self.comboBox_3.setCurrentIndex(2)
        self.horizontalLayout_3.addWidget(self.comboBox_3)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 110, 471, 22))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.test4 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test4.setFont(font)
        self.test4.setObjectName("test4")
        self.horizontalLayout_4.addWidget(self.test4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.comboBox_4 = QtWidgets.QComboBox(self.horizontalLayoutWidget_4)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("1")
        self.comboBox_4.addItem("2")
        self.comboBox_4.addItem("3")
        self.comboBox_4.addItem("4")
        self.comboBox_4.addItem("5")
        self.comboBox_4.addItem("6")
        self.comboBox_4.addItem("7")
        self.comboBox_4.addItem("8")
        self.comboBox_4.addItem("9")
        self.comboBox_4.addItem("10")
        self.comboBox_4.addItem("11")
        self.comboBox_4.addItem("12")
        self.comboBox_4.addItem("13")
        self.comboBox_4.addItem("14")
        self.comboBox_4.addItem("15")
        self.comboBox_4.addItem("16")
        self.comboBox_4.setCurrentIndex(3)
        self.horizontalLayout_4.addWidget(self.comboBox_4)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 140, 471, 22))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.test5 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test5.setFont(font)
        self.test5.setObjectName("test5")
        self.horizontalLayout_5.addWidget(self.test5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.comboBox_5 = QtWidgets.QComboBox(self.horizontalLayoutWidget_5)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("1")
        self.comboBox_5.addItem("2")
        self.comboBox_5.addItem("3")
        self.comboBox_5.addItem("4")
        self.comboBox_5.addItem("5")
        self.comboBox_5.addItem("6")
        self.comboBox_5.addItem("7")
        self.comboBox_5.addItem("8")
        self.comboBox_5.addItem("9")
        self.comboBox_5.addItem("10")
        self.comboBox_5.addItem("11")
        self.comboBox_5.addItem("12")
        self.comboBox_5.addItem("13")
        self.comboBox_5.addItem("14")
        self.comboBox_5.addItem("15")
        self.comboBox_5.addItem("16")
        self.comboBox_5.setCurrentIndex(4)
        self.horizontalLayout_5.addWidget(self.comboBox_5)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(10, 170, 471, 22))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.test6 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test6.setFont(font)
        self.test6.setObjectName("test6")
        self.horizontalLayout_6.addWidget(self.test6)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.comboBox_6 = QtWidgets.QComboBox(self.horizontalLayoutWidget_6)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("1")
        self.comboBox_6.addItem("2")
        self.comboBox_6.addItem("3")
        self.comboBox_6.addItem("4")
        self.comboBox_6.addItem("5")
        self.comboBox_6.addItem("6")
        self.comboBox_6.addItem("7")
        self.comboBox_6.addItem("8")
        self.comboBox_6.addItem("9")
        self.comboBox_6.addItem("10")
        self.comboBox_6.addItem("11")
        self.comboBox_6.addItem("12")
        self.comboBox_6.addItem("13")
        self.comboBox_6.addItem("14")
        self.comboBox_6.addItem("15")
        self.comboBox_6.addItem("16")
        self.comboBox_6.setCurrentIndex(5)
        self.horizontalLayout_6.addWidget(self.comboBox_6)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(10, 200, 471, 22))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.test7 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test7.setFont(font)
        self.test7.setObjectName("test7")
        self.horizontalLayout_7.addWidget(self.test7)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.comboBox_7 = QtWidgets.QComboBox(self.horizontalLayoutWidget_7)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("1")
        self.comboBox_7.addItem("2")
        self.comboBox_7.addItem("3")
        self.comboBox_7.addItem("4")
        self.comboBox_7.addItem("5")
        self.comboBox_7.addItem("6")
        self.comboBox_7.addItem("7")
        self.comboBox_7.addItem("8")
        self.comboBox_7.addItem("9")
        self.comboBox_7.addItem("10")
        self.comboBox_7.addItem("11")
        self.comboBox_7.addItem("12")
        self.comboBox_7.addItem("13")
        self.comboBox_7.addItem("14")
        self.comboBox_7.addItem("15")
        self.comboBox_7.addItem("16")
        self.comboBox_7.setCurrentIndex(6)
        self.horizontalLayout_7.addWidget(self.comboBox_7)
        self.horizontalLayoutWidget_8 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_8.setGeometry(QtCore.QRect(10, 230, 471, 22))
        self.horizontalLayoutWidget_8.setObjectName("horizontalLayoutWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.test8 = QtWidgets.QLabel(self.horizontalLayoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test8.setFont(font)
        self.test8.setObjectName("test8")
        self.horizontalLayout_8.addWidget(self.test8)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.comboBox_8 = QtWidgets.QComboBox(self.horizontalLayoutWidget_8)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("1")
        self.comboBox_8.addItem("2")
        self.comboBox_8.addItem("3")
        self.comboBox_8.addItem("4")
        self.comboBox_8.addItem("5")
        self.comboBox_8.addItem("6")
        self.comboBox_8.addItem("7")
        self.comboBox_8.addItem("8")
        self.comboBox_8.addItem("9")
        self.comboBox_8.addItem("10")
        self.comboBox_8.addItem("11")
        self.comboBox_8.addItem("12")
        self.comboBox_8.addItem("13")
        self.comboBox_8.addItem("14")
        self.comboBox_8.addItem("15")
        self.comboBox_8.addItem("16")
        self.comboBox_8.setCurrentIndex(7)
        self.horizontalLayout_8.addWidget(self.comboBox_8)
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(10, 260, 471, 22))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.test9 = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test9.setFont(font)
        self.test9.setObjectName("test9")
        self.horizontalLayout_9.addWidget(self.test9)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.comboBox_9 = QtWidgets.QComboBox(self.horizontalLayoutWidget_9)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("1")
        self.comboBox_9.addItem("2")
        self.comboBox_9.addItem("3")
        self.comboBox_9.addItem("4")
        self.comboBox_9.addItem("5")
        self.comboBox_9.addItem("6")
        self.comboBox_9.addItem("7")
        self.comboBox_9.addItem("8")
        self.comboBox_9.addItem("9")
        self.comboBox_9.addItem("10")
        self.comboBox_9.addItem("11")
        self.comboBox_9.addItem("12")
        self.comboBox_9.addItem("13")
        self.comboBox_9.addItem("14")
        self.comboBox_9.addItem("15")
        self.comboBox_9.addItem("16")
        self.comboBox_9.setCurrentIndex(8)
        self.horizontalLayout_9.addWidget(self.comboBox_9)
        self.horizontalLayoutWidget_10 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_10.setGeometry(QtCore.QRect(10, 290, 471, 22))
        self.horizontalLayoutWidget_10.setObjectName("horizontalLayoutWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.test10 = QtWidgets.QLabel(self.horizontalLayoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test10.setFont(font)
        self.test10.setObjectName("test10")
        self.horizontalLayout_10.addWidget(self.test10)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem9)
        self.comboBox_10 = QtWidgets.QComboBox(self.horizontalLayoutWidget_10)
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("1")
        self.comboBox_10.addItem("2")
        self.comboBox_10.addItem("3")
        self.comboBox_10.addItem("4")
        self.comboBox_10.addItem("5")
        self.comboBox_10.addItem("6")
        self.comboBox_10.addItem("7")
        self.comboBox_10.addItem("8")
        self.comboBox_10.addItem("9")
        self.comboBox_10.addItem("10")
        self.comboBox_10.addItem("11")
        self.comboBox_10.addItem("12")
        self.comboBox_10.addItem("13")
        self.comboBox_10.addItem("14")
        self.comboBox_10.addItem("15")
        self.comboBox_10.addItem("16")
        self.comboBox_10.setCurrentIndex(9)
        self.horizontalLayout_10.addWidget(self.comboBox_10)
        self.horizontalLayoutWidget_11 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_11.setGeometry(QtCore.QRect(10, 320, 471, 22))
        self.horizontalLayoutWidget_11.setObjectName("horizontalLayoutWidget_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.test11 = QtWidgets.QLabel(self.horizontalLayoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test11.setFont(font)
        self.test11.setObjectName("test11")
        self.horizontalLayout_11.addWidget(self.test11)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.comboBox_11 = QtWidgets.QComboBox(self.horizontalLayoutWidget_11)
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("1")
        self.comboBox_11.addItem("2")
        self.comboBox_11.addItem("3")
        self.comboBox_11.addItem("4")
        self.comboBox_11.addItem("5")
        self.comboBox_11.addItem("6")
        self.comboBox_11.addItem("7")
        self.comboBox_11.addItem("8")
        self.comboBox_11.addItem("9")
        self.comboBox_11.addItem("10")
        self.comboBox_11.addItem("11")
        self.comboBox_11.addItem("12")
        self.comboBox_11.addItem("13")
        self.comboBox_11.addItem("14")
        self.comboBox_11.addItem("15")
        self.comboBox_11.addItem("16")
        self.comboBox_11.setCurrentIndex(10)
        self.horizontalLayout_11.addWidget(self.comboBox_11)
        self.horizontalLayoutWidget_12 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_12.setGeometry(QtCore.QRect(10, 350, 471, 22))
        self.horizontalLayoutWidget_12.setObjectName("horizontalLayoutWidget_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.test12 = QtWidgets.QLabel(self.horizontalLayoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test12.setFont(font)
        self.test12.setObjectName("test12")
        self.horizontalLayout_12.addWidget(self.test12)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem11)
        self.comboBox_12 = QtWidgets.QComboBox(self.horizontalLayoutWidget_12)
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("1")
        self.comboBox_12.addItem("2")
        self.comboBox_12.addItem("3")
        self.comboBox_12.addItem("4")
        self.comboBox_12.addItem("5")
        self.comboBox_12.addItem("6")
        self.comboBox_12.addItem("7")
        self.comboBox_12.addItem("8")
        self.comboBox_12.addItem("9")
        self.comboBox_12.addItem("10")
        self.comboBox_12.addItem("11")
        self.comboBox_12.addItem("12")
        self.comboBox_12.addItem("13")
        self.comboBox_12.addItem("14")
        self.comboBox_12.addItem("15")
        self.comboBox_12.addItem("16")
        self.comboBox_12.setCurrentIndex(11)
        self.horizontalLayout_12.addWidget(self.comboBox_12)
        self.horizontalLayoutWidget_13 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_13.setGeometry(QtCore.QRect(10, 380, 471, 22))
        self.horizontalLayoutWidget_13.setObjectName("horizontalLayoutWidget_13")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.test13 = QtWidgets.QLabel(self.horizontalLayoutWidget_13)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test13.setFont(font)
        self.test13.setObjectName("test13")
        self.horizontalLayout_13.addWidget(self.test13)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem12)
        self.comboBox_13 = QtWidgets.QComboBox(self.horizontalLayoutWidget_13)
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.addItem("1")
        self.comboBox_13.addItem("2")
        self.comboBox_13.addItem("3")
        self.comboBox_13.addItem("4")
        self.comboBox_13.addItem("5")
        self.comboBox_13.addItem("6")
        self.comboBox_13.addItem("7")
        self.comboBox_13.addItem("8")
        self.comboBox_13.addItem("9")
        self.comboBox_13.addItem("10")
        self.comboBox_13.addItem("11")
        self.comboBox_13.addItem("12")
        self.comboBox_13.addItem("13")
        self.comboBox_13.addItem("14")
        self.comboBox_13.addItem("15")
        self.comboBox_13.addItem("16")
        self.comboBox_13.setCurrentIndex(12)
        self.horizontalLayout_13.addWidget(self.comboBox_13)
        self.horizontalLayoutWidget_14 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_14.setGeometry(QtCore.QRect(10, 470, 471, 22))
        self.horizontalLayoutWidget_14.setObjectName("horizontalLayoutWidget_14")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_14)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.test16 = QtWidgets.QLabel(self.horizontalLayoutWidget_14)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test16.setFont(font)
        self.test16.setObjectName("test16")
        self.horizontalLayout_14.addWidget(self.test16)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem13)
        self.comboBox_16 = QtWidgets.QComboBox(self.horizontalLayoutWidget_14)
        self.comboBox_16.setObjectName("comboBox_16")

        self.comboBox_16.addItem("1")
        self.comboBox_16.addItem("2")
        self.comboBox_16.addItem("3")
        self.comboBox_16.addItem("4")
        self.comboBox_16.addItem("5")
        self.comboBox_16.addItem("6")
        self.comboBox_16.addItem("7")
        self.comboBox_16.addItem("8")
        self.comboBox_16.addItem("9")
        self.comboBox_16.addItem("10")
        self.comboBox_16.addItem("11")
        self.comboBox_16.addItem("12")
        self.comboBox_16.addItem("13")
        self.comboBox_16.addItem("14")
        self.comboBox_16.addItem("15")
        self.comboBox_16.addItem("16")
        self.comboBox_16.setCurrentIndex(15)

        self.horizontalLayout_14.addWidget(self.comboBox_16)
        self.horizontalLayoutWidget_15 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_15.setGeometry(QtCore.QRect(10, 410, 471, 22))
        self.horizontalLayoutWidget_15.setObjectName("horizontalLayoutWidget_15")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_15)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.test14 = QtWidgets.QLabel(self.horizontalLayoutWidget_15)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test14.setFont(font)
        self.test14.setObjectName("test14")
        self.horizontalLayout_15.addWidget(self.test14)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem14)
        self.comboBox_14 = QtWidgets.QComboBox(self.horizontalLayoutWidget_15)
        self.comboBox_14.setObjectName("comboBox_14")

        self.comboBox_14.addItem("1")
        self.comboBox_14.addItem("2")
        self.comboBox_14.addItem("3")
        self.comboBox_14.addItem("4")
        self.comboBox_14.addItem("5")
        self.comboBox_14.addItem("6")
        self.comboBox_14.addItem("7")
        self.comboBox_14.addItem("8")
        self.comboBox_14.addItem("9")
        self.comboBox_14.addItem("10")
        self.comboBox_14.addItem("11")
        self.comboBox_14.addItem("12")
        self.comboBox_14.addItem("13")
        self.comboBox_14.addItem("14")
        self.comboBox_14.addItem("15")
        self.comboBox_14.addItem("16")
        self.comboBox_14.setCurrentIndex(13)

        self.horizontalLayout_15.addWidget(self.comboBox_14)
        self.horizontalLayoutWidget_16 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_16.setGeometry(QtCore.QRect(10, 440, 471, 22))
        self.horizontalLayoutWidget_16.setObjectName("horizontalLayoutWidget_16")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_16)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.test15 = QtWidgets.QLabel(self.horizontalLayoutWidget_16)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.test15.setFont(font)
        self.test15.setObjectName("test15")
        self.horizontalLayout_16.addWidget(self.test15)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem15)
        self.comboBox_15 = QtWidgets.QComboBox(self.horizontalLayoutWidget_16)
        self.comboBox_15.setObjectName("comboBox_15")

        self.comboBox_15.addItem("1")
        self.comboBox_15.addItem("2")
        self.comboBox_15.addItem("3")
        self.comboBox_15.addItem("4")
        self.comboBox_15.addItem("5")
        self.comboBox_15.addItem("6")
        self.comboBox_15.addItem("7")
        self.comboBox_15.addItem("8")
        self.comboBox_15.addItem("9")
        self.comboBox_15.addItem("10")
        self.comboBox_15.addItem("11")
        self.comboBox_15.addItem("12")
        self.comboBox_15.addItem("13")
        self.comboBox_15.addItem("14")
        self.comboBox_15.addItem("15")
        self.comboBox_15.addItem("16")
        self.comboBox_15.setCurrentIndex(14)

        self.horizontalLayout_16.addWidget(self.comboBox_15)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(440, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.set_values)

        self.get_values()
        self.pushButton_2.hide()
        if gui_global.admin_login:
            self.pushButton.hide()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Test Order"))
        self.label.setText(_translate("Form", "Test Order Sequence"))
        self.test1.setText(_translate("Form", "1. Unit Communication"))
        self.test2.setText(_translate("Form", "2. Temperature Measurement"))
        self.test3.setText(_translate("Form", "3. PFC Alarm Test"))
        self.test4.setText(_translate("Form", "4. SIM Registration"))
        self.test5.setText(_translate("Form", "5. DC Voltage Measurement"))
        self.test6.setText(_translate("Form", "6. DC Voltage Calibration/Verification"))
        self.test7.setText(_translate("Form", "7. DC Current Measurement (Discharging)"))
        self.test8.setText(_translate("Form", "8. LVD Contactor"))
        self.test9.setText(_translate("Form", "9. DG Logic"))
        self.test10.setText(_translate("Form", "10. SMR Communication"))
        self.test11.setText(_translate("Form", "11. DC SOurce/ Aviation Lamp"))
        self.test12.setText(_translate("Form", "12. Power Logic Test"))
        self.test13.setText(_translate("Form", "13. DC Current Measurement (Charging)"))
        self.test16.setText(_translate("Form", "16. Default"))
        self.test14.setText(_translate("Form", "14. DC Current Calibration/Verification"))
        self.test15.setText(_translate("Form", "15. Factory Restore"))
        self.pushButton.setText(_translate("Form", "SET"))
        self.pushButton_2.setText(_translate("Form", "GET"))

    def set_values(self):
        global l
        l = []
        current = {"1": str(self.comboBox_1.currentText()), "2": str(self.comboBox_2.currentText()),
                   "3": str(self.comboBox_3.currentText()), "4": str(self.comboBox_4.currentText()),
                   "5": str(self.comboBox_5.currentText()),
                   "6": str(self.comboBox_6.currentText()), "7": str(self.comboBox_7.currentText()),
                   "8": str(self.comboBox_8.currentText()), "9": str(self.comboBox_9.currentText()),
                   "10": str(self.comboBox_10.currentText()),
                   "11": str(self.comboBox_11.currentText()), "12": str(self.comboBox_12.currentText()),
                   "13": str(self.comboBox_13.currentText()), "14": str(self.comboBox_14.currentText()),
                   "15": str(self.comboBox_15.currentText()), "16": str(self.comboBox_16.currentText())}

        for i in range(1, len(current) + 1):
            l.append(current[str(i)])

        if len(l) == len(set(l)):
            with open(f"{gui_global.files_directory_location}test_order.txt", 'w') as f:
                for x in l:
                    f.write(x)
                    f.write(",")
        else:
            self.Message("Two or more test number is associated to multiple test parameters.")

    def Message(self, message):
        self.message = QtWidgets.QMessageBox()
        self.message.setWindowTitle('Error!')
        self.message.setText(message)
        self.message.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        self.message.exec_()

    def get_values(self):
        global l

        # import os
        # if os.path.exists(os.path.join(gui_global.files_directory_location, 'test_order.txt')):
        with open(f"{gui_global.files_directory_location}test_order.txt") as f:
            lines = f.readlines()

        var123 = lines[0].split(",")[0:16]

        setting = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9, "11": 10, "12": 11,
                   "13": 12, '14': 13, '15': 14, '16': 15}

        try:
            if var123[0] in setting.keys():
                # print setting[var123[0]]
                self.comboBox_1.setCurrentIndex(int(var123[0]) - 1)
        except:
            pass

        try:
            if var123[1] in setting.keys():
                # print setting[l[1]]
                self.comboBox_2.setCurrentIndex(int(var123[1]) - 1)
        except:
            pass

        try:
            if var123[2] in setting.keys():
                # print setting[l[2]]
                self.comboBox_3.setCurrentIndex(int(var123[2]) - 1)
        except:
            pass

        try:
            if var123[3] in setting.keys():
                # print setting[l[3]]
                self.comboBox_4.setCurrentIndex(int(var123[3]) - 1)
        except:
            pass

        try:
            if var123[4] in setting.keys():
                # print setting[l[4]]
                self.comboBox_5.setCurrentIndex(int(var123[4]) - 1)
        except:
            pass

        try:
            if var123[5] in setting.keys():
                # print setting[l[5]]
                self.comboBox_6.setCurrentIndex(int(var123[5]) - 1)
        except:
            pass

        try:
            if var123[6] in setting.keys():
                # print setting[l[6]]
                self.comboBox_7.setCurrentIndex(int(var123[6]) - 1)
        except:
            pass

        try:
            if var123[7] in setting.keys():
                # print setting[l[7]]
                self.comboBox_8.setCurrentIndex(int(var123[7]) - 1)
        except:
            pass

        try:
            if var123[8] in setting.keys():
                # print setting[l[8]]
                self.comboBox_9.setCurrentIndex(int(var123[8]) - 1)
        except:
            pass

        try:
            if var123[9] in setting.keys():
                # print setting[l[9]]
                self.comboBox_10.setCurrentIndex(int(var123[9]) - 1)
        except:
            pass

        try:
            if var123[10] in setting.keys():
                # print setting[l[10]]
                self.comboBox_11.setCurrentIndex(int(var123[10]) - 1)
        except:
            pass

        try:
            if var123[11] in setting.keys():
                # print setting[l[11]]
                self.comboBox_12.setCurrentIndex(int(var123[11]) - 1)
        except:
            pass

        try:
            if var123[12] in setting.keys():
                # print setting[l[12]]
                self.comboBox_13.setCurrentIndex(int(var123[12]) - 1)
        except:
            pass

        try:
            if var123[13] in setting.keys():
                # print setting[l[12]]
                self.comboBox_14.setCurrentIndex(int(var123[13]) - 1)
        except:
            pass

        try:
            if var123[14] in setting.keys():
                # print setting[l[12]]
                self.comboBox_15.setCurrentIndex(int(var123[14]) - 1)
        except:
            pass

        try:
            if var123[15] in setting.keys():
                # print setting[l[12]]
                self.comboBox_16.setCurrentIndex(int(var123[15]) - 1)
        except:
            pass

        return var123


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
