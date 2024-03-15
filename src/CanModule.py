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
        message_id = packet[0]
        global serial_no_packet, value_temp
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
                print(f"packet data {packet}")
                if gui_global.APP_STOP_FLAG == True:
                    return None
                if message_id == 1791:
                    value_flag = True
                    count = 0
                    while value_flag and count < 5:
                        message = Message(arbitration_id=message_id, is_extended_id=False, data=[packet[3], packet[4], packet[5], packet[6], packet[7], packet[8], packet[9], packet[10]])
                        print(message)
                        bus.send(message)
                        # time.sleep(0.2)
                        msg = bus.recv()
                        print(msg)
                        if msg.arbitration_id == 1663:
                            value_temp = msg.data.hex()
                            value_flag = False

                    for i in range(0, len(value_temp), 2):
                        serial_no_packet.append(value_temp[i:i+2])

                    print(serial_no_packet)
                    bus.shutdown()
                    return serial_no_packet

                elif message_id == 770:
                    value_flag = True
                    count = 0
                    while value_flag and count < 5:
                        message = Message(arbitration_id=message_id, is_extended_id= False, data=[int(packet[4], 16), int(packet[5], 16), int(packet[6], 16), int(packet[7], 16), 16, 0, 0, 0])
                        print("value of 770 or 302 id is" + str(message))
                        bus.send(message)
                        count += 1
                        # time.sleep(0.1)
                        msg = bus.recv(2)
                        print(f"value of 302 received msg is : {msg}")
                        if msg is None:
                            pass
                        elif msg.arbitration_id == 386:
                            print("value " + str(msg))
                            value_flag = False
                        # if msg.arbitration_id == 386:
                        #     print(msg.data.hex())

                    bus.shutdown()
                    return "passed"

                elif message_id == 1552:
                    value_flag = True
                    count = 0
                    while value_flag and count < 5:
                        message = Message(arbitration_id=message_id, is_extended_id=False, data=packet)
                        print(message)
                        bus.send(message)
                        count += 1
                        print(bus.recv(4))
                    bus.shutdown()
                    return "passed"
                else:
                    value_flag = True
                    count = 0
                    while value_flag and count < 5:
                        break
                gui_global.CLEAR_JIG_FLAG = True
                count = 3


            except (Exception, AttributeError) as err:
                bus.shutdown()
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