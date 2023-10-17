import test_order_done
test_order = test_order_done.Ui_Form.get_values(test_order_done.Ui_Form)
import time
import os
from excel_automation import CSV
from config_done import *
import ByteConvertor
import CanModule
import CommandDCLoad
import gui_global
from M1000Telnet import Telnet
import M2000
from prompts import Prompt


class Test:
    def dut_serial_check(self):
        self.ui = test_script.Ui_Test()
        associate_name = self.ui.associate_name_edit.text()
        if associate_name == "":
            Prompt.Message(Prompt, "Error!", "Kindly enter NAME to proceed!")

