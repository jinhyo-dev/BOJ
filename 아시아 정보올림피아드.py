students = [list(map(int, input().split())) for _ in range(int(input()))]
students.sort(key=lambda x: -x[2])
arr = []
cnt = 0
for i in students:
  if cnt == 3:
    break

  if i[0] in arr:
    if arr.count(i[0]) == 2:
      continue

  print(i[0], i[1])
  arr.append(i[0])
  cnt += 1