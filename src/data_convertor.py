import struct


def hex_to_int(value):
    try:
        return (int(value, 16))
    except Exception as err:
        return err


def hex_to_binary_string_converter(
        data):  # this function takes a hex string and convert it to binary string of 16 bits.
    binary_str = str(bin(int(data, 16)))
    binary_str = binary_str.split('b')[1]
    length = len(binary_str)

    for i in range(16 - length):
        binary_str = '0' + (str(binary_str))

    binary_str = binary_str[::-1]
    binary_str = binary_str[0:25]
    print(binary_str)
    # alarm_value = binary_str[int("8", 10)]
    # print("alarm value "+str(alarm_value))
    return binary_str


def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])


def hex_to_float(h):
    return "{0:.2f}".format(struct.unpack('!f', bytes.fromhex(h))[0])
