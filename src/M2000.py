import requests
import time
from config_done import *
import configparser

global config
config = configparser.ConfigParser()
requests.packages.urllib3.disable_warnings()  # disable warning for HTTPS


class ValueNotSetException(Exception):
    def __init__(self):
        print("Error:: Value could not be set to MCM")


class OIDNotFoundException(Exception):
    def __init__(self):
        print("Could not find oid for this value")


class M2000CommandSet():
    def __init__(self):
        req_S = requests.Session()
        self.req_s = req_S
        self.ip = ''
        self.username = ''
        self.password = ''
        self.OID_Value = None

    def SID_CODE_READ(self):
        file = open(f"{gui_global.files_directory_location}Http_SID.txt", 'r')
        sid_code = file.read()
        file.close()
        return sid_code

    def LOGIN_MCM(self):  # CREDL=[USER,PASSWord]
        # print 'Hello'
        try:
            self.ip = SettingRead('SETTING')['m2000_ip address']
            self.ip = '172.16.66.50'
            # print('ip is:' + self.ip)
            self.username = SettingRead('SETTING')['m2000_user']
            self.username = "engg1"
            self.password = SettingRead('SETTING')['m2000_password']
            ##            self.password = '8M%24ex%23engg'
            ##            self.password = '8M$Ex#engg'
            ##            req= self.req_s.get('http://'+str(self.ip)+'/req.htm?type=1&usr='+str(self.username)+'&pwd='+str(self.password),verify=False,timeout=5)
            req = self.req_s.post('http://' + str(self.ip) + '/login.htm?',
                                  'type=1&usr=' + str(self.username) + '&pwd=' + str(self.password), verify=False,
                                  timeout=5)
            # print req.text
            # print(req.text)
            sid_code = (req.text).split(',')[1][:-1]
            # print("User Login")
            file = open(f"{gui_global.files_directory_location}Http_SID.txt", 'w')
            file.write(sid_code)
            file.close()
            return [True, "Login Successful"]
        except Exception as Err:
            print('Unable to Loginx', Err)
            # LOGOUT(ip,sid_code)
            return [False, 'Unable to Login']

    # If already login we need sid to logout for that we should save SID in other file after every login
    # so that we could use sid to logout user

    def LOGOUT_MCM(self):
        try:
            sid_code = self.SID_CODE_READ()
            req = self.req_s.get('http://' + (self.ip) + '/req.htm?type=0&sid=' + str(sid_code), verify=False,
                                 timeout=5)
            ##            req= self.req_s.post('http://'+(self.ip)+'/login.htm?','type=0&sid='+str(sid_code),verify=False,timeout=5)
            code1 = (req.text)
            # print code1,' Succesfully'
            req.connection.close()
            print("Session Logout")
            return code1
        except Exception as err:
            print('Unable to Logout, Connection Lost', err)
            return False

    # def POST_DATA(self,reqt,data1):
    #     try:
    #         #sid_code = self.SID_CODE_READ()
    #         req= self.req_s.post('http://'+str(self.ip)+'/'+str(reqt),data=str(data1),verify=False,timeout=5)
    #         data2=(req.text)
    #         #print code1,' Succesfully'
    #         return data2
    #     except Exception as err:
    #         print 'Unable to post request',reqt,' Connection Lost\n',err
    #         return False

    # def ATS_REQUEST(self,reqt):#reqt='req.htm?type=1&item=11'
    #     try:
    #         #sid_code = self.SID_CODE_READ()
    #         req= self.req_s.get('http://'+str(self.ip)+'/'+str(reqt),verify=False,timeout=5)
    #         data=(req.text)
    #         data = data.split(';')
    #         #print code1,' Succesfully'
    #         return data
    #     except Exception as err:
    #         print 'Unable to Get request',reqt,' Connection Lost\n',err
    #         return [0,"Unable to request"]

    def MCM_SET_COMMAND(self, itemid, value):
        '''

        :param itemid: Item Id for paarameter to be set to  MCM
        :param value: Value of the item
        :return:
        '''

        DATA_NOT_RECIEVED = True
        count = 0
        while DATA_NOT_RECIEVED and count < 5:
            count += 1
            try:
                sid_code = self.SID_CODE_READ()
                req = 0
                # ?type=6&itm=<itemNo>&val=<value>
                req = self.req_s.get('http://' + str(self.ip) + '/req.htm?type=6&itm=' + str(itemid) + '&val=' + str(
                    (value)) + '&sid=' + sid_code, 
                                     verify=False, timeout=5)  # 3213748287/
                Log1 = str(req.text)
                print(Log1)
                SET = Log1.split(',')[1][0]  # if 1==notset else 0==set
                if SET == '0':
                    pass
                else:
                    print('in else')
                    raise ValueNotSetException()
                # print NOT_SET
                # code = req.status_code
                # print code
                # r.connection.close()
                # return int(NOT_SET)^1
                break
            except Exception as err:
                try:
                    print(err)
                    print('In set_data')
                    print('unable to request1.....TRYING AGAIN.....')
                    OID_Value = None
                    DATA_NOT_RECIEVED = True
                    self.LOGOUT_MCM()
                    connection_status = self.LOGIN_MCM()
                    ##return 0
                except:
                    pass
        self.OID_Value = None

    def MCM_GET_COMMAND(self, itemid, type_req='3'):
        '''

        :param itemid: Item Id for paarameter to be get from MCM
        :param type_
        req: Type of item needed, default value is 3
        :return: returns a list[True/False,string_value]
        '''
        DATA_NOT_RECEIVED = True
        count = 0
        GET_DATA = []
        while DATA_NOT_RECEIVED and count < 5:
            count += 1
            try:
                sid_code = self.SID_CODE_READ()
                r = 0
                if itemid.find('ALM.') != -1:
                    itemid = itemid.split('.')[1]
                    type_req = '1'
                if itemid == 'serial_number':
                    g_id = 65069
                    r = self.req_s.get(
                        'http://' + str(self.ip) + '/req.htm?type=10' + '&gid=' + str(g_id) + '&pgNo=1' + '&sid=' + str(
                            sid_code), verify=False, timeout=5)  # 3213748287/
                    Log1 = str(r.text)
                    print('printing log now..........')
                    print(Log1)
                    return_data = Log1.split('\n')
                    return_data = return_data[2]
                    return_data = return_data.split(',')

                    print(return_data[1])
                    self.OID_Value = return_data[1]

                    break
                if type_req == '3':
                    r = self.req_s.get('http://' + str(self.ip) + '/req.htm?type=' + str(type_req) + '&itms=' + str(
                        itemid) + '&sid=' + str(
                        sid_code), verify=False, timeout=5)  # 3213748287/
                    # time.sleep(0.1)
                    Log1 = str(r.text)
                    if Log1 == '9,System Status,1,0,0,0,0,,0,0;':
                        # print itemid +'required'
                        # return 'None'
                        raise (OIDNotFoundException)
                    GET_DATA = Log1.split(',')
                    print("GET_DATA from mcm:" + str(GET_DATA))
                    if GET_DATA[6] == '0':
                        return_data = GET_DATA[4]
                        DATA_NOT_RECEIVED = False
                    else:
                        try:
                            return_data = (float(GET_DATA[4]) / (10 ** int(GET_DATA[6])))
                            DATA_NOT_RECEIVED = False
                        except Exception as err:
                            print('GET_DATA from mcm is not an integer or float and following is the error:\n')
                            print(err)
                            return_data = str(GET_DATA[4])
                            DATA_NOT_RECEIVED = False
                            pass
                    # code= r.status_code
                    # return return_data
                    self.OID_Value = return_data
                else:
                    r = self.req_s.get('http://' + str(self.ip) + '/req.htm?type=9' + '&itms=3&sid=' + str(sid_code),
                                       verify=False, timeout=5)  # 3213748287/
                    Log1 = str(r.text)
                    print(Log1)

                    Log = (Log1.split(';')[1])
                    g_id = Log.split(',')[1]
                    r = self.req_s.get(
                        'http://' + str(self.ip) + '/req.htm?type=10' + '&gid=' + str(g_id) + '&pgNo=1' + '&sid=' + str(
                            sid_code),
                        verify=False, timeout=5)  # 3213748287/
                    Log = (r.text.split(';')[1]).split('\n')
                    print(Log)

                    Alarm_list = [item.split(',')[0] for item in Log]
                    return_data = 0
                    for i in Alarm_list:
                        if i == itemid:
                            # return 1
                            return_data = 1

                    self.OID_Value = return_data
                    # return self.OID_Value
                    Number_of_Alarms = Log[0]
                    break
            except OIDNotFoundException:
                print("ITEM NOT FOUND against this OID : " + itemid)
                file = open('..\\files\RequiredParameters.txt', "w")
                file.write(itemid + "\n")
                file.close()
                # return '88888888'
                self.OID_Value = '8888888888'
            except Exception as err:
                try:
                    print(err)
                    print('In get_data')
                    print('unable to get1.....TRYING AGAIN.....')
                    OID_Value = None
                    DATA_NOT_RECIEVED = True
                    self.LOGOUT_MCM()
                    connection_status = self.LOGIN_MCM()
                    # ##return 0
                    # GET_DATA.append(False)
                    # # print 'in Get_data'
                    # GET_DATA.append('unable to request1')
                    # #return GET_DATA
                except:
                    pass
            # self.OID_Value=None

        # except:
        #     print 'unable to request1'
        #     GET_DATA.append(False)
        #     # print 'in Get_data'
        #     GET_DATA.append('unable to request1')
        #     #return GET_DATA

    def GET_ALARMS(self):
        '''
        comments
        '''
        List1 = [False, '']
        try:
            try:
                sid_code = self.SID_CODE_READ()
                r = 0
                r = self.req_s.get('http://' + str(self.ip) + '/req.htm?type=10&gid=65000&pgNo=1&sid=' + sid_code,
                                   verify=False, timeout=5)  # 3213748287/
                # time.sleep(0.1)
                # print r.raise_for_status()
                Log1 = str(r.text).split(';')[1].split('\n')[:-1]
                # print Log1
                code = r.status_code
                # r.connection.close()
                return [True, Log1]
            except:
                print('unable to request1')
                Log1 = ('unable to request')
                return [False, Log1]

        except Exception as r1:
            print(r1, '\n unable to request2 ')
            print(str(self.ip) + " TIME OUT" + '\n')
            List1 = [False, 'No Data']
            return List1

    def SET_PFC(self, pfc=0, status=0, alarm_index=0):
        List1 = [False, '']
        try:
            try:
                sid_code = self.SID_CODE_READ()
                ree = self.req_s.get('http://' + self.ip + '/req.htm?type=16&pfc=' + str(pfc) + '&pol=' + str(
                    status) + '&val=' + str(alarm_index) + '&sid=' + sid_code, verify=False, timeout=5)  # + ' https/1.1'
                time.sleep(0.01)
                # ree.connection.close()
                return True
            except:
                print('unable to request1')
                time.sleep(2)
                return False

        except Exception as r1:
            print(r1, '\n unable to request2 ')
            print(str(self.ip) + " TIME OUT" + '\n')
            return False


