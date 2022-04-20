for _ in range(int(input())):
  N = int(input())
  arr = list(map(int, input().split()))
  print( 2 * (max(arr) - sum(arr) // N) + 2 * ((sum(arr) // N) - min(arr)))