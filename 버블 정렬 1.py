cnt = 0
def bubbleSort(arr):
  global cnt
  for i in range(len(arr) - 1, 0, -1):
    for j in range(i):

      if arr[j] > arr[j + 1]:
        cnt += 1
        if K == cnt:
          print(min(arr[j], arr[j+1]), max(arr[j], arr[j+1]))
          break
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

  if cnt < K:
    print(-1)

A, K = map(int, input().split())
arr = list(map(int, input().split()))

bubbleSort(arr)