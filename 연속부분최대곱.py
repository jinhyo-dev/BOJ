arr = [float(input()) for _ in range(int(input()))]
for i in range(1, len(arr)):
  arr[i] = max(arr[i], arr[i] * arr[i-1])
print("%.3f" % (max(arr)))