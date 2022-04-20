import sys
input = lambda : sys.stdin.readline().rstrip()

def mergeSort(start, end):
  global cnt, A
  if start < end:
    mid = (start + end) // 2
    mergeSort(start, mid)
    mergeSort(mid + 1, end)

    a, b = start, mid + 1
    tmp = []

    while a <= mid and b <= end:
      if A[a] <= A[b]:
        tmp.append(A[a])
        a += 1
      else:
        tmp.append(A[b])
        b += 1
        cnt += (mid - a + 1)
    
    if a <= mid:
      tmp += A[a:mid + 1]
    if b <= end:
      tmp += A[b:end + 1]

    for i in range(len(tmp)):
      A[start + i] = tmp[i]

cnt = 0
N = int(input())
A = list(map(int, input().split()))
mergeSort(0, N - 1)
print(cnt)