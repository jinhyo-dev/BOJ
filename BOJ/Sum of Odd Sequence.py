for i in range(int(input())):
  N = int(input())
  print(sum([i for i in range(1, N+1) if i % 2]))