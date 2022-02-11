n = int(input())

hour = int(n / 3600)
minute = int(n % 3600 / 60)
second = int(n % 3600 % 60)

print("시간 :", hour)
print("분 :", minute)
print("초 :", second)