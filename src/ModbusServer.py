import sys
import minimalmodbus
from _ast import Return
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL=True
import time
import os
import sys
import exception
from serial import Serial
from random import randint
from config_done import *
from TelnetCommandSet import *

read_input_register_1={}
screen_clear_count=0
port_type=''


def MODBUS_CHECK(port_type,baudrate):
    DATA_TRY_COUNT=3
    DATA_COUNT=0
    PORT_COUNT=0
    PORT_TRY_COUNT=10
    COM_TRY_COUNT=20
    COM_COUNT=0
    port_check=True
    Datain_check=True

    if port_type.lower()=='lower':
        port=SettingRead('SETTING')['rs485 lower port']
    if port_type.lower()=='upper':
        port=SettingRead('SETTING')['rs485 upper port']
    Datain_check=True
    while Datain_check and DATA_COUNT<=DATA_TRY_COUNT and COM_COUNT<=COM_TRY_COUNT:
        #print COM_COUNT
        #print DATA_COUNT
        while port_check and PORT_COUNT<=PORT_TRY_COUNT:
            
            try:
                try:
                    #print "port opening..."
                    mcm_iocl=minimalmodbus.Instrument(port,1)
                    #print "port open"
                    #print mcm_iocl
                    port_check=False
                    mcm_iocl.serial.baudrate=baudrate
                    mcm_iocl.serial.timeout=2
                except serial.SerialException:
                    #print "Port not found or could not be open"
                    PORT_COUNT+=1
                    port_check=True   
                    time.sleep(5)
                    pass
            except exceptions.ValueError:
                #print "Port already Open"
                pass
    
        try:
            try:

                                ##print"data fetch start"
                data_in=mcm_iocl.read_register(11,0,3)
                ##print"data fetch finish"
                Datain_check=False
                ##print DefaultRead

            except:
                #print"CRC error"
                COM_COUNT+=1
                data_in=0
                #Datain_check=False
                pass
        except exceptions.IOError:
            data_in=0
            DATA_COUNT+=1
            Datain_check=True
            port_check=True
            #print "No communication with the instrument (no answer)"
            time.sleep(5)
            pass                
                
            
    return data_in


def MODBUS_CLIENT_COMM(COMMAND,COUNT):

    com_port=SettingRead('SETTING')['modbus comm port']
    baud_rate=SettingRead('SETTING')['modbus comm baudrate']
    Datain_check = True
    port_check = True
    
    PACKET=[]
    for item in COMMAND:
        PACKET.append(int(item,16))



    while Datain_check:


            while port_check:
                try:

                    try:
                        global se
                        # print "port opening..."
                        se = serial.Serial(port=com_port,
                                           baudrate=baud_rate,
                                           bytesize=serial.EIGHTBITS,
                                           parity=serial.PARITY_NONE,
                                           stopbits=serial.STOPBITS_ONE,
                                           timeout=2,
                                           xonxoff=False,
                                           rtscts=False,
                                           writeTimeout=1,
                                           dsrdtr=False,
                                           interCharTimeout=None)

                        # print "port open"
                        port_check = False
                        # time.sleep(1)

                    except serial.SerialException:
                        print ("Port already Open")
                        port_check = False

                        #time.sleep(2)
                        pass
                except exceptions.ValueError:
                    print ("Port already Open")
                    pass


            try:
                try:

                    # print"data fetch start"
                    count = COUNT
                    read_list = []
                    print (PACKET)
                    outputstr = bytearray(PACKET)
                    # print outputstr
                    se.write(outputstr)
                    # print "send"
                    
                    try:
                        retry = True
                        retry_count = 0

                        while count > 0:

                            RESPONSE = se.read().encode('hex')
                            sys.stdout.write(RESPONSE)
                            if RESPONSE != '':
                                read_list.append(RESPONSE)
                                Datain_check = False
                                data_fetch = True
                                retry = False
                                count -= 1
                                
                        return read_list
# #                        if data_fetch==True:
# #                            #print"data fetch finish"
# #                        else:
# #                            #print "data fetch fail"

                        # print Datain_check
                        #se.close()
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
                    print ("No communication with the instrument (no answer)")
                    time.sleep(2)
                    pass





