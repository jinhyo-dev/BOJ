import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = set([input() for _ in range(N)])
sum = 0
for i in range(M):
  word = input()
  if word in arr:
      sum += 1
print(sum)