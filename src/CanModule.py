import time

from can import Message
from can.interfaces.ixxat import IXXATBus, exceptions

import gui_global
from config_done import *

print("CAN Module file loaded")
global serial_no_packet

serial_no_packet = []



class CAN:
    def __init__(self):
        self.bitrate = 250000  # int(SettingRead('SETTING')['can device bitrate'])
        self.name = SettingRead('SETTING')['can device name']
        self.id = SettingRead('SETTING')['can device id']


    def CAN_WRITE(self, can_channel=0, message_id=0x610, packet: list = None):
        global serial_no_packet
        if packet is None:
            packet = []
        can_device_status = True

        count = 0

        while can_device_status and count < 3:
            count += 1

            try:
                bus = IXXATBus(channel=can_channel, can_filters=[{"can_id": 0x00, "can_mask": 0x000}], bitrate=250000)

            except exceptions.VCIDeviceNotFoundError:
                bus = None

            try:
                if gui_global.APP_STOP_FLAG == True:
                    return None
                if message_id == 1791:
                    message = Message(arbitration_id=message_id, is_extended_id=False, data=[64, 1, 64, 0, 0, 0, 0, 0])
                    print(message)
                    bus.send(message)
                    time.sleep(0.2)
                    msg = bus.recv()
                    if msg.arbitration_id == 1663:
                        value_temp = msg.data.hex()

                        for i in range(0,len(value_temp), 2):
                            serial_no_packet.append(value_temp[i:i+2])

                    print(serial_no_packet)

                elif message_id == 770:
                    message = Message(arbitration_id=message_id, is_extended_id= False, data=[int(serial_no_packet[4], 16), int(serial_no_packet[5], 16), int(serial_no_packet[6], 16), int(serial_no_packet[7], 16), 16, 0, 0, 0])
                    print(message)
                    bus.send(message)
                    time.sleep(0.1)
                    # msg = bus.recv()
                    # if msg.arbitration_id == 386:
                    #     print(msg.data.hex())

                elif message_id == 1552:
                    message = Message(arbitration_id=message_id, is_extended_id=False, data=packet)
                    print(message)
                    bus.send(message)
                    time.sleep(0.1)
                    msg = bus.recv()
                    print(msg)

                bus.shutdown()
                gui_global.CLEAR_JIG_FLAG = True
                count = 3

            except (Exception, AttributeError) as err:
                print(err)
                gui_global.CLEAR_JIG_FLAG = False
                can_device_status = True
                print("CAN-USB Convertor not connected")

    def CAN_READ(self, can_channel=0, message_id=0x610, packet=None, check_id=None):
        global data
        if packet is None:
            packet = []

        can_device_status = True

        count = 0

        while can_device_status and count < 3:
            count += 1

            try:
                bus = IXXATBus(channel=can_channel, can_filters=[{"can_id": 0x00, "can_mask": 0x000}],
                               bitrate=250000)

            except exceptions.VCIDeviceNotFoundError:
                bus = None

            try:
                if gui_global.APP_STOP_FLAG == True:
                    return None
                message = Message(arbitration_id=message_id, is_extended_id=False, data=packet)
                bus.send(message)
                time.sleep(0.2)

                msg = bus.recv()
                if check_id is None:
                    data = msg.data

                elif check_id == msg.arbitration_id:
                    data = msg.data

                bus.shutdown()
                gui_global.CLEAR_JIG_FLAG = True
                return data

            except (Exception, AttributeError) as err:
                print(err)
                gui_global.CLEAR_JIG_FLAG = False
                can_device_status = True
                print("CAN-USB Convertor not connected")


# print(CAN.CAN_READ(CAN, 0,1791, [43,1,32,00,00,00,00,00]))