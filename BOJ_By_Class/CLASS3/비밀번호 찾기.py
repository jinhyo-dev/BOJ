import sys
input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
dic = dict(input().split() for _ in range(N))

for _ in range(M):
  url = input()
  print(dic.get(url))