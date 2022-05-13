def clock(n):
  clock_number = n
  for _ in range(3):
    n = (n % 1000) * 10 + n // 1000
    if clock_number > n:
      clock_number = n
  return clock_number

num = clock(int(''.join(input().split())))
cnt = 0
for i in range(1111, num+1):
  if clock(i) == i:
    cnt += 1
print(cnt)