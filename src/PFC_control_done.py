import time

from can import Message
from can.interfaces.ixxat import IXXATBus, exceptions

PFC1 = "PFC1"  # 1
PFC2 = "PFC2"  # 2
PFC3 = "PFC3"  # 4
PFC4 = "PFC4"  # 8
PFC5 = "PFC5"  # 16
PFC6 = "PFC6"  # 32
PFC7 = "PFC7"  # 64
PFC8 = "PFC8"  # 128
PFC9 = "PFC9"  # 1
PFC10 = "PFC10"  # 2
PFC11 = "PFC11"  # 4
PFC12 = "PFC12"  # 8
PFC13 = "PFC13"  # 16
PFC14 = "PFC14"  # 32
PFC15 = "PFC15"  # 64
PFC16 = "PFC16"  # 128
STOP = "STOP"  # 0


class pfc_control:
    stop_all = 00
    pfc_list_upper = {"STOP": 0, "PFC1": 1, "PFC2": 2, "PFC3": 4, "PFC4": 8, "PFC5": 16, "PFC6": 32, "PFC7": 64, "PFC8": 128}
    pfc_list_lower = {"STOP": 0, "PFC9": 1, "PFC10": 2, "PFC11": 4, "PFC12": 8, "PFC13": 16, "PFC14": 32, "PFC15": 64,
                      "PFC16": 128}
    CARD1 = 1546
    CARD2 = 1547

    def __init__(self):
        self.can_channel = None

    @staticmethod
    def pfc_set(can_channel, card_id, cont):
        cont1 = 0
        cont2 = 0

        try:
            # bus = can.interface.Bus(interface="seeedstudio", channel=0,)
            bus = IXXATBus(channel=can_channel, can_filters=[{"can_id": 0x00, "can_mask": 0x000}], bitrate=250000)

        except exceptions.VCIDeviceNotFoundError:
            bus = None

        try:
            for x in cont:
                if x in pfc_control.pfc_list_upper:
                    cont1 += pfc_control.pfc_list_upper[x]

            for x in cont:
                if x in pfc_control.pfc_list_lower:
                    cont2 += pfc_control.pfc_list_lower[x]

            op_enable_msg = Message(arbitration_id=card_id, is_extended_id=False,
                                    data=[0x2B, 0x00, 0x20, 0x00, cont1, cont2, 0, 0])

            bus.send(op_enable_msg)

            time.sleep(0.5)

            print(op_enable_msg)

            bus.shutdown()

        except AttributeError:
            print(cont)


    @staticmethod
    def read_pfc(card_id, pfc_number):
        try:
            bus = IXXATBus(channel=can_channel, can_filters=[{"can_id": 0x00, "can_mask": 0x000}], bitrate=250000)

        except exceptions.VCIDeviceNotFoundError:
            bus = None

        try:
            packet = PFC_IP_READ_PACKET()
            op_enable_msg = Message(arbitration_id=card_id, is_extended_id=False,
                                    data=packet)

            bus.send(op_enable_msg)

            time.sleep(0.5)

            data = bus.recv()

            format_data = FORMAT_PACKET(data)

            ip_pfc_status = calculate_ip_bit_location(pfc_number,format_data)

            return ip_pfc_status

            print(op_enable_msg)

            bus.shutdown()


        except exceptions as err:
            print(err)

    @staticmethod
    def pfc_stop(can_channel, card_id):
        try:
            bus = IXXATBus(channel=can_channel, can_filters=[{"can_id": 0x00, "can_mask": 0x000}], bitrate=250000)

        except exceptions.VCIDeviceNotFoundError:
            bus = None

        try:
            op_enable_msg = Message(arbitration_id=card_id, is_extended_id=False,
                                    data=[0x2B, 0x00, 0x20, 0x00, 0, 0, 0, 0])

            bus.send(op_enable_msg)

            time.sleep(0.5)

            print(op_enable_msg)

            bus.shutdown()

        except AttributeError:
            print("Attribute Error")

        print("Stopped!!!!")


def PFC_OP_READ_PACKET(pfc_io_id):
    p_id=1545+pfc_io_id
    p_rtr=0
    p_len=8
    p_d0=0x40
    p_d1=0x00
    p_d2=0x20
    p_d3=0x00
    p_d4=0x00
    p_d5=0x00
    p_d6=0x00
    p_d7=0x00
    packet=[p_id,p_rtr,p_len,p_d0,p_d1,p_d2,p_d3,p_d4,p_d5,p_d6,p_d7]
    return packet


def FORMAT_PACKET(data):
    packet = []
    d0 = '{:02x}'.format(data.data0)
    d1 = '{:02x}'.format(data.data1)
    d2 = '{:02x}'.format(data.data2)
    d3 = '{:02x}'.format(data.data3)
    d4 = '{:02x}'.format(data.data4)
    d5 = '{:02x}'.format(data.data5)
    d6 = '{:02x}'.format(data.data6)
    d7 = '{:02x}'.format(data.data7)
    packet = [d0, d1, d2, d3, d4, d5, d6, d7]
    return packet


def PFC_IP_READ_PACKET():
    p_d0=0x40
    p_d1=0x01
    p_d2=0x40
    p_d3=0x00
    p_d4=0x00
    p_d5=0x00
    p_d6=0x00
    p_d7=0x00
    packet=[p_d0,p_d1,p_d2,p_d3,p_d4,p_d5,p_d6,p_d7]
    return packet


def calculate_ip_bit_location(pfc_number,packet):
    d=int(packet[5]+packet[4],16)
    print(d)
    bit_location=pow(2,pfc_number-1)

    if bit_location&d==0:
        status=0
    else:
        status=1

    return status


print(pfc_control.pfc_set(0,0x610,[PFC1]))
