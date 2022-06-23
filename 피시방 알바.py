N = int(input())
exist = []
arr = list(map(int, input().split()))
cnt = 0
for i in arr:
  if i in exist:
    cnt += 1
  else:
    exist.append(i)

print(cnt)
