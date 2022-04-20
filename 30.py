arr = list(input())
arr.sort(reverse=True)
sum = 0
for i in arr:
  sum += int(i)
if sum % 3 != 0 or '0' not in arr:
  print(-1)
else:
  print(*arr, sep='')