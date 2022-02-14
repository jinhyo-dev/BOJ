max_arr = []
for _ in range(9):
  arr = list(map(int, input().split()))
  val = max(arr)
  max_arr.append([val, arr.index(val)+1])
print(max(max_arr)[0])
print(max_arr.index(max(max_arr))+1, max(max_arr)[1])