N = int(input())
num = 1
cnt = 2
for i in range(9, N, 3):
  num += cnt
  cnt += 1
print(num)