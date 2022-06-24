import sys
input = sys.stdin.readline
N, K, L = map(int, input().split())
VIP = []
for _ in range(N):
  tmp = list(map(int, input().split()))
  isOverK = True
  for i in tmp:
    if i < L:
      isOverK = False
      break

  if isOverK and sum(tmp) >= K:
    VIP.append(tmp)

print(len(VIP))
for i in VIP:
  for j in i:
    print(j, end=' ')
