import sys
input = sys.stdin.readline
N, K = map(int, input().split())
pies = list(map(int, input().split()))
sweetness = [pies[0] + pies[-1]]
for i in range(N-1):
  tmp = 0
  for j in range(K):
    tmp += pies[i+j]
  sweetness.append(tmp)
print(max(sweetness))