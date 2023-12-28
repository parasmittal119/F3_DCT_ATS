import os
from config_done import SettingRead
data_entry = os.listdir(r"\\SLICE\Data_Share_Temp\temp_folder_to_upload")
station_id = SettingRead("STATION")['id']+"_"
dates = []
time_date = []
for i in data_entry:
    time_stamp = i.split(station_id)[-1].split(".csv")[0]
    dates.append(time_stamp)

for i in data_entry:
    time_date.append(os.stat(r"D:\backup\backup\records_backup\\" + i).st_atime)

print(os.stat(r"D:\backup\backup\records_backup\active_5_11_12_2023.csv").st_mtime)
# print(type(os.stat(r"\\SLICE\Data_Share_Temp\temp_folder_to_upload\active_5_11_12_2023.csv").st_atime))


def backup_on_server():
    data_entry = os.listdir(r"\\SLICE\Data_Share_Temp\temp_folder_to_upload")
    time_date = []
    for i in data_entry:
        time_date.append(os.stat(r"\\SLICE\Data_Share_Temp\temp_folder_to_upload\\" + i).st_atime)
