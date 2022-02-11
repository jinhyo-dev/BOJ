arr = []
for _ in range(7):
  N = int(input())
  if N % 2 != 0:
    arr.append(N)
arr.sort()
print(sum(arr), arr[0], sep='\n') if len(arr) else print(-1)