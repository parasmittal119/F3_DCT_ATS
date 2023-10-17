import time

import exception
import serial
import pyvisa
from config_done import *

global port_number
port_number = 27

import pyvisa_py


id = '*IDN?\n'
read_op_current = 'MEAS:CURR?\n'
read_op_voltage = 'MEAS:VOLT?\n'
read_op_power = 'MEAS:POW?\n'
rem_ON = 'CONF:REM ON\n'
rem_OFF = 'CONF:REM OFF\n'
load_OFF = 'LOAD OFF\n'
load_ON = 'LOAD ON\n'
set_load_sense = 'MEAS:INP UUT\n'
read_load_sense = 'MEAS:INP?\n'
voltage_ON_condition = 'CONF:VOLT:ON 40\n'
voltage_latch_ON = 'CONF:VOLT:LATC ON\n'
set_CR_mode = 'MODE CRH\n'
read_CR_mode = 'MODE?\n'
set_CR_A = 'RES 1\n'
set_CR_resistance = 'RES:L1'
set_CC_mode = 'MODE CCH\n'
set_CC_current = 'CURR:STAT:L1'
RESET = '*RST\n'


class DC_Load:
    def __init__(self):
        self.DCLoadPort = SettingRead('SETTING')['dc load port']
        self.DCBatteryPort = SettingRead('SETTING')['battery load port']
        self.baudrate = int(SettingRead('SETTING')['dc load usb baudrate'])

    def DCLoadSet(self, command, load_type="LOAD"):
        if load_type == "LOAD":
            self.port = self.DCLoadPort
        elif load_type == "BATT":
            self.port = self.DCBatteryPort

        Datain_check = True
        port_check = True

        while Datain_check:
            while port_check:
                try:
                    try:
                        print(load_type)
                        print("Port opening...")
                        global se
                        se = serial.Serial(port=self.DCLoadPort, baudrate=self.baudrate,
                                           bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                                           stopbits=serial.STOPBITS_ONE, timeout=0.1,
                                           xonxoff=False, writeTimeout=1, rtscts=False, dsrdtr= False
                                           , interCharTimeout=None)
                        port_check = False
                    except serial.SerialException:
                        print("Port not found or could not be open")
                        port_check = True
                        print("Closing port")
                        se.close()

                        time.sleep(2)
                        pass
                except exception.ValueError:
                    print("port already open")
                    pass


        try:
            try:
                se.write(rem_ON)
                time.sleep(1)
                outputstr = command
                se.write(outputstr)
                se.write(rem_OFF)
                print("Port Closed")
                se.close()
                Datain_check = False

            except serial.SerialException:
                print("Device communicating to the system is not functioning")
                Datain_check = True
                port_check = True
                time.sleep(2)
                pass
        except exception.IOError:
            Datain_check = True
            port_check = True
            print("No Communication with the instrument (no answer)")
            time.sleep(2)
            pass

    def DCLoadRead(self, command, load_type = "LOAD"):
        if load_type == "LOAD":
            self.port = self.DCLoadPort
        elif load_type == "BATT":
            self.port = self.DCBatteryPort

        Datain_check = True
        port_check = True

        while Datain_check:
            while port_check:
                try:
                    try:
                        print(load_type)
                        print("Port opening...")
                        global se
                        se = serial.Serial(port=self.DCLoadPort, baudrate=self.baudrate,
                                           bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                                           stopbits=serial.STOPBITS_ONE, timeout=0.1,
                                           xonxoff=False, writeTimeout=1, rtscts=False, dsrdtr=False
                                           , interCharTimeout=None)
                        port_check = False
                    except serial.SerialException:
                        print("Port not found or could not be open")
                        port_check = True
                        print("Closing port")
                        se.close()

                        time.sleep(2)
                        pass
                except exception.ValueError:
                    print("port already open")
                    pass

        try:
            try:
                se.write(bytearray(command))
                data = se.readline()
                if data!="":
                    se.close()
                    print("port closed")
                    Datain_check = False
                    return data
            except serial.SerialException:
                print("Device communicating to the system is not functioning")
                Datain_check = True
                port_check = True
                time.sleep(2)
                pass
        except exception.IOError:
            Datain_check = True
            port_check = True
            print("No communication with the instrument (no answer)")
            pass

# DC_Load.DCLoadRead(DC_Load, "*IDN?")
# rm = pyvisa.ResourceManager()
# print(rm.list_resources())
# inst = rm.open_resource("GPIB0::14::INSTR")

value = serial.Serial(port="GPIB0::14::INSTR")
# print(inst.query("*IDN?"))

# rm = pyvisa_py.PyVisaLibrary()
# print(rm.list_resources())
