cnt = 0
arr = []
for _ in range(10):
  A, B = map(int, input().split())
  cnt += B - A
  arr.append(cnt)
print(max(arr))