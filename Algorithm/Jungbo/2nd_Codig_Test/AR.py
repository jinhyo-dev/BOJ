arr = list(map(int, input().split()))
for i in range(3):
  if arr[i] % 2 == 0:
    print("even")
  else:
    print("odd")  