import configparser

config = configparser.ConfigParser()


# cfgfile=open('E:\eclipse-standard-kepler\workspace\chroma_interface\\files\config.ini','w')
# config.add_section('DUT CONFIGURATION')
# config.set('DUT CONFIGURATION','ac phases type','sinGLE')
# config.set('DUT CONFIGURATION','no. of battery fuses',2)
# config.set('DUT CONFIGURATION','no. of battery lvd',1)
# config.set('DUT CONFIGURATION','no. of load lvd',1)
# config.set('DUT CONFIGURATION','load current sensor','disable')
# config.write(cfgfile)
# cfgfile.close()

def ReadFile(file, section):
    if file == 'config':
        config.read('E:\eclipse-standard-kepler\workspace\chroma_interface\\files' + '\\' + file + '.ini')
    else:
        config.read('E:\eclipse-standard-kepler\workspace\chroma_interface\\files' + '\\' + file + '.txt')
    dict1 = {}
    options = config.options(section)
    # print options
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print(("exception on %s!" % option))
            dict1[option] = None
    return dict1


def FileTimeRead(section):
    print(config.read('..\\files\\filetime.txt'))
    dict1 = {}
    options = config.options(section)
    # print options
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print(("exception on %s!" % option))
            dict1[option] = None
    return dict1


def ConfigRead(section):
    print(config.read('..\\files\config.ini'))
    dict1 = {}
    options = config.options(section)
    # print options
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print(("exception on %s!" % option))
            dict1[option] = None
    return dict1


def RJILM2000OIDRead(section):
    config.read('..\\files\oidRJILM2000.txt')
    print(("in oid read_     reading:" + section))
    dict1 = {}
    options = config.options(section)
    # print options
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print(("exception on %s!" % option))
            dict1[option] = None
    return dict1


def M2000OIDRead(section):
    config.read('..\\files\oidM2000.txt')
    print(("in oid read_     reading:" + section))
    dict1 = {}
    options = config.options(section)
    # print options
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print(("exception on %s!" % option))
            dict1[option] = None
    return dict1


def OIDRead(section):
    config.read('..\\files\oid.txt')
    print(("in oid read_     reading:" + section))
    dict1 = {}
    options = config.options(section)
    # print options
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print(("exception on %s!" % option))
            dict1[option] = None
    return dict1


def SmrDetailOIDRead(section):
    print(config.read('..\\files\smrdetailoid.txt'))
    dict1 = {}
    options = config.options(section)
    # print options
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print(("exception on %s!" % option))
            dict1[option] = None
    return dict1


def PfcJigRead(section):
    config.read('..\\files\pfcjig.txt')
    dict1 = {}
    options = config.options(section)
    # print options
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print(("exception on %s!" % option))
            dict1[option] = None
    return dict1


def VersionRead(section):
    config.read('..\\files\systemversion.txt')
    dict1 = {}
    options = config.options(section)
    # print options
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print(("exception on %s!" % option))
            dict1[option] = None
    return dict1


def DefaultRead(section):
    print(config.read('..\\files\default.txt'))
    dict1 = {}
    options = config.options(section)
    print(options)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print(("exception on %s!" % option))
            dict1[option] = None
    return dict1


def CalibrateRead(section):
    config.read('..\\files\calibrate.txt')
    dict1 = {}
    options = config.options(section)
    # print options
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print(("exception on %s!" % option))
            dict1[option] = None
    return dict1


def SettingRead(section):
    try:
        config.read('..\\files\setting.txt')
        dict1 = {}
        options = config.options(section)
        # print options
        for option in options:
            try:
                dict1[option] = config.get(section, option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                print(("exception on %s!" % option))
                dict1[option] = None
        return dict1
    except Exception as err:
        print(err)
        pass
        return None


if __name__ == '__main__':
    print(OIDRead('SYSTEM CONFIG'))

# print CalibrateRead('SHUNT')['deadband percentage']
# cfgfile=open('..\\files\\filetime.txt','w')
# config.add_section('TIME')
# config.set('TIME','time','filetime')
# config.write(cfgfile)
# cfgfile.close()
#
#
# print FileTimeRead('TIME')['time']
# print phase_type
# print type(phase_type)
# mains_low_fail_set_oid=OIDRead('MAINS SETTING')['mains low fail set']
# print mains_low_fail_set_oid
#
# ip=SettingRead('SETTING')['ip address']
# user=SettingRead('SETTING')['user']
# password=SettingRead('SETTING')['password']
# print ip
# print type(ip)

