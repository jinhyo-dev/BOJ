arr = list(map(int, input().split()))
print(1 if (arr[0] - arr[2]) >= 2 and (arr[1] - arr[3]) >= 2 else 0)