import datetime
print("This program prints the calendar of a desired month.")
f_year = int(input("Give me the year:\n"))
f_month = int(input("Give the month:\n"))

if f_month == 12:
    s_month = 1
    s_year = f_year + 1
else:
    s_month = f_month + 1
    s_year = f_year

f_date = datetime.datetime(f_year, f_month, 1)
s_date = datetime.datetime(s_year, s_month, 1)
day = f_date.weekday()

delta = s_date - f_date
num_days = delta.days

print("_____________________")
print(" Mo Tu We Th Fr Sa Su")

calendar = []
for i in range(day):
    calendar.append(" ")
for date in range(num_days):
    calendar.append(date+1)

cal_view = []
for i in range(0, len(calendar), 7):
    cal_view.append(calendar[i:i+7])
if len(cal_view[-1]) < 7:
    for i in range(7 - len(cal_view[-1])):
        cal_view[-1].append(" ")

for line in cal_view:
    print('{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}{:>3}'.format(*line))

