# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Test_script.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import gui_global


class Ui_test(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1402, 778)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(390, 27, 521, 51))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.heading = QtWidgets.QLabel(self.groupBox)
        self.heading.setGeometry(QtCore.QRect(0, 0, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.heading.setFont(font)
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 150, 301, 461))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(130, 60, 151, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 90, 151, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 120, 151, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 150, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 180, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 180, 151, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 150, 151, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(110, 220, 171, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(110, 250, 171, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(20, 250, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 220, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setGeometry(QtCore.QRect(20, 30, 91, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 280, 141, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setGeometry(QtCore.QRect(150, 280, 141, 21))
        self.checkBox_3.setObjectName("checkBox_3")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar.setGeometry(QtCore.QRect(20, 340, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.progressBar.setFont(font)
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(20, 310, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 380, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 380, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(390, 100, 521, 571))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(70, 50, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(430, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(10, 50, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(20, 80, 21, 31))
        self.label_10.setObjectName("label_10")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(70, 85, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(430, 80, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(20, 110, 21, 31))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(20, 140, 21, 31))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setGeometry(QtCore.QRect(20, 170, 21, 31))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.groupBox_3)
        self.label_19.setGeometry(QtCore.QRect(20, 200, 21, 31))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_3)
        self.label_20.setGeometry(QtCore.QRect(20, 230, 21, 31))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        self.label_21.setGeometry(QtCore.QRect(20, 260, 21, 31))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(20, 290, 21, 31))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setGeometry(QtCore.QRect(20, 320, 31, 31))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.groupBox_3)
        self.label_24.setGeometry(QtCore.QRect(20, 350, 21, 31))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.groupBox_3)
        self.label_25.setGeometry(QtCore.QRect(20, 380, 21, 31))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox_3)
        self.label_26.setGeometry(QtCore.QRect(70, 110, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.groupBox_3)
        self.label_27.setGeometry(QtCore.QRect(70, 140, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.groupBox_3)
        self.label_28.setGeometry(QtCore.QRect(70, 170, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.groupBox_3)
        self.label_29.setGeometry(QtCore.QRect(70, 200, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.groupBox_3)
        self.label_30.setGeometry(QtCore.QRect(70, 230, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.groupBox_3)
        self.label_31.setGeometry(QtCore.QRect(70, 260, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.groupBox_3)
        self.label_32.setGeometry(QtCore.QRect(70, 290, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.groupBox_3)
        self.label_33.setGeometry(QtCore.QRect(70, 320, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.groupBox_3)
        self.label_34.setGeometry(QtCore.QRect(70, 350, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.groupBox_3)
        self.label_35.setGeometry(QtCore.QRect(70, 380, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.groupBox_3)
        self.label_36.setGeometry(QtCore.QRect(70, 410, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.groupBox_3)
        self.label_37.setGeometry(QtCore.QRect(70, 440, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.groupBox_3)
        self.label_38.setGeometry(QtCore.QRect(70, 470, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.groupBox_3)
        self.label_39.setGeometry(QtCore.QRect(70, 500, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.groupBox_3)
        self.label_40.setGeometry(QtCore.QRect(70, 530, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.groupBox_3)
        self.label_41.setGeometry(QtCore.QRect(20, 410, 21, 31))
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.groupBox_3)
        self.label_42.setGeometry(QtCore.QRect(20, 440, 21, 31))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.groupBox_3)
        self.label_43.setGeometry(QtCore.QRect(20, 470, 21, 31))
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.groupBox_3)
        self.label_44.setGeometry(QtCore.QRect(20, 500, 21, 31))
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.groupBox_3)
        self.label_45.setGeometry(QtCore.QRect(20, 530, 21, 31))
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.groupBox_3)
        self.label_46.setGeometry(QtCore.QRect(430, 110, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.groupBox_3)
        self.label_47.setGeometry(QtCore.QRect(430, 140, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.groupBox_3)
        self.label_48.setGeometry(QtCore.QRect(430, 170, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.groupBox_3)
        self.label_49.setGeometry(QtCore.QRect(430, 200, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.groupBox_3)
        self.label_50.setGeometry(QtCore.QRect(430, 230, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.groupBox_3)
        self.label_51.setGeometry(QtCore.QRect(430, 260, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.groupBox_3)
        self.label_52.setGeometry(QtCore.QRect(430, 290, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.groupBox_3)
        self.label_53.setGeometry(QtCore.QRect(430, 320, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.groupBox_3)
        self.label_54.setGeometry(QtCore.QRect(430, 350, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.groupBox_3)
        self.label_55.setGeometry(QtCore.QRect(430, 380, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.groupBox_3)
        self.label_56.setGeometry(QtCore.QRect(430, 410, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.groupBox_3)
        self.label_57.setGeometry(QtCore.QRect(430, 440, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(self.groupBox_3)
        self.label_58.setGeometry(QtCore.QRect(430, 470, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_58.setFont(font)
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.groupBox_3)
        self.label_59.setGeometry(QtCore.QRect(430, 530, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.default_pending = QtWidgets.QLabel(self.groupBox_3)
        self.default_pending.setGeometry(QtCore.QRect(430, 500, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setUnderline(False)
        self.default_pending.setFont(font)
        self.default_pending.setObjectName("default_pending")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(980, 80, 341, 481))
        self.textEdit.setObjectName("textEdit")
        self.test_log = QtWidgets.QLabel(self.centralwidget)
        self.test_log.setGeometry(QtCore.QRect(980, 40, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.test_log.setFont(font)
        self.test_log.setObjectName("test_log")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1240, 50, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_62 = QtWidgets.QLabel(self.centralwidget)
        self.label_62.setGeometry(QtCore.QRect(70, 10, 161, 51))
        self.label_62.setText("")
        self.label_62.setPixmap(QtGui.QPixmap(""))
        self.label_62.setScaledContents(True)
        self.label_62.setObjectName("label_62")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(980, 580, 341, 71))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_4.setStyleSheet("border:1px solid black")

        self.final_status = QtWidgets.QLabel(self.groupBox_4)
        self.final_status.setGeometry(QtCore.QRect(0, 0, 341, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.final_status.setFont(font)
        self.final_status.setAlignment(QtCore.Qt.AlignCenter)
        self.final_status.setObjectName("final_status")

        # self.label_65 = QtWidgets.QLabel(self.centralwidget)
        # self.label_65.setGeometry(QtCore.QRect(80, 10, 181, 51))
        # self.label_65.setText("")
        # self.label_65.setPixmap(QtGui.QPixmap(f"{gui_global.image_directory_location}exicome logo.png"))
        # self.label_65.setScaledContents(True)
        # self.label_65.setObjectName("label_65")
        self.label_63 = QtWidgets.QLabel(self.centralwidget)
        self.label_63.setGeometry(QtCore.QRect(50, 50, 251, 71))
        self.label_63.setText("")
        self.label_63.setPixmap(QtGui.QPixmap(f"{gui_global.image_directory_location}exicome logo.png"))
        self.label_63.setScaledContents(True)
        self.label_63.setAlignment(QtCore.Qt.AlignCenter)
        self.label_63.setObjectName("label_63")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.heading.setText(_translate("MainWindow", "Power Plant Production ATS"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Test Details"))
        self.label_2.setText(_translate("MainWindow", "Test ID"))
        self.label_3.setText(_translate("MainWindow", "System Part No."))
        self.label_4.setText(_translate("MainWindow", "DUT Serial No."))
        self.label_5.setText(_translate("MainWindow", "Customer Name"))
        self.label_6.setText(_translate("MainWindow", "Associate Name"))
        self.label_7.setText(_translate("MainWindow", "End Time"))
        self.label_8.setText(_translate("MainWindow", "Start Time"))
        self.checkBox.setText(_translate("MainWindow", "Bar Code"))
        self.checkBox_2.setText(_translate("MainWindow", "Custom Settings"))
        self.checkBox_3.setText(_translate("MainWindow", "Manual Resources"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline; color:#00aa00;\">Test Progress:</span></p></body></html>"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_2.setText(_translate("MainWindow", "STOP"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Test Program"))
        self.label_11.setText(_translate("MainWindow", "Test Item"))
        self.label_12.setText(_translate("MainWindow", "Status"))
        self.label_13.setText(_translate("MainWindow", "S No."))
        self.label_10.setText(_translate("MainWindow", "1"))
        self.label_14.setText(_translate("MainWindow", "Controller Health"))
        self.label_15.setText(_translate("MainWindow", "Pending"))
        self.label_16.setText(_translate("MainWindow", "2"))
        self.label_17.setText(_translate("MainWindow", "3"))
        self.label_18.setText(_translate("MainWindow", "4"))
        self.label_19.setText(_translate("MainWindow", "5"))
        self.label_20.setText(_translate("MainWindow", "6"))
        self.label_21.setText(_translate("MainWindow", "7"))
        self.label_22.setText(_translate("MainWindow", "8"))
        self.label_23.setText(_translate("MainWindow", "9"))
        self.label_24.setText(_translate("MainWindow", "10"))
        self.label_25.setText(_translate("MainWindow", "11"))
        self.label_26.setText(_translate("MainWindow", "Unit Communication"))
        self.label_27.setText(_translate("MainWindow", "Temperature Measurement"))
        self.label_28.setText(_translate("MainWindow", "Output PFC"))
        self.label_29.setText(_translate("MainWindow", "Input PFC"))
        self.label_30.setText(_translate("MainWindow", "DC Voltage Measurement"))
        self.label_31.setText(_translate("MainWindow", "DC Voltage Calibration/Verification"))
        self.label_32.setText(_translate("MainWindow", "DC Current Measurement (Discharge)"))
        self.label_33.setText(_translate("MainWindow", "SMR Registration"))
        self.label_34.setText(_translate("MainWindow", "DC Current Measurement (Charge)"))
        self.label_35.setText(_translate("MainWindow", "DC Current Calibration/Verification"))
        self.label_36.setText(_translate("MainWindow", "LVD Contactor"))
        self.label_37.setText(_translate("MainWindow", "AC Phase Allocation"))
        self.label_38.setText(_translate("MainWindow", "Current Sharing / Bus Drop"))
        self.label_39.setText(_translate("MainWindow", "RS485"))
        self.label_40.setText(_translate("MainWindow", "Default"))
        self.label_41.setText(_translate("MainWindow", "12"))
        self.label_42.setText(_translate("MainWindow", "13"))
        self.label_43.setText(_translate("MainWindow", "14"))
        self.label_44.setText(_translate("MainWindow", "15"))
        self.label_45.setText(_translate("MainWindow", "16"))
        self.label_46.setText(_translate("MainWindow", "Pending"))
        self.label_47.setText(_translate("MainWindow", "Pending"))
        self.label_48.setText(_translate("MainWindow", "Pending"))
        self.label_49.setText(_translate("MainWindow", "Pending"))
        self.label_50.setText(_translate("MainWindow", "Pending"))
        self.label_51.setText(_translate("MainWindow", "Pending"))
        self.label_52.setText(_translate("MainWindow", "Pending"))
        self.label_53.setText(_translate("MainWindow", "Pending"))
        self.label_54.setText(_translate("MainWindow", "Pending"))
        self.label_55.setText(_translate("MainWindow", "Pending"))
        self.label_56.setText(_translate("MainWindow", "Pending"))
        self.label_57.setText(_translate("MainWindow", "Pending"))
        self.label_58.setText(_translate("MainWindow", "Pending"))
        self.label_59.setText(_translate("MainWindow", "Pending"))
        self.default_pending.setText(_translate("MainWindow", "RS485Pending"))
        self.test_log.setText(_translate("MainWindow", "Test Log"))
        self.final_status.setText(_translate("MainWindow", ""))
        self.pushButton_3.setText(_translate("MainWindow", "Log Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_test()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
