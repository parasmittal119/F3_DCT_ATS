import configparser

import gui_global

config = configparser.ConfigParser()


class AllException(Exception):
    pass


def CalibrateSetting(section):
    try:
        config.read(f'{gui_global.files_directory_location}calibrate.txt')
        dict1 = {}
        options = config.options(section)
        for option in options:
            try:
                dict1[option] = config.get(section, option)
            except Exception as err:
                print(err)
                dict1[option] = None
        return dict1
    except (AllException, configparser.NoSectionError, configparser.NoOptionError, TypeError) as e:
        return e


def ConfigRead(section):
    try:
        config.read(f'{gui_global.files_directory_location}config.ini')
        dict1 = {}
        options = config.options(section)
        for option in options:
            try:
                dict1[option] = config.get(section, option)
            except Exception as err:
                print(err)
                dict1[option] = None
        return dict1
    except (AllException, configparser.NoSectionError, configparser.NoOptionError, TypeError) as e:
        return e


def PFCRead(section):
    try:
        config.read(f'{gui_global.files_directory_location}pfcjig.txt')
        dict1 = {}
        options = config.options(section)
        for option in options:
            try:
                dict1[option] = config.get(section, option)
            except Exception as err:
                print(err)
                dict1[option] = None
        return dict1
    except (AllException, configparser.NoSectionError, configparser.NoOptionError, TypeError) as e:
        return e



def DefaultRead(section):
    try:
        config.read(f"{gui_global.files_directory_location}default.txt")
        dict1 = {}
        options = config.options(section)
        for option in options:
            try:
                dict1[option] = config.get(section, option)
            except Exception as err:
                print(err)
                dict1[option] = None
        return dict1
    except (AllException, configparser.NoSectionError, configparser.NoOptionError, TypeError) as e:
        return e


def FileTime(section):
    try:
        config.read(f"{gui_global.files_directory_location}filetime.txt")
        dict1 = {}
        options = config.options(section)
        for option in options:
            try:
                dict1[option] = config.get(section, option)
            except Exception as e:
                print(e)
                dict1[option] = None
        return dict1
    except (AllException, configparser.NoSectionError, configparser.NoOptionError, TypeError) as e:
        return e


def HTTPSID():
    try:
        try:
            with open(f"{gui_global.files_directory_location}Http_SID.txt") as f:
                value = f.readlines()
            return value[0]
        except Exception:
            return "File not found"
    except (AllException, configparser.NoSectionError, configparser.NoOptionError, TypeError) as e:
        return e


def OIDRead(section):
    try:
        config.read(f"{gui_global.files_directory_location}oid.txt")
        dict1 = {}
        options = config.options(section)
        for option in options:
            try:
                dict1[option] = config.get(section, option)
            except AllException as e:
                print(e)
                dict1[option] = None
        return dict1
    except (AllException, configparser.NoOptionError, configparser.NoSectionError, TypeError) as e:
        return e


def M2000OIDRead(section):
    try:
        config.read(f'{gui_global.files_directory_location}oidM2000.txt')
        print("in oid read_reading:" + section)
        dict1 = {}
        options = config.options(section)
        # print options
        for option in options:
            try:
                dict1[option] = config.get(section, option)
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1
    except (AllException, configparser.NoOptionError, configparser.NoSectionError, TypeError) as e:
        return e

def SettingRead(section):
    try:
        config.read(f'{gui_global.files_directory_location}setting.txt')
        dict1 = {}
        options = config.options(section)
        for option in options:
            try:
                dict1[option] = config.get(section, option)
            except Exception as err:
                print(err)
                dict1[option] = None
        return dict1
    except (AllException, configparser.NoSectionError, configparser.NoOptionError, TypeError) as e:
        return e


def SMRDetailOID(section):
    try:
        config.read(f'{gui_global.files_directory_location}smrdetailoid.txt')
        dict1 = {}
        options = config.options(section)
        for option in options:
            try:
                dict1[option] = config.get(section, option)
            except Exception as err:
                print(err)
                dict1[option] = None
        return dict1
    except (AllException, configparser.NoSectionError, configparser.NoOptionError, TypeError) as e:
        return e


def SystemVersion(section):
    try:
        config.read(f"{gui_global.files_directory_location}systemversion.txt")
        dict1 = {}
        options = config.options(section)
        for option in options:
            try:
                dict1[option] = config.get(section, option)
            except Exception as err:
                print(err)
                dict1[option] = None
        return dict1
    except (AllException, configparser.NoSectionError, configparser.NoOptionError, TypeError) as e:
        return e


def AlarmReading(section):
    try:
        config.read(f'{gui_global.files_directory_location}alarm_testing.txt')
        dict1 = {}
        options = config.options(section)
        for option in options:
            try:
                dict1[option] = config.get(section, option)
            except Exception as err:
                print(err)
                dict1[option] = None
        return dict1
    except (AllException, configparser.NoSectionError, configparser.NoOptionError, TypeError) as e:
        return e


def ProfileReading(section):
    try:
        config.read(f"{gui_global.files_directory_location}profile.txt")
        # config.read(f"{gui_global.files_directory_location}profile.txt')
        dict1 = {}
        options = config.options(section)
        for option in options:
            try:
                dict1[option] = config.get(section, option)
            except Exception as err:
                print(err)
                dict1[option] = None
        return dict1
    except (AllException, configparser.NoSectionError, configparser.NoOptionError, TypeError) as e:
        return e
