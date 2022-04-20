A = int(input())
B = int(input())
C = int(input())
D = int(input())

tmp = A + B + C + D
minute = tmp // 60
second = tmp % 60
print(minute, second, sep='\n')