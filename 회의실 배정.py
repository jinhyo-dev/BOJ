import sys
input = sys.stdin.readline
arr = []
cnt = 1
for _ in range(int(input())):
  A, B = map(int, input().split())
  arr.append([A, B])

arr.sort(key=lambda x:(x[1], x[0]))
tmp = arr[0][1]
for i in range(1, len(arr)):
  if tmp <= arr[i][0]:
    cnt += 1
    tmp = arr[i][1]
print(cnt)