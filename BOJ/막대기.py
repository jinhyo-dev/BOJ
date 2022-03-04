N = int(input())
sticks = [64, 32, 16, 8, 4, 2, 1]
cnt = 0
for i in sticks:
  if N >= i:
    cnt += 1
    N -= i
  if N == 0: break
print(cnt)