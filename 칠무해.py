import sys
input = sys.stdin.readline

N = int(input())
arr = [float(input()) for _ in range(N)]
arr.sort()

for i in range(7):
  print('{:.3f}'.format(arr[i]))