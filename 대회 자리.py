for _ in range(int(input())):
  P, M = map(int, input().split())
  arr = [int(input()) for _ in range(P)]
  cnt = len(arr)
  set_list = list(set(arr))
  print(cnt - len(set_list))