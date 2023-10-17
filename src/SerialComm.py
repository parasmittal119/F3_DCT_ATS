'''
This module makes serial interface with following:
1. RS-485 based SMR
2. RS-485 based PFC IO

'''

import time

import serial

global se
global count
port_check = True
Datain_check = True
baud_rate = 9600


def open_serial_comm(port_number, baud_rate, device):
    if device == "SMR":
        count = 141
    elif device == "PFCIO":
        count = 1

    Datain_check = True
    port_check = True

    while Datain_check:
        while port_check:
            try:
                try:
                    print("port opening...")
                    se = serial.Serial(port=port_number + 1,
                                       baudrate=baud_rate,
                                       bytesize=serial.EIGHTBITS,
                                       parity=serial.PARITY_NONE,
                                       stopbits=serial.STOPBITS_ONE,
                                       timeout=.1,
                                       xonxoff=False,
                                       rtscts=False,
                                       writeTimeout=1,
                                       dsrdtr=False,
                                       interCharTimeout=None)

                    print("port open")
                    port_check = False
                    # time.sleep(1)

                except serial.SerialException:
                    print("Port not found or could not be open")
                    port_check = True

                    time.sleep(2)
                    pass
            except exceptions.ValueError:
                print("Port already Open")
                pass


def set_serial_data(device):
    try:
        try:
            print("data fetch start")
            outputstr = bytearray(send_data)
            se.write(outputstr)
            print("send")
            read_list = []
            try:
                retry = True
                retry_count = 0
                while count > 0:
                    read_data = se.read().encode('hex')
                    if read_data != '':
                        read_list.append(read_data)
                        Datain_check = False
                        data_fetch = True
                        retry = False
                    else:
                        retry_count += 1
                        if retry_count > 3:
                            retry = False
                            retry_count = 0
                            data_fetch = False
                            Datain_check = True
                            port_check = True
                            if retry == False:
                                print("\n")
                                print("SMR number " + str(smr_number) + " not communicating")
                                return
                                break

                            count -= 1
                        # #                        if data_fetch==True:
                        # #                            #print"data fetch finish"
                        # #                        else:
                        # #                            #print "data fetch fail"

                        # print Datain_check
                        se.close()
                        time.sleep(.3)
            except serial.SerialException:
                print("read error")
                Datain_check = True
                port_check = True
                time.sleep(2)
                pass

        except serial.SerialException:
            print("Device communicating to the system is not functioning")
            Datain_check = True
            port_check = True
            time.sleep(2)
            pass

    except exceptions.IOError:
        Datain_check = True
        port_check = True
        print("No communication with the instrument (no answer)")
        time.sleep(2)
        pass


def serial_data_recieve(smr_number):
    smr_num_hex = int(smr_number)
    smr_read = [0xAA, 0xBB, 0xCC, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, smr_num_hex, 0, 0, 0, 0x13]

    smr_read_detail = [0xAA, 0xBB, 0xDD, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, smr_num_hex, 0, 0, 0, 0x13]
    ######################################################################

    Datain_check = True
    port_check = True

    while Datain_check:

        while port_check:
            try:

                try:
                    # print "port opening..."
                    se = serial.Serial(port=83,
                                       baudrate=9600,
                                       bytesize=serial.EIGHTBITS,
                                       parity=serial.PARITY_NONE,
                                       stopbits=serial.STOPBITS_ONE,
                                       timeout=.1,
                                       xonxoff=False,
                                       rtscts=False,
                                       writeTimeout=1,
                                       dsrdtr=False,
                                       interCharTimeout=None)

                    # print "port open"
                    port_check = False
                    # time.sleep(1)

                except serial.SerialException:
                    print("Port not found or could not be open")
                    port_check = True

                    time.sleep(2)
                    pass
            except exceptions.ValueError:
                print("Port already Open")
                pass

        try:
            try:

                # print"data fetch start"

                outputstr = bytearray(smr_read_detail)
                # print outputstr
                se.write(outputstr)
                # print "send"
                count = 141
                read_list = []
                try:
                    retry = True
                    retry_count = 0

                    while count > 0:

                        read_smr = se.read().encode('hex')
                        if read_smr != '':
                            read_list.append(read_smr)
                            Datain_check = False
                            data_fetch = True
                            retry = False
                        else:
                            retry_count += 1
                            if retry_count > 3:
                                retry = False
                                retry_count = 0
                            data_fetch = False
                            Datain_check = True
                            port_check = True
                            if retry == False:
                                print("\n")
                                print("SMR number " + str(smr_number) + " not communicating")
                                return
                                break

                        count -= 1
                    # #                        if data_fetch==True:
                    # #                            #print"data fetch finish"
                    # #                        else:
                    # #                            #print "data fetch fail"

                    # print Datain_check
                    se.close()
                    time.sleep(.3)
                except serial.SerialException:
                    print("read error")
                    Datain_check = True
                    port_check = True
                    time.sleep(2)
                    pass

            except serial.SerialException:
                print("Device communicating to the system is not functioning")
                Datain_check = True
                port_check = True
                time.sleep(2)
                pass
        except exceptions.IOError:
            Datain_check = True
            port_check = True
            print("No communication with the instrument (no answer)")
            time.sleep(2)
            pass


