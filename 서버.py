N, T = map(int, input().split())
minute = list(map(int, input().split()))
cnt = 0
for i in minute:
  if T - i >= 0:
    T -= i
    cnt += 1
  else:
    break
print(cnt)