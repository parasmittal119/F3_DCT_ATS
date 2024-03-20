import sys
sys.path.insert(0, '..\\')
import sys
#import exception
import time
import pyvisa
from config_done import *
#se.close()
global port_number
# import globalvarialbles

print ("USB COMMUNICATION")
port_number=27
identify_unit='*IDN?'
read_op_current='MEAS:CURR?'
read_op_voltage='MEAS:VOLT?'
read_op_power='MEAS:POW?'
rem_ON='CONF:REM ON'
rem_OFF='CONF:REM OFF'
load_OFF='LOAD OFF'
load_ON='LOAD ON'
set_load_sense='MEAS:INP UUT'
read_load_sense='MEAS:INP?'
voltage_ON_condition='CONF:VOLT:ON 40'
voltage_latch_ON='CONF:VOLT:LATC ON'
set_CR_mode='MODE CRH'
read_CR_mode='MODE?'
set_CR_A='RES 1'
set_CR_resistance='RES:L1'
set_CC_mode='MODE CCH'
set_CC_current='CURR:STAT:L1'
RESET='*RST'
set_CV_mode='MODE CVM'
set_CV_voltage='VOLT:STAT:L1'

##id='*IDN?'
##read_op_current='FETC:CURR?'
##read_op_voltage='FETC:VOLT?'
##read_op_power='FETC:POW?'
##rem_ON='CONF:REM ON'
##rem_OFF='CONF:REM OFF'
##load_OFF='LOAD OFF'
##load_ON='LOAD ON'
##set_load_sense='MEAS:INP UUT'
##read_load_sense='MEAS:INP?'
##voltage_ON_condition='CONF:VOLT:ON 40'
##voltage_latch_ON='CONF:VOLT:LATC ON'
##set_CR_mode='MODE CRH'
##read_CR_mode='MODE?'
##set_CR_A='RES 1'
##set_CR_resistance='RES:L1'
##set_CC_mode='MODE CCH'
##set_CC_current='CURR:STAT:L1'
##RESET='*RST'
##set_CV_mode='MODE CVM'
##set_CV_voltage='VOLT:STAT:L1'
global initial_address
initial_address = ""

class DC_LOAD():
    def __init__(self):
        self.chroma=None
        self.load_name=''
        self.rm = None

    def OPEN_DC_LOAD(self,load_type='LOAD'):
        global initial_address, address
        if initial_address == "":
            self.rm = pyvisa.ResourceManager()
            device_listed = self.rm.list_resources()

            for i in device_listed:
                if "USB" in i:
                    if "::632" in i:
                        address = str(i).split("::INSTR")[0]
                        self.chroma = self.rm.open_resource(address)
                    else:
                        pass
                elif "GPIB" in i:
                    self.chroma = self.rm.open_resource(i)

            print(self.chroma.query("*IDN?"))
            # initial_address = address
        else:
            pass
        source_status=True
        count=0
        # if SettingRead('SETTING')['ate load comm type']=='USB':
        #     if load_type=='LOAD':
        #         self.ID=SettingRead('SETTING')['dc load usb id']
        #         self.load_name='DC LOAD'
        #
        #     if load_type=='BATT':
        #         self.ID=SettingRead('SETTING')['battery load usb id']
        #         self.load_name='Battery LOAD'
        #
        # elif SettingRead('SETTING')['ate load comm type']=='GPIB':
        #     if load_type=='LOAD':
        #         self.ID=SettingRead('SETTING')['dc load gpib id']
        #         self.load_name='DC LOAD'
        #
        #     if load_type=='BATT':
        #         self.ID=SettingRead('SETTING')['battery load gpib id']
        #         self.load_name='Battery LOAD'
        #
        # elif SettingRead('SETTING')['ate load comm type'] == 'ETHERNET':
        #     if load_type == 'LOAD':
        #         self.ID = SettingRead('SETTING')['dc load ethernet id']
        #         self.load_name = 'DC LOAD'
        #         self.read_termination = '\r\n'
        #     if load_type == 'BATT':
        #         self.ID = SettingRead('SETTING')['battery load ethernet id']
        #         self.read_termination = '\r\n'

