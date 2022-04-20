for _ in range(int(input())):
  C = []
  G = []
  num = int(input())
  for _ in range(num):
    N, M = input().split()
    C.append(int(N))
    G.append(float(int(N) * float(M)))
  print(sum(C), '%.1f' % float(sum(G)/sum(C)))