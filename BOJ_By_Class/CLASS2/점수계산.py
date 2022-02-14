N = int(input())
arr = list(map(int, input().split()))
result = 0
cnt = 0

for i in arr:
  if i == 1:
    cnt += 1
    result += cnt
  else:
    cnt = 0
print(result)
  