import time
from config_done import *
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
    pfc_list_upper = {"STOP": 0, "PFC1": 1, "PFC2": 2, "PFC3": 4, "PFC4": 8, "PFC5": 16, "PFC6": 32, "PFC7": 64,
                      "PFC8": 128}
    pfc_list_lower = {"STOP": 0, "PFC9": 1, "PFC10": 2, "PFC11": 4, "PFC12": 8, "PFC13": 16, "PFC14": 32, "PFC15": 64,
                      "PFC16": 128}

    pfc_dict = {"p_load": 1, "r_phase": 2, "n_p_load_1": 3, "y_phase": 4, "n_p_load_2": 5, "b_phase": 6,
                "n_p_load_3": 7, "bus": 8, "n_p_load_4": 9, "load_mains": 10, "battery_1": 11, "battery_mains": 12,
                "battery_2": 13, "add_on_1": 14, "battery_3": 15, "add_on_2": 16, "pfc 1": 1, "pfc 2": 2,
                "pfc 3": 3, "pfc 4": 4, "pfc 5": 5, "pfc 6": 6, "pfc 7": 7, "pfc 8": 8, "pfc 9": 9, "pfc 10": 10,
                "pfc 11": 11, "pfc 12": 12, "pfc 13": 13, "pfc 14": 14, "pfc 15": 15, "pfc 16": 16, "all": 0}

    CARD1 = 1546
    CARD2 = 1547

    def __init__(self):
        self.can_channel = None

    @staticmethod
    def pfc_set(can_channel, cont, state):
        global data_packet, var, contact_value, card_id
        cont1 = 0
        cont2 = 0
        data_packet = []
        var = ''

        try:
            # bus = can.interface.Bus(interface="seeedstudio", channel=0,)
            bus = IXXATBus(channel=can_channel, can_filters=[{"can_id": 0x00, "can_mask": 0x000}], bitrate=250000)

        except exceptions.VCIDeviceNotFoundError:
            bus = None


        def send_cyclic_message(card_id: int, check_id: list, data: list):
            global msg
            stats = True
            count = 0
            while stats and count < 9:
                op = Message(arbitration_id=card_id, is_extended_id=False, data=data)
                print(op)
                bus.send(op)
                msg = bus.recv(1)
                for i in check_id:
                    if msg.arbitration_id == i:
                        print(msg)
                        stats = False
                count += 1
            if msg is None:
                return None
            else:
                return msg.data.hex()

        try:
            try:
                if int(PFCRead("PFC 1 PFC")[cont].split(" ")[1]) in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
                    print(f"text value {int(PFCRead('PFC 1 PFC')[cont].split(' ')[1])}")
                    contact_value = int(PFCRead("PFC 1 PFC")[cont].split(" ")[1])
                    card_id = 1546
                print(contact_value, card_id)
            except:
                if int(PFCRead("PFC 2 PFC")[cont].split(" ")[1]) in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
                    contact_value = pfc_control.pfc_dict[cont]
                    card_id = 1547
                print(contact_value, card_id)

            var = send_cyclic_message(card_id, check_id=[1418, 1419], data=[64, 00, 32, 00, 00, 00, 00, 00])
            print(var)

            if contact_value == 0:
                send_cyclic_message(card_id, check_id=[1418], data=[0x2B, 0x00, 0x20, 0x00, 0, 0, 0, 0])
                bus.shutdown()
                return

            for i in range(0, len(var) + 1, 2):
                data_packet.append(var[i:i + 2])

            d = int(data_packet[5] + data_packet[4], 16)
            bit_calculation = pow(2, contact_value - 1)

            if bit_calculation & d == 0:
                if state == 1:
                    d += bit_calculation
            else:
                if state == 0:
                    d -= bit_calculation

            cont2 = int(d / 256)
            cont1 = int(d % 256)

            var = send_cyclic_message(card_id, check_id=[1418], data=[0x2B, 0x00, 0x20, 0x00, cont1, cont2, 0, 0])

            print(var)
            bus.shutdown()

        except (AttributeError, Exception) as err:
            print(cont)
            print(f"Exception occurred: {err}")

    @staticmethod
    def read_pfc(card_id, pfc_number):
        try:
            bus = IXXATBus(channel=can_channel, can_filters=[{"can_id": 0x00, "can_mask": 0x000}], bitrate=250000)

        except exceptions.VCIDeviceNotFoundError:
            bus = None

        try:
            stats = True
            count = 0
            var = 0
            while stats and count < 9:
                op = Message(arbitration_id=card_id, is_extended_id=False, data=[64,1,32,0,0,0,0,0])
                print(op)
                bus.send(op)
                msg = bus.recv(1)
                if msg.arbitration_id == 1418:
                    print(msg)
                    var = msg.data.hex()
                    stats = False
                elif msg.arbitration_id == 1419:
                    print(msg)
                    var = msg.data.hex()
                    stats = False
                count += 1


            ip_pfc_status = calculate_ip_bit_location(pfc_number, var)


            print(op_enable_msg)

            bus.shutdown()

            return ip_pfc_status

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
    p_id = 1545 + pfc_io_id
    p_rtr = 0
    p_len = 8
    p_d0 = 0x40
    p_d1 = 0x00
    p_d2 = 0x20
    p_d3 = 0x00
    p_d4 = 0x00
    p_d5 = 0x00
    p_d6 = 0x00
    p_d7 = 0x00
    packet = [p_id, p_rtr, p_len, p_d0, p_d1, p_d2, p_d3, p_d4, p_d5, p_d6, p_d7]
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
    p_d0 = 0x40
    p_d1 = 0x01
    p_d2 = 0x40
    p_d3 = 0x00
    p_d4 = 0x00
    p_d5 = 0x00
    p_d6 = 0x00
    p_d7 = 0x00
    packet = [p_d0, p_d1, p_d2, p_d3, p_d4, p_d5, p_d6, p_d7]
    return packet


def calculate_ip_bit_location(pfc_number, packet):
    d = int(packet[5] + packet[4], 16)
    print(d)
    bit_location = pow(2, pfc_number - 1)

    if bit_location & d == 0:
        status = 0
    else:
        status = 1

    return status



