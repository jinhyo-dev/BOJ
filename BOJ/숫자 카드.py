N = int(input())
card = list(map(int, input().split()))
card.sort()

def binarySearch(num):
  l = 0
  r = N - 1
  while l <= r:
    mid = (l+r) // 2
    if card[mid] == num:
      return 1
    elif card[mid] > num:
      r = mid - 1
    else:
      l = mid + 1
  return 0

input()
for i in list(map(int, input().split())):
  print(binarySearch(i), end=' ')