arr = []
for _ in range(int(input())):
  arr.append(int(input()))
value = arr[-1]
if arr[2] - arr[1] == arr[1] - arr[0]:
  value += arr[2] - arr[1]
else:
  value *= arr[2] // arr[1]
print(value)
