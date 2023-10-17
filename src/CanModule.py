import time

from can import Message
from can.interfaces.ixxat import IXXATBus, exceptions

import gui_global
from config_done import *

print("CAN Module file loaded")


class CAN:
    def __init__(self):
        self.bitrate = int(SettingRead('SETTING')['can device bitrate'])
        self.name = SettingRead('SETTING')['can device name']
        self.id = SettingRead('SETTING')['can device id']

    def CAN_WRITE(self, can_channel=0, message_id=0x610, packet: list = None):
        if packet is None:
            packet = []
        can_device_status = True

        count = 0

        while can_device_status and count < 3:
            count += 1

            try:
                bus = IXXATBus(channel=can_channel, can_filters=[{"can_id": 0x00, "can_mask": 0x000}], bitrate=self.bitrate)

            except exceptions.VCIDeviceNotFoundError:
                bus = None

            try:
                if gui_global.APP_STOP_FLAG == True:
                    return None
                message = Message(arbitration_id=message_id, is_extended_id=False, data=packet)
                bus.send(message)
                time.sleep(0.2)
                bus.shutdown()
                gui_global.CLEAR_JIG_FLAG = True

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
                               bitrate=self.bitrate)

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
