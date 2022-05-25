N, L, H = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in range(L):
  del arr[0]

for i in range(H):
  del arr[-1]

print(sum(arr) / len(arr))