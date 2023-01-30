from datetime import datetime,timedelta
import math

file_name = input("Give filename:\n")
file = open(file_name, "r")
lines = file.readlines()

info = []
l = []
time_str = "00:00"
time_d = datetime.strptime(time_str, "%H:%M")

for i in lines[1:]:
    info.append(i)

for item in info:
    item = item.split(",")
    color = item[1]
    type = item[0]

    time = item[2].replace('\n', '')
    time2 = datetime.strptime(time, "%H:%M")
 
    diff = time2 - time_d
    minutes = math.floor(diff.total_seconds() / 60)
    time_d = time2


    print("Time was {} when {} {} was observed ({} minutes after previous vehicle).".format(time, color, type, minutes))