#         while source_status and count<3:
#             count+=1
#             try:
#                 # self.chroma=visa.instrument(self.ID)
# ##                pyvisa.log_to_screen()
#                 if (SettingRead('SETTING')['ate load comm type'] == 'USB') or (SettingRead('SETTING')['ate load comm type']=='GPIB'):
#                     self.rm = pyvisa.ResourceManager()
#                     self.chroma = self.rm.open_resource(self.ID)
#                     print (self.chroma)
#                 else:
#                     self.rm = pyvisa.ResourceManager()
#                     self.chroma = self.rm.open_resource(self.ID, read_termination=self.read_termination)
#                     print (self.chroma)
#                 source_status=False
#                 #print "dc load open ok"
#             except Exception as err:
#                 print ('initialization err:' + str(err))
# ##                #print "globalvarialbles.APP_STOP_FLAG: "+str(globalvarialbles.APP_STOP_FLAG)
#                 if globalvarialbles.APP_STOP_FLAG==True:
#                     return None
# ##                #print"usb not found / "+self.load_name+" not found"
#                 time.sleep(1)
#                 pass








    def DC_LOAD_SET_COMMAND(self,command,load_type='LOAD'):
        source_status=True
        count=0
        while source_status and count<3:
            count+=1
            try:
                # if globalvarialbles.APP_STOP_FLAG==True:
                    # return None
                self.OPEN_DC_LOAD(self)
                self.chroma.write(command)
                source_status=False
                # globalvarialbles.CLEAR_JIG_FLAG=True
                self.CLOSE_DC_LOAD(self)
            except Exception as err:
                print (err)
                #print err
                # globalvarialbles.CLEAR_JIG_FLAG=False
##                #print"usb not found / "+self.load_name+" is OFF"
# ##                #print "globalvarialbles.APP_STOP_FLAG: "+str(globalvarialbles.APP_STOP_FLAG)
#                 if globalvarialbles.APP_STOP_FLAG==True:
#                     return None
                time.sleep(1)
##                #print"usb not found / "+self.load_name+" is OFF. Retrying..."
                #print "Unable to set command to Load"
                self.CLOSE_DC_LOAD(self)
##                self.OPEN_DC_LOAD()
                # time.sleep(2)
                # self.OPEN_DC_LOAD(load_type)
                pass

    def DC_LOAD_READ_COMMAND(self,command,load_type='LOAD'):
        ##print "start read"
        source_status=True
        count=0
        while source_status and count<3:
            count+=1
            try:
                # if globalvarialbles.APP_STOP_FLAG==True:
                #     return None
                self.OPEN_DC_LOAD(self)
                read_data=self.chroma.query(command)
                print(read_data)
                source_status=False
                # globalvarialbles.CLEAR_JIG_FLAG=True
                self.CLOSE_DC_LOAD(self)
                return read_data
            except Exception as err:
                print(err)
                #print err
                #print err
                # globalvarialbles.CLEAR_JIG_FLAG=False
##                #print"usb not found / "+self.load_name+" is OFF"
                #print "globalvarialbles.APP_STOP_FLAG: "+str(globalvarialbles.APP_STOP_FLAG)
                # if globalvarialbles.APP_STOP_FLAG==True:
                #     return No//ne
                # time.sleep(1)
##                #print"usb not found / "+self.load_name+" is OFF. Retrying..."
                #print "Unable to read command from Load"
                self.CLOSE_DC_LOAD(self)
                # time.sleep(2)
                # self.OPEN_DC_LOAD(load_type)
                pass

    def CLOSE_DC_LOAD(self):
            try:
##                self.chroma.close()
                # self.rm.clear()
                self.rm.close()

                # del self.chroma
            except Exception as err:
                #print "dc load close err:" + str(err)
                pass



