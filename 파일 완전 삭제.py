N = int(input())
arr1 = list(input())
arr2 = list(input())

for _ in range(N):
  for i in range(len(arr1)):
    if arr1[i] == '0':
      arr1[i] = '1'
    else:
      arr1[i] = '0'
print("Deletion succeeded" if arr1 == arr2 else "Deletion failed")
