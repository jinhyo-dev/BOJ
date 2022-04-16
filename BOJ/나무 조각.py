woodpeices = list(map(int, input().split()))

for i in range(5):
  for j in range(1, 5):
    if woodpeices[j] < woodpeices[j-1]:
      woodpeices[j], woodpeices[j-1] = woodpeices[j-1],woodpeices[j]
      print(*woodpeices)