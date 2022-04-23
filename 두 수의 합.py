N = int(input())
arr = list(map(int, input().split()))
X = int(input())

arr.sort()

left, right = 0, N - 1
cnt = 0

while left < right:
  if arr[left] + arr[right] == X:
    cnt += 1
  if arr[left] + arr[right] < X:
    left += 1
    continue
  right -= 1

print(cnt)