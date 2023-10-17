# from _ast import Num

from CRCModules.CRC16 import CRC16

ACEM_PACKET = [0x14, 0x04, 0x94,
               0x5F, 0xB0, 0x43, 0x69,
               0x5F, 0xB0, 0x43, 0x67,
               0x13, 0x53, 0x43, 0x69,
               0x5F, 0xB0, 0x43, 0x55,
               0x5F, 0xB0, 0x43, 0x34,
               0x5F, 0xB0, 0x42, 0x55,
               0x5F, 0xB0, 0x43, 0x44,
               0x5F, 0xB1, 0x43, 0x55,
               0x5F, 0xB0, 0x43, 0x67,
               0x5F, 0xB0, 0x43, 0x66,
               0x5F, 0xB0, 0x43, 0x66,
               0x5F, 0xB0, 0x43, 0x44,
               0x5F, 0xB0, 0x43, 0x69,
               0x5F, 0xB0, 0x43, 0x67,
               0x5F, 0xB0, 0x44, 0x54,
               0x5F, 0xB1, 0x43, 0x55,
               0x5F, 0xB0, 0x43, 0x59,
               0x5F, 0xB0, 0x41, 0x55,
               0x5F, 0xB0, 0x54, 0x55,
               0x5F, 0xB0, 0x43, 0x44,
               0x5F, 0xB0, 0x55, 0x55,
               0x5F, 0xB0, 0x43, 0x69,
               0x5F, 0xB0, 0x43, 0x63,
               0x5F, 0xB0, 0x43, 0x61,
               0x5F, 0xB0, 0x47, 0x55,
               0x5F, 0xB0, 0x43, 0x77,
               0x5F, 0xB0, 0x43, 0x33,
               0x5F, 0xB0, 0x43, 0x34,
               0x5F, 0xB0, 0x43, 0x99,
               0x5F, 0xB0, 0x43, 0x43,
               0x5F, 0xB0, 0x43, 0x69,
               0x5F, 0xB0, 0x43, 0x55,
               0x5F, 0xB0, 0x43, 0x43,
               0x5F, 0xB0, 0x43, 0x66,
               0x5F, 0xB0, 0x43, 0x43,
               0x5F, 0xB0, 0x43, 0x55,
               0x5F, 0xB0, 0x43, 0x55,
               0x3A, 0x43]
print(len(ACEM_PACKET))

import struct


def tohex(val, nbits):
    return hex((val + (1 << nbits)) % (1 << nbits))


def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])


def hex_to_float(h):
    return struct.unpack('!f', h.decode('hex'))[0]


def ascii_to_hex(character):
    return character.encode('hex')


def FORMAT_DATA_32BYTES_4BYTES_LIST(value):
    value_float = float(value)
    data = float_to_hex(value_float)
    data = int(data, 16)
    d = '{:08x}'.format(data)
    d_int = int(d, 16)
    data_byte_list = []
    for i in range(0, 8, 2):
        data_byte_list.append(d[i:i + 2])
        # print data_byte_list
    send_byte_list = []
    send_byte_list.append(data_byte_list[2])
    send_byte_list.append(data_byte_list[3])
    send_byte_list.append(data_byte_list[0])
    send_byte_list.append(data_byte_list[1])
    return send_byte_list


def FORMAT_DATA_32BYTES_4BYTES_LIST_INT(value):
    print(value)
    value_float = int(value)
    # data=float_to_hex(value_float)
    data = value_float
    print(data)
    # data=int(data,16)
    print(data)
    d = '{:08x}'.format(data)
    d_int = int(d, 16)
    data_byte_list = []
    for i in range(0, 8, 2):
        data_byte_list.append(d[i:i + 2])
        # print data_byte_list
    send_byte_list = []
    send_byte_list.append(data_byte_list[2])
    send_byte_list.append(data_byte_list[3])
    send_byte_list.append(data_byte_list[0])
    send_byte_list.append(data_byte_list[1])
    return send_byte_list


