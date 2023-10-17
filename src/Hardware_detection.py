import can
import serial.tools.list_ports
from can.interfaces.ixxat import IXXATBus

import gui_global
from config_done import PFCRead, SettingRead
from prompts import Prompt


def HardwareSettingRead():
    if str(SettingRead("SETTING")['dc load usb id']) != str(SettingRead("SETTING")['battery load usb id']):
        Prompt.Message(Prompt, "Warning", "Load USB ID mismatch found!, Kindly correct")
        return True
    elif SettingRead('SETTING')['rs485 lower port'] == SettingRead('SETTING')['rs485 upper port'] or \
            SettingRead('SETTING')['modbus comm port'] == SettingRead('SETTING')['modbus comm port 2']:
        Prompt.Message(Prompt, "Warning", " COM Port wrongly assigned")
        return True
    elif (SettingRead('SETTING')['m1000_ip address'] or SettingRead('SETTING')['m1000_user'] or SettingRead('SETTING')[
        'm1000_password'] or SettingRead('SETTING')['m2000_ip address'] or SettingRead('SETTING')['m2000_user'] or
          SettingRead('SETTING')['m2000_password'] or SettingRead('SETTING')['db user'] or SettingRead('SETTING')[
              'db password']) == "":
        Prompt.Message(Prompt, "Warning", "Can't proceed with blanks in Hardware Setting")
        return True
    else:
        return False


def list_ports():
    try:
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]
    except Exception:
        return False


def detect_ixxat_can_devices():
    try:
        bus = IXXATBus(bustype='ixxat', channel=0)
        bus.shutdown()
        return False
    except can.CanError as e:
        print(e)
        return True


def ReadPFC():
    pfc_1 = []

    pfc_2 = []

    SectionHead = PFCRead("PFC 1 PFC")
    parameter_1 = [SectionHead['p_load'], SectionHead['r_phase'], SectionHead['n_p_load_1'], SectionHead['y_phase'],
                   SectionHead['n_p_load_2'], SectionHead['b_phase'],
                   SectionHead['n_p_load_3'], SectionHead['bus'], SectionHead['n_p_load_4'],
                   SectionHead['load_mains'],
                   SectionHead['battery_1'], SectionHead['battery_mains'],
                   SectionHead['battery_2'], SectionHead['add_on_1'], SectionHead['battery_3'],
                   SectionHead['add_on_2']]

    SectionHead = PFCRead("PFC 2 PFC")
    parameter_2 = [SectionHead['pfc 1'], SectionHead['pfc 2'], SectionHead['pfc 3'], SectionHead['pfc 4'],
                   SectionHead['pfc 5'], SectionHead['pfc 6'],
                   SectionHead['pfc 7'], SectionHead['pfc 8'], SectionHead['pfc 9'], SectionHead['pfc 10'],
                   SectionHead['pfc 11'], SectionHead['pfc 12'],
                   SectionHead['pfc 13'], SectionHead['pfc 14'], SectionHead['pfc 15'], SectionHead['pfc 16']]

    for i in parameter_1:
        pfc_1.append(i)

    for i in parameter_2:
        pfc_2.append(i)

    if len(pfc_1) == len(set(pfc_1)) and (len(pfc_2) == len(set(pfc_2))):
        return False
    else:
        # Prompt.Message(Prompt, "Runtime Error", "Can't proceed because one PFC is assigned to Two or more Parameters")
        return True


def Hardware_check():
    available_ports = list_ports()


    if available_ports == []:
        gui_global.port_status = False # True
    else:
        gui_global.port_status = False

    if gui_global.commissioning_status:
        gui_global.pfc_status = ReadPFC()
        gui_global.hardware_status = HardwareSettingRead()

    gui_global.can_status = False # detect_ixxat_can_devices()


    if gui_global.pfc_status or gui_global.can_status or gui_global.port_status or gui_global.hardware_status:
        return False
    else:
        return True
