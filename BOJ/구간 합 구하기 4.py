import sys
input = sys.stdin.readline

N ,M = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [0]
tmp = 0

for i in arr:
  tmp += i
  sum_arr.append(tmp)

for k in range(M):
  i, j = map(int, input().split())
  print(sum_arr[j] - sum_arr[i-1])