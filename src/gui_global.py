import getpass
import sys

account_user = getpass.getuser()
count = 0
can_status = False
port_status = False
pfc_status = False
gpib_status = False
admin_login = False
hardware_status = False
APP_STOP_FLAG = False
CLEAR_JIG_FLAG = False
report_pass = False
report_fail = False
commissioning_status = False
commissioning_bit = True
directory_location = f"C:/Users/{account_user}/AppData/Local/DCT_ATS/"
files_directory_location = f"C:/Users/{account_user}/AppData/Local/DCT_ATS/files/"
image_directory_location = f"C:/Users/{account_user}/AppData/Local/DCT_ATS/images/"
ate_name = ''