if __name__ == '__main__':
    MCM = M2000CommandSet()
    MCM.LOGIN_MCM()
    print('Logged in!')
    ##    val=MCM.MCM_SET_COMMAND(M2000OIDRead('ALARM')['spu fail'])
    # MCM.MCM_SET_COMMAND(M2000OIDRead('BATTERY ISOLATE')['batt1'],0)
    ##    print 'SPUFail: '+  str( val)
    # val=MCM.GET_ITEMS('22','1')
    # print val
    # MCM.SET_ITEMS('2760','0')
    # val = MCM.GET_ITEMS('ALM.81')
    # print 'ALM.81: '+str( val)
    ##    for key in M2000OIDRead("CALIBRATE CURRENT DCIO"):
    ##
    ##        val = MCM.MCM_GET_COMMAND(M2000OIDRead("CALIBRATE CURRENT DCIO")[key])
    ##        print key + ": " +str(MCM.OID_Value)
    ##        print "\n \n"
    # MCM.MCM_SET_COMMAND(M2000OIDRead('SYSTEM COMMANDS')['factory restore'], 1)
    # time.sleep(60)
    # val = MCM.MCM_GET_COMMAND('serial_number')
    # print(str(MCM.OID_Value))
    # print("\n \n")
    # variable_1 = eval(input("Enter number 1: "))
    # variable_2 = eval(input("Enter number 2: "))
    # sum = variable_1 + variable_2
    # if abs(sum) == sum:
    #     MCM.SET_PFC(9, 1, 13)
    #     print(f"SUM is + and {sum}")
    # else:
    #     MCM.SET_PFC(9, 0, 13)
    #     print(f"SUM is - and {sum}")
    MCM.LOGOUT_MCM()

# """http://172.16.66.50/req.htm?type=16&pfc=9&pol=0&val=13&sid=1597084329"""