h, m, s = map(int, input().split())
time = int(input())

hour = (h + ((m + ((s + time) // 60))) // 60) %24
minute = ((m + ((s + time) // 60))) % 60
second = (s + time) % 60
print(hour, minute, second)