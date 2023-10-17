###############################################################################
# Example: 
# Send/Receive CAN message via IXXAT CAN interface
###############################################################################
# import sys
# sys.path.insert(0, '..\\')
from config_done import *
import time
from CanModule import CAN



def format_voltage(DC_Voltage):
    format_v=[]
    temp10=DC_Voltage*10
    temp10=int(temp10)
    print (temp10)
    temp1=int(temp10/256)
    temp2=int(temp10%256)
    print (hex(temp1))
    print (hex(temp2))
    format_v=[temp2,temp1]
    return format_v


def SMR_VOLTAGE_PACKET(voltage):
    p_id=0x6FF
    p_rtr=0
    p_len=8
    p_d0=0x2B
    p_d1=0x3E
    p_d2=0x20
    p_d3=0x00
    p_d4=voltage[0]
    p_d5=voltage[1]
    p_d6=0x00
    p_d7=0x00
    packet=[p_d0,p_d1,p_d2,p_d3,p_d4,p_d5,p_d6,p_d7]
    return packet

def SMR_CURRENT_PACKET():
    p_id=0x6FF
    p_rtr=0
    p_len=8
    p_d0=0x2B
    p_d1=0x3F
    p_d2=0x20
    p_d3=0x00
    p_d4=0x71
    p_d5=0x02
    p_d6=0x00
    p_d7=0x00
    packet=[p_d0,p_d1,p_d2,p_d3,p_d4,p_d5,p_d6,p_d7]
    return packet




# def SMR_PACKET(voltage):
#     p_id=0x202
#     p_rtr=0
#     p_len=8
#     p_d0=0x00
#     p_d1=voltage[0]
#     p_d2=voltage[1]
#     p_d3=0x02
#     p_d4=0x71
#     p_d5=0x01
#     p_d6=0x0e
#     p_d7=0x00
#     packet=[p_id,p_rtr,p_len,p_d0,p_d1,p_d2,p_d3,p_d4,p_d5,p_d6,p_d7]
#     return packet


def SMR_BATTERY_SET_VOLTAGE(DC_Voltage):
    voltage = format_voltage(DC_Voltage)
    print(voltage)
    packet = SMR_VOLTAGE_PACKET(voltage)
    print(packet)
    # CAN.CAN_WRITE(message_id=1663, packet=packet)
    packet = SMR_CURRENT_PACKET()
    print(packet)
    # CAN.CAN_WRITE(message_id=1663, packet=packet)
    #DELETE_CAN_OBJECT()

# if __name__ == "__main__":
#     can=CAN_MODULE_CANIO()
#     #print format_voltage(62.5)
#     #OPEN_CAN_CONTROL_PORT()
#     SMR_BATTERY_SET_VOLTAGE(can,48.0)
    