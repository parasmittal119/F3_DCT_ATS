import cantools
from can import Message
from can.interfaces.ixxat import IXXATBus, exceptions
import time
import pandas as pd


# All the functions hard coded and by the python code are the same.
# Instead of giving smr_number as an input to functions set_smr_current and set_smr_voltage give node as an input.

class regen_setup_smr_control:
    """
    Control current and voltages of all connected SMR's.
    """

    def __init__(self, baudrate):
        self.baudrate = baudrate
        self.bus = None
        self.can_command = Message(is_extended_id=False,
                                   arbitration_id=0x77F,
                                   dlc=0x07,
                                   data=[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
        # define cycle time for cyclic message, always 5 seconds more than current time.
        self.cycle_time = time.time() + 5
        self.smr_serial_dict = {}  # making the serial number dictionary global
        self.path = ''
        self.node = None
        self.message = []
        self.can_bus()

    def can_bus(self):
        self.bus = IXXATBus(channel=0,
                            can_filters=[{"can_id": 0x00, "can_mask": 0x00}],
                            bitrate=self.baudrate)

    def send_cyclic_message(self, message):
        """
        Send cyclic message.
        """
        self.cycle_time = time.time() + 1
        self.bus.send(message)

    def convert(self, s1):

        """
        Function that converts the list of string into an actual list
        """
        list_10 = []
        i = 0
        while (i < len(s1)):

            if ((s1[i].isdigit()) or (s1[i].isalpha())):

                s2 = ""
                # print(len(s1))
                while (i < len(s1)) and (s1[i] != ',') and (s1[i] != ']'):
                    s2 += s1[i]
                    i = i + 1
                list_10.append(int(s2,
                                   16))  # Hexadecimal string is converted into interger here only for SMR serial number but not for node set. That is converted in the set_smr_node func. only
            i = i + 1

        return list_10

    def read_serial_numbers(self):
        """
        Read the serial number of all the eight SMRs from the excel file and store
        all the serial numbers in a dictionary.
        """
        path = "smr_serial\\SMR_serial_numbers.xlsx"
        data = pd.read_excel(path)
        self.smr_serial_dict = {"SMR_1": [[], []],
                                "SMR_2": [[], []],
                                "SMR_3": [[], []],
                                "SMR_4": [[], []],
                                "SMR_5": [[], []],
                                "SMR_6": [[], []],
                                "SMR_7": [[], []],
                                "SMR_8": [[], []]}

        """
        Putting the converted list from the above function in the dictionary values.
        """
        for i in range(len(data)):
            updated_list = self.convert(data["Serial No."][i])

            # print(updated_list)
            # print(type(updated_list))
            # print(updated_list[4], updated_list[5] , updated_list[6] , updated_list[7])

            for key in self.smr_serial_dict:
                self.smr_serial_dict[key][0] = (updated_list)
                self.smr_serial_dict[key][1] = (data["Node"][i])

            # print("Full Value: ", self.smr_serial_dict[key])        #full value of the key
            # print("Serial Number only: ", self.smr_serial_dict[key][0])     #only SMR serial number value of the key
            # print("Serial number: ",updated_list[4], updated_list[5] , updated_list[6] , updated_list[7])

    def set_smr_nodes(self, i):
        """
        Set all the nodes of the SMRs to vary current.
        """
        path = "smr_serial\\SMR_serial_numbers.xlsx"
        data = pd.read_excel(path)

        # self.node = hex(int((str(data["Node"][i])), 16))
        self.node = '0x6' + str(data["Node"][i])
        print("SMR node: ", self.node)
        print("SMR node type: ", type(self.node))

        # for i in range(len(data)):
        updated_list = self.convert(data["Serial No."][i])
        for key in self.smr_serial_dict:
            self.smr_serial_dict[key][0] = (updated_list)

            smr_node_set = Message(is_extended_id=False, arbitration_id=0x302, dlc=0x08,
                                   data=[self.smr_serial_dict[key][0][4],
                                         self.smr_serial_dict[key][0][5],
                                         self.smr_serial_dict[key][0][6],
                                         self.smr_serial_dict[key][0][7],
                                         int((str(data["Node"][i])), 16),
                                         0x00,
                                         0x00,
                                         0x00])
            # print(smr_node_set)

            # Send the smr node set command 5 times.
            for j in range(5):
                self.send_cyclic_message(smr_node_set)

    def set_smr_current(self, current):
        """
        Input: SMR serial number and current value to set
        Output: Message to transmit to the function convert command
        """
        self.convert_current_command(self.node, current)

    def convert_current_command(self, node_value, current_value):
        """
        Input: Current value to set.
        Output: Converted hex value
        """

        current_value = current_value * 10
        hex_current_val = ((hex(current_value)).lstrip("0x"))

        if len(hex_current_val) < 4:
            for i in range(4 - len(hex_current_val)):
                hex_current_val = "0" + hex_current_val

        fourth_bit = hex_current_val[2:4]
        fifth_bit = hex_current_val[0:2]

        # command = Message(is_extended_id=False ,
        #                   arbitration_id=0x610,
        #                   data = [0x2B, 0x3F, 0x20, 0x00 , int(fourth_bit, 16) , int(fifth_bit, 16) , 0x00, 0x00])

        command = Message(is_extended_id=False,
                          arbitration_id=int(node_value, 16),
                          data=[0x2B, 0x3F, 0x20, 0x00, int(fourth_bit, 16), int(fifth_bit, 16), 0x00, 0x00])

        # Send current command to set 5-times.
        for k in range(5):
            self.send_cyclic_message(command)

    def set_smr_voltage(self, node, voltage):
        """
        Input: SMR serial number and voltage value to set
        Output: Message to transmit to the function convert command
        """
        self.convert_voltage_command(node, voltage)

    def convert_voltage_command(self, node_value, voltage_value):
        """
        Input: Voltage value to set.
        Output: Converted hex value
        """

        voltage_value = voltage_value * 10
        hex_voltage_val = ((hex(voltage_value)).lstrip("0x"))

        if len(hex_voltage_val) < 4:
            for i in range(4 - len(hex_voltage_val)):
                hex_voltage_val = "0" + hex_voltage_val

        fourth_bit = hex_voltage_val[2:4]
        fifth_bit = hex_voltage_val[0:2]

        # command = Message(is_extended_id=False ,
        #                   arbitration_id=0x610,
        #                   data = [0x2B, 0x3E, 0x20, 0x00 , int(fourth_bit, 16) , int(fifth_bit, 16) , 0x00, 0x00])

        command = Message(is_extended_id=False,
                          arbitration_id=int(node_value, 16),
                          data=[0x2B, 0x3E, 0x20, 0x00, int(fourth_bit, 16), int(fifth_bit, 16), 0x00, 0x00])

        # Send voltage command to set 5-times.
        for k in range(5):
            self.send_cyclic_message(command)