def FORMAT_DATA_16BYTES_2BYTES_LIST(value):
    value_dec = int(value)
    data = hex(value)
    data = int(data, 16)
    d = '{:04x}'.format(data)
    d_int = int(d, 16)
    data_byte_list = []
    for i in range(0, 4, 2):
        data_byte_list.append(d[i:i + 2])
        # print data_byte_list
    send_byte_list = []

    send_byte_list.append(data_byte_list[0])
    send_byte_list.append(data_byte_list[1])
    return send_byte_list


def FORMAT_MODBUS_CRC_16BYTES_2BYTES_LIST(PACKET_HEX_LIST):
    PACKET_HEX = ''
    for item in PACKET_HEX_LIST:
        PACKET_HEX += item
    PACKET_HEX = str(PACKET_HEX)
    print("packet hex: " + PACKET_HEX)
    PACKET_ASCII = PACKET_HEX.decode("hex")
    CRC_16BYTE = '{:4X}'.format(CRC16(modbus_flag=True).calculate(PACKET_ASCII))
    decimal_CRC_16BYTE = int(CRC_16BYTE, 16)

    CRC_16BYTE = '{:4X}'.format(decimal_CRC_16BYTE)
    print(CRC_16BYTE)
    # d='{:04}'.format(str(CRC_16BYTE))
    # print len(CRC_16BYTE)
    data_byte_list = []
    for i in range(0, 4, 2):
        data_byte_list.append(CRC_16BYTE[i:i + 2])
    send_byte_list = []
    send_byte_list.append(data_byte_list[1])
    send_byte_list.append(data_byte_list[0])

    return send_byte_list


def Convert_Hex2Ascii(number1):
    print(number1)
    asciiValueH = number1 & 0xF0
    asciiValueH = asciiValueH >> 4
    asciiValueL = number1 & 0x0F

    if asciiValueH <= 9:
        asciiValueH = asciiValueH + 0x30

    elif asciiValueH >= 10 and asciiValueH <= 15:
        asciiValueH = asciiValueH + 0x37
    else:
        asciiValueH = 0

    if asciiValueL <= 9:
        print(asciiValueL)
        asciiValueL = asciiValueL + 0x30
        print(asciiValueL)
    elif asciiValueL >= 10 and asciiValueL <= 15:
        asciiValueL = asciiValueL + 0x37
    else:
        asciiValueL = 0
    print(number1)
    asciiValueH = '{:2X}'.format(asciiValueH)
    asciiValueL = '{:2X}'.format(asciiValueL)
    return [asciiValueH, asciiValueL]


hex_data = hex(0b00000001)
print(hex_data)
print(Convert_Hex2Ascii(int(hex_data, 16)))


def Convert_Ascii2Hex(number1, number2):
    dataOut1 = 0
    dataOut2 = 0

    if (number1 >= 0x41 and number1 <= 0x46):
        dataOut1 = number1 - 0x37
    elif (number1 >= 0x30 and number1 <= 0x39):
        dataOut1 = number1 - 0x30
    else:
        dataOut1 = 0

    dataOut1 = dataOut1 & 0x0f

    if (number2 >= 0x41 and number2 <= 0x46):
        dataOut2 = number2 - 0x37
    elif (number2 >= 0x30 and number2 <= 0x39):
        dataOut2 = number2 - 0x30
    else:
        dataOut2 = 0

    dataOut2 = dataOut2 & 0x0f

    dataOut1 = dataOut1 << 4
    dataOut1 = dataOut1 + dataOut2
    return dataOut1


