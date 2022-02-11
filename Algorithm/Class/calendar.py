from tarfile import DEFAULT_FORMAT


year, month, day_of_week = 2021, 11, 1

print(year, '년', month, '월:')

weekdays = ['일', '월', '화', '수', '목', '금', '토']


def leapyear(y):
    return True if ((y % 4 == 0 and y % 10 != 0) or y % 400 == 0) else False


def daysOfMonth(y, m):
    numOfDays = 31
    if (m in [4, 6, 9, 11]):
        numOfDays = 30
    elif m == 2:
        numOfDays = 29 if leapyear(year) else 28
    return numOfDays


for day in weekdays:
    print('  ', day, end=' ')
print()

for _ in range(day_of_week):
    print(' ', end=' ')

numOfMonth = daysOfMonth(year, month)

for day in range(1, numOfMonth+1):
    if (day < 10):
        print('  ', day, end=' ')
    else:
        print(' ', day, end=' ')
    if ((day_of_week + day) % 7 == 0):
        print()

print()
