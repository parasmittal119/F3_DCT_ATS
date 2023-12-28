import os
import src.config_done
data_entry = os.listdir(r"\\SLICE\Data_Share_Temp\temp_folder_to_upload")
print(data_entry)
print(type(data_entry[0].split(src.config_done.SettingRead("STATION")['id'])))