def DC_LOAD_SET_CURRENT_CR(Object,current,load_type='LOAD'):
    op_voltage=DC_LOAD_READ_OUTPUT_VOLTAGE(Object,load_type)
    #print op_voltage
    if current!=0:
        res=float(op_voltage)/current
        #res=int(res)
        #print("res: "+str(res))
        Object.DC_LOAD_SET_COMMAND(set_CR_mode,load_type)
        Object.DC_LOAD_SET_COMMAND(set_CR_resistance+" "+str(res),load_type)
        Object.DC_LOAD_SET_COMMAND(load_ON,load_type)
    else:
        Object.DC_LOAD_SET_COMMAND(load_OFF,load_type)

def DC_LOAD_SET_CURRENT_CC(current,load_type='LOAD'):
    #op_voltage=DC_LOAD_READ_OUTPUT_VOLTAGE(load_type)
    ##print op_voltage
    # DC_LOAD.DC_LOAD_SET_COMMAND(DC_LOAD, set_CC_mode,load_type)
    DC_LOAD.DC_LOAD_SET_COMMAND(DC_LOAD, set_CC_current+" "+str(current),load_type)
    DC_LOAD.DC_LOAD_SET_COMMAND(DC_LOAD, load_ON,load_type)

def DC_LOAD_SET_CURRENT_CV(Object,voltage,load_type='LOAD'):
    #op_voltage=DC_LOAD_READ_OUTPUT_VOLTAGE(load_type)
    ##print op_voltage
    Object.DC_LOAD_SET_COMMAND(set_CV_mode,load_type)
    #DC_LOAD_SET_COMMAND('VOLT:STAT:CURR MAX',load_type)
    #DC_LOAD_SET_COMMAND('VOLT:STAT:MODE 1',load_type)
    Object.DC_LOAD_SET_COMMAND(set_CV_voltage+" "+str(voltage),load_type)
    Object.DC_LOAD_SET_COMMAND(load_ON,load_type)

def DC_LOAD_READ_OUTPUT_VOLTAGE(load_type='LOAD'):
    retry_flag=True
    count=0
    while retry_flag and count<3:
        count+=1
        try:
            retry_flag=True
            while retry_flag:

                data=DC_LOAD.DC_LOAD_READ_COMMAND(read_op_voltage,load_type)

                if float(data)<1000:
                    retry_flag=False
        except:
            data=999991
            pass
        ##print data
    return data

def DC_LOAD_READ_OUTPUT_CURRENT(load_type='LOAD'):
    retry_flag=True
    count=0
    while retry_flag and count<3:
        count+=1
        try:
            ##print read_op_current
            data=DC_LOAD.DC_LOAD_READ_COMMAND(read_op_current,load_type)
            if float(data)<1000:
                retry_flag=False
        except:
            data=999992
            pass
        ##print data
    return data

def DC_LOAD_READ_OUTPUT_POWER(Object,load_type='LOAD'):
    try:
        data=Object.DC_LOAD_READ_COMMAND(read_op_power,load_type)
    except:
        data=999993
        pass

    return data



def DC_LOAD_RESET(Object,load_type='LOAD'):
    Object.DC_LOAD_SET_COMMAND(RESET,load_type)



if __name__ == "__main__":
    dcload=DC_LOAD()
    #initialize_load('BATT')
    #DC_LOAD_SET_COMMAND(load_OFF,'LOAD')
    #DC_LOAD_SET_COMMAND(load_OFF,'LOAD')
    DC_LOAD_SET_CURRENT_CC(4,'LOAD')
    #print DC_LOAD_READ_COMMAND(id,'BATT')
    #DC_LOAD_RESET('LOAD')
    # print (DC_LOAD_READ_COMMAND(id))
    #print DC_LOAD_READ_OUTPUT_CURRENT('LOAD')
    data=DC_LOAD_READ_OUTPUT_VOLTAGE('LOAD')
    print (f"data: {data}")
    input('Enter a key to proceed')
    # DC_LOAD_SET_COMMAND(load_OFF,'LOAD')
