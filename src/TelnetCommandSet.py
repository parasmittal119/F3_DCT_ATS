from __future__ import absolute_import
from __future__ import print_function

import telnetlib
import time
from builtins import str

from config_done import *

OID_Mains_Low_Fail_SET = 'TAB.5003.0'
OID_Mains_Low_Fail_RESTORE = 'TAB.5005.0'
OID_Mains_High_Fail_SET = 'TAB.5002.0'
OID_Mains_High_Fail_RESTORE = 'TAB.5004.0'

OID_Mains_Low_SET = 'TAB.1428.0'
OID_Mains_Low_RESTORE = 'TAB.1429.0'
OID_Mains_High_SET = 'TAB.1426.0'
OID_Mains_High_RESTORE = 'TAB.1427.0'

newRJIL = False
telnet = telnetlib.Telnet()


def set_isnewrjil(controller=False):
    global newRJIL
    newRJIL = controller


def get_isnewrjil():
    global newRJIL
    return newRJIL


def open_telnet():
    global telnet
    PORT_NOT_OPEN = True
    PORT_STATUS = False
    count = 0
    while PORT_NOT_OPEN and count < 3:
        count += 1
        hostserver = SettingRead('SETTING')['m1000_ip address']
        newline = "\n"
        username = SettingRead('SETTING')['m1000_user'] + newline
        if newRJIL:
            password = SettingRead('SETTING')['m1000_rjilpwd'] + newline
        else:
            password = SettingRead('SETTING')['m1000_password'] + newline
        try:

            telnet = telnetlib.Telnet(hostserver)
            print("server contacted")
            telnet.read_until(b'Login: ')
            telnet.write(bytes(username, 'utf-8') + bytes(newline, 'utf-8'))
            telnet.read_until(b"Password: ")
            telnet.write(bytes(password, 'utf-8') + bytes(newline, 'utf-8'))
            print("done")
            out1 = telnet.read_until(b'>')
            if b'Logged in successfully' in out1:
                PORT_NOT_OPEN = False
                PORT_STATUS = True
                break
        except OSError:
            PORT_STATUS = False
            PORT_NOT_OPEN = True
            print("Telnet not open/controller power off")
            time.sleep(2)

    return PORT_STATUS


def telnet_get_command(command):
    DATA_NOT_RECIEVED = True
    OID_Value = ''
    newline = "\n"
    count = 0
    while DATA_NOT_RECIEVED and count < 5:
        count += 1
        try:
            global telnet
            telnet.write(b'GET ' + bytes(command, 'utf-8') + bytes(newline, 'utf-8'))
            if command == "TAB.31.0" or command == "TAB.32.0" or command == "TAB.35.0":
                OID_Value = 0
                break
            out = telnet.read_until(b">", 5)
            if bytes(newline, 'utf-8') in out:
                splitted_lines = out.splitlines()
                if len(splitted_lines) > 2:
                    splitted_variable = splitted_lines[2]
                    extract_variable = splitted_variable.split(b' ', 1)
                    OID = extract_variable[0]
                    OID_Value = extract_variable[1]
                    OID_Value = OID_Value.decode('utf-8')
                    if OID_Value != b'':
                        DATA_NOT_RECIEVED = False
                        time.sleep(0.100)
                        break
        except Exception as err:
            OID_Value = None
            DATA_NOT_RECIEVED = True
            print(err)
            print("Telnet connection error.Reconnecting...")
            close_telnet()
            connection_status = open_telnet()
    return OID_Value


def telnet_set_command(command, value):
    OID_Value = ''
    value = str(value)
    DATA_NOT_RECIEVED = True
    newline = "\n"
    count = 0
    while DATA_NOT_RECIEVED and count < 5:
        count += 1

        try:
            global telnet
            telnet.write(bytes('SET ', 'utf-8') + bytes(command, 'utf-8') + b' ' + bytes(value, 'utf-8') + bytes(newline, 'utf-8'))
            if command == "TAB.31.0" or command == "TAB.32.0" or command == "TAB.35.0":  # to keep trying while rebooting
                print("Controller rebooted. Please wait...")
                time.sleep(6)
                OID_Value = 0
                count = 6
                break
            out = telnet.read_until(b">", 3)

            if bytes(newline, 'utf-8') in out:
                splitted_lines = out.splitlines()
                if len(splitted_lines) > 2:
                    splitted_variable = splitted_lines[2]
                    extract_variable = splitted_variable.split(b' ', 1)
                    OID = extract_variable[0]
                    OID_Value = extract_variable[1]
                    if OID_Value != b'':
                        DATA_NOT_RECIEVED = False
                        print("OID: " + str(OID))
                        print("Value: " + str(OID_Value))
                        break
                    else:
                        DATA_NOT_RECIEVED = True
                else:
                    DATA_NOT_RECIEVED = True

        except OSError:
            OID_Value = None
            DATA_NOT_RECIEVED = True
            print("Telnet connection error.Reconnecting...")
            close_telnet()
            connection_status = open_telnet()
    return OID_Value


