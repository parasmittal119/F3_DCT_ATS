import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import pyqtSignal, QObject
from report_gui import *


class WindowSignalHandler(QObject):
    openWindow = pyqtSignal()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Main Window")

        label = QLabel("Click <a href='openwindow'>here</a> to open another window.", self)
        label.setOpenExternalLinks(True)
        label.setTextInteractionFlags(label.textInteractionFlags() | Qt.TextBrowserInteraction)

        self.handler = WindowSignalHandler()
        self.handler.openWindow.connect(self.openNewWindow)
        label.linkActivated.connect(self.handleLinkActivation)

        self.setCentralWidget(label)

    def handleLinkActivation(self, link):
        if link == 'openwindow':
            self.handler.openWindow.emit()

    def openNewWindow(self):
        report = QtWidgets.QDialog()
        report.ui = Ui_report()
        report.ui.setupUi(report)
        report.exec_()
        report.show()

class NewWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("New Window")

        layout = QVBoxLayout()
        label = QLabel("This is a new window.")
        layout.addWidget(label)

        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
