import datetime
import time

import pyautogui

while True:
    im = pyautogui.screenshot()
    date_time = str(datetime.datetime.now())
    date_time = date_time.split(" ")
    date_time = date_time[0] + "_" + date_time[1][:2] + "_" + date_time[1][3:5] + "_" + date_time[1][6:8]
    im.save("D:\hidden\\" + str(date_time) + ".jpg")
    time.sleep(2)