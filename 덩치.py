arr = []

for _ in range(int(input())):
  (w, h) = map(int, input().split())
  arr.append((w, h))

for i in arr:
  grade = 1  
  for j in arr:
    if i[0] < j[0] and i[1] < j[1]:
      grade += 1
  print(grade, end=' ')