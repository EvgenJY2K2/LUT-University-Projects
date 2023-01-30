from datetime import datetime,timedelta

time1 = "2022/10/20 13:31:26"
d_time1 = datetime.strptime(time1, '%Y/%m/%d %H:%M:%S')


print("The month is {}.".format(d_time1.strftime("%B")))
print("The day is {}.".format(d_time1.strftime("%A")))

time2 = "2022/01/01 00:00:01"
d_time2 = datetime.strptime(time2, '%Y/%m/%d %H:%M:%S')
print("The New Year day was {}.".format(d_time2.strftime("%A")))

diff = d_time1 - d_time2
print("It has been {} days since New Year.".format(diff.days))

delta = timedelta(hours = 52, minutes = 34, seconds = 12)
new = d_time1 + delta
d_new = datetime.strftime(new, '%Y/%m/%d %H:%M:%S')

print("After adding 52 hours, 34 minutes, 12 seconds to the original time, it is {}.".format(d_new))