def close_telnet():
    try:
        global telnet
        telnet.close()
        del telnet
        print("Telnet Closed")
    except OSError:
        print("telnet is already closed")
        pass


if __name__ == "__main__":
    open_telnet()
    telnet_set_command('TAB.31.0', '1')  # set initialize
    # TELNET_SET_COMMAND(OIDRead('SYSTEM COMMANDS')['ate test'],"TEST_M1000_ATE")
    # print(telnet_get_command(OIDRead('SYSTEM COMMANDS')['part number']))
    # print(telnet_get_command(OIDRead('SYSTEM COMMANDS')['m1000 mac id']))
    # print(telnet_get_command(OIDRead('SYSTEM COMMANDS')['software version']))
    print(telnet_get_command(OIDRead('SYSTEM COMMANDS')['bootloader version']))
    # print(telnet_get_command(OIDRead('SYSTEM COMMANDS')['config file version']))
    for i in range(4):
        print(telnet_get_command("TAB.393.0"))

    print(telnet_get_command("TAB.394.0"))
    print(telnet_set_command("TAB.31.0", '1'))
    print(telnet_get_command('TAB.390.0'))
    # telnet_set_command(OIDRead('SYSTEM COMMANDS')['factory restore'], 1)
    # print float(TELNET_GET_COMMAND(OIDRead('BATTERY SETTING')['lion charge voltage']))
    # TELNET_SET_COMMAND(OIDRead('BATTERY SETTING')['lion charge voltage'],54)
#     print int(TELNET_GET_COMMAND(OIDRead('ALARM')['batt1 fuse fail']))
#     print int(TELNET_GET_COMMAND(OIDRead('ALARM')['batt2 fuse fail']))
#     print int(TELNET_GET_COMMAND(OIDRead('ALARM')['batt3 fuse fail']))
# TELNET_SET_COMMAND(OIDRead('LOAD ISOLATE')['load1'],1)
# TELNET_SET_COMMAND('TAB.31.0',1)
##    fuelsensor_comm_port=int(ConfigRead('DUT CONFIGURATION')['fuel sensor comm'])
##    print fuelsensor_comm_port
##    fuel_sensor_comm_port=int(TELNET_GET_COMMAND(OIDRead('RS 485')['fuel sensor comm']))
##    print fuel_sensor_comm_port
####    while 1:
##        TELNET_SET_COMMAND(OIDRead('SYSTEM COMMANDS')['ate test'],"TEST_M1000_ATE")
##        #TELNET_SET_COMMAND('TAB.180A.0',64)
##        TELNET_SET_COMMAND('TAB.55.0', 255)
# CLOSE_TELNET()

##    TELNET_SET_COMMAND('TAB.55.0', 2)
##    time.sleep(1)
##    TELNET_SET_COMMAND('TAB.55.0', 4)
##    time.sleep(1)
##    TELNET_SET_COMMAND('TAB.55.0', 8)
##    time.sleep(1)
##    TELNET_SET_COMMAND('TAB.55.0', 16)
##    time.sleep(1)
##    TELNET_SET_COMMAND('TAB.55.0', 32)
##    time.sleep(1)
##    TELNET_SET_COMMAND('TAB.55.0', 64)
##    time.sleep(1)
##    TELNET_SET_COMMAND('TAB.55.0', 128)
# print TELNET_GET_COMMAND('TAB.040C.AF')


# print Telnet_get_command('TAB.040C.AF')
# Telnet_set_command('TAB.54.0', 64)
# print Telnet_get_command('TAB.040C.AF')