def Convert_Ascii2Hex2Bytes(number1, number2, number3, number4):
    dataOut1 = 0
    dataOut2 = 0
    dataOut3 = 0
    dataOut4 = 0
    dataOut = 0
    temp = 0

    if (number1 >= 0x41 and number1 <= 0x46):
        dataOut1 = number1 - 0x37
    elif (number1 >= 0x30 and number1 <= 0x39):
        dataOut1 = number1 - 0x30
    else:
        dataOut1 = 0

    dataOut1 = dataOut1 & 0x0f

    if (number2 >= 0x41 and number2 <= 0x46):
        dataOut2 = number2 - 0x37
    elif (number2 >= 0x30 and number2 <= 0x39):
        dataOut2 = number2 - 0x30
    else:
        dataOut2 = 0

    dataOut2 = dataOut2 & 0x0f

    if (number3 >= 0x41 and number3 <= 0x46):
        dataOut3 = number3 - 0x37
    elif (number3 >= 0x30 and number3 <= 0x39):
        dataOut3 = number3 - 0x30
    else:
        dataOut3 = 0

    dataOut3 = dataOut3 & 0x0f

    if (number4 >= 0x41 and number4 <= 0x46):
        dataOut4 = number4 - 0x37
    elif (number4 >= 0x30 and number4 <= 0x39):
        dataOut4 = number4 - 0x30
    else:
        dataOut4 = 0

    dataOut4 = dataOut4 & 0x0f

    dataOut = dataOut1
    dataOut = dataOut << 4
    dataOut = dataOut + dataOut2
    dataOut = dataOut << 4
    dataOut = dataOut + dataOut3
    dataOut = dataOut << 4
    dataOut = dataOut + dataOut4

    return dataOut


def Calculate_LenghtWord(LenghtId):
    Nibble1 = 0
    Nibble2 = 0
    Nibble3 = 0
    Sum1 = 0

    Nibble1 = LenghtId / 256
    LenghtId = LenghtId % 256
    Nibble2 = LenghtId / 16
    Nibble3 = LenghtId % 16

    Sum1 = Nibble1 + Nibble2 + Nibble3
    Sum1 = ~Sum1
    Sum1 = Sum1 + 1
    Sum1 = Sum1 & 0x000F
    Sum1 = Sum1 << 12
    Sum1 = Sum1 + (Nibble1 << 8)
    Sum1 = Sum1 + (Nibble2 << 4)
    Sum1 = Sum1 + (Nibble3)
    return Sum1


def Calculate_CoslightCheckSum(frame):
    # print frame
    frame_len = len(frame)
    i = 0
    checksum = 0
    for i in range(1, frame_len):
        checksum = checksum + int(frame[i], 16)
    checksum = checksum % 65536
    checksum = ~checksum
    checksum = checksum + 1
    return checksum


def to2sCompStr(num, bitWidth):
    print(bin(num))
    num = ~Num
    print(num)
    num &= (2 << bitWidth - 1) - 1  # mask
    print(num)
    formatStr = '{:0' + str(bitWidth) + 'b}'
    ret = formatStr.format(int(num))
    return ret


if __name__ == "__main__":
    print("")
    print(tohex(50, 16))
    print(tohex(-50, 16))
    # print FORMAT_DATA_16BYTES_2BYTES_LIST(23111)
    # print FORMAT_DATA_32BYTES_4BYTES_LIST_INT(1)
#     frame=[1,2,3,4,5,6,7,8,9]
#     #print Calculate_CoslightCheckSum(frame)
#     COSLIGHT_COMMAND_PACKET=['7e', '00', '00', '30', '31', '44', '30', '38','33','45','30','30','32','30','31']
#     CheckSuminfo=Calculate_CoslightCheckSum(COSLIGHT_COMMAND_PACKET)
#     print CheckSuminfo
#     print Convert_Hex2Ascii(CheckSuminfo/256)
#     print Convert_Hex2Ascii(CheckSuminfo%256)
# print FORMAT_DATA_32BYTES_4BYTES_LIST(45.0625)
# print hex_to_float('d6604341')
#     PACKET_HEX="1404945FB043695FB04367135343695FB043555FB043345FB042555FB043445FB143555FB043675FB043665FB043665FB043445FB043695FB043675FB044545FB143555FB043595FB041555FB054555FB043445FB055555FB043695FB043635FB043615FB047555FB043775FB043335FB043345FB043995FB043435FB043695FB043555FB043435FB043665FB043435FB043555FB04355"
#     #print FORMAT_MODBUS_CRC_16BYTES_2BYTES_LIST(PACKET_HEX)
