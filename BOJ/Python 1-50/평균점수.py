cnt = 0
for _ in range(5):
  N = int(input())
  if N < 40:
    N = 40
  cnt += N

print(int(cnt/5))