def MODBUS_SERVER_COMM(MODBUS_COMM_PACKET,COMMAND_PACKET=['1v', '04', '00', '00', '00', '4a', '73', '38'],modbus_comm=1):
    #COMMAND_PACKET=['1v', '04', '00', '00', '00', '4a', '73', '38']
    PACKET=[]
    for item in MODBUS_COMM_PACKET:
        PACKET.append(int(item,16))
    #print PACKET
    if modbus_comm==1:
        com_port=SettingRead('SETTING')['modbus comm port']
        baud_rate=SettingRead('SETTING')['modbus comm baudrate']
    elif modbus_comm==2:
        com_port=SettingRead('SETTING')['modbus comm port 2']
        baud_rate=SettingRead('SETTING')['modbus comm baudrate 2']
    
    Datain_check = True
    port_check = True
    
    
    
    while Datain_check:
            while port_check:
                try:
                    try:
                        global se
                        # #print "port opening..."
                        se = serial.Serial(port=com_port,
                                           baudrate=baud_rate,
                                           bytesize=serial.EIGHTBITS,
                                           parity=serial.PARITY_NONE,
                                           stopbits=serial.STOPBITS_ONE,
                                           timeout=2,
                                           xonxoff=False,
                                           rtscts=False,
                                           writeTimeout=1,
                                           dsrdtr=False,
                                           interCharTimeout=None)

                        #print "port open"
                        port_check = False
                        # time.sleep(1)

                    except serial.SerialException:
                        #print "Port already Open"
                        #port_check = True
                        port_check = False

                        #time.sleep(2)
                        pass
                except exceptions.ValueError:
                    #print "Port already Open"
                    pass


            try:
                try:
                    packet_fail_check=0
                    while True:
                        count=len(COMMAND_PACKET)
                        flag=0
                        data_list=[]
                        packet_check_length=0
                        
                        while count>0 and packet_check_length<20:
                            packet_check_length=packet_check_length+1
                            data=se.read().encode('hex')
                            #print data
                            sys.stdout.write(data)
                            sys.stdout.write('\n')
                            if data==COMMAND_PACKET[0]:
                                flag=1
                                packet_check_length=0
                            ##print data
                            ##print "something is missing"
                            if data!="" and flag==1:
                                data_list.append(data)
                                packet_check_length=0
                                #print data
                                count-=1
                        flag=0
                        sys.stdout.write(str(data_list))
                        sys.stdout.write('\n')
                        ##print "command packet"
                        ##print COMMAND_PACKET
                        if data_list==COMMAND_PACKET:
                            sys.stdout.write('sending data \n')
                            #sys.stdout.write('\n')
                            ##print "sending data"
                            #time.sleep(REPLY_DELAY)
                            outputstr=bytearray(PACKET)
                            se.write(outputstr)
                            #se.close()
                            Datain_check = False
                            #print "data send end"  
                            result=True
                            return result
                        else:
                            sys.stdout.write('required command packet not received \n')
                            sys.stdout.write('required command packet'+str(COMMAND_PACKET)+'\n')
                            sys.stdout.write('received command packet'+str(data_list)+'\n')
                            result=False
                            #return result
                            packet_fail_check=packet_fail_check+1
                            sys.stdout.write('packet fail check count: '+str(packet_fail_check)+'\n')
                            #print packet_fail_check
                            
                        if packet_fail_check>3:
                            return False

                except serial.SerialException:
                    print("Device communicating to the system is not functioning")
                    Datain_check = True
                    port_check = True
                    time.sleep(2)
                    pass
            except exceptions.IOError:
                    Datain_check = True
                    port_check = True
                    print ("No communication with the instrument (no answer)")
                    time.sleep(2)
                    pass
        
    
    return True

#MODBUS_ACEM_COMM(ACEM_PACKET)    
def CLOSE_PORT():
    try:
        se.close()
        print ("serial port closed")
    except:
        print ("port already closed")




if __name__ == "__main__":
    packet=['1a', '04', '3a', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '00', '00', '00', '00', '00',
            '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00',
            '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', 
            '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', 
            '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', 'ab']
    #MODBUS_SERVER_COMM(packet)

    #TELNET_SET_COMMAND(OIDRead('SYSTEM COMMANDS')['factory restore'],1)
    #time.sleep(15)
    #TELNET_SET_COMMAND(OIDRead('RS 485')['modbus comm'],255)
    #TELNET_SET_COMMAND(OIDRead('RS 485')['acem comm'],255)
    #TELNET_SET_COMMAND(OIDRead('RS 485')['lithium ion comm'],255)
    #TELNET_SET_COMMAND(OIDRead('RS 485')['dg amf comm'],255)
    #TELNET_SET_COMMAND(OIDRead('RS 485')['modbus comm'],0)
     #TELNET_SET_COMMAND(OIDRead('RS 485')['bnms comm'],255)
     #TELNET_SET_COMMAND(OIDRead('RS 485')['modbus comm'],255)
    #TELNET_SET_COMMAND(OIDRead('RS 485')['modbus comm'],255)    
    #print float(MODBUS_CHECK('upper',19200))/10
    #print float(MODBUS_CHECK('lower',19200))/10
    #charge_voltage_telnet=float(Telnet_get_command(OIDRead('BATTERY SETTING')['charge voltage']))
        
    
