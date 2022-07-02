N, K = map(int, input().split())
arr = sorted(map(int, input().split()), reverse=True)
print(arr[K - 1])
