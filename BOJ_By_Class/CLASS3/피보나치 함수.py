for _ in range(int(input())):
  zero = [1, 0]
  one = [0, 1]
  N = int(input())
  if N > 1:
    for i in range(N-1):
      zero.append(one[-1])
      one.append(zero[-2]+one[-1])
  print(zero[N], one[N])