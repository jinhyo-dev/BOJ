cnt = 0
for i in range(1, int(input()) + 1):
  t = i
  while t:
    if t % 10 == 3 or t % 10 == 6 or t % 10 == 9:
      cnt += 1
    t //= 10
print(cnt)