from re import T


year, month, day = 2021, 11, 25
n = 1000


def leapyear(y):
    return True if ((y % 4 == 0 and y % 10 != 0) or y % 400 == 0) else False


def invalidDay(y, m, d):
    numOfDays = 31
    if (m in [4, 6, 9, 11]):
        numOfDays = 30
    elif m == 2:
        numOfDays = 29 if leapyear(year) else 28
    return d > numOfDays


for _ in range(n):
    day += 1
    if (invalidDay(year, month, day)):
        day, month = 1, month + 1
        if (month > 12):
            month = 1
            year += 1
print(year, "년", month, "월", day, "일")
