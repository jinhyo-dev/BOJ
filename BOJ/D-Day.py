import datetime

year1, month1, day1 = map(int, input().split())
year2, month2, day2 = map(int, input().split())

today = datetime.date(year1, month1, day1)
end = datetime.date(year2, month2, day2)

DDay = str(end - today).split(" ")[0]
print('gg' if int(DDay) >= 365243 else f'D-{DDay}')