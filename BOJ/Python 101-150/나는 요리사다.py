arr = []
for i in range(1, 6):
  _ = list(map(int, input().split()))
  arr.append([sum(_), i])
print(max(arr)[1], max(arr)[0])