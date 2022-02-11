# h, m = map(int, input().split())
# time = int(input())
# if m + time < 60:
#   print(h, m + time)
# elif m + time >= 60:
#   if h+(m + time) // 60 >= 24:
#     print(h+(m + time) // 60 - 24, (m + time)%60)
#   else:
#     print(h+(m + time) // 60, (m + time)%60)
h, m, s = map(int, input().split())
time = int(input())

hour = (h + ((m + time) // 60)) %24
minute = (m + time) % 60
print(hour, minute)