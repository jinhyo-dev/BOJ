import sys
input = sys.stdin.readline
plug = 0
for _ in range(int(input())-1):
  N = int(input())
  plug += N - 1

N = int(input())
plug += N
print(plug)